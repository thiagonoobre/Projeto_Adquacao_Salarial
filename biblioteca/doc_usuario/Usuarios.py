import os
from biblioteca.criar_tratar_doc import arquivoExiste, criarArquivo


class Usuario:

    def __init__(self, nome):
        self.nome = nome
        self.arquivo_cat = 'catalogo_categorias.csv'
        self.pasta_usuarios = 'Usuarios'

    def criar_pasta_usuarios(self):
        caminho_pasta = os.getcwd()
        caminho_completo = os.path.join(caminho_pasta, self.pasta_usuarios)
        try:
            if not os.path.exists(caminho_completo):
                os.makedirs(caminho_completo)
                print(f'Pasta {caminho_completo} criada com sucesso')
            else:
                print(f'A pasta {caminho_completo} ja existe')
        except OSError as erro:
            print(f'Erro ao criar a pasta {caminho_completo}: {erro} ')
        else:
            return caminho_completo

    def verificar_usuario(self):
        caminho_completo = self.criar_pasta_usuarios()

        pasta_do_usuario = os.path.join(caminho_completo, self.nome)
        if not os.path.exists(pasta_do_usuario):
            self.criar_usuario(pasta_do_usuario)
            print(f"Pasta do usuário '{self.nome}' criada com sucesso.")
            if not arquivoExiste(pasta_do_usuario, self.arquivo_cat):
                criarArquivo(pasta_do_usuario, self.arquivo_cat)

        else:
            print(f"A pasta do usuário '{self.nome}' já existe.")
            if not arquivoExiste(pasta_do_usuario, self.arquivo_cat):
                criarArquivo(pasta_do_usuario, self.arquivo_cat)

    def criar_usuario(self, caminho):
        usuario = os.path.join(caminho)
        try:
            os.makedirs(usuario)
        except:
            print(f'Erro ao criar Usuario {usuario}')
        else:
            print(f'usuario criado {usuario}')
