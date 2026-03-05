# Blender Python: CORE-001 Segment 1 Setup
# Usage: blender --background --python seg1_setup.py
# Creates: orthographic scene, color materials, camera, simple assets for S1 (split view) and S3 (title card)

import bpy

# Reset
bpy.ops.wm.read_factory_settings(use_empty=True)

# Scene settings
scene = bpy.context.scene
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.image_settings.file_format = 'PNG'
scene.display_settings.display_device = 'sRGB'

# Remove default cube
for obj in list(bpy.data.objects):
    bpy.data.objects.remove(obj, do_unlink=True)

# Colors
palette = {
    "real": (0.117, 0.533, 0.898, 1.0),      # blue
    "imag": (0.961, 0.486, 0.0, 1.0),        # orange
    "mag": (0.263, 0.627, 0.278, 1.0),       # green
    "angle": (0.557, 0.141, 0.667, 1.0),     # purple
    "white": (1, 1, 1, 1),
    "dark": (0.08, 0.08, 0.08, 1),
    "gray": (0.7, 0.7, 0.7, 1),
    "red": (0.9, 0.15, 0.15, 1),
    "green": (0.15, 0.7, 0.2, 1),
}

materials = {}
for name, rgba in palette.items():
    mat = bpy.data.materials.new(name=f"MAT_{name.upper()}")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
    bsdf.inputs[0].default_value = rgba  # Base Color
    bsdf.inputs[7].default_value = 1.0   # Roughness
    materials[name] = mat

# World background (flat)
if bpy.context.scene.world is None:
    bpy.context.scene.world = bpy.data.worlds.new("World")
world = bpy.context.scene.world
world.use_nodes = True
nodes = world.node_tree.nodes
bg_node = nodes.get("Background")
if bg_node is None:
    bg_node = nodes.new(type="ShaderNodeBackground")
bg_node.inputs[0].default_value = palette['white']

# Camera
cam_data = bpy.data.cameras.new("Cam")
cam_data.type = 'ORTHO'
cam_data.ortho_scale = 10
cam = bpy.data.objects.new("Cam", cam_data)
scene.collection.objects.link(cam)
cam.location = (0, -10, 0)
cam.rotation_euler = (1.5708, 0, 0)
scene.camera = cam

# Helper: create plane

def make_plane(name, size=(4, 3), loc=(0,0,0), mat=None):
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=loc)
    obj = bpy.context.view_layer.objects.active
    obj.name = name
    obj.scale.x = size[0] / 2
    obj.scale.y = size[1] / 2
    if mat:
        obj.data.materials.append(mat)
    return obj

# Helper: create text

def make_text(name, content, loc=(0,0,0), scale=1.0, mat=None, align='CENTER'):
    txt = bpy.data.curves.new(type="FONT", name=f"CURVE_{name}")
    txt.body = content
    txt.align_x = align
    txt_obj = bpy.data.objects.new(name, txt)
    txt_obj.scale = (scale, scale, scale)
    txt_obj.location = loc
    if mat:
        txt_obj.data.materials.append(mat)
    scene.collection.objects.link(txt_obj)
    bpy.context.view_layer.update()
    return txt_obj

# Collection for SEG1
seg_col = bpy.data.collections.new("SEG1")
scene.collection.children.link(seg_col)

# Shot S1: Split screen (Trig vs Complex)
left = make_plane("S1_LEFT", size=(4.8, 3.4), loc=(-2.6, 0, 0), mat=materials['gray'])
right = make_plane("S1_RIGHT", size=(4.8, 3.4), loc=(2.6, 0, 0), mat=materials['white'])
seg_col.objects.link(left)
seg_col.objects.link(right)

make_text("S1_TRIG_LABEL", "Trigonometri: 5 langkah, 10 menit", loc=(-2.6, 0, 0.05), scale=0.18, mat=materials['red'], align='CENTER')
make_text("S1_COMPLEX_LABEL", "Kompleks: 1 operasi, 10 detik", loc=(2.6, 0, 0.05), scale=0.18, mat=materials['green'], align='CENTER')

# Simple check/X marks (as planes)
bpy.ops.mesh.primitive_plane_add(size=0.5, location=(-2.6, 0.9, 0.01))
bpy.context.view_layer.update()
x_mark = bpy.context.view_layer.objects.active
x_mark.name = "S1_X"
x_mark.data.materials.append(materials['red'])

bpy.ops.mesh.primitive_plane_add(size=0.5, location=(2.6, 0.9, 0.01))
bpy.context.view_layer.update()
check = bpy.context.view_layer.objects.active
check.name = "S1_CHECK"
check.data.materials.append(materials['green'])

# Shot S3: Question card (dark bg)
q_plane = make_plane("S3_BG", size=(8.5, 4.8), loc=(0, 0, -0.01), mat=materials['dark'])
seg_col.objects.link(q_plane)
make_text("S3_QUESTION", "KENAPA HARUS BILANGAN KOMPLEKS?", loc=(0, 0, 0.02), scale=0.22, mat=materials['white'], align='CENTER')

# Arrange collections visibility
for obj in scene.collection.objects:
    obj.hide_viewport = False
    obj.hide_render = False

print("Scene ready: SEG1 base assets created. Set keyframes manually per shot.")
