from . import db
from models import ModeloBase

# Dica: data_inicio/data_fim usam db.Date (importe Date se precisar)


class Locacao(ModeloBase):
    __tablename__ = "locacoes"

    # TODO ALUNO: FK cliente_id → clientes_locadora.id
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes_locadora.id"), nullable=False)
    # TODO ALUNO: FK veiculo_id → veiculos.id
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)

    # TODO ALUNO: relationship cliente e veiculo
    cliente = db.relationship("ClienteLocadora", back_populates="locacoes")
    veiculo = db.relationship("Veiculo", back_populates="locacoes")

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_inicio.desc()).all()