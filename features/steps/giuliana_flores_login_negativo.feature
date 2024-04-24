Feature: Login Negativo

    Scenario: Login negativo no site Giuliana Flores
        Given que acesso o site Giuliana Flores
        When entro no menu da pagina inicial
        Then clico em login
        When preencho os campos de login com usuario vinicius@icloud.com e senha caju
        Then resolvo um captcha
        When clico em continuar 
        Then exibe a mensagem de erro no login