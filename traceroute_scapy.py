from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr


def scapy_traceroute(adresse_ip):
    for i in range(1, 21):
        # Construire le paquet ICMP avec un TTL incrémenté à chaque étape
        packet = IP(dst=adresse_ip, ttl=i) / ICMP()

        # Envoyer le paquet et attendre la réponse
        reponse, val = sr(packet, timeout=2, verbose=False)

        # Vérifier la réponse
        if reponse:
            # Afficher les adresses IP des routeurs intermédiaires
            print(f"{i}. {reponse[0][1].src}")
            # Si la destination est atteinte, arrêter le traceroute
            if reponse[0][1].src == adresse_ip:
                break
        else:
            print(f"{i}. *")


scapy_traceroute("8.8.8.8")

