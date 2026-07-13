# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.props import BoolProperty, IntProperty, StringProperty


def _on_autosave_toggle(self, context):
    from . import handlers
    handlers.ensure_timer_state()


class SAVEOPSA2_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    backup_dir_name: StringProperty(
        name="Backup Folder Name",
        description="Subfolder next to the blend file where backups are stored",
        default="_backup",
    )
    max_versions: IntProperty(
        name="Backup Versions",
        description=(
            "How many .blendN backups to keep in the backup folder, "
            "independent of Blender's own Save Versions setting"
        ),
        default=10,
        min=1,
        soft_max=100,
    )
    backup_when_versions_disabled: BoolProperty(
        name="Backup Even Without .blend1",
        description=(
            "When Blender's 'Save Versions' setting is 0, saving creates no "
            ".blend1 backup; copy the old file into the backup folder just "
            "before it is overwritten instead"
        ),
        default=True,
    )
    autosave_enabled: BoolProperty(
        name="Enable Auto-Backup",
        description="Periodically save a timestamped copy without touching the main file",
        default=True,
        update=_on_autosave_toggle,
    )
    auto_backup_dir_name: StringProperty(
        name="Auto-Backup Folder Name",
        description=(
            "Subfolder next to the blend file where auto-backup copies are stored; "
            "use the same name as the save backup folder to share one folder"
        ),
        default="_autobackup",
    )
    autosave_interval_min: IntProperty(
        name="Interval (minutes)",
        description="How often to write an auto-backup while the file has unsaved changes",
        default=5,
        min=1,
        soft_max=120,
    )
    max_auto_copies: IntProperty(
        name="Auto-Backups to Keep",
        description="How many auto-backup copies to keep per file",
        default=10,
        min=1,
        soft_max=100,
    )

    def draw(self, context):
        layout = self.layout

        col = layout.column(heading="On Save")
        col.prop(self, "backup_dir_name")
        col.prop(self, "max_versions")
        col.prop(self, "backup_when_versions_disabled")

        layout.separator()

        col = layout.column(heading="Auto-Backup")
        col.prop(self, "autosave_enabled")
        sub = col.column()
        sub.active = self.autosave_enabled
        sub.prop(self, "auto_backup_dir_name")
        sub.prop(self, "autosave_interval_min")
        sub.prop(self, "max_auto_copies")

        layout.separator()
        box = layout.box()
        box.alert = True
        box.label(
            text="Fully independent of Blender's built-in backup features",
            icon='ERROR',
        )
        box.label(text="Save Versions and crash-recovery autosave are not changed")
        box.label(text="Folder, naming and count above are SaveOpsA2's own settings")


def get_prefs(context=None):
    context = context or bpy.context
    return context.preferences.addons[__package__].preferences


def register():
    bpy.utils.register_class(SAVEOPSA2_Preferences)


def unregister():
    bpy.utils.unregister_class(SAVEOPSA2_Preferences)
