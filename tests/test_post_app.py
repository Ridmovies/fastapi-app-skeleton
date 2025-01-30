import pytest
from httpx import AsyncClient

# auth_prefix = f"/api/v1/auth"


@pytest.mark.asyncio
async def test_user_creation(client):
    response = await client.get(url="/dev")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_get_all_posts(client: AsyncClient):
    response = await client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.asyncio
async def test_create_post(client: AsyncClient):
    post_data = {"content": "pytest_post_1"}
    response = await client.post("/posts", json=post_data)
    assert response.status_code == 200
    assert response.json() == {"content": "pytest_post_1", "id": 1}


@pytest.mark.asyncio
async def test_get_post_by_id(client: AsyncClient):
    post_id = 1
    response = await client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json() == {"content": "pytest_post_1", "id": 1}
