from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import current_user, LoginManager

from app.config import BaseConfig

login_manager = LoginManager()
login_manager.session_protection = "strong"


def __key_func():
    if current_user.is_authenticated:
        return f"userid:{current_user.id}"
    else:
        ip_addr = get_remote_address()
        return f"ip:{ip_addr}"


limiter = Limiter(key_func=__key_func)


@limiter.request_filter
def disable_rate_limit():
    return BaseConfig.DISABLE_RATE_LIMIT
