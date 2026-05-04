from src.settings.extensions import db

from sqlalchemy import Column, Integer, String

class Usuario(db.Model):
    
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    senha = Column(String(255), nullable=False)
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    