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
w.set_camera(cameras.LensCamera(focal_plane_distance=50.0, lens_radius=10.0, look_at=(0.0,0.0,0.0), eye_point=(100.0,0.0,0.0), viewplane_distance=90.0, up_vector=(0.0,1.0,0.0)))
#w.set_camera(cameras.PinholeCamera(look_at=(0.0,0.0,0.0), eye_point=(100.0,0.0,0.0), viewplane_distance=90.0, up_vector=(0.0,1.0,0.0)))
w.render()

