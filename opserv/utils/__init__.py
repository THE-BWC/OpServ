import secrets
import string

from opserv.utils.limiter import limiter, disable_rate_limit
from opserv.utils.sentry_utils import sentry_before_send
from opserv.utils.url import sanitize_next_url, NextUrlSanitizer, encode_url

__all__ = [
    "limiter",
    "disable_rate_limit",
    "sanitize_email",
    "random_string",
    "sentry_before_send",
    "NextUrlSanitizer",
    "sanitize_next_url",
    "encode_url",
]


def sanitize_email(email_address: str, not_lower=False) -> str:
    if email_address:
        email_address = email_address.strip().replace(" ", "").replace("\n", " ")
        if not not_lower:
            email_address = email_address.lower()
    return email_address.replace("\u200f", "")


def random_string(length=10, include_digits=False):
    letters = string.ascii_lowercase
    if include_digits:
        letters += string.digits

    return "".join(secrets.choice(letters) for _ in range(length))
