#!/usr/bin/env python3
"""
Simple startup script for CitySpark without unicode logging issues
"""

import os
import sys
import logging
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

# Configure simple logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def simple_test():
    """Run simple test of the system"""
    logger.info("Starting CitySpark Complete Project Test")

    try:
        # Test core imports
        from core.ai_learning.engine import CitySparkLearningEngine

        logger.info("AI Learning Engine: OK")

        from assets.urban_art.generator import UrbanArtGenerator

        logger.info("Urban Art Generator: OK")

        # Test basic functionality
        engine = CitySparkLearningEngine()
        profile = engine.create_student_profile(
            "test", {"learning_style": "visual", "skill_level": "beginner"}
        )
        logger.info(f"Created profile: {profile['student_id']}")

        generator = UrbanArtGenerator()
        art = generator.generate_art("test prompt", "modern")
        logger.info(f"Generated art: {art['id']}")

        logger.info("All core components working correctly!")
        return True

    except Exception as e:
        logger.error(f"Test failed: {e}")
        return False


def start_servers():
    """Start both backend and frontend servers"""
    logger.info("Starting development servers...")

    # Start backend
    try:
        import subprocess
        import threading

        def start_backend():
            os.chdir(PROJECT_ROOT)
            subprocess.run([sys.executable, "main.py"], check=False)

        def start_frontend():
            frontend_path = PROJECT_ROOT / "frontend"
            if frontend_path.exists():
                os.chdir(frontend_path)
                subprocess.run(["npm", "run", "dev"], check=False)
            else:
                logger.warning("Frontend folder not found")

        # Start backend in current thread
        backend_thread = threading.Thread(target=start_backend, daemon=True)
        backend_thread.start()

        # Start frontend after 2 seconds
        import time

        time.sleep(2)
        frontend_thread = threading.Thread(target=start_frontend, daemon=True)
        frontend_thread.start()

        logger.info("Servers starting...")
        logger.info("Backend: http://127.0.0.1:8000")
        logger.info("Frontend: http://localhost:3000")
        logger.info("API Docs: http://127.0.0.1:8000/docs")

        # Keep main thread alive
        try:
            while True:
                import time

                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Shutting down servers...")

    except Exception as e:
        logger.error(f"Failed to start servers: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        success = simple_test()
        sys.exit(0 if success else 1)
    else:
        start_servers()
