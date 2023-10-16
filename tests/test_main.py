import unittest

import config
import testcases
from main import app_client

URL_INDEX: str = f"http://{config.FLASK_HOST}:{config.FLASK_PORT}"
URL_CREATE: str = URL_INDEX + '/create'
URL_READ: str = URL_INDEX + '/read'
URL_UPDATE: str = URL_INDEX + '/update'
URL_DELETE: str = URL_INDEX + '/delete'


class TestCase(unittest.TestCase):
    def test_submit_issue(self):
        for data, hash_ in zip(testcases.test_data, testcases.test_data_hash):
            result = app_client.post(URL_CREATE, data['body'], data['headers'])
            self.assertEqual(result.status_code, 201)
            self.assertEqual(result['hash'], hash_)

    def test_find_issues_by_body(self):
        for query in testcases.queries:
            result = app_client.post(URL_READ, query)
            self.assertEqual(result.status_code, 200)

    def test_find_issues_by_hash(self):
        with app_client as client:
            for hash_ in testcases.test_data_hash:
                result = client.get(URL_UPDATE, query_string={'h': hash_})
                self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
