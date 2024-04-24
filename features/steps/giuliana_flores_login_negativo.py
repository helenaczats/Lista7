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


@when(u'preencho os campos de login com usuario vinicius@icloud.com e senha caju')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").click() #digitar email (usuário correto)
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("vinicius@icloud.com")
    
    context.driver.find_element(By.ID, "ContentSite_txtPassword").click() #digitar senha incorreta (1)
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("caju")
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click() #botão continuar (1)
    context.driver.find_element(By.ID, "ContentSite_txtPassword").click() #por erro do site digitar novamente senha incorreta(1)
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("ujh")
    
@then(u'resolvo um captcha')
def step_impl(context):
    context.driver.find_element(By.ID, "adopt-accept-all-button").click() #botão aceitar cookies
    
    time.sleep(15) #tempo para resolver manualmente o captcha
    
@when(u'clico em continuar')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click() #botão continuar (2)
   

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".font_erro").text == "e-mail ou senha inválidos!"
    
 