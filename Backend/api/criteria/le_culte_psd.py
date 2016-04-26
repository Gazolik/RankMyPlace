from .gen_criteria import gen_criteria
from ..fs.fs import get_criteria
from ..db.db import closest_record

class le_culte_psd(gen_criteria): 
    MAX_DIST = 1000.0 # meters

    def rank(self, coord):
        records = get_criteria('le_culte_psd')
        dist, record = closest_record(records, coord)
        mark = 10.0 * (1.0 - (min(dist, le_culte_psd.MAX_DIST)/le_culte_psd.MAX_DIST))
        return mark
           