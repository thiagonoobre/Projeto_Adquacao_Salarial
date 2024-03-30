from libery.doc_usuario import *
class Categoria:

    def __init__(self, usuario, salario, porcet_cat):
        self.usuario = usuario
        self.salario = salario
        self.porcent_cat = porcet_cat


# programa

ad_thiago = Categorias('Essencial', 2200, 55)

print(ad_thiago.salario)
