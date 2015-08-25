__author__ = 'wickes1'


from nominatim import Nominatim

nom = Nominatim()

result = nom.query("1904 Oliver Dr, Champaign, IL")

result