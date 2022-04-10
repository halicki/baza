import subprocess
import pytest
from mockito import verify
import baza.cli


@pytest.fixture
def mock_subprocess(when):
    when(subprocess).run(...)


class TestCLI:
    def test_cli(self, mock_subprocess):
        baza.cli.main("local")
        verify(subprocess).run(["mongosh", "127.0.0.1"])
