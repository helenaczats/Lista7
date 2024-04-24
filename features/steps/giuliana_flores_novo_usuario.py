# criar usuário
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

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
  context.driver = webdriver.Chrome()   #instanciar o objeto do Selenium WebDriver especializado para o Chrome
  context.driver.maximize_window()      #maximizar a janela do navegador
  context.driver.implicitly_wait(10)    #esperar até 10 seg por qualquer elemento
  context.driver.get("https://www.giulianaflores.com.br/")
    
@when(u'entro no menu da pagina inicial')
def step_impl(context):
  context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
  
@then(u'clico em cadastrar')
def step_impl(context):
  context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
  context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
  
@when(u'registro nome, cpf, email, senha, endereco e telefone e clico em finalizar cadastro')
def step_impl(context):
  context.driver.find_element(By.ID, "ContentSite_txtName").click()
  context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Cristiane Emilly Moraes")
  context.driver.find_element(By.ID, "ContentSite_txtCpf").click()
  context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("547.635.028-40")
  context.driver.find_element(By.ID, "ContentSite_txtEmail").click()
  context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("cristiane_moraes@rauva.com")
  context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
  context.driver.execute_script("window.scrollTo(0,55)")
  context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("hig6KOLIAZ")
  context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
  context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("02870-160")
  context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
  context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("56")
  context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
  context.driver.execute_script("window.scrollTo(0,838)")
  context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("1137857137")
  context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
  time.sleep(2)
  
@then(u'sou direcionado a Home')
def step_impl(context):
  context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
  
  