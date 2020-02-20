import logging
from dotenv import load_dotenv

from scraper.webdriver.init_driver import initialize_driver
from scraper.helper.misc import delete_dir_contents
from scraper.webdriver.page import scrape_page
from logs.config.logging import logs_config
from definitions import DIR_DATA


def main():

    # load environ vars
    load_dotenv()

    # init logging
    logs_config()

    # create or clean temp dirs
    if DIR_DATA.is_dir():
        # delete files from previous run
        delete_dir_contents(DIR_DATA)
    else:
        DIR_DATA.mkdir()

    # init driver
    logging.info("Begin scrape")
    driver = initialize_driver()

    search_terms = [
        {
            "search_name": "House - paper forms",
            "input_fields": [
                {"field": "Template", "value": "SFI Template"},
                {"field": "BatesBatch", "value": "*HR*"},
                {"field": "Year", "value": "2019"},
            ],
        },
        {
            "search_name": "Senate - paper forms",
            "input_fields": [
                {"field": "Template", "value": "SFI Template"},
                {"field": "BatesBatch", "value": "*SN*"},
                {"field": "Year", "value": "2019"},
            ],
        },
        {
            "search_name": "House - web forms",
            "input_fields": [
                {"field": "Template", "value": "Web State of Financial Interests Form"},
                {"field": "03-05 State Entity", "value": "*rep*"},
                {"field": "07 Year", "value": "2019"},
            ],
        },
        {
            "search_name": "Senate - web forms",
            "input_fields": [
                {"field": "Template", "value": "Web State of Financial Interests Form"},
                {"field": "03-05 State Entity", "value": "*sen*"},
                {"field": "07 Year", "value": "2019"},
            ],
        },
    ]

    """
    TODO:
    
    > loop over each page of results:
        > loop over each row on page:
            > scrape page
    
    /// psuedo code ///
        
    driver open "https://www.ethicsrulings.pa.gov/WebLink/Search.aspx?dbid=0&repo=EthicsLF8"
    
    for search in search_terms:
        input search_terms 
        click submit
        
        # page search loop
        page_count = 1
        while True:
            wait for page results to load

            # row search loop
            row_count = 1
            while True:
                try:
                    click filer's name based on row_count
                    wait for filer page to load
                    scrape_page()
                    row_count += 1
                except NoSuchElementException:
                    logging.info("No more rows found")
                    break  # end row search loop
            
            try: 
                page_count += 1
                click page element based on page_count
            
            except NoSuchElementException:
                logging.info("no more pages found")
                break # end page search loop
            
    
    """

    # set vars - just using these numbers for testing, delete this
    start_id = 3
    end_id = 5

    for page_id in range(start_id, end_id):
        scrape_page(driver, page_id)


if __name__ == "__main__":
    main()
