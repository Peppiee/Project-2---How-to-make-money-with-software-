from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer

vandaag = datetime.date.today()
zeven_dagen_later = vandaag + datetime.timedelta(days=7)

btw = 21

bedrijfsnaam = input('Wat is uw bedrijfsnaam? ')
adres = input('Wat is uw adres? ')
postcode = input('Wat is uw postcode? ')
mail = input('Wat is uw email? ')
product = input('Wat wilt u kopen? ')
aantal = input('Hoeveel wilt u? ')
Bankrekeningnummer = input("wit is je Bankrekeningnummer")
Ten_name_van = input("Ten name van: ")
Betalingsreferentie = input("Betalingsreferentie: ")

bestelijst = {
    "besteling": [1, "cloud" , 7.00,],
    "Alie": [2, "pc", 9.00,],
    "Aice": [1, "nid", 19.00,],
    "lice": [3, "lid", 700.00,],

}

pdf_bestand = "C:\school\code\Project-2---How-to-make-money-with-software-\project 2\pdf_invoice\output.pdf"

c = canvas.Canvas(pdf_bestand, pagesize=letter)

c.setFont("Helvetica-Bold", 12)

c.drawString(80, 770, f"Factuur")

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

c.drawString(80, 490, f"factuur aan")

c.setFont("Helvetica", 12)


c.drawString(80, 470, f"{bedrijfsnaam}")
c.drawString(80, 450, f"{adres}")
c.drawString(80, 430, f"{postcode}")
c.drawString(80, 410, f"{mail}")

c.drawString(80, 370, f"Aantal : omschrijfing : Prijs per stuk : Totaalprijs")

p = 370

for naam in bestelijst:

    totaal = bestelijst[naam][0] * bestelijst[naam][2]

    bestelijst[naam].append(totaal)

for naam in bestelijst:
    print("corret toe gevoegt")

for naam, waarden in bestelijst.items():
    p -= 20
    c.drawString(80, p, f"   {waarden[0]}")
    c.drawString(120, p, f"   {waarden[1]}")
    c.drawString(195, p, f"   {waarden[2]}")
    c.drawString(250, p, f"   {waarden[3]}")

subtotaal = []

for naam in bestelijst:
    subtotaal.append(bestelijst[naam][3])


sub_totaal = sum(subtotaal)

c.drawString(80, 190, f"Subtotaal: {sub_totaal}")
c.drawString(80, 170, f"btw: {btw}%")

btw_bedrag = sub_totaal * (btw / 100)

c.drawString(80, 150, f"totaal: {btw_bedrag}")

c.setFont("Helvetica-Bold", 12)
c.drawString(80, 110, f"betaal gegevens")
c.setFont("Helvetica", 12)

c.drawString(80, 90, f"Bankrekeningnummer: {Bankrekeningnummer}")
c.drawString(80, 70, f"Ten name van: {Ten_name_van}")
c.drawString(80, 50, f"Betalingsreferentie: {Betalingsreferentie}")

c.drawString(80, 10, f"Bedankt voor uw vertrouwen in CodeMinde!")


c.save()

print(f"PDF opgeslagen als {pdf_bestand}")

