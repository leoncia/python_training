# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact
from contact import Date


class AddContact (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_contact_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def fill_contact_form(self, driver, contact):
        # fill contact form
        self.fill_field(driver, "firstname", contact.firstname)
        self.fill_field(driver, "middlename", contact.middlename)
        self.fill_field(driver, "lastname", contact.lastname)
        self.fill_field(driver, "nickname", contact.nickname)
        # self.add_file(driver) todo do stuff
        self.fill_field(driver, "title", contact.title)
        self.fill_field(driver, "company", contact.company)
        self.fill_field(driver, "address", contact.address)
        self.fill_field(driver, "home", contact.home)
        self.fill_date(driver, Date(prefix="b"))
        self.fill_date(driver, Date(prefix="a"))
        self.fill_field(driver, "mobile", contact.mobile)
        self.fill_field(driver, "work", contact.work)
        self.fill_field(driver, "fax", contact.fax)
        self.fill_field(driver, "email", contact.email)
        self.fill_field(driver, "email2", contact.email2)
        self.fill_field(driver, "email3", contact.email3)
        self.fill_field(driver, "homepage", contact.homepage)
        self.fill_field(driver, "address2", contact.address2)
        self.fill_field(driver, "phone2", contact.phone2)
        self.fill_field(driver, "notes", contact.notes)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_file(self, driver):
        driver.find_element_by_name("photo").click()
        driver.find_element_by_name("photo").clear()
        path = "C:\\Users\\Idelia\\PycharmProjects\\python_training\\testfile.txt"
        driver.find_element_by_name("photo").send_keys(path)

    def fill_date(self, driver, date):
        driver.find_element_by_name(date.prefix + "day").click()
        Select(driver.find_element_by_name(date.prefix + "day")).select_by_visible_text(date.day)
        driver.find_element_by_xpath("//option[@value='11']").click()
        driver.find_element_by_name(date.prefix + "month").click()
        Select(driver.find_element_by_name(date.prefix + "month")).select_by_visible_text("April")
        driver.find_element_by_xpath("//option[@value='" + date.month + "']").click()

        driver.find_element_by_name(date.prefix + "year").click()
        driver.find_element_by_name(date.prefix + "year").clear()
        driver.find_element_by_name(date.prefix + "year").send_keys(date.year)

    def fill_field(self, driver, field_name, value):
        driver.find_element_by_name(field_name).click()
        driver.find_element_by_name(field_name).clear()
        driver.find_element_by_name(field_name).send_keys(value)

    def return_to_home_page(self, driver):
        # return to home page
        driver.find_element_by_link_text("home page").click()

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_contact_page(driver)
        self.fill_contact_form(driver, Contact())
        self.return_to_home_page(driver)
        self.logout(driver)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
