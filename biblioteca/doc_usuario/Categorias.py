import os
from .Usuarios import Usuario


class Categoria:

    def __init__(self, nome_categoria, salario, porcet_cat):
        super.__init_subclass__(Usuario)
        self.usuario = None
        self.nome = self.usuario.nome
        self.nome_categoria = nome_categoria
        self.salario = salario
        self.porcent_cat = porcet_cat



    def criar_categoria(self):
        caminho_pasta = self.usuario.criar_pasta_usuarios()
