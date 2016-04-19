#!/usr/bin/python3
# -!- encoding:utf8 -!-

import sys, requests, urllib, json, math

# --------------- CONFIGURATION ---------------------
PRETTY_PRINT=True
# ---------------------------------------------------

# ----------------- FUNCTIONS -----------------------
def geodist(coord_from, coord_to): # coord_x is a dict like {'lat':<double>,'lon':<double>}
    dlat = math.radians(coord_to['lat'] - coord_from['lat'])
    dlon = math.radians(coord_to['lon'] - coord_from['lon'])
    a = math.pow(math.sin(dlat / 2.0), 2) + math.cos(math.radians(coord_from['lat'])) * math.cos(math.radians(coord_to['lat'])) * math.pow(math.sin(dlon / 2.0), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return 6367 * c

def geoconvert(coord): # coord is a dict like {'deg':<double>,'min':<double>,'sec':<double>,'dir':'N|S|E|W'}
    a = coord['deg'] + coord['min']/60 + coord['sec']/3600
    if coord['dir'] == 'S' or coord['dir'] == 'W':
        a = -a
    return a
# ---------------------------------------------------


# ------------------ SCRIPT -------------------------
if len(sys.argv) < 2:
    print("usage : ./addrToGeoloc.py <address>\nexample : ./addrToGeoloc.py 262 rue de Crequi")
    exit()

# rebuild address
addr_parts = []
for i in range(1,len(sys.argv)):
    addr_parts.append(sys.argv[i])

# retrieve location
LOCATION = ' '.join(addr_parts)

# build url
URL = "http://nominatim.openstreetmap.org/search.php?q="+urllib.parse.quote_plus(LOCATION)

# execute request
resp = requests.get(URL)

# parse response content
json_array = resp.text.split("nominatim_results =")[1]
json_array = json_array.split(';')[0]
json_array = json_array.strip()
res_array = json.loads(json_array)

# pretty print
if PRETTY_PRINT:
    for place in res_array:
        print("""Place :
+ osm_type              : %s
+ country_code          : %s
+ aBoundingBox          : %s
+ langaddress           : %s
+ type                  : %s
+ class                 : %s
+ admin_level           : %s
+ lat                   : %s
+ lon                   : %s
+ addressimportance     : %s
+ ref                   : %s
+ parent_place_id       : %s
+ place_id              : %s
+ label                 : %s
""" % (
place['osm_type'],
place['country_code'],
place['aBoundingBox'],
place['langaddress'],
place['type'],
place['class'],
place['admin_level'],
place['lat'],
place['lon'],
place['addressimportance'],
place['ref'],
place['parent_place_id'],
place['place_id'],
place['label']
))
else:
    print(res_array) # json array printed

print("geo functions tests")
print("Distance Londre - Paris : %s km" % geodist({'lat':51.500152,'lon':-0.126236},{'lat':48.8566667,'lon':2.3509871}))
print("Paris latitude is 48°51'23.8104''N : %s deg" % geoconvert({'deg':48.0,'min':51.0,'sec':23.8104,'dir':'N'}))
