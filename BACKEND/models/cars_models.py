from pydantic import BaseModel

class Cars(BaseModel):
    marca: str
    modelo: str
    año: int
    precio: str
    kilometraje: int
    color: str
    imagen_principal: str
    descripcion: str
