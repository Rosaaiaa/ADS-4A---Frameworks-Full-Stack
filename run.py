from flask import Flask
from src.config.data_base import init_db, db
from src.routes import init_routes
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

def create_app():
    """
    Função que cria e configura a aplicação Flask.
    """
    app = Flask(__name__)

    init_db(app)

    init_routes(app)

    return app

app = create_app()
app.config["JWT_SECRET_KEY"] = "e999c435-6b35-4c11-89f3-efe62dd15f08"
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
