import unittest
from unittest.mock import patch

from quickurl import shorten

class TestQuickurl(unittest.TestCase):
    @patch('quickurl.requests.get')
    def test_shorten_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'https://tinyurl.com/abc123'
        result = shorten('https://example.com')
        self.assertEqual(result, 'https://tinyurl.com/abc123')
        mock_get.assert_called_once_with('http://tinyurl.com/api-create.php', params={'url': 'https://example.com'}, timeout=5)

    @patch('quickurl.requests.get')
    def test_shorten_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        with self.assertRaises(ValueError):
            shorten('https://example.com')

if __name__ == '__main__':
    unittest.main()
