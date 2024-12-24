class Casa:
    def __init__(self, builder):
        self.area_aberta = builder.area_aberta
        self.comodo = builder.comodo
        self.garagem = builder.garagem
        self.jardim = builder.jardim
        self.armazem = builder.armazem

class CasaBuilder:
    def __init__(self):
        self.area_aberta = None
        self.comodo = None
        self.garagem = None
        self.jardim = None

    def set_area_aberta(self, area_aberta):
        self.area_aberta = area_aberta
        return self

    def set_comodo(self, comodo):
        self.comodo = comodo
        return self

    # ... outros métodos set para outras partes da casa

    def build(self):
        return Casa(self)

# Utilizando o Builder
builder = CasaBuilder()
casa_simples = builder.set_comodo("sala de estar").set_comodo("cozinha").set_comodo("quarto").set_comodo("banheiro").build()
casa_grande = builder.set_comodo("suíte principal").set_area_aberta("cantinho do churrasco").set_garagem("vaga 1").set_jardim("jardim dos fundos").set_armazem("armazem de comida").build()