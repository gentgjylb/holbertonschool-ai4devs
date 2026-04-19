from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from main import app
import database

# Use a test database
database.DB_PATH = "test_mvp.db"
database.init_db()

client = TestClient(app)

def test_missing_idea_field_returns_422():
    response = client.post("/api/projects", json={"title": "test"})
    assert response.status_code == 422

def test_create_project_returns_project_id():
    response = client.post("/api/projects", json={
        "title": "My Test Project",
        "raw_idea": "I want to build a testing app",
        "constraints": "No time"
    })
    assert response.status_code == 200
    data = response.json()
    assert "project_id" in data
    assert type(data["project_id"]) is str

def test_get_nonexistent_project_returns_404():
    response = client.get("/api/projects/does-not-exist")
    assert response.status_code == 404

def test_get_project_success():
    res = client.post("/api/projects", json={"title": "Test 1", "raw_idea": "Idea 1"})
    pid = res.json()["project_id"]
    
    response = client.get(f"/api/projects/{pid}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test 1"
    assert "problem_statement" in data

def test_generate_features_nonexistent_project_returns_404():
    response = client.post("/api/projects/invalid-id/features/generate")
    assert response.status_code == 404

def test_generate_features_success():
    res = client.post("/api/projects", json={"title": "Test F", "raw_idea": "Idea F"})
    pid = res.json()["project_id"]
    
    response = client.post(f"/api/projects/{pid}/features/generate")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
    assert "in_scope" in data[0]

def test_list_features_success():
    res = client.post("/api/projects", json={"title": "Test LF", "raw_idea": "Idea LF"})
    pid = res.json()["project_id"]
    client.post(f"/api/projects/{pid}/features/generate")
    
    response = client.get(f"/api/projects/{pid}/features")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_generate_stories_no_features_returns_empty_or_fail():
    res = client.post("/api/projects", json={"title": "Test S1", "raw_idea": "Idea S1"})
    pid = res.json()["project_id"]
    
    response = client.post(f"/api/projects/{pid}/stories/generate")
    assert response.status_code == 400

def test_generate_stories_success():
    res = client.post("/api/projects", json={"title": "Test S2", "raw_idea": "Idea S2"})
    pid = res.json()["project_id"]
    client.post(f"/api/projects/{pid}/features/generate")
    
    response = client.post(f"/api/projects/{pid}/stories/generate")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "full_text" in data[0]

def test_list_stories_success():
    res = client.post("/api/projects", json={"title": "Test LS", "raw_idea": "Idea LS"})
    pid = res.json()["project_id"]
    client.post(f"/api/projects/{pid}/features/generate")
    client.post(f"/api/projects/{pid}/stories/generate")
    
    response = client.get(f"/api/projects/{pid}/stories")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_export_document_success():
    res = client.post("/api/projects", json={"title": "Export Test", "raw_idea": "Export Mocking"})
    pid = res.json()["project_id"]
    client.post(f"/api/projects/{pid}/features/generate")
    client.post(f"/api/projects/{pid}/stories/generate")
    
    response = client.get(f"/api/export/{pid}")
    assert response.status_code == 200
    data = response.json()
    assert "markdown" in data
    assert "# MVP Concept" in data["markdown"]
