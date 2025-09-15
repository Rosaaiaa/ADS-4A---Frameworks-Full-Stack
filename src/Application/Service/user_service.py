from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db 
from ...Infrastructure.http.whats_app import gera_codigo

class UserService:
    @staticmethod
    def create_user(name, cnpj, email, celular, password):
        codigo = gera_codigo()

        new_user = UserDomain(name, cnpj, email, celular, password, codigo)
        user = User(name=new_user.name, cnpj=new_user.cnpj, email=new_user.email, celular=new_user.celular, password=new_user.password, status=new_user.status, codigo=new_user.codigo)        
        db.session.add(user)
        db.session.commit()
        
        return user
    
    @staticmethod
    def verifica_codigo(cnpj, codigo_user):
        user = User.query.filter_by(cnpj=cnpj).first()
        if not user:
            return False

        if codigo_user == user.codigo:
            user.status = True
            user.codigo = None 
            db.session.commit()
            return True
        else:
            return False

            
    
    @staticmethod
    def list_users():
        users = User.query.all()
        user_list = []
        for user in users:
            user_list.append(user.to_dict())
        return user_list

    @staticmethod
    def update_user(id, data):
        user = User.query.get(id)
        for chave, valor in data.items():
            setattr(user, chave, valor)

        db.session.commit()
        return user.to_dict()
    
    @staticmethod
    def delete_user(id):
        user = User.query.get(id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return user
    
    @staticmethod
    def uptate_status(id):
        user = User.query.get(id)
        print(user)

    @staticmethod
    def check_login(cnpj, password):
        user = User.query.filter_by(cnpj=cnpj, password=password).first()
        if user:
            user_dict = user.to_dict()
            return user_dict['status']
        return None