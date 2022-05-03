
"""Essai pour Mofifier la classe Union

Le but est de permettre d'exercer une introspection pour que la classe connaisse les dimensions de l'objet
qu'elle représente. Cela permettrait de réaliser des opérations de type : déplacer de la moitié de l'objet enfant..."""

#
from openpyscad import *

class Truc():
    pass

class Volume():
    """Properties for the volume of an 3D object.
    Volume has three coordinates, that represent 3 axes dimensions.
    The volume has an implicit origin in [0, 0, 0]

    volume is always a 3 positif number suites.

    """

    def __init__(self, x=None, y=None, z=None):
        """__init__(10, 20, 30) or __init__([10, 20, 30]). Data must be positive"""
        if x and isinstance(x, list):
            if len(x) == 3:
                if x[0] >=0 and x[1] >=0 and x[2] >=0:
                    self._x = x[0]
                    self._y = x[1]
                    self._z = x[2]
                else:
                    raise ValueError("Data in Volume must be positive. Received : ", x[0], x[1], x[2] )
        else:
            if x >=0 and y >= 0 and z >= 0:
                self._x = x
                self._y = y
                self._z = z
            else:
                raise ValueError("Data in Volume must be positive. Received : ", x, y, z)
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
        """Return the Union with another Volume"""
        self.x = max(self.x, vol.x)
        self.y = max(self.y, vol.y)
        self.z = max(self.z, vol.z)
        return self

    # __add__ = append


class CartesianVolume(Volume):
    def __init__(self, vol : Volume = None, origin=[0, 0, 0]):

        print(vol, origin)
        Volume.__init__(self, vol)
        self._or_x = origin[0]
        self._or_y = origin[1]
        self._or_z = origin[2]

    def __repr__(self):
        return "CartVolume of [{}, {}, {}], origin in : [{}, {}, {}]".format(self._x, self._y, self._z,
                                                                           self._or_x, self._or_y, self._or_z)
    @property
    def abs_x(self):
        return (self.x + self._or_x)

    @property
    def abs_y(self):
        return (self.y + self._or_y)

    @property
    def abs_z(self):
        return (self.z + self._or_z)

    def measured_volume(self):
        value = self.x * self.y * self.z
        return value

    def add(self, cartvol):
        new_origin = [min(self._or_x, cartvol._or_x),
                     min(self._or_y, cartvol._or_y),
                     min(self._or_z, cartvol._or_z),]

        volume = [max(self.abs_x, cartvol.abs_x) - min(self._or_x, cartvol._or_x),
                  max(self.abs_y, cartvol.abs_y) - min(self._or_y, cartvol._or_y),
                  max(self.abs_z, cartvol.abs_z) - min(self._or_z, cartvol._or_z)
        ]
        return CartesianVolume(volume, origin= new_origin)
