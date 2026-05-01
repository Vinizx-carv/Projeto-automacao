import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestMissaoLogin(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def test_fluxo_compra(self):
        driver = self.driver

        driver.get("https://www.saucedemo.com/")

        # login
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # verifica se a URL atual contém "invertory"
        self.assertIn("inventory", driver.current_url)

        # adicionar produto
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

        # ir para carrinho
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # checkout
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        
        driver.find_element(By.ID, "first-name").send_keys("Vinicius")
        driver.find_element(By.ID, "last-name").send_keys("Carvalho")
        driver.find_element(By.ID, "postal-code").send_keys("99999999")

        driver.find_element(By.ID, "continue").click()


        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        self.assertEqual(mensagem, "Thank you for your order!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()