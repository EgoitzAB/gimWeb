from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class FooterResponsiveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Establece el driver para todas las pruebas"""
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def setUp(self):
        """Establece el navegador antes de cada prueba"""
        self.driver.get("http://localhost:8001")  # Cambia por tu URL de Django local
        self.driver.set_window_size(600, 800)  # Simula una pantalla pequeña

    def test_footer_responsive_structure(self):
        """Verifica que el footer se comporte como esperado en pantallas pequeñas"""
        
        # Asegúrate de que el mapa esté en la parte superior
        footer_map = self.driver.find_element(By.CLASS_NAME, "footer-map")
        self.assertTrue(footer_map.is_displayed())
        
        # Verifica que las secciones estén una debajo de la otra
        footer_sections = self.driver.find_elements(By.CLASS_NAME, "footer-section")
        self.assertEqual(len(footer_sections), 4)  # Deben ser 4 secciones en total

        # Verifica que la sección de contacto contiene el texto esperado
        footer_contact = self.driver.find_element(By.CLASS_NAME, "footer-contact")
        self.assertIn("Dónde nos puedes encontrar", footer_contact.text)
        
    def tearDown(self):
        """Cierra el navegador después de cada prueba"""
        time.sleep(2)  # Pausa para ver el resultado de la prueba
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        """Finaliza la clase de pruebas"""
        pass

if __name__ == "__main__":
    unittest.main()
