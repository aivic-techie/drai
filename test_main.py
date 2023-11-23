from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat/", json={"message": "Hello, Dr. AI!"})
    assert response.status_code == 200
    assert "reply" in response.json()

def test_special_commands():
    commands = ["exit", "clear", "help", "info"]
    for command in commands:
        response = client.post("/chat/", json={"message": command})
        assert response.status_code == 200
        assert "reply" in response.json()

def test_get_history():
    response = client.get("/history/")
    assert response.status_code == 200
    assert "messages" in response.json()

if __name__ == "__main__":
    test_chat_endpoint()
    test_special_commands()
    test_get_history()
