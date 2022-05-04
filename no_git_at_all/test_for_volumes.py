
"""Essai pour Mofifier la classe Union

Le but est de permettre d'exercer une introspection pour que la classe connaisse les dimensions de l'objet
qu'elle représente. Cela permettrait de réaliser des opérations de type : déplacer de la moitié de l'objet enfant..."""
import sys, os
sys.path.insert(
    0,
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)
from openpyscad import *
import copy

vol1 = CartesianVolume([10, 5, 4], [1, 1, 1])
vol2 = CartesianVolume([50, 2, 12], [2, 2, 3])
# vol2 = Volume(4, 5, 100)
# vol1.union(vol2)  # ajoute

print(vol1,)
print(vol1.measured_volume())
print(vol2)
print(vol2.measured_volume())
print(vol1.add(vol2))


print("AUTRE test")
vol1 = CartesianVolume([10, 5, 4], [10, 10, 10])      # red
vol2 = CartesianVolume([20, 2, 12], [-10, -10, -10])  # blue
# vol2 = Volume(4, 5, 100)
# vol1.union(vol2)  # ajoute

print(vol1,)
print(vol1.measured_volume())
print(vol2)
print(vol2.measured_volume())
print(vol1.add(vol2))

def cv_to_ospenscad(cv):
    """transform a Cartesian Volume to its representation in openSCAD"""
    U = Union()
    U.append(Cube([cv.x, cv.y, cv.z]).translate([cv._or_x, cv._or_y, cv._or_z]))
    return U

# graphical representation of the addition of 2 CartesianVolumes
v1 = cv_to_ospenscad(vol1).color('red', 0.2)
v2 = cv_to_ospenscad(vol2).color('blue', 0.2)
v3 = cv_to_ospenscad(vol1.add(vol2)).color('green', 0.2)

output_file = __file__.replace('.py', '.scad')
(v1 + v2 + v3).write(output_file, with_print=True)
