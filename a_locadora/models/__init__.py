from .base import db, ModeloBase
from .cliente_locadora import ClienteLocadora
from .veiculo import Veiculo
from .locacao import Locacao

__all__ = ["db", "ModeloBase", "ClienteLocadora", "Veiculo", "Locacao"]