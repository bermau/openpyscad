
"""Essai pour Mofifier la classe Union

Le but est de permettre d'exercer une introspection pour que la classe connaisse les dimensions de l'objet
qu'elle représente. Cela permettrait de réaliser des opérations de type : déplacer de la moitié de l'objet enfant..."""

#
from openpyscad import *

class Truc():
    print("passé par Truc")

class Volume():
    """Properties for the volume of an 3D object.
    The volume has an origin in [0, 0, 0]"""

    def __init__(self, x=None, y=None, z=None):
        """__init__(10, 20, 30) or __init__([10, 20, 30])"""
        if x and isinstance(x, list):
            if len(x) == 3:
                self._x = x[0]
                self._y = x[1]
                self._z = x[2]
        else:
            self._x = x
            self._y = y
            self._z = z
    def __repr__(self):
        return "Volume of [{}, {}, {}]".format(self._x, self._y, self._z)
    # Maybe there is a shortcut to avoid so many repetitions in defining x,y,z a properties
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @z.setter
    def z(self, value):
        self._z = value

    @x.deleter
    def x(self):
        del self._x

    @y.deleter
    def y(self):
        del self._y

    @z.deleter
    def z(self):
        del self._z

    @property
    def volume(self):
        return [self._x, self._y, self._z]

    size = volume

    def append(self, ):
        pass


    def union(self, vol):
        self.x = max(self.x, vol.x)
        self.y = max(self.y, vol.y)
        self.z = max(self.z, vol.z)
        return self

    # __add__ = append


class CartesianVolume(Volume):
    def __init__(self, vol:Volume = None ):
        Volume.__init__(vol)
        self._or_x = origin[0]
        self._or_y = origin[1]
        self._or_z = origin[2]

    def add(self, cartvol):

        return self
