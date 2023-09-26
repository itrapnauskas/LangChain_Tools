# Projeto Langchain Chatbot

Este projeto implementa um chatbot utilizando a biblioteca Langchain, que oferece uma estrutura para integrar modelos de linguagem e ferramentas específicas em uma aplicação de chat. O chatbot inclui um conjunto de ferramentas úteis como calculadora de números Fibonacci, organizador de string alfabética, criptografador e descriptografador de palavras.

## Requisitos

- Python 3.7 ou superior.
- Biblioteca Streamlit.
- Biblioteca Langchain.

## Instalação

Clone o repositório e instale as dependências usando pip:

```bash
git clone https://github.com/username/langchain-chatbot.git
cd langchain-chatbot
pip install -r requirements.txt
```

##Execução
Para executar o chatbot, use o comando abaixo:

```bash
streamlit run app.py
```

Acesse o chatbot no navegador através do endereço fornecido no terminal.

## Estrutura do Código
O código está organizado da seguinte maneira:

### Importações: As bibliotecas necessárias são importadas, incluindo as funções e classes da Langchain e Streamlit.
### Definições de Função: Definições de funções para calcular o número de Fibonacci, organizar uma string em ordem alfabética, criptografar e descriptografar palavras.
### Definição de Ferramentas: Um conjunto de ferramentas é definido, cada uma com um nome, função e descrição associados.
### Inicialização da Memória e Agente: Um buffer de memória e um agente Langchain são inicializados com as ferramentas definidas.
### Interface Streamlit: A interface do usuário é criada usando Streamlit, permitindo a entrada do usuário e a interação com o chatbot.

##Ferramentas Disponíveis

O chatbot oferece as seguintes ferramentas:

### Fibonacci: Calcula o n-ésimo número da sequência de Fibonacci.
### Sort String: Organiza os caracteres de uma string em ordem alfabética.
### Encrypt: Criptografa uma palavra, incrementando o valor ASCII de cada caractere.
### Decrypt: Descriptografa uma palavra, decrementando o valor ASCII de cada caractere.
