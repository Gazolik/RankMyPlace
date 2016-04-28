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
			'dist_scale' : 'linear'
			}
		},
	'pit_hotellerie_plein_air' : {
		'name' : 'pit_hotellerie_plein_air',
		'type' : 'density_based',
		'params' : {
			'min_density' : 5,
			'max_density' : 100000,
                        'radius' : 1000,
			'dens_scale' : 'linear'
			}
		},
	'velov' : {
		'name' : 'velov',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 500,
			'min_density' : 3,
			'max_density' : 100000,
                        'dist_coeff' : 2,
                        'dens_coeff': 1,
                        'radius' : 500,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'le_culte' : {
		'name' : 'le_culte',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'dist_scale' : 'linear'
			}
		},
	'pit_loisirs' : {
                'name' : 'pit_loisirs',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 5,
			'max_density' : 100000,
                        'dist_coeff' : 1,
                        'dens_coeff': 3,
                        'radius' : 2000,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'tcl' : {
		'name' : 'tcl',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 500,
			'min_density' : 3,
			'max_density' : 10000,
                        'dist_coeff' : 2,
                        'dens_coeff': 1,
                        'radius' : 500,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'le_urgence' : {
		'name' : 'le_urgence',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'dist_scale' : 'linear'
			}
		},
	'le_sante' : {
		'name' : 'le_sante',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 5000,
			'dist_scale' : 'linear'
			}
		},
	'pit_commerce_et_service': {
		'name' : 'pit_commerce_et_service',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'min_density' : 10,
			'max_density' : 100000,
                        'dist_coeff' : 1,
                        'dens_coeff': 3,
                        'radius' : 1000,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'le_sport' : {
		'name' : 'le_sport',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 3,
			'max_density' : 100000,
                        'dist_coeff' : 1,
                        'dens_coeff': 3,
                        'radius' : 2000,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'pit_patrimoine_naturel' : {
		'name' : 'pit_patrimoine_naturel',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'dist_scale' : 'linear'
			}
		},
	'le_enseignement' :{
		'name' : 'le_enseignement',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'min_density' : 3,
			'max_density' : 10000,
                        'dist_coeff' : 3,
                        'dens_coeff': 2,
                        'radius' : 1000,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'pit_degustation':{
		'name' : 'pit_degustation',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 3,
			'max_density' : 10000,
                        'dist_coeff' : 3,
                        'dens_coeff': 1,
                        'radius' : 2000,
                        'dist_scale' : 'linear',
                        'dens_scale' : 'linear'
			}
		},
	'pit_hebergement_locatif':{
		'name' : 'pit_hebergement_locatif',
		'type' : 'density_based',
		'params' : {
			'min_density' : 10,
			'max_density' : 10000,
			'dens_scale' : 'linear',
                        'radius':500
			}
		},
	'le_administration':{
		'name' : 'le_administration',
		'type' : 'distance_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'dist_scale' : 'linear'
			}
		},
	'pit_hebergement_collectif':{
		'name' : 'pit_hebergement_collectif',
		'type' : 'density_based',
		'params' : {
			'min_density' : 10,
			'max_density' : 10000,
                        'radius':500,
			'dens_scale' : 'linear'
			}
		},
	'pit_hotellerie':{
		'name' : 'pit_hotellerie',
		'type' : 'density_based',
		'params' : {
			'min_density' : 5,
			'max_density' : 10000,
                        'radius':500,
			'dens_scale' : 'linear'
			}
		},
	'pit_patrimoine_culturel':{
		'name' : 'pit_hotellerie',
		'type' : 'density_based',
		'params' : {
			'min_density' : 5,
			'max_density' : 10000,
			'dens_scale' : 'linear',
			'radius':500
			}
		},
	'pit_restauration':{
		'name' : 'pit_restauration',
		'type' : 'density_based',
		'params' : {
			'min_density' : 10,
			'max_density' : 10000,
                        'radius':500,
                        'dens_scale': 'linear'
			}
		}
       }
