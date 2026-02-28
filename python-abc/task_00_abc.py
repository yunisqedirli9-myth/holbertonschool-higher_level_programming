#!/usr/bin/python3
"""
Abstrakt klas və onun törəmələrini təyin edən modul.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal abstrakt baza klası.
    Bu klasdan birbaşa obyekt yaratmaq mümkün deyil.
    """

    @abstractmethod
    def sound(self):
        """
        Heyvanın səsini qaytaran abstrakt metod.
        Törəmə klaslar tərəfindən tətbiq edilməlidir.
        """
        pass


class Dog(Animal):
    """Animal klasından törəyən Dog klası."""

    def sound(self):
        """İtin səsini qaytarır."""
        return "Bark"


class Cat(Animal):
    """Animal klasından törəyən Cat klası."""

    def sound(self):
        """Pişiyin səsini qaytarır."""
        return "Meow"
