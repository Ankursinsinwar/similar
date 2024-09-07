from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotInteractableException
import os , time

chrome_driver_path = 'C:/webdriver/chromedriver.exe'

options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument('--headless')  # Enable headless mode
# options.headless = True
# # options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--window-size=1920,1080")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
    

def upload_and_search_image(image_path):
    # Convert the relative image path to an absolute path
    absolute_image_path = os.path.abspath(image_path)
    
    # Initialize the ChromeDriver using the Service class
    service = Service(executable_path=chrome_driver_path)
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome(service=service,  options=options)
    # driver.get('https://amazon.com/')
    # print(f"Page title: {driver.title}")
    # time.sleep(3)
    # driver.quit()


    try:
        print("Navigating to the TinEye website...")
        driver.get('https://tineye.com/')
        print(f"Page title: {driver.title}")

        print("Waiting for the file input element to load...")
        file_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'image'))
        )
        file_input.send_keys(absolute_image_path)
        print("Image uploaded successfully.")

        print("Waiting for search results to load...")
        results_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.results.row'))
        )
        
        # Extract search results
        print("Extracting search results...")
        results = results_container.find_elements(By.CSS_SELECTOR, '.match-row')

        if not results:
            print("No results found.")
            return []

        # List to store extracted results
        extracted_results = []

        # Loop through the results and extract required information
        for result in results:
            try:
                # Extract image URL (thumbnail)
                image_element = result.find_element(By.CSS_SELECTOR, '.match-thumb img')
                image_url = image_element.get_attribute('src')

                # Extract domain name
                domain_name = result.find_element(By.CSS_SELECTOR, '.match h4').text

                # Extract link to the source
                link_element = result.find_element(By.CSS_SELECTOR, '.match p span a')
                source_link = link_element.get_attribute('href')

                # Extract file name or any other metadata available
                metadata_element = result.find_element(By.CSS_SELECTOR, '.match p span.crawl-date')
                metadata = metadata_element.text if metadata_element else "No metadata available"

                # Append the extracted details as a dictionary
                extracted_results.append({
                    'image_url': image_url,
                    'domain_name': domain_name,
                    'source_link': source_link,
                    'metadata': metadata
                })
                
                print(f"Extracted result: {extracted_results[-1]}")

            except NoSuchElementException as e:
                print(f"Error extracting information from a result: {e}")

        return extracted_results

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error occurred during Selenium automation: {str(e)}")
        return []
    finally:
        driver.quit()















##########################     For Debuging      ##########################



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os

# # Specify the path to your ChromeDriver
# chrome_driver_path = 'C:/webdriver/chromedriver.exe'

# def upload_and_search_image(image_path):
#     # Convert the relative image path to an absolute path
#     absolute_image_path = os.path.abspath(image_path)

#     # Initialize the ChromeDriver using the Service class
#     service = Service(executable_path=chrome_driver_path)
#     driver = webdriver.Chrome(service=service)

#     try:
#         # Navigate to the website
#         driver.get('https://tineye.com/')

#         # Wait for the file input to be present and interact with it
#         file_input = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.NAME, 'image'))
#         )
#         file_input.send_keys(absolute_image_path)

#         # Wait for the upload button to be clickable and click it
#         # search_button = WebDriverWait(driver, 20).until(
#         #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-upload'))
#         # )
#         # search_button.click()

#         # Wait for the results to load
#         results_container = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'div.results'))
#         )

#         # Extract search results
#         results = results_container.find_elements(By.CSS_SELECTOR, 'div.match')
#         extracted_results = [result.text for result in results]

#     finally:
#         driver.quit()

#     return extracted_results

