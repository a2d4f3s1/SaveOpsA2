# SPDX-License-Identifier: GPL-3.0-or-later
"""UI translation dictionary. English is the source language written in the
code; Blender looks strings up here when the interface language matches."""

translations_dict = {
    "ja_JP": {
        # --- Preferences: On Save ---
        ("*", "On Save"):
            "保存時",
        ("*", "Move the .blendN backups Blender creates on save into the backup folder"):
            "保存時に Blender が作る .blendN バックアップをバックアップフォルダへ"
            "移動します",
        ("*", "Backup Folder Name"):
            "バックアップフォルダ名",
        ("*", "Subfolder next to the blend file where backups are stored"):
            "バックアップを保存する、.blend ファイルと同じ場所のサブフォルダ",
        ("*", "Backup Versions"):
            "バックアップ世代数",
        ("*", "How many .blendN backups to keep in the backup folder, "
              "independent of Blender's own Save Versions setting"):
            "バックアップフォルダ内に保持する .blendN の世代数"
            "（Blender 本体の「バージョンを保存」設定とは独立）",

        # --- Preferences: Auto-Backup ---
        ("*", "Auto-Backup"):
            "自動バックアップ",
        ("*", "Periodically save a timestamped copy without touching the main file"):
            "本体ファイルには触れずに、タイムスタンプ付きコピーを定期的に保存します",
        ("*", "Auto-Backup Folder Name"):
            "自動バックアップフォルダ名",
        ("*", "Subfolder next to the blend file where auto-backup copies are "
              "stored; use the same name as the save backup folder to share one folder"):
            "自動バックアップのコピーを保存するサブフォルダ"
            "（保存時バックアップと同じ名前にすると 1 つのフォルダを共用します）",
        ("*", "Interval (minutes)"):
            "間隔（分）",
        ("*", "How often to write an auto-backup while the file has unsaved changes"):
            "未保存の変更がある間、自動バックアップを書き出す間隔",
        ("*", "Auto-Backups to Keep"):
            "自動バックアップ保持数",
        ("*", "How many auto-backup copies to keep per file"):
            "ファイルごとに保持する自動バックアップの数",
        ("*", 'SaveOpsA2 does not touch Blender\'s "Save Versions" or "Auto-Save"'):
            "SaveOpsA2 は Blender 標準の「バージョンを保存」、「自動保存」には"
            "手を加えません",
        ("*", 'On Save: moves the .blend1 created by "Save Versions" into the '
              "backup folder (even when it is 0, backups are still saved as .blendN)"):
            "保存時: 「バージョンを保存」が作る .blend1 をバックアップフォルダへ"
            "移します（0 の場合も、.blendN で自動で退避します）",
        ("*", "Auto-Backup: writes its own timestamped copies to a separate folder"):
            "自動バックアップ: 独自のタイムスタンプ付きコピーを別フォルダに"
            "書き出します",

        # --- Operators / File menu ---
        ("*", "Backup Now"):
            "今すぐバックアップ",
        ("*", "Save a timestamped snapshot copy into the backup folder"):
            "タイムスタンプ付きのスナップショットコピーをバックアップフォルダへ保存します",
        ("*", "Open Backup Folder"):
            "バックアップフォルダを開く",
        ("*", "Open this file's backup folder in the system file browser"):
            "このファイルのバックアップフォルダをシステムのファイルブラウザで開きます",
        ("*", "Open Auto-Backup Folder"):
            "自動バックアップフォルダを開く",
        ("*", "Folder"):
            "フォルダ",
        ("*", "Save Backups"):
            "保存時バックアップ",
        ("*", "Folder holding backups made on save"):
            "保存時に作られたバックアップが入るフォルダ",
        ("*", "Auto-Backups"):
            "自動バックアップ",
        ("*", "Folder holding timer snapshot copies"):
            "タイマーによるスナップショットコピーが入るフォルダ",

        ("*", "Reset All Preferences"):
            "すべての設定をリセット",
        ("*", "Reset every SaveOpsA2 setting to its default value"):
            "SaveOpsA2 の設定をすべてデフォルト値に戻します",

        # Operator button labels are looked up with the "Operator" context.
        ("Operator", "Backup Now"):
            "今すぐバックアップ",
        ("Operator", "Open Backup Folder"):
            "バックアップフォルダを開く",
        ("Operator", "Open Auto-Backup Folder"):
            "自動バックアップフォルダを開く",
        ("Operator", "Reset All Preferences"):
            "すべての設定をリセット",

        # --- Report messages ---
        ("*", "Preferences reset to defaults"):
            "設定をデフォルト値に戻しました",
        ("*", "No backup folder yet"):
            "バックアップフォルダはまだありません",
        ("*", "File has not been saved yet"):
            "ファイルはまだ保存されていません",
        ("*", "File is inside a backup folder, skipping snapshot"):
            "ファイルがバックアップフォルダ内にあるため、スナップショットを"
            "スキップしました",
        ("*", "Could not create backup folder: {error}"):
            "バックアップフォルダを作成できませんでした: {error}",
        ("*", "Backup failed: {error}"):
            "バックアップに失敗しました: {error}",
        ("*", "Backup saved: {name}"):
            "バックアップを保存しました: {name}",
    },
}
