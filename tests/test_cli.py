import subprocess
import sys

from scanpath import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "scanpath", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
