# SPDX-License-Identifier: GPL-3.0-or-later
"""SaveOpsA2: blend file backups on save and on a timer."""

import bpy

from . import handlers, operators, prefs, translations

# handlers last: its timer reads preferences on registration.
_modules = (prefs, operators, handlers)


def register():
    bpy.app.translations.register(__package__, translations.translations_dict)
    for module in _modules:
        module.register()


def unregister():
    for module in reversed(_modules):
        module.unregister()
    bpy.app.translations.unregister(__package__)
