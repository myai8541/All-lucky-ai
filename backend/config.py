from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API Configuration
    app_name: str = "All-Lucky-ai"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/all_lucky_ai"
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # API Keys
    runway_ml_api_key: str
    openai_api_key: str
    huggingface_api_key: Optional[str] = None
    
    # JWT
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24
    
    # Video Settings
    default_video_quality: str = "1080p"
    max_video_duration: int = 1800  # 30 minutes
    video_output_path: str = "./output/videos"
    video_temp_path: str = "./temp"
    
    # Processing
    max_concurrent_jobs: int = 2
    job_timeout_minutes: int = 60
    
    # Storage
    storage_path: str = "./storage"
    max_file_size_mb: int = 5000
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
