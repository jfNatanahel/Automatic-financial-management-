#Logica y analisis real.
import panda as pd
from app.models.gasto_model import Gasto
from typing import List

def leer_movientos():
    df = pd.read_cvs("automatic-financial-magagement-/backend/app/data/movimientos.csv", parse_dates=["fecha"])
    return df
def obtener_resumen_categoria():
    #Leer los movimientos
    #Seleccionar que columna y realizar una suma.
    #Retornar un diccionario con la categoria y el monto total.