#!/usr/bin/python3
from ..fs.fs import load_database_psd
from ..algorithm.algorithm import closest_record
from ..algorithm.algorithm import density_around
from ..debug.debug import watch_time
from ..algorithm.algorithm import records_around
#


def rank(spec):
    """
        Calculate a rank for a criteria at certain coordinates with certain specifications
        Input:
            spec = {'criteria': criterias_dict[<criteria_code>],
                'coordinates': {'lat':<lat>,'lon':<lon>},
                'dist':[<min_dist, max_dist>],
                'dens':[<min_dens>,<max_dens>]}
        Output:
            Return triplet (mark/10, found_element, (density|None))
    """
    typ = spec['criteria']['type']
    if typ == 'distance_based':
        return distance_based(spec['criteria'], spec['coordinates'],spec['dist'])
    elif typ == 'density_based':
        return density_based(spec['criteria'], spec['coordinates'],spec['dens'])
    elif typ == 'dist_dens_based':
        return dist_dens_based(spec['criteria'], spec['coordinates'],spec['dens'],spec['dist'])
    elif typ == 'custom':
        return custom(spec['criteria'], spec['coordinates'])
    else:
        return (None, None, None)  # error case


# @watch_time
def distance_based(criteria, coord, min_max_dist):
    """
        Generic distance calculation
    """
    # take default value if min and max dist are not given
    if min_max_dist:
        min_dist = min_max_dist[0]
        max_dist = min_max_dist[1]
    else:
        max_dist = criteria['params']['max_dist']
        min_dist = criteria['params']['min_dist']
    scale = criteria['params']['dist_scale']
    # read in database
    records = load_database_psd(criteria['name'])
    # default mark
    mark = -1.0
    if not records:
        print('[gen_criteria.distance_based]> %s' % criteria['name'])
    else:
        # get closest record
        dist, record = closest_record(records, coord)
        # is it in our circle 
        if dist < min_dist or dist > max_dist:
            # if it's not in the circle mark = 0
            mark = 0.0
            record = None
        # here to implement other kind of ranking
        else:
            if scale == 'log':
                # todo
                mark = -1.0
            elif scale == 'linear':
                mark = 10.0 * (1.0 - ((dist - min_dist) / (max_dist - min_dist)))
    # finally return mark and record for details
    return (mark, record, None)


# @watch_time
def density_based(criteria, coord, min_max_dens):
    """
        Generic density calculation
    """
    # take default value if min and max dist are not given
    if min_max_dens:
        min_density = min_max_dens[0]
        max_density = min_max_dens[1]
    else:
        max_density = criteria['params']['max_density']
        min_density = criteria['params']['min_density']
    radius = criteria['params']['radius']
    scale = criteria['params']['dens_scale']
    # read in database
    records = load_database_psd(criteria['name'])
    # default mark
    mark = -1.0
    closest = None
    if not records:
        print('[gen_criteria.density_based]> %s' % criteria['name'])
    else:
        # get density
        density, closest, min_dist = density_around(records, coord, radius)
        # is it in our "density circle"
        #here to implement other kind of density ranking
        if density < min_density:
            mark = 10 * (density / min_density)
            closest = None
        elif density > max_density:
            if density > max_density + min_density:
                mark = 0.0
            else:
                mark = 10 * ((max_density + min_density - density) / min_density)
        else:
            mark = 10.0
    # finally return mark and record for details
    return (mark, closest, density)


# @watch_time
def dist_dens_based(criteria, coord, min_max_dens, min_max_dist):
    """
        Generic hybrid density/distance calculation
    """
    mark_density, record, density = density_based(criteria, coord, min_max_dens)
    mark_dist, closest, empty = distance_based(criteria, coord, min_max_dist)
    mark = (criteria['params']['dist_coeff'] * mark_dist + criteria['params']['dens_coeff'] * mark_density) / (criteria['params']['dist_coeff'] + criteria['params']['dens_coeff'])
    return (mark, closest, density)


# @watch_time
def custom(criteria, coord):
    """
        Customized calculation
    """
    if criteria['name'] == "bruit":
        return custom_bruit(criteria, coord)
    else:
        print('[gen_criteria.py|custom]> /!\ Profil custom non disponible /!\\')
        return(-1.0, None, None)


# @watch_time
def custom_bruit(criteria, coord):
    """
        Customized calculation for criteria 'bruit'
    """
    # radius get
    radius = criteria['params']['radius']
    max_noise = criteria['params']['max']
    min_noise =criteria['params']['min']
    # read in database
    records_db = load_database_psd(criteria['name'])
    # closest records
    records = records_around(records_db, coord, radius)
    # default mark
    mark = -1.0
    if not records:
        print('[gen_criteria.py|custom_bruit]> no record found around for %s' % criteria['name'])
    else:
        records_size = len(records)
        s = 0
        for record in records:
            noise = record['data']['value']
            noise_mark = 10 * (1.0 - ((noise - min_noise) / (max_noise - min_noise)))
            s += noise_mark
        mark = s / records_size
    # on retourne la note et pas de record
    return (mark, None, None)
