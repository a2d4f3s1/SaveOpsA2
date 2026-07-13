# SPDX-License-Identifier: GPL-3.0-or-later
"""Path, naming and rotation logic shared by handlers and operators."""

import os
import re
import shutil
import time
from pathlib import Path

import bpy

# Set while SaveOps itself writes a snapshot copy, so the save handlers can
# tell our own saves apart from the user's. Handlers and timers all run on
# Blender's main thread, so a plain bool is race-free.
_internal_save_in_progress = False

TIMESTAMP_FMT = "%Y-%m-%d_%H-%M-%S"
MANUAL_TAG = "v"      # backups taken from .blendN files / pre-save copies
AUTO_TAG = "auto"     # timer and "Backup Now" snapshot copies

_DEFAULT_BACKUP_DIR = "_backup"
_INVALID_DIR_CHARS = re.compile(r'[<>:"/\\|?*]')


def sanitize_dir_name(name: str) -> str:
    """A single safe folder name; falls back to the default on anything fishy."""
    name = (name or "").strip()
    if not name or name in (".", "..") or _INVALID_DIR_CHARS.search(name):
        return _DEFAULT_BACKUP_DIR
    return name


def backup_dir_for(blend_filepath: str, dir_name: str) -> Path:
    return Path(blend_filepath).parent / sanitize_dir_name(dir_name)


def backup_dir_names(prefs) -> set:
    """Sanitized folder names of both backup targets, for nesting guards."""
    return {
        sanitize_dir_name(prefs.backup_dir_name),
        sanitize_dir_name(prefs.auto_backup_dir_name),
    }


def make_backup_name(stem: str, tag: str, when: float) -> str:
    return f"{stem}_{tag}_{time.strftime(TIMESTAMP_FMT, time.localtime(when))}.blend"


def unique_path(target: Path) -> Path:
    """Avoid same-second collisions with a -N suffix (still matches our pattern)."""
    if not target.exists():
        return target
    for n in range(1, 1000):
        candidate = target.with_name(f"{target.stem}-{n}{target.suffix}")
        if not candidate.exists():
            return candidate
    return target


def owned_backup_pattern(stem: str, tag: str) -> re.Pattern:
    """Matches only names this add-on generates for this exact stem and tag.

    Rotation must never delete a file it cannot prove it created itself.
    """
    return re.compile(
        re.escape(stem)
        + "_" + tag
        + r"_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(?:-\d+)?\.blend"
    )


def move_blendn_files(blend_filepath: str, prefs) -> list:
    """Move .blend1 .. .blendN left next to the file into the backup folder."""
    base = Path(blend_filepath)
    save_version = bpy.context.preferences.filepaths.save_version
    moved = []
    for n in range(1, max(save_version, 1) + 1):
        src = Path(f"{blend_filepath}{n}")
        if not src.is_file():
            continue
        try:
            backup_dir = backup_dir_for(blend_filepath, prefs.backup_dir_name)
            backup_dir.mkdir(parents=True, exist_ok=True)
            dst = unique_path(
                backup_dir / make_backup_name(base.stem, MANUAL_TAG, src.stat().st_mtime)
            )
            shutil.move(str(src), str(dst))
            moved.append(dst)
        except OSError as ex:
            print(f"SaveOps: could not move {src.name}: {ex}")
    return moved


def rotate(backup_dir: Path, stem: str, tag: str, keep: int) -> int:
    """Delete the oldest owned backups beyond `keep`. Returns how many were deleted."""
    keep = max(keep, 1)
    if not backup_dir.is_dir():
        return 0
    pattern = owned_backup_pattern(stem, tag)
    # Only direct children, only regular files, only full name matches.
    # Timestamps sort lexicographically, so sorting by name is chronological.
    matches = sorted(
        p for p in backup_dir.iterdir()
        if p.is_file() and pattern.fullmatch(p.name)
    )
    deleted = 0
    for p in matches[:-keep]:
        try:
            os.remove(p)
            deleted += 1
        except OSError as ex:
            print(f"SaveOps: could not delete old backup {p.name}: {ex}")
    return deleted


def snapshot_copy(prefs) -> tuple:
    """Write a timestamped copy of the working state without touching the main file.

    Returns (ok, message); callers report it (operator) or print it (timer).
    """
    global _internal_save_in_progress

    blend_filepath = bpy.data.filepath
    if not blend_filepath:
        return False, "File has not been saved yet"
    base = Path(blend_filepath)
    if base.parent.name in backup_dir_names(prefs):
        return False, "File is inside a backup folder, skipping snapshot"

    try:
        backup_dir = backup_dir_for(blend_filepath, prefs.auto_backup_dir_name)
        backup_dir.mkdir(parents=True, exist_ok=True)
        target = unique_path(
            backup_dir / make_backup_name(base.stem, AUTO_TAG, time.time())
        )
    except OSError as ex:
        return False, f"Could not create backup folder: {ex}"

    _internal_save_in_progress = True
    try:
        # relative_remap=False keeps stored paths identical to the main file,
        # so a backup restored back into the project folder resolves as-is.
        bpy.ops.wm.save_as_mainfile(
            filepath=str(target),
            copy=True,
            check_existing=False,
            relative_remap=False,
        )
    except Exception as ex:
        return False, f"Backup failed: {ex}"
    finally:
        _internal_save_in_progress = False

    rotate(backup_dir, base.stem, AUTO_TAG, prefs.max_auto_copies)
    return True, f"Backup saved: {target.name}"
