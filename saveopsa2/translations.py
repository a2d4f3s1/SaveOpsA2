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
            "（Blender 本体の「保存バージョン数」設定とは独立）",
        ("*", "Backup Even Without .blend1"):
            ".blend1 が作られなくてもバックアップ",
        ("*", "When Blender's 'Save Versions' setting is 0, saving creates no "
              ".blend1 backup; copy the old file into the backup folder just "
              "before it is overwritten instead"):
            "Blender 本体の「保存バージョン数」が 0 だと保存時に .blend1 が"
            "作られません。代わりに、上書きされる直前の古いファイルを"
            "バックアップフォルダへコピーします",

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
        ("*", "Fully independent of Blender's built-in backup features"):
            "Blender 標準のバックアップ機能とは完全に独立しています",
        ("*", "Save Versions and crash-recovery autosave are not changed"):
            "標準の「保存バージョン数」とクラッシュ復旧用自動保存の設定・動作は"
            "一切変更しません",
        ("*", "Folder, naming and count below are SaveOpsA2's own settings"):
            "以下のフォルダ・命名・世代数はすべて SaveOpsA2 独自の設定です",

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
