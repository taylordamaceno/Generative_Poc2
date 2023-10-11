class PrevisãoOrçamentária:
    def __init__(self, database_url, api_key):
        self.database = psycopg2.connect(database_url)
        self.cursor = self.database.cursor()
        self.openai = openai.OpenAI(api_key)

    def obter_dados(self):
        """Obtém os dados da tabela `financas`."""
        self.cursor.execute("""
            SELECT preco_medio, valor_calculo, taxa_juros, inflacao, crescimento_vendas
            FROM financas
            WHERE id = 1
        """)
        return self.cursor.fetchone()

    def gerar_previsão(self, dados):
        """Gera a previsão orçamentária com base nos dados fornecidos."""
        mensagem = f"""
            Eu estou tentando fazer uma previsão orçamentária. Aqui estão os dados que tenho:
            - Preço médio: {dados[0]}
            - Valor de cálculo: {dados[1]}
            - Taxa de juros: {dados[2]}%
            - Inflação esperada: {dados[3]}%
            - Crescimento das vendas esperado: {dados[4]}%
            Com base nesses dados, qual seria sua previsão orçamentária para o próximo mês?
        """
        response = self.openai.Completion.create(
            engine="davinci",
            prompt=mensagem,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def fechar(self):
        """Fecha a conexão com o banco de dados."""
        self.cursor.close()
        self.database.close()

