import os
from libery.criar_tratar_doc import arquivoExiste, criarArquivo


def verificar_usuario(nome):
    if not os.path.exists(nome):
        criar_usuario(nome)
        print(f"Pasta do usuário '{nome}' criada com sucesso.")
        if not arquivoExiste(nome, cat):
            criarArquivo(nome, cat)

    else:
        print(f"A pasta do usuário '{nome}' já existe.")
        if not arquivoExiste(nome, cat):
            criarArquivo(nome, cat)


def criar_usuario(nome):
    try:
        os.makedirs(nome)
    except:
        print('Erro ao criar Usuario')
    else:
        print('usuario criado')


cat = 'catalogo_categorias.csv'


verificar_usuario('Thiago')



