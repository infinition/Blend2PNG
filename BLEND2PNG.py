import bpy  
import os

# path to the folder With R pour les double slash

file_path = bpy.data.filepath
file_name = bpy.path.display_name_from_filepath(file_path)
file_ext = '.blend'
file_dir = file_path.replace(file_name+file_ext, r'')

#set render settings
bpy.data.scenes[0].render.resolution_x = 256
bpy.data.scenes[0].render.resolution_y = 256
bpy.data.scenes[0].render.resolution_percentage = 100
#render
bpy.ops.render.opengl(view_context = False)
#save image
img_name = file_name+".png"
bpy.data.images['Render Result'].save_render(file_dir+img_name)
bpy.ops.image.open(filepath = file_dir+img_name)
bpy.data.images[img_name].pack()
#close blender
bpy.ops.wm.quit_blender()
