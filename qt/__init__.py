# Copyright (C) 2014 Oleh Prypin <blaxpirit@gmail.com>
# 
# This file is part of UniversalQt.
# 
# UniversalQt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# UniversalQt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with UniversalQt.  If not, see <http://www.gnu.org/licenses/>.


_prefer = ['pyside', 'pyqt4', 'pyqt5']

def init(*prefer):
    global _prefer
    global Signal, Slot, version
    if prefer:
        _prefer = [m.lower() for m in prefer]
    from . import core
    Signal = core.Signal
    Slot = core.Slot
    module = core.module
    version = 5 if module=='pyqt5' else 4

    globals().update((k, v) for k, v in core.Qt.__dict__.items() if not k.startswith('_'))

__all__ = 'core gui widgets network svg webkit'.split()
