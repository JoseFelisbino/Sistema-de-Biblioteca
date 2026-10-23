from entity.usuario import Usuario 

class UsuarioService:
  def __init__(self):
    self.lista = []

  def cadastrar(self, nome, matricula):
    novoUsuario = Usuario(nome, matricula)
    self.lista.append(novoUsuario)
    return novoUsuario
