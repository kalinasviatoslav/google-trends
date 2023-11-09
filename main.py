from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

import time
import os

from GoogleTrendsVars import geoPicker, timePicker

GoogleTrendsLink = "https://trends.google.com/trends/explore"
GoogleTrendsConnectionError = 'Error 429 (Too Many Requests)!!1'
max_amount_of_search_suggestions = 4
sleep_time_for_uploading_data = 3
country = "United States"
current_dir = os.getcwd()


def get_user_select_time_frame():
    print("Choose one of the options for time frame selection:")
    for index, option in enumerate(timePicker):
        print(f"{index + 1}|||{option[0]}")
    choice = input("Enter the number of your choice: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(timePicker):
            selected_option = timePicker[choice - 1]
            print(f"You chose: {selected_option}")
            return choice
        else:
            print("Invalid choice. Please enter a valid number.")
            get_user_select_time_frame()
    except ValueError:
        print("Invalid input. Please enter a number.")
        get_user_select_time_frame()


def select_time_frame():
    user_selected_time_frame = get_user_select_time_frame()
    if user_selected_time_frame != 1:
        driver.get(GoogleTrendsLink + timePicker[user_selected_time_frame - 1][1])
    return timePicker[user_selected_time_frame - 1][1] or ""


def get_user_country_selection():
    print("Choose one of the options for country selection:")
    for index, option in enumerate(geoPicker):
        print(f"{index + 1}|||{option['name']}")

    choice = input("Enter the number of your choice: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(geoPicker):
            selected_option = geoPicker[choice - 1]
            print(f"You chose: {selected_option}")
            return selected_option['name']
        else:
            print("Invalid choice. Please enter a valid number.")
            get_user_country_selection()
    except ValueError:
        print("Invalid input. Please enter a number.")
        get_user_country_selection()


def select_country():
    custom_select = driver.find_element(By.CLASS_NAME, "hierarchy-select")
    custom_select.click()
    choose_country = driver.find_element(By.ID, value='input-10')

    choose_country.send_keys(get_user_country_selection())
    choose_country.send_keys(Keys.ARROW_DOWN)
    choose_country.send_keys(Keys.RETURN)


def save_results():
    buttons = driver.find_elements(By.CSS_SELECTOR, "button.widget-actions-item.export")
    ok_button = driver.find_element(By.CLASS_NAME, "cookieBarButton.cookieBarConsentButton")
    ok_button.click()
    time.sleep(sleep_time_for_uploading_data * 4)
    for button in buttons:
        button.click()
        time.sleep(1)
    print(f'All results has been saved to {new_folder_relative_path} folder')


def open_google_trends_page(driver, query_param):
    driver.get(GoogleTrendsLink + query_param)
    if driver.title == GoogleTrendsConnectionError:
        open_google_trends_page(driver, query_param)
    return driver


def let_user_chose_from_options(options):
    print("Choose one of the options:")
    for i, option in enumerate(options, 1):
        print(f"{i} -> {option}")

    choice = input("Enter the number of your choice: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(options):
            selected_option = options[choice - 1]
            print(f"You chose: {selected_option}")
            return choice
        else:
            print("Invalid choice. Please enter a valid number.")
            let_user_chose_from_options(options)
    except ValueError:
        print("Invalid input. Please enter a number.")
        let_user_chose_from_options(options)


def apply_user_selection(user_search_input, user_selected_option_number):
    search_box.clear()
    search_box.send_keys(user_search_input)
    time.sleep(sleep_time_for_uploading_data)
    for item in range(user_selected_option_number):
        search_box.send_keys(Keys.ARROW_DOWN)
    search_box.send_keys(Keys.RETURN)


def get_suggestions():
    search_box.send_keys(user_search_input)
    time.sleep(sleep_time_for_uploading_data)
    suggestions = []
    titles = driver.find_elements(By.CSS_SELECTOR, ".autocomplete-entity.autocomplete-title")
    descriptions = driver.find_elements(By.CSS_SELECTOR, ".autocomplete-entity.autocomplete-desc")

    if len(titles) == len(descriptions):
        for title, desc in zip(titles, descriptions):
            title_text = title.text
            desc_text = desc.text
            suggestions.append(f"{title_text} ||| {desc_text}")
    return suggestions


def create_new_folder(new_folder_relative_path):
    try:
        os.mkdir(new_folder_relative_path)
    except FileExistsError:
        print('Folder this results already exists and will be rewrited')


while True:
    user_search_input = input("Please enter key words for search \n")
    new_folder_relative_path = f"output/{user_search_input}"
    create_new_folder(new_folder_relative_path)
    download_folder = os.path.join(current_dir, new_folder_relative_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    date_query_param = select_time_frame()
    open_google_trends_page(driver, date_query_param)
    time.sleep(sleep_time_for_uploading_data)

    search_box = driver.find_element(By.ID, "input-29")
    suggestions = get_suggestions()
    user_selected_option_number = let_user_chose_from_options(suggestions[:max_amount_of_search_suggestions])
    apply_user_selection(user_search_input, user_selected_option_number)
    select_country()
    time.sleep(sleep_time_for_uploading_data)
    save_results()
    driver.quit()
    should_continue = input("Do you want to continue the search? (Y/N): ")
    if should_continue.lower() != 'y':
        break
