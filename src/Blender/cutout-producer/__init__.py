import bpy
import os

from . import ui, operator

bl_info = {
    "name": "Cutout Producer",
    "author": "Aodaruma",
    "version": (0, 0, 1),
    "blender": (3, 3, 0),
    "location": "View3D > Sidebar > Cutout Producer",
    "description": "Helper of making cutout animation in Blender",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"
}

register_class_tuples = [
    ui.register_classes,
    operator.register_classes,
]


def register():
    for register_class_tuple in register_class_tuples:
        for register_class in register_class_tuple:
            bpy.utils.register_class(register_class)

    print("Registered {} with {} modules".format(
        bl_info["name"], len(register_class_tuples)))


def unregister():
    for register_class_tuple in reversed(register_class_tuples):
        for register_class in reversed(register_class_tuple):
            bpy.utils.unregister_class(register_class)

    print("Unregistered {}".format(bl_info["name"]))


if __name__ == "__main__":
    register()
