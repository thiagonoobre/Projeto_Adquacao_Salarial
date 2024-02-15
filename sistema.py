from libery.criar_tratar_doc import *

cat_di_df = 'catalogo_despesas_investimentos.csv'

if not arquivoExiste(cat_di_df):
    criarArquivo(cat_di_df)

lerArquivo(cat_di_df)

