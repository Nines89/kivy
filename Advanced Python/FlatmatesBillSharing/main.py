import webbrowser

from filestack import Client
from fpdf import FPDF


class Bill:
    """
    Object that contains data about the bill, souch a total amount
    and the period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatname person to share the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 1)


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        # add icon
        pdf.image(name="logo.png", w=60, h=60)
        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        # ln permette di andare a capo dopo la cella in questione
        # align riguarda la posizione nella cella, non nel documento
        # questo effetto viene dato mettendo w=0 (la cella occupa l'intero documento)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align="C", ln=1)

        pdf.set_font(family='Times', size=18)
        # inserte labels period
        pdf.cell(w=87, h=40, txt='Period: ', border=0)
        pdf.cell(w=50, h=40, txt=bill.period, border=0, ln=1)

        # inserte labels name amount flatmates
        pdf.cell(w=87, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=50, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # inserte labels name amount flatmates
        pdf.cell(w=87, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=50, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        pdf.output(self.filename)
        # apre direttamente il pdf
        webbrowser.open(self.filename)

"""#creiamo una nuova classe, altrimenti potremmo mandare solo un pdf
#per la classe in questione vedi file_stack.py"""
class FileSharer:
    def __init__(self, file_path, api_key):
        self.api_key = api_key
        self.file_path = file_path

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.file_path)
        return new_file_link


if __name__ == '__main__':
    bill = Bill(120, "March 2022")
    john = Flatmate("John", 20)
    marry = Flatmate("Marry", 25)
    print("John pays: ", john.pays(bill, marry))
    print("Marry pays: ", marry.pays(bill, john))

    pdf_report = PdfReport(filename="Report1.pdf")
    pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)

    file_sharer = FileSharer(file_path=pdf_report.filename, api_key="specific api")
