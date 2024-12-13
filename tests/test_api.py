from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_rank_endpoint():
    response = client.post("/api/news/rank", json={
        "user_keywords": ["inteligência artificial", "tecnologia", "saúde"],
        "news": [
            {"title": "Avanço em IA na saúde", "content": "IA está revolucionando diagnósticos médicos."},
            {"title": "Esporte e saúde", "content": "Exercícios são essenciais para uma vida saudável."},
            {"title": "Novas tecnologias", "content": "Smartphones estão cada vez mais avançados."}
        ]
    })
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["title"] == "Avanço em IA na saúde"
