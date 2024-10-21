from flask import render_template, Flask, url_for, redirect,request,session
from models import db,classe, matiere, enseignant
from forms import classeForm,enseignantForm,matiereForm
from models import enseignant_matiere
from flask_migrate import Migrate

app=Flask(__name__)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:40503@localhost/projetlycee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="40503"
db.init_app(app)

@app.route("/admin",methods=["GET","POST"])
def admin():
    administrateur={"Landry":"40503","joseph":60506,"pascal":240411}
    if request.method=="POST":
        for k in administrateur:
            if k==request.form["user"] and administrateur[k]==request.form["password"]:
                session["name"]=k
                return redirect(url_for('connection'))
    return render_template("login.html")

@app.route("/Administrateur")
def connection():
    return render_template("admin.html",data=session["name"])
@app.route("/",methods=["GET","POST"])
def index():
    administrateur={"Landry":40503,"joseph":60506,"pascal":240411}
    if request.method=="POST":
        for k in administrateur:
            if k==request.form["user"] and administrateur[k]==request.form["password"]:
                session["user"]=k
                return redirect(url_for("admin"))
    return render_template('base.html')  # Assure-toi que 'index.html' existe

@app.route('/ajouterClasse',methods=["GET","POST"])
def addClasse():
    form=classeForm()
    if form.validate_on_submit():
        classe1=classe(code=form.code.data,
                      nom=form.nom.data,
                      niveau=form.niveau.data,
                      heurecours=form.heurecours.data
                      )
        db.session.add(classe1)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('addClasse.html',form=form)
def obtenirMatiere():
    return matiere
@app.route('/ajouterMatiere',methods=["GET",'POST'])
def addMatiere():
    form=matiereForm()
    if form.validate_on_submit():
        matiere1=matiere(id=form.id.data,intitule=form.intitule.data)
        db.session.add(matiere1)
        db.session.commit()
        return redirect(url_for("admin"))
    return render_template('addMatiere.html',form=form)
@app.route('/ajouterEnseignant',methods=["GET","POST"])
def addEnseignant():
    form = enseignantForm()
    
    #form.matieres.choices = [(matiere1.id, matiere1.intitule) for matiere1 in obtenirMatiere().query.all()]
    if form.validate_on_submit():
        enseignant1=enseignant(matricule=form.matricule.data,
                             nom=form.nom.data,
                             prenom=form.prenom.data,
                             datenaissance=form.datenaissance.data,
                             heurecourssemaines=form.heurecourssemaines.data,
                             status=form.status.data
                             )
        
        db.session.add(enseignant1)
        db.session.commit()
        return redirect(url_for("admin"))
    return render_template("addEnseignant.html",form=form)

@app.route("/manager",methods=["GET","POST"])
def manager():
    if request.method=="POST":
        

if __name__=="__main__":
    app.run(debug=True)
    

