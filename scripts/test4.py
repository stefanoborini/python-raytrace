import raytrace 
from raytrace import objects
from raytrace import samplers
from raytrace import cameras

w=raytrace.World()
w.set_sampler(samplers.Random(16,2))
w.add_object(objects.Plane( point=(0.0,0.0,0.0), normal=(0.0,1.0,0.0), color=(0.3, 0.3, 0.3)))
w.add_object(objects.Sphere(center=(0.0,0.0,0.0), radius=5.0, color=(1.0,0.0,0.0)))
w.add_object(objects.Sphere(center=(10.0,0.0,0.0), radius=5.0, color=(1.0,0.2,0.0)))
w.add_object(objects.Sphere(center=(20.0,0.0,0.0), radius=5.0, color=(1.0,0.4,0.0)))
w.add_object(objects.Sphere(center=(30.0,0.0,0.0), radius=5.0, color=(1.0,0.6,0.0)))
w.add_object(objects.Sphere(center=(40.0,0.0,0.0), radius=5.0, color=(1.0,0.8,0.0)))
w.add_object(objects.Sphere(center=(50.0,0.0,0.0), radius=5.0, color=(1.0,1.0,0.0)))
#w.set_camera(cameras.LensCamera(focal_plane_distance=20.0, lens_radius=5.0, look_at=(0.0,0.0,0.0), eye_point=(50.0,10.0,10.0), viewplane_distance=48.0, up_vector=(1.0,1.0,0.0)))
w.set_camera(cameras.PinholeCamera(look_at=(0.0,0.0,0.0), eye_point=(50.0,50.0,0.0), viewplane_distance=68.0, up_vector=(0.0,1.0,0.0)))
w.render()

