def construireLesSalles():
    liste=[]
    for i in range(listeClasse.shape[0]):
        l=list(listeClasse.iloc[i])
        #print(l)
        S=Salle(l[0],l[3],14,[(l[1],int(l[2]))])
        #print(S)
        etat=True
        if i==0:
            liste.append(S)
            #print(S)
        else:
            for elt in liste:
                if S==elt:
                    elt.listeMatiere.append((l[1],int(l[2])))
                    etat=False
                    break
            if etat:
                liste.append(S)
    return liste
