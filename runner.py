
import logging
from dotenv import load_dotenv

from scraper.webdriver.init_driver import initialize_driver
from scraper.helper.misc import delete_dir_contents
from scraper.webdriver.page import scrape_page
from logs.config.logging import logs_config
from definitions import DIR_DATA, PATH_DATA_MASTERLIST

def main():

    # load environ vars
    load_dotenv()

    # init logging
    logs_config()

    # clean up temp dirs
    delete_dir_contents(DIR_DATA)

    # set vars
    start_id = 3
    end_id = 5

    # init driver
    logging.info("Begin scrape")
    driver = initialize_driver()

    for page_id in range(start_id, end_id):
        scrape_page(driver, page_id)


if __name__ == '__main__':
    main()