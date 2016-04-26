

def ranking_handler(path, data, api_param):
    #extraire les criteres utiles
    criteres= data['criteres']
    nomcriteres=[c['name'] for c in criteres if c['coef'] !=0]

    #evaluer les criteres
    notes = {}
    for i in nomcriteres:
        notes[i] = criterias_dic[i].rank()
    #faire une moyenne
    moy = sum(notes.values())/len(nomcriteres)

    #retourner les notes
    ret_data = {"moyenne":moy,"notes":notes}
    return Response(api_param).serialized(ret_data)
