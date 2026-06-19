from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AgentOS API"
    debug: bool = False
    
    # API Keys for Knowledge Module
    dify_api_key: str = ""
    dify_api_url: str = "https://api.dify.ai/v1"
    
    # NVIDIA APIs
    nvidia_api_key: str = ""
    gemini_api_key: str = ""
    
    # Instagram (Meta Graph API)
    instagram_access_token: str = ""
    instagram_user_id: str = ""
    
    # Threads (Meta Threads API)
    threads_access_token: str = ""
    threads_user_id: str = ""
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
