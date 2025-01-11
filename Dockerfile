# Usar a imagem oficial do Python 3.10
FROM python:3.10-slim

# Instalar dependências do sistema necessárias para o Poetry
RUN apt-get update \
    && apt-get install -y \
        curl \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Adicionar o Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo pyproject.toml e poetry.lock para o container
COPY pyproject.toml poetry.lock /app/

# Instalar as dependências do projeto usando o Poetry
RUN poetry install --no-root

# Copiar o restante dos arquivos do projeto para o container
COPY . /app/

# Definir a variável de ambiente FLASK_APP
ENV FLASK_APP=main.py

# Definir o ENTRYPOINT para rodar o Flask com o Poetry
ENTRYPOINT ["poetry", "run", "flask", "run"]

# Definir o CMD para passar os parâmetros padrão
CMD ["--host=0.0.0.0"]

