"""/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Developer: Alan Odom
 * 
 * The Original Code is Copyright (C) 2018 Alan Odom
 * All rights reserved.
 * ***** END GPL LICENSE BLOCK *****
 */"""

bl_info={
"name": "MIDI Nodes",
"description": "MIDI NODES v 0.01",
"author": "Alan Odom",
"version": (0, 0, 1),
"blender": (2, 80, 0),
"location": "View3D > Tools Panel /Properties panel",
"wiki_url": "https://github.com/Clockmender/My-AN-Nodes",
"category": "User Interface"}

if "bpy" in locals():
    import importlib
    if 'music_nodes' in locals():
        print("reloading some_module")
        modules = (music_nodes)
        for m in modules:
            importlib.reload(m)
else:
    print("loading music_nodes for first time")
    from . import startup_music_nodes
import bpy, sys, traceback, pdb


def register():
    print("Hecate GUI: registring")
    from bpy.utils import register_class
    
    register_class(MUSIC_NODES_OT_gui)
   
   
def unregister():
    print("Hecate GUI: unregistring")
    from bpy.utils import unregister_class
    unregister_class(MUSIC_NODES_OT_gui)
    

if __name__ == "__main__":

    register()