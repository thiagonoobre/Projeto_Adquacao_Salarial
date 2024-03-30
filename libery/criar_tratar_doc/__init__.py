import pandas as pd


def arquivoExiste(nome_pasta, nome_arq):
    try:
        pd.read_csv(f'{nome_pasta} / {nome_arq}')
    except:
        return False
    else:
        return True


def criarArquivo(nome_pasta, nome_arq):
    try:
        df = pd.DataFrame()
        df.to_csv(f'{nome_pasta}/{nome_arq}', index=False, sep=';')

    except:
        print('Houve um erro na criação do aquivo')
    else:
        print(f'Aquivo {nome_arq} criado com sucesso!')


def lerArquivo(nome_arq):
    try:
        df = pd.read_csv(nome_arq, sep=';')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(df)
