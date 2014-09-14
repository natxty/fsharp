import os
import app
import unittest
import tempfile

class FsharpTestCase(unittest.TestCase):

    def setUp(self):
    	app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
    	app.app.config['TESTING'] = False

    def test_empty_url(self):
        rv = self.app.post('/jqchx', data=dict(url=''))
        assert 'Error: please submit a url' in rv.data

    def test_malformed_url(self):
        rv = self.app.post('/jqchx', data=dict(url='http://google'))
        assert 'Error: please submit a valid url' in rv.data

    def test_known_no_jq(self):
        rv = self.app.post('/jqchx', data=dict(url='http://nathanielclark.com/nojquery.php'))
        assert 'jQuery is not used at this site' in rv.data

    def test_known_version_jq(self):
        rv = self.app.post('/jqchx', data=dict(url='http://nathanielclark.com'))
        assert '1.7.2' in rv.data

if __name__ == '__main__':
    unittest.main()