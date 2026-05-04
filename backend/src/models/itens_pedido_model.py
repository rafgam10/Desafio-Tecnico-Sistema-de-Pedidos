from src.settings.extensions import db

from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Itens(db.Model):
    
    __tablename__ = "itens"
    
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    nome_produto = Column(String(255), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    
    def __init__(self, pedido_id, nome_produto, quantidade, preco):
        self.pedido_id = pedido_id
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco = preco