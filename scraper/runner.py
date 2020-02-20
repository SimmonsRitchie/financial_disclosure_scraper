import time
import csv
import logging
from dotenv import load_dotenv

from scraper.webdriver.init_driver import initialize_driver
from scraper.helper.misc import delete_dir_contents
from logs.config.logging import logs_config
from definitions import DIR_DATA, PATH_DATA_MASTERLIST

def main():

    # load environ vars
    load_dotenv()

    # init logging
    logs_config()

    # clean up temp dirs
    delete_dir_contents(DIR_DATA)

    # init driver
    logging.info("Begin scrape")
    driver = initialize_driver()

    # set vars
    start_id = 3
    end_id =  5

    for pageId in range(start_id, end_id):
        logging.info(f"Scraping page id: {pageId}")

        url = "https://www.ethicsrulings.pa.gov/WebLink/DocView.aspx?id=" + str(pageId) + "&dbid=0&repo=EthicsLF8"
        driver.get(url)
        time.sleep(3)

        # Check whether SFI is found
        try:
            errorMsg = driver.find_element_by_id('ErrorMsg')  # if page access is denied
            logging.info("Page loaded with an error message")
            logging.info(f"Message: {errorMsg.text}")
        except Exception:
            logging.info("Page loaded without error message")

            try:
                imageCanvas = driver.find_element_by_id('imageCanvas')  # if page has any form content
                logging.info("#imageCanvas element found")

            except Exception:
                logging.info("No #imageCanvas element found, go to next page ID...")
                continue

            breadcrumbDiv = driver.find_element_by_class_name('breadcrumbEntry')
            breadcrumbList = breadcrumbDiv.find_element_by_tag_name('ul')
            breadcrumbListItems = breadcrumbList.find_elements_by_tag_name('li')

            folderListItem = breadcrumbListItems[1]
            folderName = folderListItem.find_element_by_tag_name('a')

            target_folder_name = 'Statement Of Financial Interest'

            if folderName.text == target_folder_name:  # if page displays Financial Interest files
                logging.info(f"Folder name contains: {target_folder_name}")

                # Scrape Metadata table
                logging.info(f"Scraping metadata table")
                table = driver.find_element_by_id('metadataTable')
                tbody = table.find_element_by_tag_name('tbody')
                trList = tbody.find_elements_by_tag_name('tr')
                tdList = []
                for tr in trList:
                    try:
                        td = tr.find_elements_by_xpath(".//td")
                        if isinstance(td, list):
                            for item in td:
                                tdList.append(item)
                        else:
                            tdList.append(td)

                    except Exception:
                        continue

                data = []
                for td in tdList:
                    try:
                        fieldValue = td.find_element_by_xpath(".//span").text
                        data.append(fieldValue)
                    except Exception:
                        try:
                            fieldValue = td.find_element_by_xpath(".//div").text
                            data.append(fieldValue)
                        except Exception:
                            continue

                data.append(pageId)  # unique ID for filing

                with open(PATH_DATA_MASTERLIST, 'a',
                          newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(data)

                # Download PDF
                toolbar = driver.find_element_by_id('imageToolbar')

                btnList = toolbar.find_elements_by_tag_name('button')
                btnPrintModal = btnList[7]
                btnPrintModal.click()  # opens print modal

                printDiv = driver.find_element_by_id('dialogButtons')
                printDiv.find_element_by_class_name('btn').click()
                logging.info(f"Downloading PDF...")
                time.sleep(5)
                logging.info("Go to next page ID")
                continue

            else:
                logging.info(f"Folder name doesn't contain: {target_folder_name}")
                logging.info(f"Go to next page ID")
                continue

        continue

if __name__ == '__main__':
    main()