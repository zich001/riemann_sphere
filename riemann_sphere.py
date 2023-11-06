import bpy
import numpy as np
from mathutils import Vector
#Define SF
sf=2 # The scale factor of square relative to unit square in Blender 2.8
def projection(u, v):
  try:
    u*=sf
    v*=sf
    theta = np.pi - 2*(np.arctan((u**2+v**2)**(1/2)))
    phi = np.arctan(v/u)
    if u < 0:
      phi = phi + np.pi 
    z = np.cos(theta)
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    
    return Vector((x/sf,y/sf,z/sf))
  except:
    return Vector((0,0,0))

plane = bpy.context.active_object
plane.shape_key_add(name='plane')
plane.data.shape_keys.use_relative = True

sk = plane.shape_key_add(name = 'sphere')
for i in range(len(sk.data)):
    u,v,z = sk.data[i].co[:]
    sk.data[i].co = projection(u,v)
