from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..criteria.gen_criteria import rank
from ..criteria.criterias import criterias_dict
import json

def ranking_handler(path, data, api_param):
    #extraire les criteres utiles
    d = json.loads(data['data'][0])
    criteres= d['criteres']
    nomcriteres=[k for k,v in criteres.items() if v !=0]

    #evaluer les criteres
    notes = {}
    for i in nomcriteres:
        spec = {'criteria':criterias_dict[i],'coordinates':{'lat':d['lat'],'lon':d['lon']}}
        notes[i],e = rank(spec)
    #faire une moyenne
    moy = sum(notes.values())/len(nomcriteres)

    #retourner les notes
    ret_data = {"moyenne":moy,"notes":notes}
    print(json.dumps(ret_data))
    return Response(api_param).serialized(ret_data)
