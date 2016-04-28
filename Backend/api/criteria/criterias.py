criterias_dict = {
	'bruit' : {
		'name' : 'bruit',
		'type' : 'custom',
		'params' : { } #todo
		},
	'le_deplacement' : {
		'name' : 'le_deplacement',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'scale' : 'linear'
			}
		},
	'pit_hotellerie_plein_air' : {
		'name' : 'pit_hotellerie_plein_air',
		'type' : 'density_based',
		'params' : {
			'min_density' : 5,
			'max_density' : 100000,
                        'radius' : 1000,
			'scale' : 'linear'
			}
		},
	'velov' : {
		'name' : 'velov',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 500,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'le_culte' : {
		'name' : 'le_culte',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'scale' : 'linear'
			}
		},
	'pit_loisirs' : {
                'name' : 'pit_loisirs',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 5
			}
		},
	'tcl' : {
		'name' : 'tcl',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 500,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'le_urgence' : {
		'name' : 'le_urgence',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'scale' : 'linear'
			}
		},
	'le_sante' : {
		'name' : 'le_sante',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 5000,
			'scale' : 'linear'
			}
		},
	'pit_commerce_et_service': {
		'name' : 'pit_commerce_et_service',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 10
			}
		},
	'le_sport' : {
		'name' : 'le_sport',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'pit_patrimoine_naturel' : {
		'name' : 'pit_patrimoine_naturel',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'scale' : 'linear'
			}
		},
	'le_enseignement' :{
		'name' : 'le_enseignement',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'pit_degustation':{
		'name' : 'pit_degustation',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'pit_hebergement_locatif':{
		'name' : 'pit_hebergement_locatif',
		'type' : 'density_based',
		'params' : {
			'min_density' : 10,
			'max_density' : 10000,
			'scale' : 'linear',
                        'radius':500
			}
		},
	'le_administration':{
		'name' : 'le_administration',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'scale' : 'linear'
			}
		},
	'pit_hebergement_collectif':{
		'name' : 'pit_hebergement_collectif',
		'type' : 'density_based',
		'params' : {
			'min_density' : 10,
			'max_density' : 10000,
                        'radius':500,
			'scale' : 'linear'
			}
		},
	'pit_hotellerie':{
		'name' : 'pit_hotellerie',
		'type' : 'density_based',
		'params' : {
			'min_density' : 5,
			'max_density' : 10000,
                        'radius':500,
			'scale' : 'linear'
			}
		},
	'pit_patrimoine_culturel':{
		'name' : 'pit_hotellerie',
		'type' : 'density_based',
		'params' : {
			'min_density' : 5,
			'max_density' : 10000,
			'radius':500,
			'scale' : 'linear'
			}
		},
	'pit_restauration':{
		'name' : 'pit_restauration',
		'type' : 'density_based',
		'params' : {
			'min_density' : 10,
			'max_density' : 10000,
                        'radius':500,
                        'scale': 'linear'
			}
		}
       }
