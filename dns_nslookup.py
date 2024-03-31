import socket
import dns.resolver

def dns_lookup(domain):
    try:
        # Résolution d'adresse associée à un nom de domaine
        reponse = dns.resolver.resolve(domain, 'A')
        print(f"Adresse IP associée à {domain}:")
        for rep in reponse:
            print(rep.address)

        # Résolution inverse
        addr = socket.gethostbyname(domain)
        print(f"\nRésolution inverse pour {domain}: {socket.gethostbyaddr(addr)}")
    except dns.resolver.NXDOMAIN:
        print(f"Aucun enregistrement trouvé pour {domain}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

