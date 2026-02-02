"""
⚙️ CitySpark Configuration
Application settings and environment configuration
"""

import os
from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """Application settings"""

    class Config:
        extra = "ignore"

    # Application
    APP_NAME: str = "CitySpark Complete Platform"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = False
    SECRET_KEY: str = "your-secret-key-here"

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    ALLOWED_HOSTS: List[str] = ["*"]

    # Database
    DATABASE_URL: str = "sqlite:///./cityspark.db"
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_CACHE_TTL: int = 3600

    # AI/ML Models
    AI_MODEL_PATH: str = "./ai_models"
    SENTIMENT_MODEL: str = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    TOPIC_MODEL: str = "facebook/bart-large-mnli"

    # GitHub Integration
    GITHUB_API_TOKEN: Optional[str] = None
    GITHUB_API_URL: str = "https://api.github.com"
    GITHUB_RATE_LIMIT: int = 5000

    # Omniscient Core AI Hub
    AI_HUB_API_URL: Optional[str] = None
    AI_HUB_API_KEY: Optional[str] = None
    AI_HUB_TIMEOUT: int = 30

    # File Storage
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: str = ".jpg,.jpeg,.png,.gif,.pdf,.docx"

    # Email
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USERNAME: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    # Security
    JWT_SECRET_KEY: str = "jwt-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 1440  # 24 hours

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "./cityspark.log"

    # Features
    ENABLE_AI_FEATURES: bool = True
    ENABLE_ART_GENERATION: bool = True
    ENABLE_GITHUB_SCRAPING: bool = True
    ENABLE_OMNISCIENT_HUB: bool = False

    # Performance
    CACHE_ENABLED: bool = True
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 3600

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


# Create global settings instance
settings = Settings()
