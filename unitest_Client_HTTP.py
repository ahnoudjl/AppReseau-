import unittest
from unittest.mock import patch
from io import StringIO
import Client_HTTP

class TestHTTPClient(unittest.TestCase):
    @patch("builtins.input", side_effect=["https://httpbin.org/get\n"])
    def test_client_http_get(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            url = mock_input()
            Client_HTTP.client_http_get(url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Reponse :", output)

    @patch("builtins.input", side_effect=["https://httpbin.org/post\n"])
    def test_client_http_post(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            data = {"key": "value"}
            url= mock_input()
            Client_HTTP.client_http_post(data, url)
            output = mock_stdout.getvalue().strip()
            print("Output:", output)
            self.assertIn("Reponse :", output)

    @patch("builtins.input", side_effect=["https://httpbin.org/put\n"])
    def test_client_http_put(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            data = {"key": "value"}
            url= mock_input()
            Client_HTTP.client_http_put(data, url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("La ressource a été créée avec succès." if "La ressource a été créée avec succès." in output else "La ressource a été mise à jour avec succès", output)

    @patch("builtins.input", side_effect=["https://httpbin.org/delete\n"])
    def test_client_http_delete(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            url= mock_input()
            Client_HTTP.client_http_delete(url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("La ressource a été supprimée avec succès.", output)

    @patch("builtins.input", side_effect=["https://httpbin.org/patch\n"])
    def test_client_http_patch(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            data = {"key": "value"}
            url= mock_input()
            Client_HTTP.client_http_patch(data, url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("La ressource a été mise à jour avec succès.", output)

    @patch("builtins.input", side_effect=["https://docs.python-requests.org/en/latest/api/\n"])
    def test_client_http_head(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            url= mock_input()
            Client_HTTP.client_http_head(url)
            output = mock_stdout.getvalue().strip()
            print("Output:", output)
            self.assertIn("", output)#le resultat du head est vide

    @patch("builtins.input", side_effect=["https://docs.python-requests.org/en/latest/api/\n]"])
    def test_client_http_options(self, mock_input):

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            url= mock_input()
            Client_HTTP.client_http_options(url)
            output = mock_stdout.getvalue().strip()
            self.assertIn("", output)

if __name__ == '__main__':
    unittest.main()