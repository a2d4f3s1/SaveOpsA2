# SPDX-License-Identifier: GPL-3.0-or-later
"""SaveOps: timestamped blend file backups on save and on a timer."""

from . import handlers, operators, prefs

# handlers last: its timer reads preferences on registration.
_modules = (prefs, operators, handlers)


def register():
    for module in _modules:
        module.register()


def unregister():
    for module in reversed(_modules):
        module.unregister()
