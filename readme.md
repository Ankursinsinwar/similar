# Django & Selenium Automation with TinEye

## Project Overview
This project automates the process of uploading an image from a Django webpage to the TinEye reverse image search website using Selenium. Once the image is uploaded and searched on TinEye, the results are fetched and displayed on the webpage of the Django application.

## Features
- Upload an image through the Django webpage.
- Automate the image search on TinEye using Selenium.
- Display the search result from TinEye on the Django webpage.

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.x
- Django
- Selenium
- A browser driver (e.g., ChromeDriver for Google Chrome)
- TinEye account (if required for advanced features)

## Installation

1. **Clone the repository**:
   ```
    git clone https://github.com/Ankursinsinwar/similar.git
    cd similar
   ```
2. **Create a virtual environment**:
##### Bash
   ```bash
   python3 -m venv env
  source env/bin/activate

```

##### powershell
  ```powershell
    python -m venv env
   .\env\Scripts\Activate
```
3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up Django**: Run the following command to make migrations and migrate the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Set up Selenium**:
- Download the appropriate web driver for your browser from the relevant provider's website (e.g., ChromeDriver for Chrome from https://developer.chrome.com/docs/chromedriver/downloads).
- Update the path to the driver in your Selenium setup.

6. **Configure TinEye Integration**:
- Ensure the Selenium script properly handles the TinEye upload and search logic

## Usage

1. **Run the Django server:**

   ```
   python manage.py runserver
   ```

2. **Upload an Image:**

* navigating to the root URL (`''`) of your Django application. This page will typically have a form where you can select an image file from your computer.
* Select the image you want to search for using TinEye. Make sure the image format is supported by TinEye (e.g., JPEG, PNG, GIF).
* Submit the form to upload the image to your Django application.

3. **Automated Search:**

Once you submit the form, the Django application will trigger the Selenium script. This script will:

  * Open the TinEye website in a web browser.
  * Upload the selected image to TinEye using appropriate methods (e.g., file upload form, API).
  * Perform a reverse image search on TinEye using the uploaded image.

4. **View Results:**

The search results from TinEye will be fetched by the Selenium script and displayed on the webpage of your Django application. This page will typically show information about the matching images found on the web, including thumbnails and links to the original websites.

## Project Structure

* `manage.py`: Django project management script.
* `similarapp/`: Contains the Django app files.
    * `views.py`: Handles image upload logic and rendering the results page.
    * `forms.py`: Defines the form for uploading images on the Django webpage.
* `templates/index.html`: Template for upload the image and also displaying the TinEye search results.
* `selenium_script.py`: Contains the Selenium automation script for uploading the image to TinEye and retrieving results.