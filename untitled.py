import bpy
import random
import mathutils

"""Example of creating a camera and a few spotlights.

Although this creates quite a rudimentary scene, it is our first attempt
at adding lights and cameras to a scene with python, so pretty good considering.
"""

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

# Set out output resolutions to vertical HD
bpy.context.scene.render.resolution_x = 1080
bpy.context.scene.render.resolution_y = 1920

bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)

#bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(60, 60, 1))

def random_color():
    def r_int():
        return random.random()
    return r_int(), r_int(), r_int(), r_int()

"""
# Pop something in there to look at
for x in range(-4, 8, 2):
    for y in range(-4, 8, 2):
        bpy.ops.mesh.primitive_cube_add(location=(x-1, y-1, 0))
        
        # Make ourselves a material with a random colour
        material = bpy.data.materials.new(name='RandomColour')
        material.use_nodes = False
        material.diffuse_color = random_color()
        material.roughness = 0
        
        # Apply the material to each object
        a = bpy.context.active_object
        a.data.materials.append(material)
"""

current = mathutils.Vector()

options = ['up', 'down', 'left', 'right', 'in', 'out']

s = 2 
total = 0

for cool in range(30):
    
    current.x = random.randint(-8, 8)
    current.y = random.randint(-5, 8)
    current.z = random.randint(-8, 8) - 10
    
    material = bpy.data.materials.new(name='RandomColour')
    material.use_nodes = False
    material.diffuse_color = random_color()
    material.roughness = 0
    
    amount = random.randint(10, 40)
    total += amount
    for turn in range(amount):
        
        direction = random.choice(options)
        if direction == 'up':    
            current.y += 1 * s
        if direction == 'down':
            current.y -=1 * s
        if direction == 'right':
            current.x += 1 * s
        if direction == 'left':
            current.x -= 1 * s
        if direction == 'in':
            current.z += 1 * s
        if direction == 'out':
            current.z -= 1 * s

        bpy.ops.mesh.primitive_cube_add()
        c = bpy.context.active_object
        c.location = current
        c.data.materials.append(material)
        
for j in bpy.data.collections[0].objects:
    j.scale[0] = 0
    j.scale[1] = 0
    j.scale[2] = 0
    j.keyframe_insert(data_path='scale', frame=0)

for k, i in enumerate(bpy.data.collections[0].objects, 1):
    i.scale[0] = 0
    i.scale[1] = 0
    i.scale[2] = 0
    i.keyframe_insert(data_path='scale', frame=k-1)
    i.scale[0] = 1
    i.scale[1] = 1
    i.scale[2] = 1
    i.keyframe_insert(data_path='scale', frame=k)

"""
# For each 30 second section, go through the collection,
# if its's a cube, scale the object to a random size
# and add a keyframe to it.
for k in range(total, total+900, 120):
    for e, i in enumerate(bpy.data.collections[0].objects):
        if 'Cube' in i.name:
            if e == 0:
                for axis in range(3):
                    i.scale[axis] = 1
            for j in range(3):
                i.scale[j] = random.randint(0, 2)
            i.keyframe_insert(data_path='scale', frame=k)
"""

# Render up until the 900th frame
bpy.context.scene.frame_end = total

# Create a grid of spotlights hovering obove the scene
count = 1
for x in range(0, 20, 2):
    for y in range(0, 20, 2):
        bpy.ops.object.light_add(type='POINT', location=(x-10+1, y-10+1, 10))
        light = bpy.context.object
        light.name = "Light" + str(count)
        count +=1

# Add ourselves a camera
#bpy.ops.object.camera_add(location=(0, -10, 4), rotation=(1.2, 0, 0))
bpy.ops.object.camera_add(location=(34, -34, 4.8), rotation=(1.2, 0, 0.8))
#bpy.ops.object.camera_add(location=(0, 0, 28), rotation=(0, 0.1, 0.3))
camera = bpy.context.object
camera.name = "Camera"

bpy.context.object.data.lens = 50

# Hopefully ths will get rid of flickering
bpy.context.object.data.clip_start = 1
bpy.context.object.data.clip_end = 50