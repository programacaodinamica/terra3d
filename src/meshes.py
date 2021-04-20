from math import pi, cos, sin


def sphere(r=1, paralelos=10, meridianos=20):
    epsilon = 0.00005
    vertices = []
    uvtex = []

    for p in range(paralelos):
        phi = p * ((pi - 2*epsilon)/(paralelos-1)) + epsilon
        for m in range(meridianos):
            theta = m * (2*pi/meridianos)
            uv = ((1.0/meridianos)*m, (1.0/(paralelos-1))*p)
            uvtex.append(uv)
            v = (-r*sin(theta)*sin(phi), r*cos(phi), r*cos(theta)*sin(phi))
            vertices.append(v)
        theta = 0.0
        uvtex.append((1.0, (1.0/(paralelos-1))*p))
        v = (-r*sin(theta)*sin(phi), r*cos(phi), r*cos(theta)*sin(phi))
        vertices.append(v)

    faces = []
    for i in range(paralelos-1):
        for j in range(meridianos):
            t1 = (i*(meridianos+1) + j,
                            (i+1)*(meridianos+1) + j+1,
                            (i+1)*(meridianos+1) + j)
            t2 = (i*(meridianos+1) +j,
                            i*(meridianos+1) + j+1,
                            (i+1)*(meridianos+1) + j+1)
            faces.append(tuple((k+1 for k in t1)))
            faces.append(tuple((k+1 for k in t2)))
    
    return vertices, faces, uvtex
    

def quad():
    vertices = [
        (1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0)
    ]
    uvtextures = [
        (1.0, 0.0), 
        (0.0, 0.0), 
        (0.0, 1.0), 
        (1.0, 1.0)
    ]
    indices = [
        (1, 2, 3), (3, 4, 1)
    ]
    return vertices, indices, uvtextures