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
    RELEASE = os.environ.get("RELEASE", "development")

    ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    FLASK_SECRET = os.environ.get("FLASK_SECRET", "my-secret-key")
    URL = os.environ.get("URL", "http://127.0.0.1:5000")
    LANDING_PAGE_URL = os.environ.get("LANDING_PAGE_URL") or "https://the-bwc.com"
    STATUS_PAGE_URL = os.environ.get("STATUS_PAGE_URL") or "https://status.the-bwc.com"
    BRAND_NAME = os.environ.get("BRAND_NAME", "Black Widow Company")
    BRAND_URL = os.environ.get("BRAND_URL", "https://www.the-bwc.com")
    COLOR_LOG = "COLOR_LOG" in os.environ
    SENTRY_DSN = os.environ.get("SENTRY_DSN")

    # Turnstile
    TURNSTILE_SECRET = os.environ.get("TURNSTILE_SECRET")
    TURNSTILE_SITEKEY = os.environ.get("TURNSTILE_SITEKEY")

    # Storage
    STORAGE_TYPE = "s3"
    # Local Storage
    LOCAL_STORAGE_PATH = ""
    # Minio/S3 Storage
    S3_ENDPOINT = os.environ.get("S3_ENDPOINT")
    S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
    S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")
    S3_SECURE = os.environ.get("S3_SECURE", True)
    S3_BUCKET = os.environ.get("S3_BUCKET")
    S3_URL = f"http://{S3_ENDPOINT}/{S3_BUCKET}"

    # Database
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", 3306)
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
    DB_URI = os.environ.get(
        "DB_URI", f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Redis
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
    REDIS_USER = os.environ.get("REDIS_USER")
    REDIS_PASS = os.environ.get("REDIS_PASS")
    if REDIS_USER and REDIS_PASS:
        REDIS_URI = os.environ.get(
            "REDIS_URI", f"redis://{REDIS_USER}:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}"
        )
    else:
        REDIS_URI = os.environ.get("REDIS_URI", f"redis://{REDIS_HOST}:{REDIS_PORT}")

    # domains that can be present in the &next= section when using absolute urls
    ALLOWED_REDIRECT_DOMAINS = []

    # Auth
    DISABLE_REGISTRATION = os.environ.get("DISABLE_REGISTRATION", False)
    SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME", "opserv")
    DISABLE_RATE_LIMIT = os.environ.get("DISABLE_RATE_LIMIT", False)

    # OAuth2 providers
    OAUTH2_CLIENT_ID = os.environ.get("OAUTH2_CLIENT_ID")
    OAUTH2_CLIENT_SECRET = os.environ.get("OAUTH2_CLIENT_SECRET")
    OAUTH2_METADATA_URL = os.environ.get("OAUTH2_METADATA_URL")
    OAUTH2_SCOPE = os.environ.get("OAUTH2_CLIENT_SCOPE", "openid profile email")

    # Image paths
    IMAGE_PATHS = ImagePaths
    IMAGE_URL = S3_URL
    if S3_SECURE:
        IMAGE_URL = IMAGE_URL.replace("http", "https")

    # Socials
    SOCIALS = Socials

    # Email
    POSTFIX_SERVER = os.environ.get("POSTFIX_SERVER")
    POSTFIX_PORT = os.environ.get("POSTFIX_PORT")
    POSTFIX_USER = os.environ.get("POSTFIX_USER")
    POSTFIX_PASS = os.environ.get("POSTFIX_PASS")
    POSTFIX_USE_TLS = os.environ.get("POSTFIX_USE_TLS", True)
    NOREPLY_EMAIL = os.environ.get("NOREPLY_EMAIL")
