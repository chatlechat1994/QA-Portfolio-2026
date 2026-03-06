import pytest

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None) # Optional: cleans up the table more