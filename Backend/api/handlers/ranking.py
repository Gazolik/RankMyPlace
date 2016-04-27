from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..criteria.gen_criteria import rank
import json

def ranking_handler(path, data, api_param):
    print(json.loads(data['data'][0]))
    #extraire les criteres utiles
    criteres= json.loads(data['data'][0])['criteres']
    print(criteres)
    nomcriteres=[c['name'] for c in criteres if c['coef'] !=0]

    #evaluer les criteres
    notes = {}
    for i in nomcriteres:
        notes[i] = 5#rank({'criteria':criterias_dict[i],coordinates:{'lat':data['lat'],'lon':data['lon']}})
    #faire une moyenne
    moy = sum(notes.values())/len(nomcriteres)

    #retourner les notes
    ret_data = {"moyenne":moy,"notes":notes}
    print(json.dumps(ret_data))
    return Response(api_param).serialized(ret_data)
