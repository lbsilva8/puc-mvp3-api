from pydantic import BaseModel
from typing import Optional, List
from model.serie import Serie


class SerieSchema(BaseModel):
    """Define como uma nova serie/filme deve ser representado ao ser adicionado
    """
    nome: str = "Wandinha"
    status: Optional[str] = "Aguardando"
    temporada: float = 1.0
    aplicativo: str = "Netflix"
    categoria: str = "Serie"

class SerieBuscaNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da serie/filme.
    """
    nome: str = "Wandinha"

class SerieBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da serie/filme.
    """
    id: int = 1

class ListagemSeriesSchema(BaseModel):
    """Define como uma listagem de serie/filme será retornada.
    """
    series:List[SerieSchema]

class SerieCategoriaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da serie.
    """
    categoria:List[SerieSchema]

def apresenta_series(series: List[Serie]):
    """ Retorna uma representação da serie/filme seguindo o schema definido em
        SerieViewSchema.
    """
    result = []
    for serie in series:
        result.append({
            "nome": serie.nome,
            "status": serie.status,
            "temporada": serie.temporada,
            "aplicativo": serie.aplicativo,
            "categoria": serie.categoria
        })
    return {"series": result}

class SerieViewSchema(BaseModel):
    """ Define como um item será retornado: item + comentários.
    """
    id: int = 1
    nome: str = "Wandinha"
    status: str = "Aguardando"
    temporada: float = 1.0
    aplicativo: str = "Netflix"
    categoria: str = "Serie"

class SerieDelSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_serie(serie: Serie):
    """ Retorna uma representação da serie/filme seguindo o schema definido em
        SerieViewSchema.
    """
    return{
        "id": serie.id,
        "nome": serie.nome,
        "status": serie.status,
        "temporada": serie.temporada,
        "aplicativo": serie.aplicativo,
        "categoria": serie.categoria
    }