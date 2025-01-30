from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer

vandaag = datetime.date.today()
zeven_dagen_later = vandaag + datetime.timedelta(days=7)

bestelijst = {
    "besteling": [1, 7.00,],
    "Alie": [2, 9.00,],
    "Aice": [1, 19.00,],
    "lice": [3, 700.00,],

}

pdf_bestand = "C:/school/code/leren_progameren/project 2/pdf_invoice/output.pdf"

bedrijfsnaam = input('Wat is uw bedrijfsnaam? ')
adres = input('Wat is uw adres? ')
postcode = input('Wat is uw postcode? ')
mail = input('Wat is uw email? ')
product = input('Wat wilt u kopen? ')
aantal = input('Hoeveel wilt u? ')

c = canvas.Canvas(pdf_bestand, pagesize=letter)

c.setFont("Helvetica-Bold", 12)

c.drawString(80, 770, f"Facatuur")

c.setFont("Helvetica", 12)

c.drawString(80, 750, f"Codeminds")
c.drawString(80, 730, f"lichtenburglaan 24")
c.drawString(80, 710, f"1234 AB Amstelveen")
c.drawString(80, 690, f"0612345678")
c.drawString(80, 670, f"info@codeminds.nl")
c.drawString(80, 650, f"98765432")
c.drawString(80, 630, f"Nl987654321B01")

c.drawString(80, 580, f"Factuurnummer: CM-2025-001")
c.drawString(80, 560, f"Factuurdatum: {vandaag}")
c.drawString(80, 540, f"Vervaldatum: {zeven_dagen_later}")

c.setFont("Helvetica-Bold", 12)

c.drawString(80, 490, f"facatuur aan")

c.setFont("Helvetica", 12)


c.drawString(80, 470, f"{bedrijfsnaam}")
c.drawString(80, 450, f"{adres}")
c.drawString(80, 430, f"{postcode}")
c.drawString(80, 410, f"{mail}")

c.drawString(80, 390, f"Aantal : Prijs per stuk : Totaalprijs")

p = 390

for naam in bestelijst:

    totaal = bestelijst[naam][0] * bestelijst[naam][1]

    bestelijst[naam].append(totaal)

for naam in bestelijst:
    print(f"{naam}: {bestelijst[naam]}")

for naam, waarden in bestelijst.items():
    p -= 20
    c.drawString(80, p, f"{waarden[0]} : {waarden[1]} : {waarden[2]}")

c.save()

print(f"PDF opgeslagen als {pdf_bestand}")

