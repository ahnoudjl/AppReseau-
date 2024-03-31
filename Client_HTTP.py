import requests
def client_http_get(url):

    # requête get
    reponse=requests.get(url)
    # verifiez que le statut de la réponse est correct
    if reponse.status_code != 200 :
        print("url est pas valide")

    else:
        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.text)

def client_http_post(data, url):
    # requête POST
    reponse = requests.post(url, data=data, json=None)

    # Vérifiez le statut de la réponse
    if reponse.status_code != 200:
        print("url est pas valide")

    else:
        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.json)

def client_http_put(data,url):

    # requête PUT
    response = requests.put(url, json=data)

    # réponse
    if response.status_code == 200:
        print("La ressource a été mise à jour avec succès")
        print(response.json())  # Afficher la réponse JSON du serveur
    elif response.status_code == 201:
        print("La ressource a été créée avec succès.")
        print(response.json())
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}.")
        print("URL non valide ou problème lors de la mise à jour de la ressource.")

def client_http_delete(url):

    # requête DELETE
    response = requests.delete(url)

    # réponse
    if response.status_code == 200:
        print("La ressource a été supprimée avec succès.")
        print(response.json())  # Afficher la réponse JSON du serveur
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}.")
        print("URL non valide ou problème lors de la suppression de la ressource.")

def client_http_patch(data, url):


    # requête PATCH
    response = requests.patch(url, json=data)

    # réponse
    if response.status_code == 200:
        print("La ressource a été mise à jour avec succès.")
        print(response.json())  # Afficher la réponse JSON du serveur
    else:
        print(f"La requête a échoué avec le code d'état {response.status_code}.")
        print("URL non valide ou problème lors de la mise à jour de la ressource.")

def client_http_head(url):

    # requête head
    reponse = requests.head(url)
    # verifiez que le statut de la réponse est correct
    if reponse.status_code != 200:
        print("url est pas valide")


    else:

        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.headers)
def client_http_options(url):

    # requête options
    reponse = requests.options(url)
    # verifiez que le statut de la réponse est correct

    if reponse.status_code == 200:
        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.text)


    else:
        print("url est pas valide")


client_http_options("https://docs.python-requests.org/en/latest/api/")