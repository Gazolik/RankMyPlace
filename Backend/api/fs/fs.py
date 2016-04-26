
import json

def get_static(nom_structure) :
	with open('./static/'+nom_structure+'.json', encoding='latin-1') as f :
		return json.loads(f.read())

def get_critere(nom_critere) :
	data = None
	with open('./data/processed/'+nom_critere+'_psd.json', encoding='latin-1') as f:
		data = json.load(f)
	return data
