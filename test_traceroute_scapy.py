import unittest
from unittest.mock import patch
from io import StringIO
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr
from traceroute_scapy import scapy_traceroute
class TestScapyTraceroute(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_scapy_traceroute(self, mock_stdout):
        adresse_ip = "8.8.8.8"
        scapy_traceroute(adresse_ip)
        expected_output = "1. 192.168.1.1\n2. 80.10.238.161\n3. 80.12.193.194\n4. 80.12.193.190\n5. 193.252.160.53\n6. *\n7. 72.14.218.40\n8. 72.14.236.91\n9. 142.251.253.35\n10. 8.8.8.8\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()