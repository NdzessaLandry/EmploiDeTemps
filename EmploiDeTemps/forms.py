from flask_wtf import FlaskForm
#from wtforms import SelectMultipleField
from wtforms import StringField, IntegerField, DateField, SelectField, TimeField
#from flask_wtf_sqlalchemy import QuerySelectMultipleField
from wtforms.validators import DataRequired
from models import matiere

class classeForm(FlaskForm):
    code=StringField('CodeDeLaSalle',validators=[DataRequired()])
    nom=StringField("NomClasse",validators=[DataRequired()])
    niveau=IntegerField("NiveauDeLaClasse")
    heurecours=IntegerField("NombreHeureCours")
    
class matiereForm(FlaskForm):
    id=IntegerField("Id de la matiere",validators=[DataRequired()])
    intitule=StringField('Intitule de la matiere',validators=[DataRequired()])
    
class enseignantForm(FlaskForm):
    matricule=StringField('Matricule',validators=[DataRequired()])
    nom=StringField('NomDeEnseignant')
    prenom=StringField('Prenom')
    datenaissance=DateField("DateNaissance")
    heurecourssemaines=IntegerField('HuresDeCoursParSemaie')
    status=SelectField("Status de l'enseignant ",choices=[('1',"PLEG"),("2","PSEG"),("3","Censeur"),("4","Surveillant"),])
    nombreMatiere=IntegerField("Nombre de matiere dispensé par l'enseignant")
    #matieres = SelectMultipleField('Matières', coerce=int)