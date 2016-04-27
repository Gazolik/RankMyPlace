import json

def create_heatmap(filename, criteria) :
    out_file = filename.split('/')[-1].replace('_grid', '_heatmap')
	with open(filename, 'r') as f :
		points = json.load(f)
		heatmap=[]
		for p in points :
			spec['criteria']=criteria
			spec['coordinates']={'lat':p[0],'lon':p[1]}
			mark=rank(spec)
			heatmap.append([p, mark])
		
		with open(criteria+'_'+out_file, 'w') as heatmap_file :
			heatmap_file.write(json.dumps({
					'criteria':criteria,
					'heatmap':heatmap
				}))
		