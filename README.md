

# Calculadora Simples com Flet

Este projeto é uma calculadora simples desenvolvida em Python usando a biblioteca **Flet** para criar a interface gráfica. A aplicação possui um visual moderno, com tema escuro, e suporta operações básicas de cálculo.

## Funcionalidades

* Interface gráfica com botões para números (0-9), operadores (+, -, \*, /), porcentagem (%), ponto decimal (.) e ações especiais (C para limpar, ⌫ para apagar o último caractere, = para calcular).
* Suporte para cálculos usando a função `eval`, com tratamento para erros de cálculo.
* Botão para limpar toda a entrada.
* Botão para apagar o último caractere digitado.
* Exibição do resultado na parte superior da tela, alinhado à direita.
* Estilização personalizada dos botões com cores diferentes para números, operadores, botão limpar e botão de cálculo (=).

## Como funciona o código

* A função `main` configura a janela da aplicação, definindo título, tamanho e cor de fundo.
* Uma variável `todos_valores` armazena a expressão matemática digitada pelo usuário.
* Quando o usuário clica nos botões de números e operadores, o texto é adicionado à expressão e exibido na tela.
* O botão "=" avalia a expressão usando `eval` (com conversão de `%` para `/100`).
* O botão "C" limpa a expressão.
* O botão "⌫" apaga o último caractere digitado.
* A interface é organizada em linhas de botões (`Rows`) dentro de uma coluna (`Column`), com estilo consistente e responsivo.

## Como executar

Para rodar a calculadora, é necessário ter o Python instalado e a biblioteca Flet. Você pode instalar o Flet com:

```bash
pip install flet
```

Em seguida, execute o script Python:

```bash
python calculadora.py
```


