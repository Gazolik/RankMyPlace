"""from .bruit_psd import bruit_psd
from .le_deplacement_psd import le_deplacement_psd
from .pit_hotellerie_plein_air_psd import pit_hotellerie_plein_air_psd
from .velov_psd import velov_psd
from .le_culte_psd import le_culte_psd
from .pit_equipement_psd import pit_equipement_psd
from .le_intercommunalite_psd import le_intercommunalite_psd
from .tcl_psd import tcl_psd
from .le_urgence_psd import le_urgence_psd
from .le_habitat_psd import le_habitat_psd
from .le_sante_psd import le_sante_psd
from .pit_commerce_et_service_psd import pit_commerce_et_service_psd
from .le_sport_psd import le_sport_psd
from .pit_patrimoine_naturel_psd import pit_patrimoine_naturel_psd
from .le_enseignement_psd import le_enseignement_psd
from .pit_degustation_psd import pit_degustation_psd
from .pit_hebergement_locatif_psd import pit_hebergement_locatif_psd
from .le_administration_psd import le_administration_psd
from .pit_hebergement_collectif_psd import pit_hebergement_collectif_psd
from .pit_hotellerie_psd import pit_hotellerie_psd
from .pit_patrimoine_culturel_psd import pit_patrimoine_culturel_psd
from .pit_restauration_psd import pit_restauration_psd"""

criterias_dict = {
	'bruit_psd' : {
		'name' : 'bruit_psd',
		'type' : 'custom',
		'params' : { } #todo
		},
	'le_deplacement_psd' : {
		'name' : 'le_deplacement_psd',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : '0',
			'max_dist' : '1000',
			'scale' : 'linear'
			}
		},
	'pit_hotellerie_plein_air_psd' : {
		'name' : 'pit_hotellerie_plein_air_psd',
		'type' : 'density_based',
		'params' : {
			'min_density' : '0',
			'max_density' : '3',
			'scale' : 'linear'
			}
		},
	'velov_psd' : {
		'name' : 'velov_psd',
		'type' : 'dist_dens_based',
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '500', 
			'min_density' : '0',
			'max_density' : '3'
			}
		},
	'le_culte_psd' : {
		'name' : 'le_culte_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '2000',
			'scale' : 'linear' 
			}
		},
	'pit_equipement_psd' : { #todo comprendre ce que c'est pour donner les valeurs
		'name' : 'pit_equipement_psd',
		'type' : 'dist_dens_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '1000', 
			'min_density' : '0',
			'max_density' : '10'
			}
		},
	'le_intercommunalite_psd' : { #todo comprendre ce que c'est pour donner les valeu
		'name' : 'le_intercommunalite_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '1000',
			'scale' : 'linear'
			}
		},
	'tcl_psd' : {
		'name' : 'tcl_psd',
		'type' : 'dist_dens_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '500',
			'min_density' : '0',
			'max_density' : '3'
			}
		},
	'le_urgence_psd' : {
		'name' : 'le_urgence_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '1000',
			'scale' : 'linear'
			}
		},
	#'le_habitat_psd' : {} voir si c'est utile avant
	'le_sante_psd' : {
		'name' : 'le_sante_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '5000',
			'scale' : 'linear'
			}
		},
	'pit_commerce_et_service_psd': {
		'name' : 'pit_commerce_et_service_psd',
		'type' : 'dist_dens_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '2000',
			'min_density' : '0',
			'max_density' : '10'
			}
		},
	'le_sport_psd' : {
		'name' : 'le_sport_psd',
		'type' : 'dist_dens_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '2000',
			'min_density' : '0',
			'max_density' : '3'
			}
		},
	'pit_patrimoine_naturel_psd' : {
		'name' : 'pit_patrimoine_naturel_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '2000',
			'scale' : 'linear'
			}
		},
	'le_enseignement_psd' :{
		'name' : 'le_enseignement_psd',
		'type' : 'dist_dens_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '2000',
			'min_density' : '0',
			'max_density' : '3'
			}
		},
	'pit_degustation_psd':{
		'name' : 'pit_degustation_psd',
		'type' : 'dist_dens_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '2000',
			'min_density' : '0',
			'max_density' : '3'
			}
		},
	'pit_hebergement_locatif_psd':{
		'name' : 'pit_hebergement_locatif_psd',
		'type' : 'density_based'
		'params' : { 
			'min_density' : '0',
			'max_density' : '10',
			'scale' : 'linear'
			}
		},
	'le_administration_psd':{
		'name' : 'le_administration_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_dist' : '0',
			'max_dist' : '1000',
			'scale' : 'linear'
			}
		},
	'pit_hebergement_collectif_psd':{
		'name' : 'pit_hebergement_collectif_psd',
		'type' : 'density_based'
		'params' : { 
			'min_density' : '0',
			'max_density' : '10',
			'scale' : 'linear'
			}
		},
	'pit_hotellerie_psd':{
		'name' : 'pit_hotellerie_psd',
		'type' : 'density_based'
		'params' : { 
			'min_density' : '0',
			'max_density' : '5',
			'scale' : 'linear'
			}
		},
	'pit_patrimoine_culturel_psd':{
		'name' : 'pit_hotellerie_psd',
		'type' : 'distance_based'
		'params' : { 
			'min_density' : '0',
			'max_density' : '5',
			'scale' : 'linear'
			}
		},
	'pit_restauration_psd':{
		'name' : 'pit_restauration_psd',
		'type' : 'density_based'
		'params' : { 
			'min_density' : '0',
			'max_density' : '10'
			}
		},
   """ 'bruit_psd': bruit_psd(),
    'le_deplacement_psd':le_deplacement_psd(),
    'pit_hotellerie_plein_air_psd':pit_hotellerie_plein_air_psd(),
    'velov_psd':velov_psd(),
    'le_culte_psd':le_culte_psd(),
    'pit_equipement_psd':pit_equipement_psd(),
    'le_intercommunalite_psd':le_intercommunalite_psd(),
    'tcl_psd':tcl_psd(),
    'le_urgence_psd':le_urgence_psd(),
    'le_habitat_psd':le_habitat_psd(),
    'le_sante_psd':le_sante_psd(),
    'pit_commerce_et_service_psd':pit_commerce_et_service_psd(),
    'le_sport_psd':le_sport_psd(),
    'pit_patrimoine_naturel_psd':pit_patrimoine_naturel_psd(),
    'le_enseignement_psd':le_enseignement_psd(),
    'pit_degustation_psd':pit_degustation_psd(),
    'pit_hebergement_locatif_psd':pit_hebergement_locatif_psd(),
    'le_administration_psd':le_administration_psd(),
    'pit_hebergement_collectif_psd':pit_hebergement_collectif_psd(),
    'pit_hotellerie_psd':pit_hotellerie_psd(),
    'pit_patrimoine_culturel_psd':pit_patrimoine_culturel_psd(),
    'pit_restauration_psd':pit_restauration_psd()"""
    }
