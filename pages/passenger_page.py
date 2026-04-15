from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


class PassengerPage(BasePage):

    
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    DOB = (By.XPATH, "(//input[@placeholder='DD/MM/YYYY*'])[2]")
    EMAIL = (By.XPATH, "//input[@placeholder='Email*']")
    PHONE = (By.XPATH, "//input[@placeholder='Phone Number*']")
    ADDRESS = (By.XPATH, "//input[@placeholder='Address*']")
    NATIONALITY = (By.XPATH, "//input[@placeholder='Nationality*']")
    POST_CODE = (By.XPATH, "//input[@placeholder='Post Code*']")
    PASSPORT_NO = (By.ID, "passport")
    FEMALE_BTN = (By.XPATH, "//div[@data-value='female']")

    
    MEAL_DROPDOWN = (By.ID, "meal")
    LUGGAGE_DROPDOWN = (By.ID, "luggage")

    ADD_PASSENGER_BTN = (By.ID, "addPassengerBtn")

    

    def enter_passenger_details(self):
        self.send_keys(self.FIRST_NAME, "John")
        self.send_keys(self.LAST_NAME, "Doe")
        self.send_keys(self.DOB, "01/01/1995")
        self.send_keys(self.EMAIL, "test@gmail.com")
        self.send_keys(self.PHONE, "9876543210")
        self.send_keys(self.ADDRESS, "Hyderabad")
        self.send_keys(self.NATIONALITY, "Indian")
        self.send_keys(self.POST_CODE, "500001")
        self.send_keys(self.PASSPORT_NO, "A1234567")

        self.click(self.FEMALE_BTN)

    
    def select_meal(self, meal_name):
        element = self.wait.until(EC.element_to_be_clickable(self.MEAL_DROPDOWN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)
        time.sleep(1)  

        dropdown = Select(element)
        dropdown.select_by_visible_text(meal_name)

        print(f"Meal selected: {meal_name}")

   
    def select_luggage(self, luggage_option):
        element = self.wait.until(EC.element_to_be_clickable(self.LUGGAGE_DROPDOWN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)
        time.sleep(1)

        dropdown = Select(element)
        dropdown.select_by_visible_text(luggage_option)

        print(f"Luggage selected: {luggage_option}")

    
    def click_add_passenger(self):
        time.sleep(1)
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_PASSENGER_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)
        element.click()

        alert = self.wait.until(EC.alert_is_present())
        print(f"Alert text: {alert.text}")
        alert.accept()


        print("Passenger added successfully")