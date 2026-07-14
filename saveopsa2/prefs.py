# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.app.translations import pgettext_rpt as rpt_
from bpy.props import BoolProperty, IntProperty, StringProperty

# Every user-facing setting, for the reset operator. Kept explicit so RNA
# internals like bl_idname can never be unset by accident.
_PREF_PROPS = (
    "save_backup_enabled",
    "backup_dir_name",
    "max_versions",
    "autosave_enabled",
    "auto_backup_dir_name",
    "autosave_interval_min",
    "max_auto_copies",
)


def _on_autosave_toggle(self, context):
    from . import handlers
    handlers.ensure_timer_state()


class SAVEOPSA2_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    save_backup_enabled: BoolProperty(
        name="On Save",
        description="Move the .blendN backups Blender creates on save into the backup folder",
        default=True,
    )
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
    autosave_enabled: BoolProperty(
        name="Auto-Backup",
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

        box = layout.box()
        box.alert = True
        box.label(
            text='SaveOpsA2 does not touch Blender\'s "Save Versions" or "Auto-Save"',
            icon='ERROR',
        )
        sub = box.column(align=True)
        sub.label(
            text='On Save: moves the .blend1 created by "Save Versions" into the '
                 "backup folder (even when it is 0, backups are still saved as .blendN)"
        )
        sub.label(text="Auto-Backup: writes its own timestamped copies to a separate folder")

        box = layout.box()
        row = box.row()
        row.prop(self, "save_backup_enabled", text="")
        row.label(text="On Save")
        col = box.column()
        col.active = self.save_backup_enabled
        col.prop(self, "backup_dir_name")
        col.prop(self, "max_versions")

        box = layout.box()
        row = box.row()
        row.prop(self, "autosave_enabled", text="")
        row.label(text="Auto-Backup")
        col = box.column()
        col.active = self.autosave_enabled
        col.prop(self, "auto_backup_dir_name")
        col.prop(self, "autosave_interval_min")
        col.prop(self, "max_auto_copies")

        layout.separator()
        layout.operator(SAVEOPSA2_OT_reset_preferences.bl_idname, icon='LOOP_BACK')


class SAVEOPSA2_OT_reset_preferences(bpy.types.Operator):
    bl_idname = "saveopsa2.reset_preferences"
    bl_label = "Reset All Preferences"
    bl_description = "Reset every SaveOpsA2 setting to its default value"

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        prefs = get_prefs(context)
        for name in _PREF_PROPS:
            # Drops the stored override so the class default shows through.
            prefs.property_unset(name)
        # property_unset does not fire update callbacks; resync the timer.
        from . import handlers
        handlers.ensure_timer_state()
        self.report({'INFO'}, rpt_("Preferences reset to defaults"))
        return {'FINISHED'}


def get_prefs(context=None):
    context = context or bpy.context
    return context.preferences.addons[__package__].preferences


_classes = (
    SAVEOPSA2_Preferences,
    SAVEOPSA2_OT_reset_preferences,
)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
