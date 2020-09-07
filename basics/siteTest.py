import os
import unittest

from selenium import webdriver


class SiteTest(unittest.TestCase):
    def setUp(self):
        root_dir = os.path.abspath(os.curdir)
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get('https://google.com/')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":  # means that the Python interpreter is executing the script, not importing it
    unittest.main()
