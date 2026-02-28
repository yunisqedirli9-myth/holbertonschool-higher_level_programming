#!/usr/bin/python3
"""
Abstrakt klaslar və Duck Typing konseptini nümayiş etdirən modul.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Bütün həndəsi fiqurlar üçün abstrakt baza klası."""

    @abstractmethod
    def area(self):
        """Sahəni hesablayan abstrakt metod."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimetri hesablayan abstrakt metod."""
        pass


class Circle(Shape):
    """Circle (Çevrə) klası."""

    def __init__(self, radius):
        """Radiusu mənimsədir."""
        self.radius = radius

    def area(self):
        """Çevrənin sahəsini qaytarır."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Çevrənin perimetrini qaytarır."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle (Düzbucaqlı) klası."""

    def __init__(self, width, height):
        """Eni və hündürlüyü mənimsədir."""
        self.width = width
        self.height = height

    def area(self):
        """Düzbucaqlının sahəsini qaytarır."""
        return self.width * self.height

    def perimeter(self):
        """Düzbucaqlının perimetrini qaytarır."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Duck typing istifadə edərək fiqur haqqında məlumatı çap edir.
    Test sisteminin gözlədiyi dəqiq format: 'Area: {}' və 'Perimeter: {}'
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
