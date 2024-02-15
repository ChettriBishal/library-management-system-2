from src.models.database import USER_DB
from src.helpers.initialisation import init_all
from unittest.mock import patch
import pytest

import pytest

from src.models.database import USER_DB


@pytest.fixture(scope="session")
def change_db(monkeypatch):
    monkeypatch.setattr(USER_DB, "DB_PATH", "test.db")



