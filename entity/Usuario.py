class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}"