
"""Essai pour Mofifier la classe Union

Le but est de permettre d'exercer une introspection pour que la classe connaisse les dimensions de l'objet
qu'elle représente. Cela permettrait de réaliser des opérations de type : déplacer de la moitié de l'objet enfant..."""
import sys, os
sys.path.insert(
    0,
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)
from openpyscad import *

U = Union()

U.append(Cube([10, 20, 30]))
U.append(Cube([10, 10, 5]).translate([0, 0, 20]))

vol1 = Volume([10, 5, 4])
vol2 = Volume(4, 5, 100)
vol1.union(vol2)  # ajoute

vol3 = Volume(-10, 0, 10)
vol = vol2.union(vol3)

print(vol1, vol2, vol3, vol)

T = Truc()

output_file = __file__.replace('.py', '.scad')
U.write(output_file, with_print=True)
