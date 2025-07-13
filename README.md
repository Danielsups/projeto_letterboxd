# Extrator de Listas Letterboxd 🎬

Este é um projeto universitário desenvolvido em Django que permite a um utilizador extrair, visualizar e ordenar filmes de qualquer lista pública do site [Letterboxd](https://letterboxd.com). A aplicação demonstra conceitos fundamentais de desenvolvimento web com Django, manipulação de banco de dados com SQLite, e técnicas de web scraping com BeautifulSoup.

<br>

## ✨ Funcionalidades

* **Extração de Dados via URL:** Insira a URL de uma lista do Letterboxd e a aplicação irá extrair automaticamente os dados de todos os filmes contidos nela.
* **Visualização em Tabela:** Os dados extraídos são apresentados numa tabela limpa e organizada.
* **Ordenação Dinâmica:** Ordene os resultados por nota (maior para menor e vice-versa), nome do filme, ou ano de lançamento sem precisar de recarregar a página de forma demorada.
* **Limpeza Automática e Manual:** O banco de dados é limpo automaticamente sempre que uma nova lista é extraída, garantindo que os dados são sempre frescos. Um botão de limpeza manual também está disponível.
* **Feedback de Carregamento:** Uma animação de carregamento informa ao utilizador que o processo de extração (que pode ser demorado) está em andamento.

<br>



<br>

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Django
* **Web Scraping:** BeautifulSoup4, Requests
* **Frontend:** HTML5, CSS3, JavaScript (vanilla)
* **Banco de Dados:** SQLite (padrão do Django)

<br>

## 🚀 Instalação e Execução

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

* [Python 3.8+](https://www.python.org/downloads/)
* `pip` (gerenciador de pacotes do Python)

### Criando o Ficheiro de Dependências

Para facilitar a instalação, é uma boa prática criar um ficheiro `requirements.txt`. No seu terminal, na pasta raiz do projeto, execute o seguinte comando:

```bash
pip freeze > requirements.txt
```

Isso listará todas as bibliotecas Python que utilizámos num ficheiro, tornando a instalação mais fácil para outras pessoas.

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Danielsups/projeto_letterboxd
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd projeto_letterboxd
    ```

3.  **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**
    * **No Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **No macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Instale as dependências a partir do ficheiro `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Aplique as migrações do banco de dados:**
    Este comando cria o ficheiro de banco de dados `db.sqlite3` e as tabelas necessárias.
    ```bash
    python manage.py migrate
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse a aplicação:**
    Abra o seu navegador e vá para [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

<br>

## 💻 Como Usar

1.  **Extrair uma lista:** Copie a URL de uma lista pública do Letterboxd, cole no campo de formulário e clique em "Extrair Filmes".
2.  **Aguarde o carregamento:** A extração pode demorar alguns minutos. A tela de carregamento indicará que o processo está em andamento.
3.  **Ordenar os resultados:** Após a tabela ser exibida, use o menu "Ordenar por:" para reorganizar os dados conforme a sua preferência. A lista será atualizada automaticamente.
4.  **Limpar os dados:** Utilize o botão "Limpar Banco de Dados" para apagar todos os registos e começar de novo. Note que ao extrair uma nova lista, a limpeza já é feita automaticamente.

<br>

## 📄 Licença

Este projeto está sob a licença MIT. Veja o ficheiro `LICENSE` para mais detalhes.
