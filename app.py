import sklearn
import joblib
import pandas as pd
from fonctions_maisons import extraire_la_premiere_lettre
from flask import Flask, request

#Load Model
pipeline=joblib.load('titanic.model')

# Démarrer l'application flask
app = Flask('__name__')


# Faire des prédiction
@app.route('/predict',methods=['POST'])
def predict(): 
  df=pd.DataFrame(request.json)
  resultat=pipeline.predict(df)[0]
  return(str(resultat) , 201)


#Test de l'API
@app.route('/ping',methods=['GET'])
def ping():
  return('pong',200)

# Page d'accueil
@app.route('/')
def index():
  return "<h1>Bienvenue dans notre API. Utiliser  /predict en POST pour faire des prédictions sur le Titanic <h1>"

# Si on est le main, on lance
if __name__ == "__main__":
  app.run(host='0.0.0.0')