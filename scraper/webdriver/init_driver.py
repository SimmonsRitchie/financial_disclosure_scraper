from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import os
import logging
from definitions import DIR_DATA_PDFS


def initialize_driver():

    """ Initializes Chrome Driver and options. """

    logging.info("Init chrome driver...")

    # set up Chrome options
    chrome_options = Options()

    # Headless or non-headless
    if os.environ.get("RUN_HEADLESS") == "TRUE":
        logging.info("Mode: Headless")
        chrome_options.add_argument("--headless")
    else:
        logging.info("Mode: GUI")

    # PDF downloads
    pdf_download_path = str(DIR_DATA_PDFS)
    logging.info(f"PDFs will be saved to: {pdf_download_path}")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": pdf_download_path,  # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,  # It will not show PDF directly in chrome
        },
    )

    # If CHROME_DRIVER_PATH is set in env variables then use that path, otherwise default to PATH locations
    chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")
    if chrome_driver_path:
        chrome_driver_path = Path(chrome_driver_path) if chrome_driver_path else None
        driver = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=chrome_driver_path
        )
    else:
        driver = webdriver.Chrome(chrome_options=chrome_options)

    logging.info("Chrome driver initialized")
    return driver
