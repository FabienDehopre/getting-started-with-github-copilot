import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

# Snapshot of the initial state captured at import time
INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities dict to its initial state after each test."""
    yield
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
