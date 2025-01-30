from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
import json

with open('2000-096.json', 'r') as file:
    data = json.load(file)

bestelijst = {

}

ordernummer = data['order']['ordernummer']
orderdatum = data['order']['orderdatum']
betaaltermijn = data['order']['betaaltermijn']

naam = data['order']['klant']['naam']
adres = data['order']['klant']['adres']
postcode = data['order']['klant']['postcode']
stad = data['order']['klant']['stad']
KVK_nummer = data['order']['klant']['KVK-nummer']

# producten

productnaam = data['order']['producten'][0]['productnaam']
aantal = data['order']['producten'][0]['aantal']
prijs_per_stuk_excl_btw = data['order']['producten'][0]['prijs_per_stuk_excl_btw']
btw = data['order']['producten'][0]['btw_percentage']

for i in range(1):
    bestelijst[f"bestelling {i}"] = [aantal, productnaam, prijs_per_stuk_excl_btw]

mail = "info@***********"
Bankrekeningnummer = 10242982854924
Ten_name_van = "codemind"
Betalingsreferentie = 1058901850195



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

c.drawString(80, 580, f"Factuurnummer: {ordernummer}")
c.drawString(80, 560, f"Factuurdatum: {orderdatum}")
c.drawString(80, 540, f"Vervaldatum: {betaaltermijn}")

c.setFont("Helvetica-Bold", 12)

c.drawString(80, 490, f"factuur aan")

c.setFont("Helvetica", 12)


c.drawString(80, 470, f"{naam}")
c.drawString(80, 450, f"{adres}")
c.drawString(80, 430, f"{postcode}")
c.drawString(80, 410, f"{mail}")

c.drawString(80, 370, f"Aantal      :      omschrijfing      :      Prijs per stuk      :      Totaalprijs")

p = 370

for naam in bestelijst:
    totaal = bestelijst[naam][0] * bestelijst[naam][2]
    
    totaal = round(totaal, 2)
    
    bestelijst[naam].append(totaal)

for naam in bestelijst:
    print("corret toe gevoegt")

for naam, waarden in bestelijst.items():
    p -= 20
    c.drawString(80, p, f"   {waarden[0]}")
    c.drawString(120, p, f"   {waarden[1]}")
    c.drawString(260, p, f"   {waarden[2]}")
    c.drawString(370, p, f"   {waarden[3]}")

subtotaal = []

for naam in bestelijst:
    subtotaal.append(bestelijst[naam][3])


sub_totaal = sum(subtotaal)

c.drawString(80, 190, f"Subtotaal: {sub_totaal}")
c.drawString(80, 170, f"btw: {btw}%")

btw_bedrag = sub_totaal * (btw / 100)
btw_bedrag += sub_totaal

c.drawString(80, 150, f"totaal: {round(btw_bedrag),2}")

c.setFont("Helvetica-Bold", 12)
c.drawString(80, 110, f"betaal gegevens")
c.setFont("Helvetica", 12)

c.drawString(80, 90, f"Bankrekeningnummer: {Bankrekeningnummer}")
c.drawString(80, 70, f"Ten name van: {Ten_name_van}")
c.drawString(80, 50, f"Betalingsreferentie: {Betalingsreferentie}")

c.drawString(80, 10, f"Bedankt voor uw vertrouwen in CodeMinde!")


c.save()

print(f"PDF opgeslagen als {pdf_bestand}")

