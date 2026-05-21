class EnderecoUsuario(object):
    def add(usuario, cep, logradouro, numero, bairro, complemento=None):
        return {
            "usuario": usuario,
            "enderecos": [{
                "cep": cep,    
                "logradouro": logradouro,
                "numero": numero,
                "bairro": bairro,
                "complemento": complemento
            }]    
        }