# SaveOpsA2

[日本語](README.md) | [English](README.en.md)

Blend file backups on save and timed auto-backup copies for Blender 4.2+,
fully independent of Blender's built-in backup features.

![Preferences](docs/SaveOpsA2_UI_preference.png)

> [!IMPORTANT]
> **Nothing in Blender is changed.** *Save Versions*, crash-recovery
> autosave, save state and undo history all keep working exactly as before —
> SaveOpsA2 only adds safety on top. The backup **folder, naming and
> generation count** are all its own settings, and removing the add-on
> leaves everything as it was.

## Features

### On Save — .blendN backup chain

Every time you save, the `.blend1` file Blender creates next to your file is
moved into a `_backup/` subfolder and kept as `<name>.blend1` (newest) …
`<name>.blendN` (oldest) — the same naming convention as Blender's Save
Versions, but in its own folder, so your project folder stays clean.

- The generation count is the add-on's own **Backup Versions** setting
  (default 10), independent of Blender's *Save Versions* value.
- Rotation only ever renames or deletes files that match the exact same file
  name stem. Anything else in the folder is never touched.
- **Backup Even Without .blend1** — when Blender's *Save Versions* is 0 and
  no `.blend1` is created, the old file is copied into the chain just before
  it is overwritten.
- The whole feature can be switched off with the checkbox in the group
  header.

### Auto-Backup — timed snapshot copies

While the file has unsaved changes, a timestamped copy
(`<name>_auto_YYYYMMDD-HHMMSS.blend`) is written to an `_autobackup/`
subfolder at a configurable interval (default 5 minutes).

- The main file is never touched: save state, undo history and the
  "unsaved changes" flag all stay exactly as they are.
- Skips while a render is running and retries shortly after.
- Keeps its own generation count per file (default 10).
- A failing backup never interrupts your save.

### File menu

- **Backup Now** — write a snapshot copy immediately.
- **Open Backup Folder** / **Open Auto-Backup Folder** — open the backup
  folders in the system file browser.

## Installation

1. Download `saveopsa2-<version>.zip` from
   [Releases](https://github.com/a2d4f3s1/SaveOpsA2/releases).
2. In Blender: `Edit → Preferences → Get Extensions → ⌄ (top-right menu) →
   Install from Disk…` and pick the zip.
3. Enable **SaveOpsA2**.

Requires Blender 4.2 or newer. The UI is available in English and Japanese.

## License

GPL-3.0-or-later
