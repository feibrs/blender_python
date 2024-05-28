import bpy
import math
import random as r

def rc():
    return [r.random() for i in range(4)]

def go(xx = 0, yy = 0, zz = 0):
    space = 2
    for x in range(4):
        for y in range(4):
            for z in range(4):
                bpy.ops.mesh.primitive_cube_add(location=(xx + x * space, yy + y * space, zz + z * space))
                
                # Make ourselves a material with a random colour
                material = bpy.data.materials.new(name='RandomColour')
                material.use_nodes = False
                material.diffuse_color = rc()
                material.roughness = 0
            
                # Apply the material to each object
                a = bpy.context.active_object
                a.data.materials.append(material)


    for i in bpy.data.collections[0].objects:
        i.scale[0] = 0
        i.scale[1] = 0
        i.scale[2] = 0
        i.keyframe_insert(data_path='scale', frame=0)

    for k, i in enumerate(bpy.data.collections[0].objects, 1):
        i.scale[0] = 1
        i.scale[1] = 1 + (math.cos(k) * 0.2)
        i.scale[2] = 1
        i.keyframe_insert(data_path='scale', frame=k)

"""
for k in range(0, 900, 60):
    for e, i in enumerate(bpy.data.collections[0].objects):
        e = int(e/2)
        i.scale[0] = math.sin(k + e) * 0.5
        i.scale[1] = math.cos(k + e) * 0.5
        i.scale[2] = math.cos(k + e) * 0.5
        i.keyframe_insert(data_path='scale', frame=k + 1)
"""

c_x, c_y, c_z = 0, 0, 0
choice = ['up', 'down', 'left', 'right', 'in', 'out']
size = 8
for cube in range(8):
    c = r.choice(choice)
    if c == 'left': c_x -= size
    elif c == 'right': c_x += size
    elif c == 'up': c_y += size
    elif c == 'down': c_y -= size
    elif c == 'in': c_z -= size
    elif c == 'out': c_z += size
    go(c_x, c_y, c_z)
