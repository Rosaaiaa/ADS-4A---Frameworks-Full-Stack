from flask import request, jsonify, make_response
from src.Application.Service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        name = data.get('name')
        cnpj = data.get('cnpj')
        email = data.get('email')
        celular = data.get('celular')
        password = data.get('password')

        if not name or not email or not password:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        user = UserService.create_user(name, cnpj, email, celular, password)
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)
    
    @staticmethod
    def list_users():
        users = UserService.list_users()
        return make_response(jsonify({
            "users": users
        }), 200)

    @staticmethod
    def update_user(id):
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Missing update data"}), 400)
        
        updated_user = UserService.update_user(id, data)
        return make_response(jsonify({
            "mensagem": "User atualizado com sucesso",
            "usuarios": updated_user
        }), 200)

    @staticmethod
    def delete_user(id):
        user = UserService.delete_user(id)
        if user == None:
            return make_response(jsonify({
                "mensagem": "Não existe User com esse ID"
            }))
        return make_response(jsonify({
            "mensagem": "User deletado com sucesso"
        }), 200)