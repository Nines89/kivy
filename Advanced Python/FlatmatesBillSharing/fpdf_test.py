from fpdf import FPDF


if __name__ == "__main__":
    pdf = FPDF( orientation='P', unit='pt', format='A4')
    pdf.add_page()

    #add test
    pdf.set_font(family='Times', size=24, style='B')
    # ln permette di andare a capo dopo la cella in questione
    # align riguarda la posizione nella cella, non nel documento
    #questo effetto viene dato mettendo w=0 (la cella occupa l'intero documento)
    pdf.cell(w=0, h=80, txt='Flatmates Bill', align="C", ln=1)
    pdf.cell(w=87, h=40, txt='Period: ', border=0)
    pdf.cell(w=50, h=40, txt='March 2021', border=0)
    pdf.output("bill.pdf")
