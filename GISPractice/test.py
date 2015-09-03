__author__ = 'wickes1'


from nominatim import Nominatim

nom = Nominatim()

result = nom.query("1904 Oliver Dr, Champaign, IL")

result

def foo(fuzzy):
    """pass it something fuzzy and it'll return five of that"""
    return fuzzy * 5

print foo()