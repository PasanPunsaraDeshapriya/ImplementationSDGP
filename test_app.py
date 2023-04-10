import unittest
from app import app

class TestFlaskRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
      response = self.app.get('/')
      self.assertEqual(response.status_code, 500)
        
    def test_login_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_signup_route(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_careerFinderModel(self):
        response = self.app.get('/careerFinderModel')
        self.assertEqual(response.status_code, 200)

    def test_universityFinder(self):
        response = self.app.get('/universityFinder')
        self.assertEqual(response.status_code, 200)

    def test_careerFinder(self):
        response = self.app.get('/careerFinder')
        self.assertEqual(response.status_code, 200)

    def test_programFinder(self):
        response = self.app.get('/programFinder')
        self.assertEqual(response.status_code, 200)

    def test_career(self):
        response = self.app.get('/career')
        self.assertEqual(response.status_code, 200)

    def test_program(self):
        response = self.app.get('/program')
        self.assertEqual(response.status_code, 200)
        
    def test_program(self):
        response = self.app.get('/program')
        self.assertEqual(response.status_code, 200)
    
if _name_ == '_main_':
    unittest.main()
