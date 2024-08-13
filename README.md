# Projeto FastAPI com Google Generative AI

Este projeto implementa uma API REST usando FastAPI, que interage com o Google Generative AI para gerar respostas baseadas em prompts fornecidos pelo usuário. A API permite o envio de prompts via requisições POST e retorna a resposta gerada pelo modelo.

## Funcionalidades

- **Enviar prompt:** Envia um prompt para o modelo de IA generativa e retorna uma resposta.
- **Configuração de CORS:** Configura permissões para que a API possa ser acessada de diferentes origens.
- **Tratamento de exceções:** Lida com erros e retorna respostas adequadas em caso de falhas.

## Tecnologias Utilizadas

- Python 3.x
- FastAPI
- Pydantic
- Google Generative AI
- Uvicorn (para execução do servidor)
- HTML e JavaScript (para interação via página web)

## Requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

## Instalação

### Windows

1. **Clone o repositório:**

    Abra o Prompt de Comando e execute:

    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    cd seu-projeto
    ```

2. **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual:**

    ```bash
    .\venv\Scripts\activate
    ```

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure sua chave da API:**

    No arquivo `recursos.py`, adicione sua chave da API Google Generative AI na função `api_key()`.

6. **Abra a página `index.html` no navegador:**

    Navegue até o diretório do projeto e abra o arquivo `index.html` no seu navegador (basta dar um duplo clique no arquivo ou abrir manualmente pelo navegador).

7. **Inicie o servidor:**

    Execute o servidor com o comando:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

8. **Interaja com a API através da página web ou via API:**

    - **Via página web:** Use a página `index.html` para enviar prompts e visualizar as respostas diretamente no navegador.
    - **Via API:** Envie requisições POST para a rota `/chat/` com o seguinte corpo JSON:

    ```json
    {
      "prompt": "Seu texto aqui"
    }
    ```

### Linux

1. **Clone o repositório:**

    Abra o terminal e execute:

    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    cd seu-projeto
    ```

2. **Crie um ambiente virtual:**

    ```bash
    python3 -m venv venv
    ```

3. **Ative o ambiente virtual:**

    ```bash
    source venv/bin/activate
    ```

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure sua chave da API:**

    No arquivo `recursos.py`, adicione sua chave da API Google Generative AI na função `api_key()`.

6. **Abra a página `index.html` no navegador:**

    Navegue até o diretório do projeto e abra o arquivo `index.html` no seu navegador (basta dar um duplo clique no arquivo ou abrir manualmente pelo navegador).

7. **Inicie o servidor:**

    Execute o servidor com o comando:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

8. **Interaja com a API através da página web ou via API:**

    - **Via página web:** Use a página `index.html` para enviar prompts e visualizar as respostas diretamente no navegador.
    - **Via API:** Envie requisições POST para a rota `/chat/` com o seguinte corpo JSON:

    ```json
    {
      "prompt": "Seu texto aqui"
    }
    ```

