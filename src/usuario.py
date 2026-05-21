class Usuario(object):
    def create(name, email, password, created_at):
        return {
            "name": name,
            "email": email,
            "password": password,
            "created_at": created_at
        }
    
