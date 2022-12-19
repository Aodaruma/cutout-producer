import bpy


class COP_OT_EditMesh(bpy.types.Operator):
    bl_idname = "object.cutout_producer"
    bl_label = "Cutout Producer"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}
