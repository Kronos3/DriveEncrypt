#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  meta.py
#
#  Copyright 2016 Andrei Tumbar <atuser@Kronos>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

def safe_dict (_dict, key):
    try:
        _dict[key]
    except KeyError:
        return None
    else:
        return _dict[key]

class meta:
    def __init__ (self):
        self.path = None
        self.mime = None
        self.size = None
        self.gdid = None
        self._enc = False
        self.s_enc = None # Size of encryption
        self.file = None # FILE * object
        self.last_mod = None
        self.creation = None
        self.owner = None
    
    def generate  (self, _dict):
        for key in _dict:
            exec ("self.%s = _dict['%s']" % (key, key))