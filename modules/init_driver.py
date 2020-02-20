from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import os
import logging

def initialize_driver():
    logging.info("Init chrome driver...")
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": "/Volumes/Dan_T5/development/PythonProjects/scrapers/temple/sfi_scraper/scraped",  # Change default directory for downloads
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
    })

    # Headless or non-headless
    if os.environ.get("RUN_HEADLESS") == "TRUE":
        logging.info("Mode: Headless")
        chrome_options.add_argument(
            "--headless"
        )
    else:
        logging.info("Mode: GUI")

    # If CHROME_DRIVER_PATH is set in env variables then use that path, otherwise default to PATH locations
    chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")
    if chrome_driver_path:
        chrome_driver_path = Path(chrome_driver_path) if chrome_driver_path else None
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)
    else:
        driver = webdriver.Chrome(chrome_options=chrome_options)

    logging.info("Chrome driver initialized")
    return driver