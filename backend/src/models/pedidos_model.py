from src.settings.extensions import db

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from datetime import datetime

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
    status = Column(Enum, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow(), nullable=False)
    
    def __init__(self, user_id, status = Status_Pedido.PENDENTE.value):
        self.user_id = user_id
        self.status = status