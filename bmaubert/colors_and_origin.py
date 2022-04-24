
from openpyscad import *

eps = 0.01
X_LONG = 800
Y_LONG = 400
Z_LONG = 300
solid_wheel_radius = 12
solid_wheel_height = 11

def mark_origin(obj):
    pass

def bar_2020(l):
    """Very symple representation of V-Slot"""
    return Cube([l, 20, 20]) + Cube([2,2,2]).color('red').color(alpha=0.2)

if __name__ == '__main__':

    output_file = __file__.replace('.py', '.scad')
    C1 = Cylinder(r=solid_wheel_radius, h=solid_wheel_height).translate([60, 0, 9]). color("BLUE", 0.2)
    C2 = Cylinder(r=20, h = 15).color('#AA00FF', 0.5)    # purple-like
    # U = Sphere(r=10).color(alpha=0.5)

    (C1+C2).write(output_file, with_print=True)

"""
    C1._get_params()
    'v=[60, 0, 9]'
    C2._get_params()
    '"red"alpha=0.2'
"""









