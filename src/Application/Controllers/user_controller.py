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
    def login():
        cnpj = request.json.get("cnpj", None)
        password = request.json.get("password", None)

        user_status = UserService.check_login(cnpj, password)

        if user_status == None:
            return make_response(jsonify({
                "mensagem": "Credenciais inválidas. Por favor valide o cnpj e senha digitados."
            }))
        elif user_status == '0':
            return make_response(jsonify({
                "mensagem": "Usuário não ativado."
            }))

        access_token = create_access_token(identity=cnpj)
        return jsonify(access_token=access_token)
