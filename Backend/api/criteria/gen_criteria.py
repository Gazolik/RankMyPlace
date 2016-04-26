#
# Old gen_criteria
#
#class gen_criteria:
#    """ classe generique representant un critere"""
#    def __init__(self):
#        pass
#
#    def rank(self):
#        """ Cette methode est la methode d'evaluation d'un critere"""
#        pass

from ..fs.fs import get_criteria
from ..db.db import closest_record, density_around

#
#   Calcul la note pour un critère donné avec les specifications reçues
#
#   retourne un couple (note_sur_dix, element_trouvé)
#
def rank(spec):
    typ = spec['criteria']['type'] 
    if typ == 'distance_based':
        return distance_based(spec['criteria'], spec['coordinates'])
    elif typ == 'density_based':
        return density_based(spec['criteria'], spec['coordinates'], spec['radius'])
    elif typ == 'dist_dens_based':
        return dist_dens_based(spec['criteria'], spec['coordinates'])
    elif typ == 'custom':
        return custom(spec['criteria'], spec['coordinates'])
    else:
        return (None, None) # error case

#
#   Calcul de distance générique, paramètres attendus :
#       + min_dist
#       + max_dist
#       + scale
#
#   retourne un couple (note_sur_dix, element_trouvé)
#
def distance_based(criteria, coord):
    # récupération et calcul des paramètres
    max_dist = criteria['params']['max_dist']
    min_dist = criteria['params']['min_dist']
    scale = criteria['params']['scale']
    # lecture dans la base
    records = get_criteria(criteria['name'])
    # récupération du point le plus proche
    dist, record = closest_record(records, coord)
    # création de la note vide
    mark = None
    # vérification d'appartenance à l'anneau
    if dist < min_dist or dist > max_dist:
        # le lieu le plus proche n'est pas dans l'anneau, on retourne 0 
        mark = 0.0
        record = None 
    # calcul de la note en fonction de l'échelle
    else:
        if scale == 'log':
            # todo
            mark = -1.0
        elif scale == 'linear':
            mark = 10.0 * ( 1.0 - ( (dist - min_dist) / (max_dist - min_dist) ) )
        # else: mark = None (cf. initialisation de mark)
    # finally return mark and record for details
    return (mark, closest)

#
#   Calcul de densité générique, paramètres attendus :
#       + max_density
#       + min_density
#       + scale
#
#   retourne un couple (note_sur_dix, element_trouvé)
#
def density_based(criteria, coord, radius):
    # récupération et calcul des paramètres
    max_density = criteria['params']['max_density']
    min_density = criteria['params']['min_density']
    scale = criteria['params']['scale']
    # lecture dans la base
    records = get_criteria(criteria['name'])
    # récupération de la densité
    density, closest, min_dist = density_around(records, coord, radius)
    # création de la note vide
    mark = None
    # vérification d'appartenance à l'anneau
    if density < min_density or density > max_dist:
        # la densité n'est pas dans l'anneau, on retourne 0 
        mark = 0.0
        closest = None 
    # calcul de la note en fonction de l'échelle
    else:
        if scale == 'log':
            # todo
            mark = -1.0
        elif scale == 'linear':
            mark = 10.0 * ( min(density - min_density, max_density - min_density ) / (max_density - min_density) )
        # else: mark = None (cf. initialisation de mark)
    # finally return mark and record for details
    return (mark, closest)

#
#   Calcul générique couplage de distance et densité, paramètres attendus :
#       + max_dist
#       + min_dist
#       + max_density
#       + min_density
#       + dist_coeff
#       + dens_coeff
#       + dist_scale
#       + dens_scale
#
#   retourne un couple (note_sur_dix, element_trouvé)
#
def dist_dens_based(criteria, coord):
    # todo
    return (None, None)

#
#   Calcul customisé pour les données spéciales
#
def custom(criteria, coord):
    # todo
    return (None, None)
