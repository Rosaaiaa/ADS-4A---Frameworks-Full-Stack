from src.Application.Controllers.user_controller import UserController
from flask import jsonify, make_response

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    @app.route('/user/ativacao', methods=['POST'])
    def ativacao_user():
        return UserController.ativacao()
    
    @app.route('/user', methods=['GET'])
    def get_users():
        users = UserController.list_users()
        return users
    
    @app.route('/user/<int:id>', methods=['PUT'])
    def update_user(id):
        return UserController.update_user(id)
    
    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        return UserController.delete_user(id)
    
    @app.route('/login', methods=['POST'])
    def login():
        return UserController.login()

    

