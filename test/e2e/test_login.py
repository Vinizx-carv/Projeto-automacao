import unittest
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


class TestMissaoLogin(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 50)

    def test_fluxo_compra(self):
        driver = self.driver

        driver.get("https://www.saucedemo.com/")

        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        if not username or not password:
            raise ValueError("Credenciais não carregadas")

        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)

        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        self.assertIn("inventory", driver.current_url)

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        self.wait.until(EC.url_contains("checkout-step-one"))

        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Vinicius")

        driver.find_element(By.ID, "last-name").send_keys("Carvalho")
        driver.find_element(By.ID, "postal-code").send_keys("99999999")

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        self.assertEqual(mensagem, "Thank you for your order!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()