from pages.login_page import LoginPage
from pages.flight_page import FlightPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage
from config.config import EMAIL, PASSWORD
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_complete_booking(driver):

    login = LoginPage(driver)
    flight = FlightPage(driver)
    passenger = PassengerPage(driver)
    payment = PaymentPage(driver)

    # Step 1: Login
    login.open_website()
    login.click_signup_login()
    login.login(EMAIL, PASSWORD)

    # Step 2: Flight
    flight.go_to_flight()
    flight.click_book_now()
    flight.select_seats(1)

    time.sleep(2)   # 👈 IMPORTANT


    flight.click_add_passengers()

    # Step 3: Passenger
    passenger.enter_passenger_details()
    time.sleep(2) 
    passenger.select_meal("Veg")
    passenger.select_luggage("Check-in Baggage (15 Kg)")

    time.sleep(2) 
    passenger.click_add_passenger()

    payment.click_continue_payment()

    payment.verify_payment_page()
