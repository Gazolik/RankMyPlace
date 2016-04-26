def get_profiles() : 
	data = None 
	with open('../../profile/profiles.json') as file : 
		data = json.load(file) 
	return data

def get_critere(nom_critere) :
	data = None
	with open('../../data/origin/'+nom_critere+'.json') as file :
		data = json.load(file)
	return data
