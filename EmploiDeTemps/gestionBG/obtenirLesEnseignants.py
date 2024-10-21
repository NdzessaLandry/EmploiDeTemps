data=read_csv("dataEn.csv")
#print(data)
def construireLesEnseignants():
    liste=[]
    for i in range(data.shape[0]):
        l=list(data.iloc[i])
        #print(l)
        E=Enseignant([l[1]],l[2],l[0])
        #print(S)
        etat=True
        if i==0:
            liste.append(E)
            #print(S)
        else:
            for elt in liste:
                if E==elt:
                    elt.listeMatiere.append(l[1])
                    etat=False
                    break
            if etat:
                liste.append(E)
    return liste
