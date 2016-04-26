from .gen_criteria import gen_criteria
from ..fs.fs import get_criteria
from ..db.db import closest_record

class pit_hebergement_collectif_psd(gen_criteria):
     MAX_DENSITY = 10
     
     def rank(self, coord, radius) :
          records = get_criteria('pit_hebergement_collectif_psd')
          density, closest, min_dist = density_around(records, coord, radius)
          mark = 10.0 * min(density, pit_hebergement_collectif_psd.MAX_DENSITY)/pit_hebergement_collectif_psd.MAX_DENSITY
          return mark
