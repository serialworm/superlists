#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # As a user I can visit the home page
        self.browser.get('http://localhost:8000')

        # I notice "To-Do" is in the title and header text
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # As a user I see an input field to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # As a user I can enter my todo item in a form
        inputbox.send_keys('Buy peacock feathers')

        # When I press the enter key the data in the form is saved
        # and the text I previously entered no appears as
        # a todo item on the page
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy peacock feathers' for row in rows),
            'New to-do item did not appear in table'
        )

        # As a user I still see a place to enter another todo
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
