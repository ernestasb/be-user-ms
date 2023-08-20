"""
Test extensions.py module.
"""

import pytest

from src.errors import CustomException
from src.security import SecurityManager


def test_env_validation(monkeypatch):
    """Test env validation.

    :param monkeypatch: pytest monkeypatch fixture
    :type monkeypatch: MonkeyPatch
    """
    # test env validation
    monkeypatch.setattr("src.security.required_variables", ["KEY"])
    with pytest.raises(SystemExit):
        SecurityManager.validate_env()
