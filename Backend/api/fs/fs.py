import json

def get_static(basename) :
	data = None
	with open('./profile/'+basename+'.json') as f :
		data = json.load(f)
	return data

def get_criteria(basename) :
	data = None
	with open('./data/database/'+basename+'_psd.json') as f:
		data = json.load(f)
	return data
