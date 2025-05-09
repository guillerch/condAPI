from fastapi.testclient import TestClient
from condAPI.endpoints import root_router  # importa el objeto app

client = TestClient(root_router)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "routes" in resp.json()