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
			'min_dist' : 0,
			'max_dist' : 1000,
			'scale' : 'linear'
			}
		},
	'pit_hotellerie_plein_air_psd' : {
		'name' : 'pit_hotellerie_plein_air_psd',
		'type' : 'density_based',
		'params' : {
			'min_density' : 0,
			'max_density' : 3,
			'scale' : 'linear'
			}
		},
	'velov_psd' : {
		'name' : 'velov_psd',
		'type' : 'dist_dens_based',
		'params' : {
			'min_dist' : 0,
			'max_dist' : 500,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'le_culte_psd' : {
		'name' : 'le_culte_psd',
		'type' : 'distance_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'scale' : 'linear'
			}
		},
	'pit_loisirs_psd' : {
                'name' : 'pit_loisirs_psd',
		'type' : 'dist_dens_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 5
			}
		},
	'tcl_psd' : {
		'name' : 'tcl_psd',
		'type' : 'dist_dens_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 500,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'le_urgence_psd' : {
		'name' : 'le_urgence_psd',
		'type' : 'distance_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'scale' : 'linear'
			}
		},
	'le_sante_psd' : {
		'name' : 'le_sante_psd',
		'type' : 'distance_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 5000,
			'scale' : 'linear'
			}
		},
	'pit_commerce_et_service_psd': {
		'name' : 'pit_commerce_et_service_psd',
		'type' : 'dist_dens_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 10
			}
		},
	'le_sport_psd' : {
		'name' : 'le_sport_psd',
		'type' : 'dist_dens_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'pit_patrimoine_naturel_psd' : {
		'name' : 'pit_patrimoine_naturel_psd',
		'type' : 'distance_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'scale' : 'linear'
			}
		},
	'le_enseignement_psd' :{
		'name' : 'le_enseignement_psd',
		'type' : 'dist_dens_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'pit_degustation_psd':{
		'name' : 'pit_degustation_psd',
		'type' : 'dist_dens_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 2000,
			'min_density' : 0,
			'max_density' : 3
			}
		},
	'pit_hebergement_locatif_psd':{
		'name' : 'pit_hebergement_locatif_psd',
		'type' : 'density_based'
		'params' : {
			'min_density' : 0,
			'max_density' : 10,
			'scale' : 'linear'
			}
		},
	'le_administration_psd':{
		'name' : 'le_administration_psd',
		'type' : 'distance_based'
		'params' : {
			'min_dist' : 0,
			'max_dist' : 1000,
			'scale' : 'linear'
			}
		},
	'pit_hebergement_collectif_psd':{
		'name' : 'pit_hebergement_collectif_psd',
		'type' : 'density_based'
		'params' : {
			'min_density' : 0,
			'max_density' : 10,
			'scale' : 'linear'
			}
		},
	'pit_hotellerie_psd':{
		'name' : 'pit_hotellerie_psd',
		'type' : 'density_based'
		'params' : {
			'min_density' : 0,
			'max_density' : 5,
			'scale' : 'linear'
			}
		},
	'pit_patrimoine_culturel_psd':{
		'name' : 'pit_hotellerie_psd',
		'type' : 'distance_based'
		'params' : {
			'min_density' : 0,
			'max_density' : 5,
			'scale' : 'linear'
			}
		},
	'pit_restauration_psd':{
		'name' : 'pit_restauration_psd',
		'type' : 'density_based'
		'params' : {
			'min_density' : 0,
			'max_density' : 10,
                        'scale': 'linear'
			}
		}
       }
