import os

if os.environ.get("FLASK_ENV") == "development":
    from dotenv import load_dotenv
    load_dotenv()


class BaseConfig:
    # Base
    ENVIRONMENT = os.environ.get("FLASK_ENV", "development")
    FLASK_SECRET = os.environ.get("FLASK_SECRET", "my-secret-key")
    URL = os.environ.get("URL", "http://127.0.0.1:5000")
    BRAND_NAME = os.environ.get("BRAND_NAME", "Black Widow Company")
    BRAND_URL = os.environ.get("BRAND_URL", "https://www.the-bwc.com")

    # Minio
    MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
    MINIO_SECURE = os.environ.get("MINIO_SECURE", True)
    MINIO_BUCKET = os.environ.get("MINIO_BUCKET")

    # Database
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", 3306)
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
    DB_URI = os.environ.get("DB_URI", f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # OAuth2 providers
    OAUTH2_CLIENT_ID = os.environ.get("OAUTH2_CLIENT_ID")
    OAUTH2_CLIENT_SECRET = os.environ.get("OAUTH2_CLIENT_SECRET")
    OAUTH2_METADATA_URL = os.environ.get("OAUTH2_METADATA_URL")
    OAUTH2_SCOPE = os.environ.get("OAUTH2_CLIENT_SCOPE", "openid profile email")


class ImagePaths:
    BADGES = "badges"
    MEDALS = "medals"
    RIBBONS = "ribbons"
    RANKS = "ranks"
    FORUM = "forum"
    COMMUNITY = "community"
    GAMES = "games"
    ROLES = "roles"
    SQUADS = "squads"
    TASKFORCES = "taskforces"
    UTILITIES = "utilities"
