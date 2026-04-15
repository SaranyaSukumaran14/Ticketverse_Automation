import os
from datetime import datetime

def take_screenshot(driver, name):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{folder}/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)