import os

if os.environ.get("FLASK_ENV") == "development":
    from dotenv import load_dotenv

    load_dotenv()

Socials = [
    {
        "name": "Discord",
        "icon": "discord",
        "color": "#7289DA",
        "tooltip": "Join our Discord server!",
        "url": "https://discord.the-bwc.com",
    },
    {
        "name": "Twitter",
        "icon": "twitter",
        "color": "#1DA1F2",
        "tooltip": "Follow us on Twitter!",
        "url": "https://twitter.com/bwc_gaming",
    },
    {
        "name": "Facebook",
        "icon": "facebook",
        "color": "#1877F2",
        "tooltip": "Like us on Facebook!",
        "url": "https://www.facebook.com/theblackwidowcompany",
    },
    {
        "name": "YouTube",
        "icon": "youtube",
        "color": "#FF0000",
        "tooltip": "Subscribe to our YouTube channel!",
        "url": "https://www.youtube.com/@BlackWidowCompanyBroadcasting",
    },
    {
        "name": "Twitch",
        "icon": "twitch",
        "color": "#6441A5",
        "tooltip": "Follow us on Twitch!",
        "url": "https://www.twitch.tv/blackwidowcompany",
    },
    {
        "name": "Instagram",
        "icon": "instagram",
        "color": "#C13584",
        "tooltip": "Follow us on Instagram!",
        "url": "https://www.instagram.com/theblackwidowcompany",
    },
    {
        "name": "GitHub",
        "icon": "github",
        "color": "#181717",
        "tooltip": "Check out our GitHub!",
        "url": "https://www.github.com/THE-BWC",
    },
]


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


class BaseConfig:
    # Base
    ENVIRONMENT = os.environ.get("FLASK_ENV", "development")
    FLASK_SECRET = os.environ.get("FLASK_SECRET", "my-secret-key")
    URL = os.environ.get("URL", "http://127.0.0.1:5000")
    LANDING_PAGE_URL = os.environ.get("LANDING_PAGE_URL") or "https://the-bwc.com"
    STATUS_PAGE_URL = os.environ.get("STATUS_PAGE_URL") or "https://status.the-bwc.com"
    BRAND_NAME = os.environ.get("BRAND_NAME", "Black Widow Company")
    BRAND_URL = os.environ.get("BRAND_URL", "https://www.the-bwc.com")
    COLOR_LOG = "COLOR_LOG" in os.environ

    # Minio
    MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
    MINIO_SECURE = os.environ.get("MINIO_SECURE", True)
    MINIO_BUCKET = os.environ.get("MINIO_BUCKET")
    MINIO_URL = f"http://{MINIO_ENDPOINT}/{MINIO_BUCKET}"

    # Database
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", 3306)
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
    DB_URI = os.environ.get(
        "DB_URI", f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # domains that can be present in the &next= section when using absolute urls
    ALLOWED_REDIRECT_DOMAINS = []

    # Auth
    DISABLE_REGISTRATION = os.environ.get("DISABLE_REGISTRATION", False)
    SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME", "bwc_opserv")
    DISABLE_RATE_LIMIT = os.environ.get("DISABLE_RATE_LIMIT", False)

    # OAuth2 providers
    OAUTH2_CLIENT_ID = os.environ.get("OAUTH2_CLIENT_ID")
    OAUTH2_CLIENT_SECRET = os.environ.get("OAUTH2_CLIENT_SECRET")
    OAUTH2_METADATA_URL = os.environ.get("OAUTH2_METADATA_URL")
    OAUTH2_SCOPE = os.environ.get("OAUTH2_CLIENT_SCOPE", "openid profile email")

    # Image paths
    IMAGE_PATHS = ImagePaths
    IMAGE_URL = MINIO_URL
    if MINIO_SECURE:
        IMAGE_URL = IMAGE_URL.replace("http", "https")

    # Socials
    SOCIALS = Socials
