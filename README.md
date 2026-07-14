# SaveOpsA2

Blend file backups on save and timed auto-backup copies, for Blender 4.2+.

![Preferences](docs/SaveOpsA2_UI_preference.png)

> [!WARNING]
> **SaveOpsA2 is fully independent of Blender's built-in backup features.**
> It never changes Blender's *Save Versions* or crash-recovery autosave.
> The backup **folder, naming and generation count** are all the add-on's
> own settings — nothing overlaps, nothing conflicts.

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

1. Download `saveopsa2-<version>.zip` (or build it from source, see below).
2. In Blender: `Edit → Preferences → Get Extensions → ⌄ (top-right menu) →
   Install from Disk…` and pick the zip.
3. Enable **SaveOpsA2**.

Requires Blender 4.2 or newer. The UI is available in English and Japanese.

## Building from source

```
blender --command extension build --source-dir saveopsa2 --output-dir dist
```

## License

GPL-3.0-or-later

---

# 日本語

Blender 4.2+ 向けの保存バックアップ拡張です。保存時のバックアップ保管と、
タイマーによる自動バックアップコピーを行います。

> [!WARNING]
> **SaveOpsA2 は Blender 標準のバックアップ機能から完全に独立しています。**
> 標準の「保存バージョン数（Save Versions）」やクラッシュ復旧用の自動保存の
> 設定・動作は一切変更しません。バックアップの**フォルダ・命名・世代数**は
> すべてアドオン独自の設定で、標準機能と重複も競合もしません。

## 機能

### 保存時バックアップ — .blendN チェーン

保存のたびに、Blender がファイルの隣に作る `.blend1` を `_backup/`
サブフォルダへ移動し、`<名前>.blend1`（最新）〜 `<名前>.blendN`（最古）として
保持します。標準の Save Versions と同じ命名規則を別フォルダで運用するため、
プロジェクトフォルダが散らかりません。

- 世代数はアドオン独自の **Backup Versions** 設定（既定 10）。Blender 本体の
  「保存バージョン数」とは無関係です
- ローテーションが改名・削除するのは**同じファイル名 stem に完全一致する
  ファイルだけ**。フォルダ内の他のファイルには絶対に触れません
- **.blend1 が作られなくてもバックアップ** — 「保存バージョン数」が 0 の
  環境では、上書き直前の古いファイルをコピーしてチェーンに退避します
- グループヘッダのチェックボックスで機能ごと無効化できます

### 自動バックアップ — 定期スナップショット

未保存の変更がある間、タイムスタンプ付きコピー
（`<名前>_auto_YYYYMMDD-HHMMSS.blend`）を `_autobackup/` サブフォルダへ
設定間隔（既定 5 分）で書き出します。

- 本体ファイルには一切触れません。保存状態・undo 履歴・「未保存」フラグは
  そのまま維持されます
- レンダリング中はスキップし、少し後に再試行します
- ファイルごとに独自の保持数（既定 10）でローテーションします
- バックアップの失敗がユーザーの保存を妨げることはありません

### File メニュー

- **今すぐバックアップ** — スナップショットコピーを即時書き出し
- **バックアップフォルダを開く** / **自動バックアップフォルダを開く** —
  各フォルダをシステムのファイルブラウザで開きます

## インストール

1. `saveopsa2-<version>.zip` を入手します（下記の手順でソースからビルドも可）
2. Blender の `編集 → プリファレンス → エクステンション入手 → 右上の ⌄ →
   ディスクからインストール…` で zip を選択
3. **SaveOpsA2** を有効化

Blender 4.2 以降が必要です。UI は英語と日本語に対応しています。

## ソースからのビルド

```
blender --command extension build --source-dir saveopsa2 --output-dir dist
```

## ライセンス

GPL-3.0-or-later
