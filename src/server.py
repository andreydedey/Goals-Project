from flask import Flask

from src.routes.user_routes import user_route_bp
from src.routes.goal_routes import goal_route_bp
from src.routes.goal_completion_routes import goal_completion_route_bp
from src.models.config.connection import db_connection_handler
from src.models.config.seed import create_seeds

app = Flask(__name__)

# Connect to database
db_connection_handler.connect_to_db()

# seed data
create_seeds()

# Register Bluepring
app.register_blueprint(goal_route_bp)
app.register_blueprint(user_route_bp)
app.register_blueprint(goal_completion_route_bp)
