bl_info = {
    "name": "No Save Addon",
    "author": "pixelvisionstudios",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "description": "Hides the save button.",
    "category": "In Development",
}

import bpy

def hide_save_button(layout):
    save_button = layout.operator("wm.save_as_mainfile", text="", icon="SAVE")
    save_button.bl_idname = "fake_operator"
    save_button.bl_label = "Save (Not Really)"
    save_button.bl_description = "Save your work (or not)"

class NoSaveAddonPanel(bpy.types.Panel):
    bl_label = "No Save Addon"
    bl_idname = "PT_NoSaveAddonPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        hide_save_button(layout)

def register():
    bpy.utils.register_class(NoSaveAddonPanel)

def unregister():
    bpy.utils.unregister_class(NoSaveAddonPanel)

if __name__ == "__main__":
    register()
