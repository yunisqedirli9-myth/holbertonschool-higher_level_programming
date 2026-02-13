#!/usr/bin/python3

def islower(c):
    """Simvolun kiçik hərf olub-olmadığını yoxlayır."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
