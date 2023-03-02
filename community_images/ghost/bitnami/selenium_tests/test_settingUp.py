# Generated by Selenium IDEi
# pylint: skip-file

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSettingUp():
  def setup_method(self, method): # pylint: disable=unused-argument
     """setup method."""
     chrome_options = Options()
     chrome_options.add_argument("--headless")
     chrome_options.add_argument('--disable-dev-shm-usage')
     chrome_options.add_argument("disable-infobars")
     chrome_options.add_argument("--disable-extensions")
     chrome_options.add_argument("--disable-gpu")
     chrome_options.add_argument("--no-sandbox")
     self.driver = webdriver.Chrome(options=chrome_options)  # pylint: disable=attribute-defined-outside-init
     self.driver.implicitly_wait(10)

  def teardown_method(self, method):
    self.driver.quit()

  def test_settingUp(self, params):
    self.driver.get("http://localhost:{}/".format(params["port"]))
    self.driver.set_window_size(1280, 1024)
    self.driver.find_element(By.LINK_TEXT, "About").click()
    time.sleep(4)
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.get("http://localhost:{}/ghost/".format(params["port"]))
    time.sleep(3)
    self.driver.find_element(By.ID, "identification").click()
    self.driver.find_element(By.ID, "identification").send_keys("user@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("bitnami123")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    time.sleep(3)
    self.driver.get("http://localhost:{}/ghost/#/members".format(params["port"]))
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//span[contains(.,'Add yourself as a member to test')]").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".gh-members-help-card:nth-child(1) > .gh-members-help-content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//a[contains(@href, \'#/dashboard/\')]").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    #self.driver.find_element(By.CSS_SELECTOR, ".sun_svg__a:nth-child(3)").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//a[contains(@href, \'#/posts/\')]").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'New post\')]").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//textarea").send_keys("Rapidfort Inc")
    self.driver.find_element(By.XPATH, "//textarea").send_keys(Keys.ENTER)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".koenig-plus-menu-button").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(6) .f-small").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".stroke-middarkgrey").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(4) .f-small").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".koenig-editor__editor")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Sample Blog'}", element)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".gh-editor-preview-trigger > span").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".gh-editor-preview-trigger > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".gh-post-preview-mode:nth-child(2) svg").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".right > .darkgrey > span").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".gh-btn-black > span").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Publish post, right now\')]").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(2)
    self.driver.get("http://localhost:{}/ghost/".format(params["port"]))
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#ember18 > .gh-nav-viewname").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".settings_svg__a:nth-child(3)").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".settings_svg__a:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.XPATH, "//a[contains(@href, \'#/settings/design/\')]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".gh-nav-design-tab:nth-child(2)").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".color-picker").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".color-picker").send_keys("#0c0307")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".gh-nav-design-tab:nth-child(2)").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".gh-nav-design-tab:nth-child(4)").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Save\')]").click()
    time.sleep(2) 
    self.driver.find_element(By.XPATH, "//a[contains(@href, \'#/settings/\')]").click()
    time.sleep(2)