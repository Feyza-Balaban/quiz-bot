from fastapi.testclient import TestClient
from quiz_bot.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Feyza! Your GET endpoint works 🎉"}
