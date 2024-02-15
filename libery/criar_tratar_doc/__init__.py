import pandas as pd


def arquivoExiste(nome):
    try:
        pd.read_csv(nome)
    except:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        df = pd.DataFrame()
        df.to_csv(nome, index=False, sep=';')
    except:
        print('Houve um erro na criação do aquivo')
    else:
        print(f'Aquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        df = pd.read_csv(nome)
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(df)

