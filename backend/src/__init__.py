from flask import Flask
from .settings.config import Config
from .settings.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    try:
        from .routes import register_routes
        register_routes(app)
        
        from src.models.usuarios_model import Usuario
        from src.models.pedidos_model import Pedido
        from src.models.itens_pedido_model import Itens
        
    except Exception:
        pass

    return app
