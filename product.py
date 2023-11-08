from pydantic import BaseModel


class Product(BaseModel):
    nome: str
    valor: float
