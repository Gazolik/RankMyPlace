

def ranking_handler(path, data, api_param):
    #extraire les criteres utiles
    criteres= data['criteres']
    nomcriteres=[c['name'] for c in criteres if c['coef'] !=0]

    #evaluer les criteres

    #faire une moyenne

    #retourner les notes
