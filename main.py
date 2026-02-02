#!/usr/bin/env python3
"""
🚀 CitySpark Complete Project - Main Application
AI-Powered Educational Platform with Urban Art Integration
"""

import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(PROJECT_ROOT / "cityspark.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


def create_app():
    """Create and configure the FastAPI application."""
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        from fastapi.staticfiles import StaticFiles
        from api.routes import router as api_router
        from core.config import settings

        logger.info("🏗️  Creating CitySpark application...")

        # Create FastAPI app
        app = FastAPI(
            title="🚀 CitySpark Complete API",
            description="AI-Powered Educational Platform with Urban Art Integration",
            version="2.0.0",
            docs_url="/docs",
            redoc_url="/redoc",
            openapi_url="/openapi.json",
        )

        # Configure CORS
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_HOSTS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Include API routes
        app.include_router(api_router, prefix="/api")

        # Serve static files
        app.mount("/static", StaticFiles(directory="assets"), name="static")

        # Root endpoint
        @app.get("/")
        async def root():
            return {
                "message": "🚀 Welcome to CitySpark Complete!",
                "version": "2.0.0",
                "description": "AI-Powered Educational Platform with Urban Art Integration",
                "docs": "/docs",
                "features": [
                    "🎓 Personalized Learning",
                    "🎨 Urban Art Gallery",
                    "🤖 AI-Powered Content",
                    "📊 Advanced Analytics",
                    "🔗 GitHub Integration",
                    "💡 LuminScript Tools",
                ],
            }

        logger.info("✅ Application created successfully")
        return app

    except ImportError as e:
        logger.error(f"❌ Missing dependencies: {e}")
        return None
    except Exception as e:
        logger.error(f"❌ Failed to create app: {e}")
        return None


def initialize_components():
    """Initialize all core components."""
    logger.info("🔧 Initializing CitySpark components...")

    components = []

    # Core Learning Engine
    try:
        from core.ai_learning.engine import CitySparkLearningEngine

        learning_engine = CitySparkLearningEngine()
        components.append(("AI Learning Engine", learning_engine))
        logger.info("✅ AI Learning Engine initialized")
    except Exception as e:
        logger.warning(f"⚠️  AI Learning Engine failed: {e}")

    # Urban Art Generator
    try:
        from assets.urban_art.generator import UrbanArtGenerator

        art_generator = UrbanArtGenerator()
        components.append(("Urban Art Generator", art_generator))
        logger.info("✅ Urban Art Generator initialized")
    except Exception as e:
        logger.warning(f"⚠️  Urban Art Generator failed: {e}")

    # GitHub Scraper
    try:
        from integration.github_scraper.scraper import GitHubScraper

        github_scraper = GitHubScraper()
        components.append(("GitHub Scraper", github_scraper))
        logger.info("✅ GitHub Scraper initialized")
    except Exception as e:
        logger.warning(f"⚠️  GitHub Scraper failed: {e}")

    # Omniscient Hub Connector
    try:
        from integration.omniscient_hub.connector import OmniscientHubConnector

        hub_connector = OmniscientHubConnector()
        components.append(("Omniscient Hub Connector", hub_connector))
        logger.info("✅ Omniscient Hub Connector initialized")
    except Exception as e:
        logger.warning(f"⚠️  Omniscient Hub Connector failed: {e}")

    return components


def run_server(app, host="127.0.0.1", port=8000):
    """Run the FastAPI server."""
    try:
        import uvicorn

        logger.info(f"🚀 Starting server on http://{host}:{port}")
        logger.info("📚 API Documentation: http://{}:{}/docs".format(host, port))
        logger.info("🔍 Redoc: http://{}:{}/redoc".format(host, port))
        logger.info("🏠 Home: http://{}:{}".format(host, port))

        uvicorn.run(app, host=host, port=port, reload=True, log_level="info")

    except ImportError:
        logger.error("❌ Uvicorn not installed. Run: pip install uvicorn")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Failed to start server: {e}")
        sys.exit(1)


def run_simple_mode():
    """Run in simple mode without heavy dependencies."""
    logger.info("🔄 Starting in simple mode...")

    try:
        from fastapi import FastAPI
        import uvicorn

        app = FastAPI(title="CitySpark Simple Mode")

        @app.get("/")
        async def root():
            return {
                "message": "🚀 CitySpark Running in Simple Mode",
                "status": "active",
                "features": [
                    "🎓 Educational Platform",
                    "🎨 Urban Art Integration",
                    "🤖 AI-Powered Learning",
                    "📊 Analytics Dashboard",
                ],
            }

        @app.get("/api/health")
        async def health():
            return {
                "status": "healthy",
                "mode": "simple",
                "message": "CitySpark is running successfully",
            }

        uvicorn.run(app, host="127.0.0.1", port=8000)

    except ImportError:
        logger.error(
            "❌ FastAPI not available. Install with: pip install fastapi uvicorn"
        )
        sys.exit(1)


def main():
    """Main entry point."""
    logger.info("🚀 Starting CitySpark Complete Project...")
    logger.info(f"📁 Project directory: {PROJECT_ROOT}")

    try:
        # Try to create full application
        app = create_app()

        if app:
            # Initialize components
            components = initialize_components()
            logger.info(f"✅ {len(components)} components initialized")

            # Run the server
            run_server(app)
        else:
            # Fall back to simple mode
            logger.warning("⚠️  Falling back to simple mode...")
            run_simple_mode()

    except KeyboardInterrupt:
        logger.info("🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        logger.info("🔄 Starting in simple mode...")
        run_simple_mode()


if __name__ == "__main__":
    main()
