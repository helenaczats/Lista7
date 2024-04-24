# login positivo
import pytest
import time
import json
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@then(u'clico em login')
def step_impl(context):
  context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
  
@when(u'preencho os campos de login com usuario vinicius.manuel.dasilva@icloud.com e senha QAZwsx123')
def step_impl(context):
  context.driver.find_element(By.ID, "ContentSite_txtEmail").click()
  context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("vinicius.manuel.dasilva@icloud.com")
  context.driver.find_element(By.ID, "ContentSite_txtPassword").click()
  context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("QAZwsx123")
  context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
  context.driver.find_element(By.ID, "ContentSite_txtPassword").click()
  context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("QAZwsx123")
  
@when(u'resolvo um captcha')
def step_impl(context):
  context.driver.find_element(By.ID, "adopt-accept-all-button").click()
  time.sleep(10) #resolver manualmente captcha

@Then(u'clico em continuar')
def step_impl(context):
  context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
  