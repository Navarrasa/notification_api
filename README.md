# Sistema de Notificação de status de API's

## Este pequeno sistema tem o objetivo de:
- Aprender a utilizar FastAPI para a criação de API's poderosas;
- Criar um pequeno sistema que informa quando uma API é modificada de alguma forma relevante;
- Utilização de WebSockets, para a comunicação entre a API e o servidor (navegador), possibilitando a atualização em tempo real;


## Tecnologias Utilizadas:
- Python 3.x.x
- HTML5
- CSS3
- JavaScript

## Como utilizar:

- Primeiro, tenha esses programas instalados:
- Python 3+;
- Visual Studio Code (ou a IDE de sua preferência);
- pip

- Passo 1:
Abra o diretório clonado em seu lugar de preferencia no dispositivo (Abra com o Explorer ou com o Visual Studio Code diretamente);
- Passo 2 (Explorer):
Na aba de caminhos do explorer (ao lado esquerdo da aba de pesquisas), digite `cmd`
- Passo 3 (Explorer):
No cmd (Terminal de Comandos do Windows), digite `code .`
- Passo 4 (Visual Studio Code):
Com o VSCode aberto, aperte as teclas `Ctrl + J`, um atalho para abrir o cmd do VSCode
- Passo 5 (Visual Studio Code):
Digite os comandos `python -m venv .env`, aguarde a operação finalizar,
Digite .env/Scripts/activate,
Digite pip install -r requirements.txt
Aguarde as operações finalizarem.
- Passo 6:
Execute o comando `uvicorn main:app --reload`
- Passo 7:
Verifique as notificações das API's que desejar no arquivo `server.py`, adicionando URL's de API's na linha 29, uma lista com URL's de API's.



# Referências:

- FastAPI
[text](https://fastapi.tiangolo.com/#sponsors)
- WebSockets
[text](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
- GitHub - Gustavo Garcia
[text](https://github.com/GustavoGarciaPereira/websocket-notifications-demo/blob/main/readme.md)