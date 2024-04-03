import os
from biblioteca.criar_tratar_doc import arquivoExiste, criarArquivo


class Usuario:

    def __init__(self, nome):
        self.nome = nome
        self.arquivo_cat = 'catalogo_categorias.csv'

    def verificar_usuario(self):
        if not os.path.exists(self.nome):
            self.criar_usuario()
            print(f"Pasta do usuário '{self.nome}' criada com sucesso.")
            if not arquivoExiste(self.nome, self.arquivo_cat):
                criarArquivo(self.nome, self.arquivo_cat)

        else:
            print(f"A pasta do usuário '{self.nome}' já existe.")
            if not arquivoExiste(self.nome, self.arquivo_cat):
                criarArquivo(self.nome, self.arquivo_cat)

    def criar_usuario(self):
        try:
            os.makedirs(self.nome)
        except:
            print('Erro ao criar Usuario')
        else:
            print('usuario criado')

