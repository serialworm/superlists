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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        # and the text I previously entered now appears as
        # a todo item on the page
        inputbox.send_keys(Keys.ENTER)

        # As a user I still see a place to enter another todo
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use the feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use the feathers to make a fly')

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
