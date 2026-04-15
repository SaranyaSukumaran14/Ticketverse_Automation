from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PaymentPage(BasePage):

    CONTINUE_PAYMENT = (By.XPATH, "//button[contains(text(),'Continue Payment')]")

    
    def click_continue_payment(self):
        self.click(self.CONTINUE_PAYMENT)

    def verify_payment_page(self):
        assert "payment" in self.driver.page_source.lower()
        print("Payment page loaded successfully")