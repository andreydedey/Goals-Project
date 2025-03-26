from flask import Flask

from src.routes.goal_routes import goal_route_bp
from src.routes.user_routes import user_route_bp
from src.models.config.connection import db_connection_handler

app = Flask(__name__)

# Conectar no Banco de Dados
db_connection_handler.connect_to_db()

# Registrar Blueprint
app.register_blueprint(goal_route_bp)
app.register_blueprint(user_route_bp)
