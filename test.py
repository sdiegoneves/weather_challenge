import os
import app
import unittest
import tempfile
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        app.file = "database_test"
        self.app = app.app.test_client()


    def tearDown(self):
        content_file = []
        with open("database_test", 'w') as outfile:  
            json.dump(content_file, outfile)

    def test_create_city(self):
        response = self.app.post('/create', data=json.dumps(dict(name='Rio de janeiro', country_code="BR")),content_type='application/json')          
        assert "True" in response.data.decode("utf-8")   

        response = self.app.post('/create', data=json.dumps(dict(name='Rio de janeiro', country_code="BG")),content_type='application/json')
        assert "False" in response.data.decode("utf-8") 

        response = self.app.get('/city/1')
        assert "Rio de janeiro" in response.data.decode("utf-8") 

if __name__ == '__main__':
    unittest.main()