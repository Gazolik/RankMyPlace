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
    ret_note = []
    somme = 0
    print('nom   note   coef')
    for i in nomcriteres:
        spec = {'criteria':criterias_dict[i],'coordinates':{'lat':d['lat'],'lon':d['lon']}}
        notes[i],e = rank(spec)
        somme = somme + notes[i]*criteres[i]
        ret_note.append({"name":criterias_dict[i]['realname'],"note":notes[i]})
    #faire une moyenne
    moy = somme/sum(criteres.values())

    #retourner les notes
    ret_data = {"moyenne":moy,"notes":ret_note}
    print(json.dumps(ret_data))
    return Response(api_param).serialized(ret_data)
