# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o container
COPY ./app ./app

# Expor a porta que o FastAPI usa
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
FROM ubuntu:latest
LABEL authors="pedro"

ENTRYPOINT ["top", "-b"]