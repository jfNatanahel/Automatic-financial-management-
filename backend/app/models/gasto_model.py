#DEfine estructura de datos
from pydantic import BaseModel
from datetime import date

class Gasto(BaseModel):
    fecha: date
    descripcion: str
    monto: float 
    categoria : str