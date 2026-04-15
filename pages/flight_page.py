from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import time


class FlightPage(BasePage):

    FLIGHT_MENU = (By.XPATH, "//span[contains(text(),'Flights')]")
    BOOK_NOW = (By.XPATH, "(//button[@class='flight-right-btn'])[1]")

    AVAILABLE_SEATS = (By.XPATH,"//div[contains(@class,'seat') and not(contains(@class,'booked'))]")

    ADD_PASSENGERS_BTN = (By.XPATH,"//button[contains(text(),'Add Passengers')]")

    

    def go_to_flight(self):
        element = self.wait.until(EC.element_to_be_clickable(self.FLIGHT_MENU))
        element.click()

    def click_book_now(self):
        self.driver.execute_script("window.scrollBy(0, 300)")
        element = self.wait.until(EC.element_to_be_clickable(self.BOOK_NOW))

        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def select_seats(self, count):
        seats = self.wait.until(EC.presence_of_all_elements_located(self.AVAILABLE_SEATS))

        selected = 0

        for seat in seats:
            if selected >= count:
                break

            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",seat)

                ActionChains(self.driver).move_to_element(seat).click().perform()

                time.sleep(1)

                if "selected" in seat.get_attribute("class"):
                    selected += 1
                    print(f"Seat {selected} selected")
                else:
                    print("Clicked but not selected")

            except Exception as e:
                print("Seat click failed:", e)

        print(f"Total seats selected: {selected}")

    def click_add_passengers(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.ADD_PASSENGERS_BTN))
            element.click()
        
        except:
            self.accept_alert()
            print("Alert handled, continuing")