
"""Essai pour Mofifier la classe Union

Le but est de permettre d'exercer une introspection pour que la classe connaisse les dimensions de l'objet
qu'elle représente. Cela permettrait de réaliser des opérations de type : déplacer de la moitié de l'objet enfant..."""
import sys, os
sys.path.insert(
    0,
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)
from openpyscad import *


vol1 = CartesianVolume([10, 5, 4], [1, 1, 1])

vol2 = CartesianVolume([50, 2, 12], [2, 2, 3])
# vol2 = Volume(4, 5, 100)
# vol1.union(vol2)  # ajoute

print(vol1,)
print(vol1.measured_volume())
print(vol2)
print(vol2.measured_volume())

print(vol1.add(vol2))
