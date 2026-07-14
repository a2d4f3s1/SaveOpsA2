# SPDX-License-Identifier: GPL-3.0-or-later

import os
from pathlib import Path

import bpy
from bpy.app.handlers import persistent

from . import core
from .prefs import get_prefs


def _same_path(a: str, b: str) -> bool:
    return os.path.normcase(os.path.normpath(a)) == os.path.normcase(os.path.normpath(b))


@persistent
def saveopsa2_save_pre(filepath, *_):
    """Fallback for Save Versions = 0: no .blend1 will exist, so copy the file
    that is about to be overwritten into the backup folder ourselves."""
    if core._internal_save_in_progress:
        return
    try:
        prefs = get_prefs()
        if not prefs.save_backup_enabled:
            return
        if not prefs.backup_when_versions_disabled:
            return
        if bpy.context.preferences.filepaths.save_version > 0:
            return
        # Only an overwrite of the current file loses data; Save As to a new
        # path leaves the old file on disk.
        if not filepath or not bpy.data.filepath:
            return
        if not _same_path(filepath, bpy.data.filepath):
            return
        src = Path(filepath)
        if not src.is_file():
            return
        if src.parent.name in core.backup_dir_names(prefs):
            return
        backup_dir = core.backup_dir_for(filepath, prefs.backup_dir_name)
        backup_dir.mkdir(parents=True, exist_ok=True)
        core.insert_into_chain(src, backup_dir, src.stem, prefs.max_versions, copy=True)
    except Exception as ex:
        # A failing backup must never break the user's save.
        print(f"SaveOpsA2: pre-save backup failed: {ex}")


@persistent
def saveopsa2_save_post(filepath, *_):
    """Move the .blendN files Blender just created into the backup chain."""
    try:
        if core._internal_save_in_progress:
            return
        # copy=True saves also fire save_post, with the copy's path; the main
        # file path is only what the user actually saved.
        if not filepath or not bpy.data.filepath:
            return
        if not _same_path(filepath, bpy.data.filepath):
            return
        prefs = get_prefs()
        if not prefs.save_backup_enabled:
            return
        path = Path(filepath)
        # Saving a file that already lives in a backup folder must not nest.
        if path.parent.name in core.backup_dir_names(prefs):
            return
        core.move_blendn_files(filepath, prefs)
    except Exception as ex:
        print(f"SaveOpsA2: post-save backup failed: {ex}")


def autosave_tick():
    try:
        prefs = get_prefs()
    except Exception:
        return 60.0
    interval = max(prefs.autosave_interval_min, 1) * 60.0
    if not prefs.autosave_enabled:
        return interval
    if bpy.app.background:
        return interval
    if not bpy.data.filepath or not bpy.data.is_dirty:
        return interval
    for job in ('RENDER', 'RENDER_PREVIEW'):
        try:
            if bpy.app.is_job_running(job):
                return 30.0  # busy: retry soon instead of skipping a whole interval
        except TypeError:
            pass
    ok, msg = core.snapshot_copy(prefs)
    if not ok:
        print(f"SaveOpsA2: auto-backup failed: {msg}")
    return interval


def ensure_timer_state():
    try:
        prefs = get_prefs()
        enabled = prefs.autosave_enabled
    except Exception:
        enabled = False
    registered = bpy.app.timers.is_registered(autosave_tick)
    if enabled and not registered:
        interval = max(prefs.autosave_interval_min, 1) * 60.0
        # persistent=True keeps the timer alive across file loads.
        bpy.app.timers.register(autosave_tick, first_interval=interval, persistent=True)
    elif not enabled and registered:
        bpy.app.timers.unregister(autosave_tick)


def register():
    h = bpy.app.handlers
    if saveopsa2_save_pre not in h.save_pre:
        h.save_pre.append(saveopsa2_save_pre)
    if saveopsa2_save_post not in h.save_post:
        h.save_post.append(saveopsa2_save_post)
    ensure_timer_state()


def unregister():
    h = bpy.app.handlers
    if saveopsa2_save_pre in h.save_pre:
        h.save_pre.remove(saveopsa2_save_pre)
    if saveopsa2_save_post in h.save_post:
        h.save_post.remove(saveopsa2_save_post)
    if bpy.app.timers.is_registered(autosave_tick):
        bpy.app.timers.unregister(autosave_tick)
