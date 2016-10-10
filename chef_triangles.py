# codeforces, codechef and spoj

import math

is_triangle = lambda a,b,c: a+b>c and a+c>b and b+c>a

def make_right_angle_triangle(radius, side):
    # a2 + b2 = c2
    return [radius, side, math.sqrt(radius**2 + side**2)]




def get_inradius(a,b,c):
    """
    How to find the inradius of a triangle with given side lengths?
    Using Heron's Formula.
    """
    sp = (a+b+c)/2 # semi-perimeter

    # Heron's Formula:
    triangle_area = math.sqrt(sp * (sp-a) * (sp-b) * (sp-c))
    inradius = triangle_area / sp
    return inradius

def get_triangles_from_inradius(inradius):
    triangles = ((i, j, k) for i in range(inradius, 100) for j in range(inradius, 100) for k in range(inradius, 100) if is_triangle(i, j, k) and get_inradius(i,j,k) == inradius)
    triangles = sorted(set(tuple(sorted(i)) for i in triangles))
    print(triangles)
    return triangles

if __name__ == '__main__':
    n = 2
    triangles = get_triangles_from_inradius(n)
    triangle_strings = "\n".join(" ".join(str(k) for k in i) for i in triangles)
    print(len(triangles))
    print(triangle_strings)