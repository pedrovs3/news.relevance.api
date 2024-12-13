# Use a imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de dependências para o container
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Baixe os recursos necessários do NLTK
RUN python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

# Copie o código da aplicação para o container
COPY ./app ./app

# Expor a porta que o FastAPI usará
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
