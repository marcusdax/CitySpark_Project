import pytest
from fastapi.testclient import TestClient
from main import create_app

# Test client setup
app = create_app()
if app:
    client = TestClient(app)
else:
    client = None


def test_root_endpoint():
    """Test the root endpoint"""
    if not client:
        pytest.skip("App not available")

    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "CitySpark" in data["message"]


def test_health_endpoint():
    """Test the health check endpoint"""
    if not client:
        pytest.skip("App not available")

    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_learning_profile_creation():
    """Test student profile creation"""
    if not client:
        pytest.skip("App not available")

    profile_data = {
        "student_id": "test_student_1",
        "learning_style": "visual",
        "skill_level": "beginner",
        "interests": ["AI", "art"],
        "goals": ["learn programming"],
        "strengths": ["creativity"],
        "weaknesses": ["math"],
    }

    response = client.post("/api/learning/profiles", json=profile_data)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student profile created successfully"
    assert "profile" in data


def test_art_generation():
    """Test urban art generation"""
    if not client:
        pytest.skip("App not available")

    art_request = {
        "prompt": "modern city skyline with neon lights",
        "style": "modern",
        "user_id": "test_user_1",
    }

    response = client.post("/api/art/generate", json=art_request)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Art generated successfully"
    assert "art_piece" in data


def test_art_gallery():
    """Test art gallery endpoint"""
    if not client:
        pytest.skip("App not available")

    response = client.get("/api/art/gallery")
    assert response.status_code == 200
    data = response.json()
    assert "gallery" in data
    assert "total_count" in data


def test_ai_recommendations():
    """Test AI recommendations endpoint"""
    if not client:
        pytest.skip("App not available")

    # First create a student profile
    profile_data = {
        "student_id": "test_student_2",
        "learning_style": "auditory",
        "skill_level": "intermediate",
    }
    client.post("/api/learning/profiles", json=profile_data)

    # Get recommendations
    response = client.get("/api/learning/recommendations/test_student_2")
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert "total_count" in data


def test_learning_path_generation():
    """Test learning path generation"""
    if not client:
        pytest.skip("App not available")

    # First create a student profile
    profile_data = {
        "student_id": "test_student_3",
        "learning_style": "kinesthetic",
        "skill_level": "beginner",
    }
    client.post("/api/learning/profiles", json=profile_data)

    # Generate learning path
    path_request = {
        "student_id": "test_student_3",
        "subject": "python_programming",
        "goals": ["learn basics", "build project"],
    }

    response = client.post("/api/learning/paths", json=path_request)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Learning path generated successfully"
    assert "path" in data


def test_performance_analysis():
    """Test performance analysis endpoint"""
    if not client:
        pytest.skip("App not available")

    # First create a student profile
    profile_data = {
        "student_id": "test_student_4",
        "learning_style": "visual",
        "skill_level": "beginner",
    }
    client.post("/api/learning/profiles", json=profile_data)

    # Analyze performance
    performance_data = {
        "student_id": "test_student_4",
        "score": 85.5,
        "time_spent": 45,
        "difficulty": "medium",
        "completion_rate": 1.0,
        "module": "python_basics",
        "activity_type": "quiz",
    }

    response = client.post("/api/learning/analyze", json=performance_data)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Performance analysis completed"
    assert "analysis" in data


def test_art_styles():
    """Test art styles endpoint"""
    if not client:
        pytest.skip("App not available")

    response = client.get("/api/art/styles")
    assert response.status_code == 200
    data = response.json()
    assert "styles" in data
    assert len(data["styles"]) > 0
    assert "modern" in data["styles"]


def test_featured_content():
    """Test featured content endpoint"""
    if not client:
        pytest.skip("App not available")

    response = client.get("/api/featured")
    assert response.status_code == 200
    data = response.json()
    assert "featured_courses" in data
    assert "featured_art" in data
    assert "featured_resources" in data


def test_statistics():
    """Test statistics endpoint"""
    if not client:
        pytest.skip("App not available")

    response = client.get("/api/stats")
    assert response.status_code == 200
    data = response.json()
    assert "learning" in data
    assert "art" in data
    assert "github" in data
    assert "ai" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
