import json
import os
print(os.getcwd())


with open('./2000-096.json', 'r') as file:



    data = json.load(file)



    print(data)
    # order
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
    btw_percentage = data['order']['producten'][0]['btw_percentage']