import json

def get_static(nom_structure) :
	data = None
	with open('./profile/'+nom_structure+'.json') as f :
		data = json.load(f)
	return data

def get_critere(nom_critere) :
	data = None
	with open('./data/processed/'+nom_critere+'_psd.json') as f:
		data = json.load(f)
	return data
