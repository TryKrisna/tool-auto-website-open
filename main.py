from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Function to perform scrolling (top to bottom and bottom to top)
def scroll_actions(driver):
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for scrolling to settle (adjust as needed)

    # Scroll back to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)  # Wait for scrolling to settle (adjust as needed)

# Function to perform clicks
def perform_clicks(driver):
    try:
        # Example click on a button or link (adjust selector as needed)
        element = driver.find_element(By.CSS_SELECTOR, 'your-selector')
        element.click()
        time.sleep(1)  # Wait after click (adjust as needed)
    except Exception as e:
        print(f"Error clicking element: {e}")

# Function to open and interact with the website
def open_and_interact(url, repetitions):
    try:
        # Get current script directory
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Set path to chromedriver.exe
        chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')

        # Configure Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")  # Open incognito mode

        # Set Chromedriver service
        service = Service(chromedriver_path)

        # Create WebDriver instance
        driver = webdriver.Chrome(service=service, options=options)

        # Open the website
        driver.get(url)
        time.sleep(2)  # Adjust as needed for the page to load

        # Perform actions multiple times
        for _ in range(repetitions):
            # Perform scrolling both ways
            scroll_actions(driver)

            # Perform clicks periodically (adjust frequency as needed)
            perform_clicks(driver)

        # Close the browser
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get URL and repetitions from user input
    url = input("Enter the URL: ")
    repetitions = int(input("Enter the number of times to repeat: "))

    # Execute the script
    open_and_interact(url, repetitions)

    # Keep console window open (remove this if using --noconsole with pyinstaller)
    input("Press Enter to exit...")
