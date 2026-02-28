#!/usr/bin/python3
"""BaseGeometry modulunu təyin edir."""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza klası."""

    def area(self):
        """Sahəni hesablayır (hələ tətbiq edilməyib)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin müsbət tam ədəd olub-olmadığını yoxlayır.

        Args:
            name (str): Parametrin adı (həmişə string).
            value (int): Yoxlanılacaq dəyər.
        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçik və ya bərabərdirsə.
        """
        # PEP 8 (E721) xətasının həlli: '==' əvəzinə 'is not' istifadəsi
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
