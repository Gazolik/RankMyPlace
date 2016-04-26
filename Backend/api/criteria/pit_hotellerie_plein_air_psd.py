from .gen_criteria import gen_criteria
class pit_hotellerie_plein_air_psd(gen_criteria):
     MAX_DENSITY = 3
     
     def rank(self, coord, radius) : 
          records = get_criteria('pit_hotellerie_plein_air_psd')
          density, closest, min_dist = density_around(records, coord, radius)
          mark = 10.0 * min(density, pit_hotellerie_plein_air_psd.MAX_DENSITY)/pit_hotellerie_plein_air_psd.MAX_DENSITY
          return mark
