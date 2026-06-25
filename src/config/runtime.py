import os

def get_api_url():
    env = os.getenv("APP_ENV", "local")

    if env == "docker":
        return "http://api:8000/api/v1/predict"

    elif env == "hf":
        return None

    else:
        return "http://127.0.0.1:8000/api/v1/predict"