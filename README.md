﻿# **News Relevance API**

A **News Relevance API** é um serviço desenvolvido com **FastAPI** que permite classificar notícias com base em sua relevância para palavras-chave fornecidas pelo usuário. O sistema utiliza **TF-IDF** e **similaridade de cosseno** para calcular a relevância, garantindo resultados precisos e eficientes.

---

## **Funcionalidades**

- Classificação de notícias com base em palavras-chave.
- Suporte a pré-processamento avançado de texto (lemmatização e expansão de sinônimos).
- Compressão automática das respostas com Gzip para maior eficiência.
- Validação rigorosa dos dados com **Pydantic**.
- Estrutura modular e escalável para fácil manutenção e expansão.

---

## **Tecnologias Utilizadas**

- **Python 3.10**
- **FastAPI**: Framework web moderno e rápido.
- **Scikit-learn**: Para cálculos de TF-IDF e similaridade de cosseno.
- **NLTK**: Para lematização e manipulação de texto.
- **Uvicorn**: Servidor ASGI para FastAPI.

---

## **Instalação**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/news-relevance-api.git
   cd news-relevance-api
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Baixe os recursos necessários do NLTK:
   ```bash
   python -m nltk.downloader wordnet omw-1.4
   ```

---

## **Uso**

### **Executar o Servidor**
Para iniciar a aplicação, execute o seguinte comando:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 3000
```

A API estará disponível em **http://localhost:3000**.

---

### **Endpoints**

#### **1. Classificar Notícias**
**Endpoint:**  
`POST /api/news/rank`

**Exemplo de Requisição:**
```json
{
    "user_keywords": ["inteligência artificial", "saúde", "diagnóstico"],
    "news": [
        {
            "title": "Avanços da IA na Medicina",
            "content": "A inteligência artificial está revolucionando a medicina, especialmente no diagnóstico de doenças complexas."
        },
        {
            "title": "Esportes e saúde",
            "content": "Estudos recentes mostram que exercícios regulares trazem benefícios à saúde física e mental."
        }
    ]
}
```

**Exemplo de Resposta:**
```json
[
    {
        "title": "Avanços da IA na Medicina",
        "content": "A inteligência artificial está revolucionando a medicina, especialmente no diagnóstico de doenças complexas.",
        "relevance": 0.85
    },
    {
        "title": "Esportes e saúde",
        "content": "Estudos recentes mostram que exercícios regulares trazem benefícios à saúde física e mental.",
        "relevance": 0.45
    }
]
```

---

## **Testes**

1. Instale a biblioteca de testes:
   ```bash
   pip install pytest
   ```

2. Execute os testes:
   ```bash
   pytest
   ```

Os testes estão localizados na pasta `tests/` e cobrem os principais fluxos de trabalho da API.

---

## **Docker**

### **Construir a Imagem**
```bash
docker build -t news-relevance-api .
```

### **Executar o Container**
```bash
docker run -d --name news-relevance-api -p 3000:3000 news-relevance-api
```

Acesse a API em **http://localhost:3000**.

---

## **Contribuição**

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:
1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Realize suas alterações e faça o commit:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. Envie suas alterações:
   ```bash
   git push origin minha-nova-feature
   ```
5. Abra um Pull Request no repositório principal.

---

## **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## **Autores**

- **Pedro Vieira**  
  LinkedIn: [Pedro Vieira](https://www.linkedin.com/in/pedrovs3/)  
  GitHub: [Pedrovs3](https://github.com/pedrovs3)
