# FakePinterest

FakePinterest é uma aplicação web desenvolvida em Flask que simula algumas funcionalidades básicas de um site de compartilhamento de imagens.

## Requisitos

- Python 3.8+
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Instalação

### Clonando o repositório

```bash
git clone https://github.com/seu-usuario/fakepinterest.git
cd fakepinterest
```

### Instalando as dependências

Utilize o Poetry para instalar as dependências do projeto:

```bash
poetry install
```

### Configurando variáveis de ambiente

Crie um arquivo `.__init__.py` na raiz do projeto e adicione as variáveis de ambiente necessárias. Exemplo:

```
FLASK_APP=app
FLASK_ENV=development
DATABASE_URL=sqlite:///fakepinterest.db
SECRET_KEY=your_secret_key
```

### Criando a instância do banco de dados

Execução o script `create_database.py`

```bash
poetry run python create_database.py
```

## Executando a aplicação

### Localmente

Para rodar a aplicação localmente, utilize o comando:

```bash
ENV FLASK_APP=main.py
```

```bash
poetry run python main.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`.

### Usando Docker

Para criar e rodar um container Docker da aplicação, siga os passos abaixo:

1. Construa a imagem Docker:

   ```bash
   docker build -t fakepinterest .
   ```

2. Rode o container:

   ```bash
   docker run -d -p 5000:5000 --name fakepinterest_container fakepinterest
   ```

A aplicação estará disponível em `http://127.0.0.1:5000`.

## Estrutura do Projeto

```
fakepinterest/
├── __init__.py
├── create_database.py
├── forms.py
├── models.py
├── routes.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── fotos_posts/
│   └── fotos_site/
├── templates/
│   ├── criar_conta.html
│   ├── feed.html
│   ├── homepage.html
│   ├── navbar.html
│   └── perfil.html
├── instance/
│   └── fakepinterest.db
├── main.py
├── pyproject.toml
├── README.md
└── Dockerfile
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
