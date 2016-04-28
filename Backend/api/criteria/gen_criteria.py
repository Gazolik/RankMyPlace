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

from ..fs.fs import load_database_psd
from ..algorithm.algorithm import closest_record, density_around
from ..debug.debug import watch_time
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
        return density_based(spec['criteria'], spec['coordinates'])
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
@watch_time
def distance_based(criteria, coord):
    # récupération et calcul des paramètres
    max_dist = criteria['params']['max_dist']
    min_dist = criteria['params']['min_dist']
    scale = criteria['params']['dist_scale']
    # lecture dans la base
    records = load_database_psd(criteria['name'])
    if not records:
        print('[gen_criteria.distance_based] %s'%criteria['name'])
        return (-1.0, None)
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
    return (mark, record)

#
#   Calcul de densité générique, paramètres attendus :
#       + max_density
#       + min_density
#       + scale
#
#   retourne un couple (note_sur_dix, element_trouvé)
#
@watch_time
def density_based(criteria, coord):
    # récupération et calcul des paramètres
    max_density = criteria['params']['max_density']
    min_density = criteria['params']['min_density']
    radius = criteria['params']['radius']
    scale = criteria['params']['dens_scale']
    # lecture dans la base
    records = load_database_psd(criteria['name'])
    if not records :
    	print('[gen_criteria.density_based] %s'%criteria['name'])
    	return (-1.0, None)
    # récupération de la densité
    density, closest, min_dist = density_around(records, coord, radius)
    # création de la note vide
    mark = None
    # vérification d'appartenance à l'anneau
    if density < min_density:
        mark =  10*(density/min_density)
        closest = None
    elif density > max_density:
        if density > max_density + min_density:
            mark = 0.0
        else:
            mark = 10*((max_density+min_density-density)/min_density)
    # calcul de la note en fonction de l'échelle
    else:
        mark = 10.0
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
@watch_time
def dist_dens_based(criteria, coord):
    mark_density, record = density_based(criteria, coord)
    mark_dist, closest = distance_based(criteria, coord)
    mark = (criteria['params']['dist_coeff']*mark_dist+criteria['params']['dist_coeff']*mark_density)/(criteria['params']['dist_coeff']+criteria['params']['dens_coeff'])
    return (mark, closest)

#
#   Calcul customisé pour les données spéciales
#
@watch_time
def custom(criteria, coord):
    if criteria == "bruit":
        custom_bruit(criteria, coord)
    else:
        abort('Profil custom non disponible')

#
#   Calcul customisé pour le bruit
#
@watch_time
def custom_bruit(criteria, coord):
    # récupération du rayon
    radius = criteria['params']['radius']
    # lecture dans la base
    records_db = load_database_psd(criteria['name'])
    # récupération des records les plus proches
    records = records_around(records_db, coord, radius)
    if not records:
        print('[gen_criteria.custom] %s'%criteria['name'])
        return (-1.0, None)
    # création des variables necessaires au traitement
    records_size = len(records)
    mark = 0
    sum = 0
    if records_size == 0:
        # trop peu d'information le critère ne doit pas
        # être pris en compte
        return (-1, None)
    else:
        for record in records:
            sum += record['data']['value']
        mark = sum/records_size
    # on retoure la note et pas de record
    return (mark, None)
