import unittest
import requests
import json


class TestAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5000"

    @classmethod
    def setUpClass(cls):
        # Load test payloads from the JSON file
        with open('test_payloads.json') as f:
            cls.endpoints = json.load(f)['endpoints']

    def post_request(self, endpoint, payload):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload)
        return response.status_code, response.json()

    def test_endpoints(self):
        for endpoint in self.endpoints:
            url = endpoint['url']
            for test_case in endpoint['tests']:
                with self.subTest(f"{endpoint['name']} - {test_case['description']}"):
                    status_code, _ = self.post_request(url, test_case['payload'])
                    self.assertEqual(status_code, test_case['expected_status'])


if __name__ == '__main__':
    unittest.main()
