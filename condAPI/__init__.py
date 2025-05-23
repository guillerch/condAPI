# __init__.py

"""
condAPI - A Python library for conditional API handling.
"""

__version__ = "1.0.1"
__author__ = "Guillerch"
__all__ = ["start_service"]

from .__main__ import start_service
from .endpoints import *