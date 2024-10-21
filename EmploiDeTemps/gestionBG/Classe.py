class Salle:
    def __init__(self,nom,niveau,nombreHeureSemaine,listeMatiere:list):
        #La liste des matiers d'une salle sera consituée d'un couple (intitulé, heureParSemaine)
        self.nom=nom
        self.niveau=niveau
        self.listeMatiere=listeMatiere
        self.listeEnseignant=[]
        self.nombreHeureSemaine=nombreHeureSemaine
    def attribuerEnseignant(self,matiere,heure, E:Enseignant,jour):
        if self.nombreHeureSemaine!=0:
            self.nombreHeureSemaine-=heure
            self.listeEnseignant.append((E, heure,matiere,jour))
            return True
        else:
            return False
    
    def valider(self,matiere,heure):
        for i in range(len(self.listeMatiere)):
            if self.listeMatiere[i][0]==matiere:
                a=self.listeMatiere[i][1]-heure
                self.listeMatiere[i]=(matiere,a)
                break
                
    def heureMatiere(self,matiere):
        for elt in self.listeMatiere:
            if elt[0]==matiere:
                if elt[1]>=10:
                    self.valider(matiere,3)
                    return 3
                else :
                    self.valider(matiere,3)
                    return 2
    def retournerEnseignant(self,matiere):
        for elt in self.listeEnseignant:
            if elt[2]==matiere:
                return elt[0]
    def __eq__(self, value: object) -> bool:
        return self.nom==value.nom
    
    def __repr__(self) -> str:
        char=self.nom
        for elt in self.listeMatiere:
            char2="/n"
            for elt2 in elt:
                char2+=str(elt2)
            char+="/n"
        return char
