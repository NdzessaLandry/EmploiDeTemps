from random import randint
from emploiDeTemps import triEnseignant,Salle,Enseignant
from pandas import read_csv
import numpy as np
from ClasseSalle import construireLesSalles
from ClasseEnseignant import construireLesEnseignants
from tqdm import tqdm
import time

listeClasse=construireLesSalles()
listeEnseignant=construireLesEnseignants()
#print(listeEnseignant)
listeJour=["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
def produireEmploiDeTemps():
    for i in tqdm(range(len(listeClasse))):
        matiereChoisie=["aucune"]
        while listeClasse[i].nombreHeureSemaine!=0:
            #print(listeClasse[i].nombreHeureSemaine)
            n=randint(0,len(listeClasse[i].listeMatiere)-1)
            matiere=listeClasse[i].listeMatiere[n][0]
            if matiere not in matiereChoisie:
                E=triEnseignant(matiere,listeEnseignant)
                #print(E.listeMatiere)
                #print(E)
                matiereChoisie.append(matiere)
                j=randint(0,4)
                jour=listeJour[j]
                E.attribuerUneSalle(listeClasse[i].nom,listeClasse[i].heureMatiere(matiere),jour,matiere)
                listeClasse[i].attribuerEnseignant(matiere,listeClasse[i].heureMatiere(matiere),E,jour)
            else:
                #print(matiere)
                #print(listeClasse[i].listeEnseignant)
                E=listeClasse[i].retournerEnseignant(matiere)
                #print(E)
                j=randint(0,4)
                jour=listeJour[j]
                approbation=True
                while approbation:
                    j=randint(0,4)
                    jour=listeJour[j]
                    approbation=E.donneMatiereSalle(jour,listeClasse[i].nom,matiere)
                E.attribuerUneSalle(listeClasse[i].nom,listeClasse[i].heureMatiere(matiere),jour,matiere)
                listeClasse[i].attribuerEnseignant(matiere,listeClasse[i].heureMatiere(matiere),E,jour)
        #time.sleep(1)
    return listeEnseignant

l=produireEmploiDeTemps()
with open("emploiTemps.txt","w") as fic:
    for elt in listeClasse:
        print(elt.nom+"=", elt.listeEnseignant,file=fic)
    


    