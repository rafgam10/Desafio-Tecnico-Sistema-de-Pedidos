from src.settings.extensions import db

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import Enum as EnumSQL
from datetime import datetime
from enum import Enum

class Status_Pedido(Enum):
    PENDENTE = "pendente"
    EM_PROCESSAMENTO = "em_processamento"
    ENVIADO = "enviado"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"

class Pedido(db.Model):
    
    __tablename__ = "pedidos"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    status = Column(EnumSQL, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow(), nullable=False)
    
    usuario = db.relationship("Usuario", back_populates="pedidos")
    
    def __init__(self, user_id, status = Status_Pedido.PENDENTE.value):
        self.user_id = user_id
        self.status = status