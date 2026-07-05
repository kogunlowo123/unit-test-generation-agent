"""Test configuration for Unit Test Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "unit-test-generation-agent", "category": "Software Engineering"}
