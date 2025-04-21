from app import app
import pytest
def test_hello_world():
    """Test the hello_world function."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"<p>Hello, World!</p>"    