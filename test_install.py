"""Run: python3 test_install.py  — exercises install.py against a throwaway $HOME."""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent

with tempfile.TemporaryDirectory() as home:
    home = Path(home)
    (home / ".tmux.conf").write_text("old")  # pre-existing file must be backed up, not lost
    env = {**os.environ, "HOME": str(home)}
    run = lambda: subprocess.run([sys.executable, REPO / "install.py"], env=env, check=True)

    run()
    assert (home / ".tmux.conf").resolve() == REPO / "tmux/tmux.conf"
    assert (home / ".config/nvim").resolve() == REPO / "nvim"
    backups = list(home.glob(".tmux.conf.bak-*"))
    assert len(backups) == 1 and backups[0].read_text() == "old"

    run()  # second run is a no-op
    assert len(list(home.glob("*.bak-*"))) == 1

print("ok")
