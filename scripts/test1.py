import raytrace 
from raytrace import objects

w=raytrace.World()
w.add_object(objects.Sphere(center=(0.0,-25.0,0.0), radius=80.0, color=(1.0,0.0,0.0)))
w.add_object(objects.Sphere(center=(0.0,30.0,0.0), radius=60.0, color=(1.0,1.0,0.0)))
w.add_object(objects.Plane(point=(0.0,0.0,0.0), normal=(0,1.0,1.0), color=(0.0,0.3,0.0)))
w.render()

