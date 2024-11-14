"""
This module needs to import all the auth routes so that they can be registered in the app.
Except for the base.py file and other utility files.
"""

from . import application

__all__ = [
    "application",
]
