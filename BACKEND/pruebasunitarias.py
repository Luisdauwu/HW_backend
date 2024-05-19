import unittest
from unittest.mock import patch
from app import app, DAOUSER

class TestDeliveryServiceAPI(unittest.TestCase):

    def setUp(self):
        # Configurar la aplicación de Flask para realizar las pruebas
        self.app = app.test_client()

    def test_create_user(self):
        # Prueba para crear un usuario
        user_data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        response = self.app.post('/users/', json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('username' in response.json)
        self.assertEqual(response.json['username'], 'test_user')

    def test_login(self):
        # Prueba para el inicio de sesión de un usuario existente
        user_data = {
            'username': 'admin',
            'password': 'admin'
        }
        response = self.app.post('/users/login', json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.json)

    def test_login_invalid_credentials(self):
        # Prueba para el inicio de sesión con credenciales inválidas
        user_data = {
            'username': 'invalid_user',
            'password': 'invalid_password'
        }
        response = self.app.post('/users/login', json=user_data)
        self.assertEqual(response.status_code, 401)
        self.assertTrue('mensaje' in response.json)
        self.assertEqual(response.json['mensaje'], 'Credenciales inválidas')

if __name__ == '__main__':
    unittest.main()
