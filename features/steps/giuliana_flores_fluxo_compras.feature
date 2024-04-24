Feature: Fluxo de Compras

Scenario: Fluxo de compras site Giuliana Flores
        Given que acesso o site Giuliana Flores
        When entro no menu da pagina inicial
        Then clico em login
        When preencho os campos de login com usuario vinicius.manuel.dasilva@icloud.com e senha QAZwsx123
        When resolvo um captcha
        Then clico em continuar 
        Then sou direcionado a Home
        When clico no Banner Colecao de Rosas
        When clico no produto Sensacional Rosa Vermelha 
        When digito o CEP, data de entrega, periodo de entrega
        Then adiciono o produto no carrinho
        When digito o nome, tipo de endereco, numero da casa do destinatario e cartao em branco
        When removo o produto 
        Then verifico que o carrinho esta vazio 
        Then realizo logout