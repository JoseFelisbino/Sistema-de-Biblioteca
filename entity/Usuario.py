class Usuario:
    _contador_id = 1

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.idUsuario = Usuario._contador_id

        Usuario._contador_id += 1
    
    def __str__(self):
        return f"ID: {self.idUsuario}, Nome: {self.nome}, Matrícula: {self.matricula}"
