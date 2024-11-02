import secrets
import string
import urllib.parse
from typing import List, Optional

from app.config import BaseConfig


def sanitize_email(email_address: str, not_lower=False) -> str:
    if email_address:
        email_address = email_address.strip().replace(" ", "").replace("\n", " ")
        if not not_lower:
            email_address = email_address.lower()
    return email_address.replace("\u200f", "")


class NextUrlSanitizer:
    @staticmethod
    def sanitize(url: Optional[str], allowed_domains: List[str]) -> Optional[str]:
        if not url:
            return None
        replaced = url.replace("\\", "/")
        result = urllib.parse.urlparse(replaced)
        if result.hostname:
            if result.hostname in allowed_domains:
                return replaced
            else:
                return None
        if result.path and result.path[0] == "/" and not result.path.startswith("//"):
            if result.query:
                return f"{result.path}?{result.query}"
            return result.path

        return None


def sanitize_next_url(url: Optional[str]) -> Optional[str]:
    return NextUrlSanitizer.sanitize(url, BaseConfig.ALLOWED_REDIRECT_DOMAINS)


def encode_url(url: str) -> str:
    return urllib.parse.quote(url, safe="")


def random_string(length=10, include_digits=False):
    letters = string.ascii_lowercase
    if include_digits:
        letters += string.digits

    return "".join(secrets.choice(letters) for _ in range(length))
