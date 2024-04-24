Feature: Realizar Login

    Scenario: Realizar login no site Giuliana Flores
        Given que acesso o site Giuliana Flores
        When entro no menu da pagina inicial
        Then clico em login
        When preencho os campos de login com usuario vinicius.manuel.dasilva@icloud.com e senha QAZwsx123
        When resolvo um captcha
        Then clico em continuar 
        Then sou direcionado a Home

        