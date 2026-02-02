"""
🧪 CitySpark Simple Test Suite
Quick verification that all components are working
"""

import sys
import os
import requests
import json
import time
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_imports():
    """Test that all main modules can be imported"""
    print("[IMPORT] Testing imports...")

    try:
        from core.ai_learning.engine import CitySparkLearningEngine

        print("[OK] AI Learning Engine imported")
    except Exception as e:
        print(f"[FAIL] AI Learning Engine failed: {e}")

    try:
        from assets.urban_art.generator import UrbanArtGenerator

        print("[OK] Urban Art Generator imported")
    except Exception as e:
        print(f"[FAIL] Urban Art Generator failed: {e}")

    try:
        from api.routes.learning import router as learning_router

        print("[OK] Learning API router imported")
    except Exception as e:
        print(f"[FAIL] Learning API router failed: {e}")

    try:
        from api.routes.art import router as art_router

        print("[OK] Art API router imported")
    except Exception as e:
        print(f"[FAIL] Art API router failed: {e}")


def test_learning_engine():
    """Test AI Learning Engine"""
    print("\n[AI] Testing AI Learning Engine...")

    try:
        from core.ai_learning.engine import CitySparkLearningEngine

        engine = CitySparkLearningEngine()

        # Test student profile creation
        profile_data = {
            "learning_style": "visual",
            "skill_level": "beginner",
            "interests": ["AI", "art"],
            "goals": ["learn programming"],
            "strengths": ["creativity"],
            "weaknesses": ["math"],
        }

        profile = engine.create_student_profile("test_student", profile_data)
        print("[OK] Student profile created")

        # Test performance analysis
        performance_data = {
            "score": 85.5,
            "time_spent": 45,
            "difficulty": "medium",
            "completion_rate": 1.0,
            "module": "python_basics",
            "activity_type": "quiz",
        }

        analysis = engine.analyze_performance("test_student", performance_data)
        print("[OK] Performance analysis completed")

        # Test learning path generation
        learning_path = engine.generate_learning_path(
            "test_student", "python_programming", ["learn basics", "build project"]
        )
        print("[OK] Learning path generated")

        # Test recommendations
        recommendations = engine.get_recommendations("test_student")
        print(f"[OK] Generated {len(recommendations)} recommendations")

        return True

    except Exception as e:
        print(f"❌ Learning Engine test failed: {e}")
        return False


def test_art_generator():
    """Test Urban Art Generator"""
    print("\n[ART] Testing Urban Art Generator...")

    try:
        from assets.urban_art.generator import UrbanArtGenerator

        generator = UrbanArtGenerator()

        # Test art generation
        art_piece = generator.generate_art(
            "modern city skyline with neon lights", "modern", "test_user"
        )
        print("[OK] Art piece generated")

        # Test gallery access
        gallery = generator.get_gallery()
        print(f"[OK] Gallery accessed with {len(gallery)} pieces")

        # Test popular art
        popular = generator.get_popular_art()
        print(f"[OK] Popular art retrieved: {len(popular)} pieces")

        # Test style suggestions
        suggestions = generator.get_style_suggestions("city urban modern")
        print(f"[OK] Style suggestions: {suggestions}")

        return True

    except Exception as e:
        print(f"❌ Art Generator test failed: {e}")
        return False


def test_api_endpoints():
    """Test API endpoints if server is running"""
    print("\n[API] Testing API Endpoints...")

    base_url = "http://127.0.0.1:8000"

    # Test endpoints to check
    endpoints = [
        ("/", "Root endpoint"),
        ("/api/health", "Health check"),
        ("/api/status", "System status"),
        ("/api/learning/courses", "Courses list"),
        ("/api/art/gallery", "Art gallery"),
        ("/api/art/styles", "Art styles"),
    ]

    results = []

    for endpoint, description in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            if response.status_code == 200:
                print(f"[OK] {description}: {response.status_code}")
                results.append(True)
            else:
                print(f"[WARN] {description}: {response.status_code}")
                results.append(False)
        except requests.exceptions.ConnectionError:
            print(f"[FAIL] {description}: Server not running")
            results.append(False)
        except Exception as e:
            print(f"[FAIL] {description}: {e}")
            results.append(False)

    return all(results)


def test_configuration():
    """Test configuration loading"""
    print("\n[CONFIG] Testing Configuration...")

    try:
        from core.config import settings

        print(f"[OK] App Name: {settings.APP_NAME}")
        print(f"[OK] App Version: {settings.APP_VERSION}")
        print(f"[OK] Debug Mode: {settings.DEBUG}")
        print(f"[OK] Host: {settings.HOST}")
        print(f"[OK] Port: {settings.PORT}")

        return True

    except Exception as e:
        print(f"[FAIL] Configuration test failed: {e}")
        return False


def test_file_structure():
    """Test that all necessary files and folders exist"""
    print("\n[FILE] Testing File Structure...")

    required_files = [
        "main.py",
        "requirements.txt",
        "package.json",
        "README.md",
        "SETUP.md",
        ".env.example",
    ]

    required_folders = [
        "core/ai_learning",
        "core/curriculum",
        "core/assessment",
        "core/analytics",
        "integration/omniscient_hub",
        "integration/apex_insight",
        "integration/github_scraper",
        "luminscript/educational",
        "luminscript/interactive",
        "luminscript/ai_assistant",
        "assets/github",
        "assets/templates",
        "assets/resources",
        "assets/urban_art",
        "api/routes",
        "frontend/src",
        "docs",
        "scripts",
        "tests",
    ]

    missing_items = []

    # Check files
    for file in required_files:
        if os.path.exists(file):
            print(f"[OK] {file}")
        else:
            print(f"[FAIL] {file} - Missing")
            missing_items.append(file)

    # Check folders
    for folder in required_folders:
        if os.path.exists(folder):
            print(f"[OK] {folder}/")
        else:
            print(f"[FAIL] {folder}/ - Missing")
            missing_items.append(folder)

    return len(missing_items) == 0


def run_full_test():
    """Run complete test suite"""
    print("Starting CitySpark Complete Test Suite")
    print("=" * 50)

    start_time = time.time()

    test_results = []

    # Run all tests
    test_results.append(("File Structure", test_file_structure()))
    test_results.append(("Configuration", test_configuration()))
    test_results.append(("Learning Engine", test_learning_engine()))
    test_results.append(("Art Generator", test_art_generator()))
    test_results.append(("API Endpoints", test_api_endpoints()))

    # Calculate results
    end_time = time.time()
    total_time = end_time - start_time

    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)

    print("\n" + "=" * 50)
    print("Test Results Summary")
    print("=" * 50)

    for test_name, result in test_results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{test_name:<20} {status}")

    print("-" * 50)
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed / total) * 100:.1f}%")
    print(f"Total Time: {total_time:.2f} seconds")

    if passed == total:
        print("\n[SUCCESS] All tests passed! CitySpark is ready to go!")
        return True
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed. Check the output above.")
        return False


def main():
    """Main function to run tests"""
    if len(sys.argv) > 1:
        test_name = sys.argv[1]

        if test_name == "imports":
            test_imports()
        elif test_name == "learning":
            test_learning_engine()
        elif test_name == "art":
            test_art_generator()
        elif test_name == "api":
            test_api_endpoints()
        elif test_name == "config":
            test_configuration()
        elif test_name == "structure":
            test_file_structure()
        else:
            print(f"Unknown test: {test_name}")
            print("Available tests: imports, learning, art, api, config, structure")
    else:
        success = run_full_test()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
