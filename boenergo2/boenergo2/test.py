import unittest
import requests

class GuessColorTests(unittest.TestCase):
    def test_guess_color_valid_number(self):
        url = 'http://localhost:5000/guess-color'
        data = {'item_number': 45}
        
        response = requests.post(url, json=data)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('item_number', response_data)
        self.assertIn('color', response_data)

    def test_guess_color_invalid_number(self):
        url = 'http://localhost:5000/guess-color'
        data = {'item_number': 101}
        
        response = requests.post(url, json=data)
        
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertIn('error', response_data)

if __name__ == '__main__':
    unittest.main()

