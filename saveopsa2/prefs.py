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
        name="Save Backups to Keep",
        description="How many moved .blend1 backups to keep per file",
        default=10,
        min=1,
        soft_max=100,
    )
    backup_when_versions_disabled: BoolProperty(
        name="Backup on Save when 'Save Versions' is 0",
        description=(
            "If Blender's Save Versions preference is 0 no .blend1 is created; "
            "copy the previous file into the backup folder before it is overwritten"
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
        default="_backup",
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
        layout.label(
            text="Blender's own crash-recovery autosave (temp folder) is not affected.",
            icon='INFO',
        )


def get_prefs(context=None):
    context = context or bpy.context
    return context.preferences.addons[__package__].preferences


def register():
    bpy.utils.register_class(SAVEOPSA2_Preferences)


def unregister():
    bpy.utils.unregister_class(SAVEOPSA2_Preferences)
