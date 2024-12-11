
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_example_endpoint():
    response = client.get("/api/v1/example")
    assert response.status_code == 200
    assert response.json() == {"message": "This is an example endpoint"}

