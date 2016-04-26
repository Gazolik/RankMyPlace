from .gen_criteria import gen_criteria
class pit_patrimoine_naturel_psd(gen_criteria): 
    MAX_DIST = 500.0 # meters

    def rank(self, coord):
        records = get_criteria('pit_patrimoine_naturel_psd')
        dist, record = closest_record(records, coord)
        mark = 10.0 * (1.0 - (min(dist, pit_patrimoine_naturel_psd.MAX_DIST)/pit_patrimoine_naturel_psd.MAX_DIST))