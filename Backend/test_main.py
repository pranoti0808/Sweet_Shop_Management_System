import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
token = ""  # Global JWT token for protected routes
sweet_id = None  # To store created sweet's ID

# ---------------------------
# 1️⃣ Register user
# ---------------------------
def test_register_user():
    response = client.post("/api/auth/register", json={
        "username": "testuser1",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "User registered"}

# ---------------------------
# 2️⃣ Register duplicate user
# ---------------------------
def test_register_duplicate_user():
    response = client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

# ---------------------------
# 3️⃣ Login user
# ---------------------------
def test_login_user():
    global token
    response = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["role"] == "USER"
    token = data["access_token"]

# ---------------------------
# 4️⃣ Invalid login
# ---------------------------
def test_invalid_login():
    response = client.post("/api/auth/login", json={
        "username": "wronguser",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert "Invalid credentials" in response.json()["detail"]

# ---------------------------
# 5️⃣ Add sweet (JWT required)
# ---------------------------
def test_add_sweet():
    global sweet_id
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/sweets", json={
        "name": "Ladoo",
        "category": "Indian",
        "price": 10,
        "quantity": 50
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ladoo"
    sweet_id = data.get("id")  # Save sweet ID for update/delete

# ---------------------------
# 6️⃣ Add sweet without token
# ---------------------------
def test_add_sweet_no_token():
    response = client.post("/api/sweets", json={
        "name": "Barfi",
        "category": "Indian",
        "price": 20,
        "quantity": 30
    })
    assert response.status_code == 401

# ---------------------------
# 7️⃣ Get all sweets
# ---------------------------
def test_get_sweets():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/sweets", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(sweet["name"] == "Ladoo" for sweet in data)

# ---------------------------
# 8️⃣ Update sweet
# ---------------------------
def test_update_sweet():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put(f"/api/sweets/{sweet_id}", json={
        "name": "Ladoo Special",
        "category": "Indian",
        "price": 12,
        "quantity": 60
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ladoo Special"
    assert data["price"] == 12

# ---------------------------
# 9️⃣ Delete sweet
# ---------------------------
def test_delete_sweet():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete(f"/api/sweets/{sweet_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Sweet deleted"

# ---------------------------
# 🔟 Get sweets after deletion
# ---------------------------
def test_get_sweets_after_delete():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/sweets", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert all(sweet["id"] != sweet_id for sweet in data)
