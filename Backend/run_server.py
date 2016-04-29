#!/usr/bin/python3
#-!-encoding:UTF-8-!-
# import server and API
from api.py_rest.pyrest.rest_server.rest_api.restapi import RestAPI
from api.py_rest.pyrest.rest_server.firewall.firewall import Firewall
from api.py_rest.pyrest.rest_server.restserver import RestServer
# import api handlers
from api.handlers.profile import profiles_handler
from api.handlers.criteria import criterias_handler
from api.handlers.ranking import ranking_handler
from api.handlers.heatmap import heatmap_base_handler, heatmap_grid_handler, avg_heatmap_grid_handler
# initialize REST API
api = RestAPI()
api.add_path(RestAPI.GET, '/profiles', profiles_handler)
api.add_path(RestAPI.GET, '/criterias', criterias_handler)
api.add_path(RestAPI.POST,'/ranking', ranking_handler)
api.add_path(RestAPI.GET, '/heatmap', heatmap_base_handler)
api.add_path(RestAPI.GET, '/heatmap/{grid_basename}/{criteria_name}', heatmap_grid_handler)
api.add_path(RestAPI.POST, '/heatmap/{grid_basename}', avg_heatmap_grid_handler)

# initialize Firewall
firewall = Firewall(persistentLog=False)

# initialize and run server
server = RestServer(8000, api, firewall)
server.run()
