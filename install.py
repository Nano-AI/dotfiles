#!/usr/bin/env python3
"""Symlink the configs in this repo into $HOME. Safe to re-run.

Anything already at a target path (that isn't our link) is moved to
<target>.bak-<timestamp> first, so nothing is overwritten.
"""
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent

LINKS = {
    "aerospace/aerospace.toml": ".aerospace.toml",
    "kitty": ".config/kitty",
    "tmux/tmux.conf": ".tmux.conf",
    "nvim": ".config/nvim",
    "zsh/zshrc": ".zshrc",
    "zsh/zprofile": ".zprofile",
    "git/gitconfig": ".gitconfig",
    # Whole dir, not the json: Karabiner replaces the file on save, which would break a file link.
    "karabiner": ".config/karabiner",
}


def main():
    home = Path.home()
    stamp = time.strftime("%Y%m%d%H%M%S")
    for src_rel, dst_rel in LINKS.items():
        src, dst = REPO / src_rel, home / dst_rel
        if dst.is_symlink() and dst.resolve() == src:
            print(f"ok      {dst}")
            continue
        if dst.exists() or dst.is_symlink():
            backup = dst.with_name(f"{dst.name}.bak-{stamp}")
            dst.rename(backup)
            print(f"backup  {dst} -> {backup.name}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.symlink_to(src)
        print(f"link    {dst} -> {src}")


if __name__ == "__main__":
    main()
