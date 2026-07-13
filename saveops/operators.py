# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.props import EnumProperty

from . import core
from .prefs import get_prefs


class SAVEOPS_OT_backup_now(bpy.types.Operator):
    bl_idname = "saveops.backup_now"
    bl_label = "Backup Now"
    bl_description = "Save a timestamped snapshot copy into the backup folder"

    @classmethod
    def poll(cls, context):
        return bool(bpy.data.filepath)

    def execute(self, context):
        ok, msg = core.snapshot_copy(get_prefs(context))
        self.report({'INFO'} if ok else {'ERROR'}, msg)
        return {'FINISHED'} if ok else {'CANCELLED'}


class SAVEOPS_OT_open_backup_folder(bpy.types.Operator):
    bl_idname = "saveops.open_backup_folder"
    bl_label = "Open Backup Folder"
    bl_description = "Open this file's backup folder in the system file browser"

    which: EnumProperty(
        name="Folder",
        items=(
            ('SAVE', "Save Backups", "Folder holding backups made on save"),
            ('AUTO', "Auto-Backups", "Folder holding timer snapshot copies"),
        ),
        default='SAVE',
    )

    @classmethod
    def poll(cls, context):
        return bool(bpy.data.filepath)

    def execute(self, context):
        prefs = get_prefs(context)
        dir_name = prefs.backup_dir_name if self.which == 'SAVE' else prefs.auto_backup_dir_name
        backup_dir = core.backup_dir_for(bpy.data.filepath, dir_name)
        if not backup_dir.is_dir():
            self.report({'ERROR'}, "No backup folder yet")
            return {'CANCELLED'}
        bpy.ops.wm.path_open(filepath=str(backup_dir))
        return {'FINISHED'}


def draw_file_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(SAVEOPS_OT_backup_now.bl_idname, icon='FILE_TICK')
    op = layout.operator(
        SAVEOPS_OT_open_backup_folder.bl_idname, icon='FILE_FOLDER'
    )
    op.which = 'SAVE'
    # A second entry only makes sense when auto-backups live somewhere else.
    if len(core.backup_dir_names(get_prefs(context))) > 1:
        op = layout.operator(
            SAVEOPS_OT_open_backup_folder.bl_idname,
            text="Open Auto-Backup Folder",
            icon='FILE_FOLDER',
        )
        op.which = 'AUTO'


_classes = (
    SAVEOPS_OT_backup_now,
    SAVEOPS_OT_open_backup_folder,
)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file.append(draw_file_menu)


def unregister():
    bpy.types.TOPBAR_MT_file.remove(draw_file_menu)
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
