import pandas as pd
def extraire_la_premiere_lettre(serie):
  # récuperer une serie en argument
  # retourner un DataFrame (Compatible)
  return (pd.DataFrame(serie.str[0]))# recuperer la première lettre 
