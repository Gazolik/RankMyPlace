from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..criteria.gen_criteria import rank
from ..criteria.criterias import criterias_dict
from ..algorithm.algorithm import satisfaction, coord_dist
import json


def ranking_handler(path, data, api_param):
    """
        Handler called on /ranking route
        input data:
            {'lat':<lat>, 'lon':<lon>, 'criterias':{
                'criteria_code1':{'dist':[(<min_dist>, <max_dist>)], 'dens':[(<min_dens>,<max_dens>)], 'coef':<coef>}, 'criteria_code2':{...}...}
            }
    """
    # useful criterias extract
    data_dict = json.loads(data['data'][0])
    criterias = data_dict['criteres']
    marks = {}
    ret_marks = []
    sum_marks = 0
    #criterias marking
    for code in criterias.keys():
        spec = {'criteria': criterias_dict[code],
                'coordinates': {'lat':data_dict['lat'],'lon': data_dict['lon']},
                'dist':criterias[code]['dist'],
                'dens':criterias[code]['dens']}
        #mark
        mark, closest, density = rank(spec)
        closest_dist = 0
        if closest:
            closest_dist = coord_dist({
                'lat':data_dict['lat'],
                'lon':data_dict['lon']},
                {'lat':closest['coordinates']['lat'],'lon':closest['coordinates']['lon']})
            closest_dist = round(closest_dist,2)
       

        radius = criterias_dict[code]['params'].get('radius', None)
        if radius:
            radius = int(radius)
        
        #fulfill the response
        satis = -101
        if criterias[code]['coef'] > 0:
            sum_marks += (mark * criterias[code]['coef'])
            satis = round(satisfaction(max(mark, 0), criterias[code]['coef']),2)
        ret_marks.append({
            'name': criterias_dict[code]['realname'],
            'note':round(mark,2),
            'satisfaction':satis,
            'closest': closest,
            'closestDist': closest_dist,
            'density': {
                'value': density,
                'radius': radius
            }
            })
    #simple avg
    sum_coefs = 0
    for code in criterias.keys():
        sum_coefs += criterias[code]['coef']
    avg = (sum_marks / sum_coefs) if sum_marks != 0 else 0.0
    # return marks
    ret_data = {'moyenne': round(avg, 2), 'notes': ret_marks}
    return Response(api_param).serialized(ret_data)
