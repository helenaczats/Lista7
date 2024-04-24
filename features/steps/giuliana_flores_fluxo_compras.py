# Fluxo de Compras
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


@when(u'clico no Banner Colecao de Rosas')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner").click() #clica no banner
    time.sleep(10)
    
@when(u'clico no produto Sensacional Rosa Vermelha')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .image-content > img").click() #clica no produto
    context.driver.execute_script("window.scrollTo(0,139.5)") #rola a tela
    
@when(u'digito o CEP, data de entrega, periodo de entrega')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtZip").click() #digitar CEP
    context.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("01153000")
    context.driver.find_element(By.CSS_SELECTOR, ".jOpenShippingPopup").click()
    context.driver.find_element(By.CSS_SELECTOR, ".selectDate").click() #selecionar data de entrega
    context.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("2024.04.20")
    context.driver.find_element(By.CSS_SELECTOR, ".jPeriodRadio").click() #selecionar período do dia da entrega
    context.driver.find_element(By.ID, "btConfirmShippingData").click() #botão OK
    
@then(u'adiciono o produto no carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click() #adicionar produto ao carrinho
    context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click() #botão continuar
  
@when(u'digito o nome, tipo de endereco, numero da casa do destinatario e cartao em branco')
def step_impl(context):
    context.driver.find_element(By.ID, "txtDsDestinationName").click() #nome do destinatário
    context.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Gisele")
    
    context.driver.find_element(By.ID, "ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_1_0").click() #tipo de endereço
    
    context.driver.find_element(By.ID, "txtDsNumber").click() #número da casa
    context.driver.find_element(By.ID, "txtDsNumber").send_keys("39")
    
    context.driver.find_element(By.ID, "rbBlankGiftCard").click() #botão cartão em branco
    
    context.driver.find_element(By.ID, "btnContinue").click() #botão continue
    time.sleep(10)

@when(u'removo o produto')
def step_impl(context):
    context.driver.back() #retorna  1 página
    context.driver.back()
    
    context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_lbtRemoveProduct_0").click() #remover produtos do carrinho
    
@then(u'verifico que o carrinho esta vazio')
def step_impl(context):
    numero_carrinho = context.driver.find_elements(By.CSS_SELECTOR, ".bg_carrinho jBasketLink")
    assert len(numero_carrinho) == 0 #valida quantidade   
   
@then(u'realizo logout')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click() #menu
    context.driver.find_element(By.CSS_SELECTOR, "li:nth-child(11) > a:nth-child(2)").click() #logout
  