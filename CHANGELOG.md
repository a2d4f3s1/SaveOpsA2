# Changelog

## 1.2.6 — 2026-07-14

Initial release.

- On-save backups: the `.blend1` Blender creates is kept as a
  `<name>.blend1..N` chain in a `_backup/` subfolder, with the add-on's own
  generation count. Rotation only affects files with the same name stem.
- Fallback for *Save Versions* = 0: the file about to be overwritten is
  copied into the chain instead.
- Auto-backup: timestamped copies (`<name>_auto_YYYYMMDD-HHMMSS.blend`)
  in `_autobackup/` while the file has unsaved changes; the main file is
  never touched.
- File menu: Backup Now, Open Backup Folder / Open Auto-Backup Folder.
- Preferences: grouped settings with per-feature enable checkboxes and a
  reset-to-defaults button.
- English / Japanese UI.
