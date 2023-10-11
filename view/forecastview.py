class PrevisãoOrçamentáriaView:
    def __init__(self, previsão):
        self.previsão = previsão

    def gerar_pdf(self):
        """Gera o documento PDF com a previsão."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "Previsão Orçamentária", 0, 1, "C")
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(200, 10, self.previsão.gerar_previsão())
        return pdf.output("previsoes.pdf")

