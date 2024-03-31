import unittest
from unittest.mock import patch
from io import StringIO
import dns_nslookup

class TestDNSLookup(unittest.TestCase):
    def test_dns_lookup(self):
        # Utiliser patch pour simuler la saisie utilisateur
        with patch('builtins.input', return_value='google.com'), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dns_nslookup.dns_lookup("google.com")

        # Récupérer la sortie standard simulée
        output = mock_stdout.getvalue()

        # Vérifier que l'adresse IP associée à example.com est présente dans la sortie
        self.assertIn("Adresse IP associée à google.com:", output)

        # Vérifier que le message "Aucun enregistrement trouvé" n'est pas présent dans la sortie
        self.assertNotIn("Aucun enregistrement trouvé", output)

if __name__ == '__main__':
    unittest.main()