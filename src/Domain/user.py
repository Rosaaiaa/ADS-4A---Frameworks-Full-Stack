class UserDomain:
    def __init__(self, name, cnpj, email, celular, password):
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.celular = celular
        self.password = password
        self.status = False
    
    def to_dict(self):
        return {
            "name": self.name,
            "cnpj": self.cnpj,
            "email": self.email,
            "celular": self.celular,
            "password": self.password,
            "status": self.status
        }
