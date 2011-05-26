import raytrace 
from raytrace import objects

w=raytrace.World()
w.add_object(objects.Sphere(center=(0.0,0.0,0.0), radius=10.0, color=(1.0,1.0,1.0)))
w.add_object(objects.Sphere(center=(50.0,0.0,0.0), radius=10.0, color=(1.0,0.0,0.0)))
w.add_object(objects.Sphere(center=(0.0,50.0,0.0), radius=10.0, color=(0.0,1.0,0.0)))
w.add_object(objects.Sphere(center=(0.0,0.0,50.0), radius=10.0, color=(0.0,0.0,1.0)))
w.render()

