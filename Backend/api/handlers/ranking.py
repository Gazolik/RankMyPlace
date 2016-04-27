from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..criteria.ranking import rank

def ranking_handler(path, data, api_param):
    #extraire les criteres utiles
    criteres= data['criteres']
    nomcriteres=[c['name'] for c in criteres if c['coef'] !=0]

    #evaluer les criteres
    notes = {}
    for i in nomcriteres:
        notes[i] = rank({'criteria':criterias_dict[i],coordinates:{'lat':data['lat'],'lon':data['lon']}})
    #faire une moyenne
    moy = sum(notes.values())/len(nomcriteres)

    #retourner les notes
    ret_data = {"moyenne":moy,"notes":notes}
    return Response(api_param).serialized(ret_data)
