__author__ = 'wickes1'


from nominatim import Nominatim, NominatimReverse
import csv

# define function to lookup coordinates



def getCoords(location):
    nom = Nominatim()
    try:
        data = nom.query(location)
        entity = data[0]
        result = [entity['lat'], entity['lon']]
    except:
        result = False
    return result


# read in the data

players = []

with open('illinoisjeopardy.csv', 'rt') as filein:
    filein = csv.reader(filein)
    headers = next(filein)
    for player in filein:
        players.append(player)

print headers

# look through the list of player info and get out the location statements


locindex = headers.index('loc')
nameindex = headers.index('name')

writetheserows = []

for player in players:
    city = player[locindex]
    results =  getCoords(city)
    if results != False:
        lat = results[0]
        lon = results[1]
    else:
        lat = 'missing'
        lon = 'missing'
    print "done", city
    writetheserows.append([city, lat, lon])

# write the file

headers = ['city', 'lat', 'lon']

with open('illinoislatlon.csv', 'wt') as fileout:
    fileout = csv.writer(fileout)
    fileout.writerow(headers)
    fileout.writerows(writetheserows)