from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import sr1, sr


def scapy_ping(adresse_ip):
    # Construire le paquet ICMP (ping)
    packet = IP(dst=adresse_ip) / ICMP()

    try:
        # Envoyer le paquet
        reponse = sr1  (packet, timeout=2, verbose=False)

        # Vérifier la reponse
        if reponse:
            print(f"Réponse reçue de {reponse.src}")
        else:
            print("Aucune réponse reçue")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


