from django.apps import apps
from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class AutoPartssUnitTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_tienda_app_registrada(self):
        """Verifica que la aplicación 'tienda' esté correctamente cargada en Django."""
        self.assertTrue(apps.is_installed("tienda"))

    def test_ruta_principal_responde(self):
        """Verifica que la ruta raíz del proyecto responda sin errores de servidor (500)."""
        response = self.client.get("/")
        self.assertIn(response.status_code, [200, 301, 302])

    def test_ruta_admin_accesible(self):
        """Verifica que el endpoint de administración esté enrutado y operativo."""
        response = self.client.get("/admin/login/")
        self.assertIn(response.status_code, [200, 302])

    def test_modelo_usuario_operativo(self):
        """Verifica que el modelo de usuarios de la base de datos de pruebas responda a consultas."""
        User = get_user_model()
        total_usuarios = User.objects.count()
        self.assertEqual(total_usuarios, 0)