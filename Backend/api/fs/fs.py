
import json

def get_static(basename) :
	data = None
	with open('./profile/'+basename+'.json', encoding='latin-1') as f :
		data = json.load(f)
	return data

def get_criteria(basename) :
	data = None
	with open('./data/database/'+basename+'_psd.json', encoding='latin-1') as f:
		data = json.load(f)
	return data
