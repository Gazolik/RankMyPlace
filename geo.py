#!/usr/bin/python3
# -!- encoding:utf8 -!-

import math, re, requests, urllib, json

#
# @brief Parses a string to create a coordinate dictionary
# @param string formatted using one of the following formats :
#           + 40° 26′ 46″ N 79° 58′ 56″ W
#           + 40° 26.767′ N 79° 58.933′ W
#           + 40.446° N 79.982° W
# @return {'lat':<double>,'lon':<double>}
#
def geo_parse(string):
    string = string.replace(' ', '') # remove all spaces
    # check input format
    p = re.compile('([\d\.]+°([\d\.]+′)*([\d\.]+″)*(N|S|E|W)){2}')
    if not p.match(string):
        print("Invalid input format.")
        exit()
    # prepare local vars
    coord = {'lat':0.0,'lon':0.0}
    for i in range(2):
        dg = mn = sc = o = ''
        # retrieve degrees
        while string[:1] != '°':
            dg += string[:1]
            string = string[1:]
        # remove '°'
        string = string[1:]
        # retrieve minutes
        if '′' in string:
            while string[:1] != '′':
                mn += string[:1]
                string = string[1:]
            # remove '′'
            string = string[1:]
        # retrieve seconds
        if '″' in string:
            while string[:1] != '″':
                sc += string[:1]
                string = string[1:]
                # remove '″'
            string = string[1:]
        # retrieve direction
        o = string[:1]
        string = string[1:]
        # convert strings to decimal degrees
        val = 0.0
        if len(sc) > 0 and len(mn) > 0:
            val = float(dg) + float(mn)/60 + float(sc)/3600 
        elif len(mn) > 0:
            val = float(dg) + float(mn)/60
        else:
            val = float(dg)
        # opposite value for South and West orientations
        if o == 'S' or o == 'W': 
            val = -val
        # fill coord dictionary
        if i == 0:
            coord['lat'] = val
        else:
            coord['lon'] = val
    # finally return coord dictionary
    return coord

#
# @brief 
# @param coord_x is a dict like {'lat':<double>,'lon':<double>}
# @param format can be 
#           + 40° 26′ 46″ N 79° 58′ 56″ W (full, default)
#           + 40° 26.767′ N 79° 58.933′ W (min)
#           + 40.446° N 79.982° W         (deg)
#
def geo_print(coord):
    latdg, latmn, latsc = float_to_deg_min_sec(coord['lat'])
    londg, lonmn, lonsc = float_to_deg_min_sec(coord['lon'])
    print("%02d° %02d′ %02d″ %s %02d° %02d′ %02d″ %s" % (latdg, latmn, latsc, 'N' if coord['lat'] > 0 else 'S', 
                                             londg, lonmn, lonsc, 'E' if coord['lon'] > 0 else 'W'))

#
# internal convert function
#
def float_to_deg_min_sec(num):
    num = abs(num)
    dg = math.floor(num)
    mn = math.floor(60 * (num - dg))
    sc = 3600 * ((num - dg) - mn/60.0)
    return (dg, mn, sc)
#
# @brief Calculate the distance in kilometers between two geo coordinates
# @param coord_x is a dict like {'lat':<double>,'lon':<double>}
#
def geo_dist(coord_from, coord_to): 
    dlat = math.radians(coord_to['lat'] - coord_from['lat'])
    dlon = math.radians(coord_to['lon'] - coord_from['lon'])
    a = math.pow(math.sin(dlat / 2.0), 2) + math.cos(math.radians(coord_from['lat'])) * math.cos(math.radians(coord_to['lat'])) * math.pow(math.sin(dlon / 2.0), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return 6367 * c

#
# @brief Return details about a place searched by name
# @warning This function may become deprecated as OpenStreetMap - Nominatim evolves
#
def geo_locator(place):
    # build url
    url = "http://nominatim.openstreetmap.org/search.php?q=" + urllib.parse.quote_plus(place)
    # execute request
    resp = requests.get(url)
    # parse response content
    json_array = resp.text.split("nominatim_results =")[1]
    json_array = json_array.split(';')[0]
    json_array = json_array.strip()
    res_array = json.loads(json_array)
    # return response as an array of dictionaries
    return res_array


# ----------------------------- TESTS ZONE ---------------------------
print('Test coordinates : 47°03′36″N 0°52′42″W')
# geo_parse test 
coord = geo_parse('47°03′36″N 0°52′42″W')
print('Lat : %s deg\nLon : %s deg' % (coord['lat'], coord['lon']))
# geo_print test 
geo_print(coord)
# geo_dist test
print("Lyon-Cholet : %.3f km (direct flight distance)" % geo_dist(geo_parse('45°45′36″N 4°50′24″E'), geo_parse('47°03′36″N 0°52′42″W')))
# geo_locator test
print(json.dumps(geo_locator('INSA de Lyon')[0], sort_keys=True, indent=2))