class PrevisãoOrçamentáriaController:
    def __init__(self, database_url, api_key):
        self.previsão = PrevisãoOrçamentária(database_url, api_key)
        self.view = PrevisãoOrçamentáriaView(self.previsão)

    def executar(self):
        """Executa todas as etapas da previsão."""
        previsão = self.previsão.gerar_previsão()
        pdf = self.view.gerar_pdf()
        with open("previsoes.pdf", "wb") as f:
            f.write(pdf)

