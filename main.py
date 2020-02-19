from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import sys
from modules.init_driver import initialize_driver

def main():

    driver = initialize_driver()

    for pageId in range(int(sys.argv[1]), int(sys.argv[2])):

        url = "https://www.ethicsrulings.pa.gov/WebLink/DocView.aspx?id=" + str(pageId) + "&dbid=0&repo=EthicsLF8"
        driver.get(url)
        time.sleep(3)

        try:
            errorMsg = driver.find_element_by_id('ErrorMsg')  # if page access is denied
        except Exception:

            try:
                imageCanvas = driver.find_element_by_id('imageCanvas')  # if page has any form content
            except Exception:
                continue

            breadcrumbDiv = driver.find_element_by_class_name('breadcrumbEntry')
            breadcrumbList = breadcrumbDiv.find_element_by_tag_name('ul')
            breadcrumbListItems = breadcrumbList.find_elements_by_tag_name('li')

            folderListItem = breadcrumbListItems[1]
            folderName = folderListItem.find_element_by_tag_name('a')

            if folderName.text == 'Statement Of Financial Interest':  # if page displays Financial Interest files

                # Scrape Metadata table
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

                with open('/Users/deborahwalker/Desktop/FinancialDisclosureMasterlist' + sys.argv[3] + '.csv', 'a',
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
                time.sleep(5)
                continue

            else:
                continue

        continue

if __name__ == '__main__':
    main()