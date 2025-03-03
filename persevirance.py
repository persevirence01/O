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

if __name__ == "__main__":
    main()
