import raytrace 
from raytrace import objects
from raytrace import samplers
from raytrace import cameras

w=raytrace.World()
w.set_sampler(samplers.Random(16,2))
w.add_object(objects.Sphere(center=(0.0,0.0,0.0), radius=10.0, color=(1.0,1.0,1.0)))
w.add_object(objects.Sphere(center=(50.0,0.0,0.0), radius=10.0, color=(1.0,0.0,0.0)))
w.add_object(objects.Sphere(center=(0.0,50.0,0.0), radius=10.0, color=(0.0,1.0,0.0)))
w.add_object(objects.Sphere(center=(0.0,0.0,50.0), radius=10.0, color=(0.0,0.0,1.0)))
w.render()

