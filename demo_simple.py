"""
CitySpark Features Demonstration - Simple Version
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))


def print_section(title):
    print(f"\n{'=' * 50}")
    print(f"[DEMO] {title}")
    print("=" * 50)


def demonstrate_simple():
    print_section("CITYSPARK SIMPLE DEMONSTRATION")

    try:
        # Test AI Learning Engine
        print("\n1. Testing AI Learning Engine...")
        from core.ai_learning.engine import CitySparkLearningEngine

        engine = CitySparkLearningEngine()
        profile = engine.create_student_profile(
            "demo_student", {"learning_style": "visual", "skill_level": "beginner"}
        )
        print(f"   OK - Created profile: {profile['student_id']}")

        # Test Urban Art Generator
        print("\n2. Testing Urban Art Generator...")
        from assets.urban_art.generator import UrbanArtGenerator

        generator = UrbanArtGenerator()
        art = generator.generate_art("city skyline", "modern")
        print(f"   OK - Generated art: {art['title']}")

        # Test Configuration
        print("\n3. Testing Configuration...")
        from core.config import settings

        print(f"   OK - App Name: {settings.APP_NAME}")
        print(f"   OK - Port: {settings.PORT}")
        print(f"   OK - AI Features: {settings.ENABLE_AI_FEATURES}")

        # Test Integration
        print("\n4. Testing Integration Modules...")
        from integration.github_scraper.scraper import GitHubScraper
        from integration.omniscient_hub.connector import OmniscientHubConnector

        print("   OK - GitHub Scraper loaded")
        print("   OK - Omniscient Hub Connector loaded")

        print("\n" + "=" * 50)
        print("SUCCESS: All core components working!")
        print("=" * 50)

        print("\nWHAT YOU CAN DO NOW:")
        print("1. Start API server: python main.py")
        print("2. Access documentation: http://127.0.0.1:8000/docs")
        print("3. Test learning endpoints: POST /api/learning/profiles")
        print("4. Generate urban art: POST /api/art/generate")
        print("5. Get AI recommendations: POST /api/ai/recommendations")
        print("6. Check system health: GET /api/health")

        return True

    except Exception as e:
        print(f"\nERROR: Demo failed - {e}")
        return False


if __name__ == "__main__":
    demonstrate_simple()
