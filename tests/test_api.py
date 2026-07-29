import pytest
from httpx import ASGITransport, AsyncClient
from src.api.main import app

@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c

@pytest.mark.asyncio
async def test_recommend(client):
    r = await client.post("/api/v1/recommend/user", json={"user_id": "U-1", "n_recommendations": 5, "strategy": "hybrid"})
    assert r.status_code == 200
    d = r.json()
    assert d["strategy"] == "hybrid"
    assert len(d["recommendations"]) == 5

@pytest.mark.asyncio
async def test_similar(client):
    r = await client.post("/api/v1/recommend/similar", json={"item_id": "ITEM-0001", "n_similar": 3})
    assert r.status_code == 200
    assert len(r.json()["recommendations"]) == 3

@pytest.mark.asyncio
async def test_ab(client):
    r = await client.post("/api/v1/experiments/ab-test?strategy_a=collaborative&strategy_b=hybrid")
    assert r.status_code == 200
    d = r.json()
    assert "winner" in d
    assert "uplift_pct" in d
