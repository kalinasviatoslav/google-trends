from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from utils import *

while True:
    user_search_input = input("Please enter key words for search \n")
    new_folder_relative_path = f"output/{user_search_input}"
    new_folder_relative_path = create_new_folder(new_folder_relative_path)
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
    date_query_param = select_time_frame(driver)
    open_google_trends_page(driver, date_query_param)
    time.sleep(sleep_time_for_uploading_data)
    search_box = driver.find_element(By.ID, "input-29")
    suggestions = get_suggestions(search_box, user_search_input, driver)
    user_selected_option_number = let_user_chose_search_type(suggestions[:max_amount_of_search_suggestions])
    apply_user_selection(user_search_input, user_selected_option_number, search_box)
    select_country(driver)
    time.sleep(sleep_time_for_uploading_data)
    save_results(driver)
    driver.quit()
    should_continue = input("Do you want to continue the search? (Y/N): ")
    if should_continue.lower() != 'y':
        break
