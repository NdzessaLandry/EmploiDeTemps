class Enseignant:
    def __init__(self, listeMatiere:list, nombreHeureSemaine:int, nom:str):
        self.listeMatiere=listeMatiere
        self.nombreHeureSemaine=nombreHeureSemaine
        self.nom=nom
        self.listeClasse=[]
    def attribuerUneSalle(self,nomSalle:str,nombreHeure:int,jour:str,matiere:str):
        if self.nombreHeureSemaine!=0 and matiere in self.listeMatiere: 
            self.nombreHeureSemaine-=nombreHeure
            self.listeClasse.append((nomSalle,nombreHeure,jour))
            return True
        return False
    def __eq__(self, value: object) -> bool:
        return self.nom==value.nom
    def __repr__(self) -> str:
        return self.nom
    def donneMatiereSalle(self,jour,nomSalle,matiere):
        if matiere in self.listeMatiere:
            for elt in self.listeClasse:
                if elt[0]==nomSalle and elt[2]==jour:
                    return True
        return False
def triEnseignant(matiere:str,listeEnseigant:list):
    l=[]
    for E in listeEnseigant:
        if matiere in E.listeMatiere:
            l.append(E)
        else:
            pass
    try:
        n=randint(0,len(l)-1)
        return l[n]
    except:
        return l[0]

