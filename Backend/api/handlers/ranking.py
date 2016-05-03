from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..criteria.gen_criteria import rank
from ..criteria.criterias import criterias_dict
from ..algorithm.algorithm import satisfaction
import json


def ranking_handler(path, data, api_param):
    """
        TODO : doc
    """
    # extraire les criteres utiles
    d = json.loads(data['data'][0])
    criteres = d['criteres']
    # evaluer les criteres
    notes = {}
    ret_note = []
    somme = 0
    for i in criteres.keys():
        spec = {'criteria': criterias_dict[i], 'coordinates': {'lat':d['lat'],'lon': d['lon']}, 'dist':criteres[i]['dist'],'dens':criteres[i]['dens']}
        note, closest, density = rank(spec)
        # récupération du rayon dans le cas d'une densité
        # on retourne explicitement None si on ne trouve pas la clé radius dans params
        radius = criterias_dict[i]['params'].get('radius', None)
        if radius:
            radius = int(radius)
        # traitement en fonction du coeff du critère
        if criteres[i]['coef'] == 0 :
            ret_note.append({
                'name': criterias_dict[i]['realname'],
                'note':note,
                'satisfaction':-101,
                'closest': closest,
                'density': {
                    'value': density,
                    'radius': radius
                }
            })
        else :
            notes[i] = note
            somme = somme + notes[i] * criteres[i]['coef']
            note_finale = notes[i]
            #calcul de satisfaction
            satis = satisfaction(max(note_finale,0), criteres[i]['coef'])
            ret_note.append({
                'name': criterias_dict[i]['realname'],
                'note': round(note_finale, 2),
                'satisfaction':round(satis, 2),
                'closest': closest,
                'density': {
                    'value': density,
                    'radius': radius
                }
            })
    # faire une moyenne
    somme_coef = 0
    for i in criteres.keys():
        somme_coef += criteres[i]['coef']
    if somme != 0:
        moy = somme / somme_coef
    else:
        moy = 0.0
    # retourner les notes
    ret_data = {'moyenne': round(moy, 2), 'notes': ret_note}
    return Response(api_param).serialized(ret_data)
