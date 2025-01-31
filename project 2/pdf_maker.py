import json
import os
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

map_pad = "C:\\school\\code\\Project-2---How-to-make-money-with-software-\\project 2\\test_set_PC"
pdf_map = "C:\\school\\code\\Project-2---How-to-make-money-with-software-\\project 2\\pdf_invoice"
doelmap = "C:\\school\\code\\Project-2---How-to-make-money-with-software-\\project 2\\json_order_error"




for bestand in os.listdir(map_pad):
    if bestand.endswith(".json"): 
        bestandspad = os.path.join(map_pad, bestand) 
        
        try:
            with open(bestandspad, "r", encoding="utf-8") as file:
                data = json.load(file)
                bron = bestandspad
        except Exception as e:
            print(f"Fout bij openen van {bestand}: {e}")
            continue 
        
        try:
            bestelijst = {}

            ordernummer = data['order']['ordernummer']
            orderdatum = data['order']['orderdatum']
            betaaltermijn = data['order']['betaaltermijn']

            naam = data['order']['klant']['naam']
            adres = data['order']['klant']['adres']
            postcode = data['order']['klant']['postcode']
            stad = data['order']['klant']['stad']
            KVK_nummer = data['order']['klant']['KVK-nummer']

            factuur = data.get('order', {})
            producten = factuur.get('producten', [])

            totaal_1 = []

            for product in producten:
                productnaam = product.get('productnaam', 'Onbekend product')
                aantal = product.get('aantal', 0) 
                prijs_per_stuk_excl_btw = product.get('prijs_per_stuk_excl_btw', 0)  
                btw = product.get('btw_percentage', 0)
                bestelijst[f"bestelling {product}"] = [aantal, productnaam, prijs_per_stuk_excl_btw]
                totaal_1.append(aantal * prijs_per_stuk_excl_btw * (btw / 100))

            btw_bedrag = sum(totaal_1)

            mail = "info@***********"
            Bankrekeningnummer = 10242982854924
            Ten_name_van = "codemind"
            Betalingsreferentie = 1058901850195

            pdf_bestand = os.path.join(pdf_map, f"factuur_{ordernummer}.pdf")

            c = canvas.Canvas(pdf_bestand, pagesize=letter)

            c.setFont("Helvetica-Bold", 12)
            c.drawString(80, 770, "Factuur van")

            c.setFont("Helvetica", 12)
            c.drawString(80, 750, "Codeminds")
            c.drawString(80, 730, "lichtenburglaan 24")
            c.drawString(80, 710, "1234 AB Amstelveen")
            c.drawString(80, 690, "0612345678")
            c.drawString(80, 670, "info@codeminds.nl")
            c.drawString(80, 650, "98765432")
            c.drawString(80, 630, "Nl987654321B01")

            c.setFont("Helvetica-Bold", 12)
            c.drawString(80, 580, f"Factuurnummer: {ordernummer}")
            c.drawString(80, 560, f"Factuurdatum: {orderdatum}")
            c.drawString(80, 540, f"Vervaldatum: {betaaltermijn}")

            c.setFont("Helvetica", 12)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(80, 490, "factuur aan")

            c.setFont("Helvetica", 12)
            c.drawString(80, 470, f"{naam}")
            c.drawString(80, 450, f"{adres}")
            c.drawString(80, 430, f"{postcode}")
            c.drawString(80, 410, f"{mail}")

            c.drawString(80, 370, "Aantal            :            omschrijving            :            Prijs per stuk            :            Totaalprijs")

            p = 370

            for naam in bestelijst:
                totaal = bestelijst[naam][0] * bestelijst[naam][2]
                totaal = round(totaal, 2)
                bestelijst[naam].append(totaal)

            c.setFont("Courier", 12)
            for naam, waarden in bestelijst.items():
                p -= 20
                if p <= 0:
                    c.showPage()
                    p = 730
                    c.drawString(100, p, "Dit is de tweede pagina.")
                c.setFont("Helvetica", 12)
                c.drawString(80, p, f"{str(waarden[0]):>5}")
                c.setFont("Helvetica", 8)
                c.drawString(150, p, f"{str(waarden[1]):<20}")
                c.setFont("Helvetica", 12)
                c.drawString(350, p, f"{str(waarden[2]):>8}")
                c.drawString(490, p, f"{str(waarden[3]):>10}")

                print (p)


            subtotaal = []
            for naam in bestelijst:
                subtotaal.append(bestelijst[naam][3])
            
            if p <= 100:
                p = 750
                c.showPage()

            p -= 20
            
            sub_totaal = sum(subtotaal)
            c.drawString(430, p, "Subtotaal:")
            c.drawString(490, p, f"{sub_totaal:>10.2f}")

            p -= 20

            btw_percentage = (sub_totaal / btw_bedrag) * 100
            c.drawString(430, p, "btw:")
            c.drawString(490, p, f"{(100 - btw):>10.2f}")
            c.drawString(550, p, "%")

            p -= 20

            btw_bedrag += sub_totaal
            c.drawString(430, p, "totaal:")
            c.drawString(490, p, f"{btw_bedrag:>10.2f}")

            p -= 20

            c.setFont("Helvetica-Bold", 12)
            c.drawString(80, p, "betaal gegevens")
            c.setFont("Helvetica", 12)

            p -= 20
            if p <= 100:
                p = 750
                c.showPage()
                
            c.drawString(80, p, f"Bankrekeningnummer: {Bankrekeningnummer}")
            p -= 20
            c.drawString(80, p, f"Ten name van: {Ten_name_van}")
            p -= 20
            c.drawString(80, p, f"Betalingsreferentie: {Betalingsreferentie}")
            p -= 20
            c.drawString(80, p, "Bedankt voor uw vertrouwen in CodeMinde!")
            p -= 20

            

            
            

            c.save()

            print(f"PDF opgeslagen als {pdf_bestand}")

        except:
            shutil.move(bron, doelmap)

