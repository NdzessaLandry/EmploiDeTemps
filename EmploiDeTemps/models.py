#Ce fichier définie la structure des tables dans la base de données

from flask_sqlalchemy import SQLAlchemy 
db=SQLAlchemy()
class classe(db.Model):
    __tablename__="classe"
    code=db.Column(db.String(5),primary_key=True)
    nom=db.Column(db.String(10),nullable=False)
    niveau=db.Column(db.SmallInteger)
    heurecours=db.Column(db.SmallInteger)
    def __repr__(self):
        return f'Classe {self.nom}'
    
class enseignant(db.Model):
    __tablename__="enseignant"
    matricule=db.Column(db.String(20),primary_key=True)
    nom=db.Column(db.String(20))
    prenom=db.Column(db.String(20))
    datenaissance=db.Column(db.Date())
    heurecourssemaines=db.Column(db.SmallInteger)
    status=db.Column(db.String(1))
    #matieres = db.relationship('EnseignantMatiere', back_populates='enseignant')

    def __repr__(self):
        return f'Enseignant {self.nom} {self.prenom}'
class matiere(db.Model):
    __tablename__='matiere'
    id=db.Column(db.SmallInteger,primary_key=True)
    intitule=db.Column(db.String(20))
    #enseignants = db.relationship('EnseignantMatiere', back_populates='matiere')
    def __repr__(self):
        return f'Matiere {self.intitule}'
    
class enseignant_matiere(db.Model):
    __tablename__='EnseignantMatiere'
    idEnseignant=db.Column(db.String(20),db.ForeignKey("Enseignant.matricule"),primary_key=True)
    idMatiere=db.Column(db.SmallInteger,db.ForeignKey("Matiere.id"),primary_key=True)
   # enseignant = db.relationship('Enseignant', back_populates='matieres')
    #matiere = db.relationship('Matiere', back_populates='enseignants')
class enseignant_matiere_classe(db.Model):
    __tablename__='EnseignantMatiereClasse'
    idEnseignant=db.Column(db.String(20),db.ForeignKey("Enseignant.matricule"),primary_key=True)
    idMatiere=db.Column(db.SmallInteger,db.ForeignKey('Matiere.id'),primary_key=True)
    idClasse=db.Column(db.String(5),db.ForeignKey("classe.code"),primary_key=True)
    jour=db.Column(db.String(10))
    duree=db.Column(db.SmallInteger)
    periode=db.Column(db.Time,nullable=False)
    