from pydantic import BaseModel


class PokemonSchame(BaseModel): # contrato de dados, shcema de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True