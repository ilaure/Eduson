"""
A simple selenium test example written by python
"""
import argparse
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Get url"""
        parser = argparse.ArgumentParser()
        parser.add_argument('--url', dest='url', type=str, help='Testing url base host')
        self.args = parser.parse_args()

        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Find and click top-left logo button"""
        try:
            link = self.args.url
            search_string = "Apple Pomace"
            expected_item_price = "0.89¤"

            print('Will start browser with link:', link)

            self.driver.get(link)
            app_welcome_banner = self.driver.find_element(By.XPATH, "//*[@id=\"mat-dialog-0\"]/app-welcome-banner/div"
                                                                    "/div[2]/button[1]")
            app_welcome_banner.click()

            cancel_button = self.driver.find_element(By.XPATH, "//*[@id=\"cancelButton\"]")
            cancel_button.click()

            search_query = self.driver.find_element(By.XPATH, "//*[@id=\"searchQuery\"]")
            search_query.click()

            input_area = self.driver.find_element(By.XPATH, "//*[@id=\"mat-input-0\"]")
            input_area.send_keys(search_string)
            input_area.send_keys(Keys.ENTER)

            actual_search_string = self.driver.find_element(By.XPATH, "//*[@id=\"searchValue\"]").text
            print(f'\nSearch page for \'{actual_search_string}\'')

            actual_item_price = self.driver.find_element(By.CLASS_NAME, "item-price").text
            print(f'Item-price is \'{actual_item_price}\'')

            assert actual_search_string == search_string, f'This is not a right search page.'
            assert actual_item_price == expected_item_price, f'Price for item is not correct.'

        except Exception as ex:
            self.fail(ex)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
