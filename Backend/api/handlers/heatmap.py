from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..fs.fs import load_heatmap, list_database_psd, list_heatmap_grids

#
#
#
def heatmap_base_handler(path, data, api_params):
    data = {
        'criteria_names' : list_database_psd(),
        'grid_basenames' : list_heatmap_grids(),
        'routes' : [
            '/heatmap/{grid_basename}/{criteria_name}'
        ]
    }
    return Response(api_params).serialized(data)
#
#
#
def heatmap_grid_handler(path, data, api_params):
    data = {}
    parts = path.split('/')
    if len(parts) == 4: # on attend ['','heatmap','<grid_name>','<criteria_name>']
        grid_basename = parts[2]
        criteria_name = parts[3]
        data = { 'heatmap' : load_heatmap(grid_basename, criteria_name) }
    return Response(api_params).serialized(data)