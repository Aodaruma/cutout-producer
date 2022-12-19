import bpy


class COP_PT_3DviewPanel(bpy.types.Panel):
    bl_label = "Cutout Producer"
    bl_idname = "OBJECT_PT_cutout_producer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Cutout Producer'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.cutout_producer")
