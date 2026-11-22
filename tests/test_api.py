from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to File Organizer!",
        "version": "1.0.0",
    }

def test_openapi_schema():
    response = client.get("/openapi.json")

    assert response.status_code == 200

    schema = response.json()

    assert schema["info"]["title"] == "File Organizer"
    assert schema["info"]["version"] == "1.0.0"
    assert "/" in schema["paths"]
    assert "get" in schema["paths"]["/"]