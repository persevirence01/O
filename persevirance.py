import logging
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from plyer import notification
import pyautogui
import psutil
import os
import keyboard
import pyperclip

# Initialize logging for terminal output
logging.basicConfig(level=logging.INFO)

# Initialize Faker for random data generation
fake = Faker()

# Configure the correct path to the Firefox geckodriver
geckodriver_path = os.path.join(os.path.expanduser("~"), "Desktop", "geckodriver.exe")


# Set up the Selenium WebDriver with FirefoxOptions
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

# Ensure only one instance of FirefoxDriver is created
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)


# Function to generate a random email address
def generate_random_email():
    return fake.user_name() + str(random.randint(1000, 9999)) + "@outlook.com"


# Function to generate random name and surname
def generate_random_name():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


# Function to scan for buttons and click the first clickable one
def scan_and_click(buttons, timeout=1):
    while True:
        for button_locator in buttons:
            try:
                button = WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable(button_locator)
                )
                button.click()
                logging.info(f"Clicked button with locator: {button_locator}")
                return
            except Exception:
                pass  # Button not found or not clickable yet, keep scanning
        time.sleep(1)


# Function to check if Firefox is running
def is_firefox_open():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and 'firefox' in proc.info['name'].lower():
            return True
    return False



# Function to open CMD using Win + R shortcut and type 'start firefox'
def open_cmd_and_run_firefox():
    pyautogui.hotkey('win', 'r')  # Open the Run window
    time.sleep(2)
    pyautogui.write('cmd')  # Type 'cmd' to open the command prompt
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('start firefox')  # Type 'start firefox' to open Firefox
    pyautogui.press('enter')
    time.sleep(7)  # Wait for Firefox to launch

# Function to switch to the Firefox window (Alt + Tab)
def focus_firefox():
    pyautogui.hotkey('alt', 'tab')  # Switch to the next window (Firefox)

# Function to focus the Firefox address bar using Ctrl + L
def focus_address_bar():
    pyautogui.hotkey('ctrl', 'l')  # Focus the address bar in Firefox

# Exit CMD properly
    pyautogui.write('exit')
    pyautogui.press('enter')
   

# Function to paste the AliExpress URL in the address bar
def open_aliexpress():
    pyautogui.hotkey('ctrl', 'l')  # Focus the address bar
    time.sleep(0.5)  # Short delay to ensure the address bar is focused
    pyautogui.write("https://login.aliexpress.com/?spm=a2g0o.login_signup.register.0.0.3e1a2d67UZoVAA")  # AliExpress URL
    pyautogui.press('enter')  # Press Enter to go to the URL
    time.sleep(5)  # Wait for the page to load

# Function to simulate pressing Tab 5 times in 1 second with 0.2s delay
def press_tab_6_times():
    for _ in range(6):
        pyautogui.press('tab')
        time.sleep(0.2)  # 0.2 second delay between each tab press

# Function to type the email and press Enter
def type_email_and_submit(email):
    email_prefix = email.split("@")[0]  # Get the part before "@outlook.com"
    
    pyautogui.write(email_prefix, interval=0.05)  # Type the email prefix
    time.sleep(0.5)

    # Copy '@' to clipboard and paste it
    pyperclip.copy("@")
    pyautogui.hotkey("ctrl", "v")  # Paste '@' symbol

    time.sleep(0.2)

    pyautogui.write("outlook.com", interval=0.05)  # Type the rest of the email domain
    time.sleep(0.5)

    pyautogui.press('enter')  # Press Enter to submit the email
    time.sleep(5)






    # Switch to Outlook tab and scan for AliExpress email
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to Outlook tab. Scanning for AliExpress email.")
    
    while True:
        try:
            email_subject = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'AliExpress')]")
            ))
            email_subject.click()
            print("AliExpress email found and clicked.")
            break
        except Exception:
            print("AliExpress email not found, retrying...")
            time.sleep(1)
    
    # Extract the 4-digit code
    code_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "x_code"))
    )
    code = code_element.get_attribute("innerText").strip()
    print(f"Extracted 4-digit code: {code}")
    
    # Switch back to AliExpress tab and paste the code
    driver.switch_to.window(driver.window_handles[0])
    pyautogui.write(code, interval=0.05)
    pyautogui.press('enter')
    print("Pasted the 4-digit code into AliExpress and submitted.")

    



# Main function that executes all steps
def main():
    logging.info("1. Opening the Outlook sign-up page.")
    driver.get("https://signup.live.com/signup?lic=1&mkt=fr-be")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameInput"))
    )

    random_email = generate_random_email()
    logging.info(f"2. Generated random email: {random_email}")

    email_input = driver.find_element(By.ID, "usernameInput")
    email_input.send_keys(random_email)

    logging.info("4. Clicking the 'Suivant' button for the email input.")
    next_button = driver.find_element(By.ID, "nextButton")
    next_button.click()

    time.sleep(2)
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "Password"))
    )

    logging.info("5. Entering the password.")
    password_input = driver.find_element(By.ID, "Password")
    password_input.send_keys("dreamer9")

    time.sleep(2)
    
    logging.info("6. Clicking the 'Suivant' button for the password.")
    next_button_password = driver.find_element(By.ID, "nextButton")
    next_button_password.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "firstNameInput"))
    )

    first_name, last_name = generate_random_name()
    logging.info(f"7. Generated random name: {first_name} {last_name}")

    first_name_input = driver.find_element(By.ID, "firstNameInput")
    first_name_input.send_keys(first_name)

    time.sleep(1)

    last_name_input = driver.find_element(By.ID, "lastNameInput")
    last_name_input.send_keys(last_name)

    time.sleep(1)
    
    logging.info("10. Clicking the 'Suivant' button for the name.")
    next_button_name = driver.find_element(By.ID, "nextButton")
    next_button_name.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "BirthDay"))
    )

    logging.info("11. Selecting a random day.")
    day_dropdown = driver.find_element(By.ID, "BirthDay")
    random_day = random.randint(1, 31)
    day_dropdown.send_keys(str(random_day))

    logging.info("12. Selecting a random month.")
    month_dropdown = driver.find_element(By.ID, "BirthMonth")
    month_dropdown.click()
    month_options = driver.find_elements(By.XPATH, "//select[@id='BirthMonth']/option")
    random_month = month_options[random.randint(1, len(month_options) - 1)]
    random_month.click()

    random_year = random.randint(1970, 2005)
    year_input = driver.find_element(By.ID, "BirthYear")
    year_input.send_keys(str(random_year))
    logging.info(f"13. Entered random year: {random_year}")

    time.sleep(3)
    
    logging.info("14. Clicking the 'Suivant' button for birthdate.")
    next_button_birth = driver.find_element(By.ID, "nextButton")
    next_button_birth.click()

    notification.notify(
        title="Solve Captcha",
        message="Please solve the CAPTCHA on the browser.",
        timeout=10,
    )
    logging.info("Notification sent to solve CAPTCHA.")
   
    scan_and_click(buttons)
    time.sleep(5)

    # Task 16: Scan for "Oui" or "Ok" buttons and click the first one
    logging.info("16. Scanning for 'Oui' or 'Ok' buttons.")
    buttons = [
        (By.ID, "acceptButton"),  # "Oui" button
        (By.XPATH, "//*[@id='id__0']"),  # "Ok" button
    ]
    scan_and_click(buttons)

    time.sleep(6)

    # Task 16.5: Open Outlook inbox in the same tab before launching CMD
    logging.info("16.5 Opening Outlook inbox.")
    driver.get("https://outlook.live.com/mail/0/")
    time.sleep(5)  # Allow time for the page to load

    # Task 17: Open CMD and Firefox, navigate to AliExpress, and enter the email
    logging.info("17. Opening CMD and Firefox, navigating to AliExpress.")
    open_cmd_and_run_firefox()
    focus_firefox()
    focus_address_bar()
    open_aliexpress()

    # Press Tab 5 times to reach the email input field
    press_tab_6_times()

    # Type the random email generated above and submit it
    type_email_and_submit(random_email)

    # Press Tab twice, type "Zidane" and submit
    type_name_and_submit()


if __name__ == "__main__":
    main()
