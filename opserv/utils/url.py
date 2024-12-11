import urllib.parse
from typing import List, Optional

from opserv.config import BaseConfig


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
