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
        self.wait = WebDriverWait(self.driver, 15)


    def safe_click(self, locator):
        driver = self.driver
        wait = self.wait

        element = wait.until(EC.presence_of_element_located(locator))


        try:
            wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return
        except:
            pass


        try:
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )
            element.click()
            return
        except:
            pass

      
        driver.execute_script("arguments[0].click();", element)

    def test_fluxo_compra(self):
        driver = self.driver

        driver.get("https://www.saucedemo.com/")

        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        if not username or not password:
            raise RuntimeError("Credenciais não carregadas")

   
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)

        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

      
        errors = driver.find_elements(By.CLASS_NAME, "error-message-container")
        if errors:
            raise AssertionError(f"Login falhou: {errors[0].text}")

       
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
        )
        self.wait.until(EC.url_contains("inventory"))

     
        self.safe_click((By.ID, "add-to-cart-sauce-labs-backpack"))

      
        self.safe_click((By.CLASS_NAME, "shopping_cart_link"))
        self.wait.until(EC.url_contains("cart"))

  
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        checkout_btn = self.wait.until(
            EC.visibility_of_element_located((By.ID, "checkout"))
        )

        self.wait.until(lambda d: checkout_btn.is_displayed())

        driver.execute_script("arguments[0].click();", checkout_btn)

        self.wait.until(lambda d: "checkout-step-one" in d.current_url)


        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Vinicius")

        driver.find_element(By.ID, "last-name").send_keys("Carvalho")
        driver.find_element(By.ID, "postal-code").send_keys("99999999")

        self.safe_click((By.ID, "continue"))

        self.safe_click((By.ID, "finish"))

        mensagem = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        self.assertEqual(mensagem, "Thank you for your order!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()