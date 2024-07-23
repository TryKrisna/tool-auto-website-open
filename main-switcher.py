# import os
# import random
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.common.by import By
# # import pyautogui
#
# # Function to perform scrolling (top to bottom and bottom to top)
# def scroll_actions(driver):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     driver.execute_script("window.scrollTo(0, 0);")
#     time.sleep(2)
#
# # Function to perform clicks
# def perform_clicks(driver):
#     try:
#         element = driver.find_element(By.CSS_SELECTOR, 'your-selector')  # Adjust selector as needed
#         element.click()
#         time.sleep(1)
#     except Exception as e:
#         print(f"Error clicking element: {e}")
#
# # Function to open and interact with the website
# def open_and_interact(url, repetitions):
#     try:
#         script_dir = os.path.dirname(os.path.realpath(__file__))
#         chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')
#         edgedriver_path = os.path.join(script_dir, 'msedgedriver.exe')
#
#         browser_choice = random.choice(['chrome', 'edge'])
#
#         if browser_choice == 'chrome':
#             options = webdriver.ChromeOptions()
#             options.add_argument("--incognito")
#             service = ChromeService(chromedriver_path)
#             driver = webdriver.Chrome(service=service, options=options)
#         else:
#             options = webdriver.EdgeOptions()
#             options.add_argument("--inprivate")
#             service = EdgeService(edgedriver_path)
#             driver = webdriver.Edge(service=service, options=options)
#
#         driver.get(url)
#         time.sleep(2)
#
#         # for _ in range(repetitions):
#         scroll_actions(driver)
#         perform_clicks(driver)
#
#         driver.quit()
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# # Function to rotate Surfshark connection using pyautogui
# # def rotate_surfshark():
# #     try:
# #         # Open Surfshark (adjust the path to your Surfshark executable)
# #         os.startfile(r"C:\Path\To\Surfshark.exe")
# #         time.sleep(10)  # Wait for Surfshark to open
# #
# #         # Click on the 'Connect' button or similar (coordinates may need adjustment)
# #         connect_button = pyautogui.locateCenterOnScreen('connect_button.png')
# #         if connect_button:
# #             pyautogui.click(connect_button)
# #             time.sleep(5)  # Wait for connection to establish
# #
# #         # Optionally, disconnect and reconnect to rotate the IP
# #         disconnect_button = pyautogui.locateCenterOnScreen('disconnect_button.png')
# #         if disconnect_button:
# #             pyautogui.click(disconnect_button)
# #             time.sleep(5)
# #             pyautogui.click(connect_button)
# #             time.sleep(5)
# #
# #     except Exception as e:
# #         print(f"Error rotating Surfshark connection: {e}")
#
# if __name__ == "__main__":
#     url = input("Enter the URL: ")
#     repetitions = int(input("Enter the number of times to repeat actions in browser: "))
#
#     # Run the process multiple times
#     for i in range(repetitions):  # Adjust the number of iterations as needed
#         print(f"Iteration {i + 1}")
#         # rotate_surfshark()
#         open_and_interact(url, repetitions)
#         print(f"Iteration {i + 1} completed.")
#         time.sleep(10)  # Optional: Wait between iterations
#
#     input("Press Enter to exit...")

#
# # === > Next generation v1
# import os
# import random
# import time
# from datetime import datetime, timedelta
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.common.by import By
# # import pyautogui
#
# # Function to perform scrolling (top to bottom and bottom to top)
# def scroll_actions(driver):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     driver.execute_script("window.scrollTo(0, 0);")
#     time.sleep(2)
#
# # Function to perform clicks
# def perform_clicks(driver):
#     try:
#         element = driver.find_element(By.CSS_SELECTOR, 'your-selector')  # Adjust selector as needed
#         element.click()
#         time.sleep(1)
#     except Exception as e:
#         print(f"Error clicking element: {e}")
#
# # Function to open and interact with the website
# def open_and_interact(url, repetitions):
#     try:
#         script_dir = os.path.dirname(os.path.realpath(__file__))
#         chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')
#         edgedriver_path = os.path.join(script_dir, 'msedgedriver.exe')
#
#         browser_choice = random.choice(['chrome', 'edge'])
#
#         if browser_choice == 'chrome':
#             options = webdriver.ChromeOptions()
#             options.add_argument("--incognito")
#             service = ChromeService(chromedriver_path)
#             driver = webdriver.Chrome(service=service, options=options)
#         else:
#             options = webdriver.EdgeOptions()
#             options.add_argument("--inprivate")
#             service = EdgeService(edgedriver_path)
#             driver = webdriver.Edge(service=service, options=options)
#
#         driver.get(url)
#         time.sleep(2)
#
#         for _ in range(repetitions):
#             scroll_actions(driver)
#             perform_clicks(driver)
#
#         driver.quit()
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     url = input("Enter the URL: ")
#     repetitions = int(input("Enter the number of times to repeat actions in the browser: "))
#     duration_minutes = int(input("Enter the duration (in minutes) to run the script: "))
#
#     end_time = datetime.now() + timedelta(minutes=duration_minutes)
#
#     # Run the process until the specified end time
#     while datetime.now() < end_time:
#         print(f"Running iteration at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#         open_and_interact(url, repetitions)
#         print(f"Iteration completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#         time.sleep(10)  # Optional: Wait between iterations
#
#     print("Finished running script.")
#     input("Press Enter to exit...")




#========================== Final test
import os
import random
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By

# Function to perform scrolling (top to bottom and bottom to top)
def scroll_actions(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

# Function to perform clicks
def perform_clicks(driver):
    try:
        element = driver.find_element(By.CSS_SELECTOR, 'your-selector')  # Adjust selector as needed
        element.click()
        time.sleep(1)
    except Exception as e:
        print(f"Error clicking element: {e}")

# Function to open and interact with the website
def open_and_interact(url, repetitions):
    try:
        # Set paths for WebDriver executables
        chromedriver_path = './chromedriver.exe'
        edgedriver_path = './msedgedriver.exe'

        browser_choice = random.choice(['chrome', 'edge'])

        if browser_choice == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            service = ChromeService(chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            options = webdriver.EdgeOptions()
            options.add_argument("--inprivate")
            service = EdgeService(edgedriver_path)
            driver = webdriver.Edge(service=service, options=options)

        driver.get(url)
        time.sleep(2)

        for _ in range(repetitions):
            scroll_actions(driver)
            perform_clicks(driver)

        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    repetitions = int(input("Enter the number of times to repeat actions in the browser: "))
    duration_minutes = int(input("Enter the duration (in minutes) to run the script: "))

    end_time = datetime.now() + timedelta(minutes=duration_minutes)

    # Run the process until the specified end time
    while datetime.now() < end_time:
        print(f"Running iteration at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        open_and_interact(url, repetitions)
        print(f"Iteration completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(10)  # Optional: Wait between iterations

    print("Finished running script.")
    input("Press Enter to exit...")
