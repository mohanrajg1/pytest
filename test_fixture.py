import pytest


@pytest.fixture
def setup_1():
    print("Setup method")
    yield
    print("Cleanup method")


def test_1(setup_1):
    print("Test1")


def test_2(setup_1):
    print("Test2")
