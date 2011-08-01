import math

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def norm(a):
    return math.sqrt(sum(map(lambda x: x*x, a)))

def normalized(a):
    n = norm(a)
    return (a[0]/n, a[1]/n, a[2]/n)

def cross(b,c):
    return ( b[1]*c[2] - b[2]*c[1],
         b[2]*c[0] - b[0]*c[2],
         b[0]*c[1] - b[1]*c[0],
         )

def vecmul(n,v):
    return (v[0]*n, v[1]*n, v[2]*n)

def vecsum(a,b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

