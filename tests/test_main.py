from fastapi.testclient import TestClient

from src.main import app

# Create a TestClient for the FastAPI app
client = TestClient(app)

def test_read_root():
    # Make a GET request to the root endpoint
    response = client.get("/")

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response JSON body
    assert response.json() == {"message": "Hello, World!"}
