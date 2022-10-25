from filestack import Client


"""
Solitamente lo scritto tra < > tende a significare "sostituisce con il tuo valore"
per ottenere la tua api_key, vai su filestack.com,
registrati, ed in alto a destra potrai copiare la tua api
client = Client('apiKeyDiPaolo')
"""

client = Client('<YOUR_API_KEY>')
#creaiamo il file da uploadare
new_file_link = client.upload(filepath='design.txt')

#new_file_link caricherà un file in un url che si può stampare ed usare

#QUESTA E' UNA CAZZO DI FIGATA

print(new_file_link)