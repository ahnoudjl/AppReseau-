import unittest
from unittest.mock import patch

from scapy.layers.inet import ICMP, IP

from ping_scapy import scapy_ping

class TestScapyPing(unittest.TestCase):

    @patch("builtins.print")  # Mock la fonction print
    @patch("scapy.sendrecv.sr1")  # Mock la fonction sr1
    def test_scapy_ping_with_response(self, mock_sr1, mock_print):
        # Configurer le mock pour simuler une réponse
        mock_response = IP(src="8.8.8.8") / ICMP()
        mock_sr1.return_value = mock_response

        # Appeler la fonction à tester
        scapy_ping("8.8.8.8")

        # Vérifier que la fonction print a été appelée avec la bonne valeur
        mock_print.assert_called_with(f"Réponse reçue de {mock_response.src}")

if __name__ == "__main__":
    unittest.main()