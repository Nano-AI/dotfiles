#!/usr/bin/env python3
"""Symlink the configs in this repo into $HOME. Safe to re-run.

Anything already at a target path (that isn't our link) is moved to
<target>.bak-<timestamp> first, so nothing is overwritten.
"""
import shutil
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
}

# Copied, not linked: Karabiner's root daemon fails to open karabiner.json through a link
# into ~/Documents, which silently disables every remap. After changing it in the GUI:
#   cp ~/.config/karabiner/karabiner.json karabiner/
COPIES = {
    "karabiner/karabiner.json": ".config/karabiner/karabiner.json",
}


def install(src, dst, stamp, copy):
    if copy:
        done = dst.is_file() and dst.read_bytes() == src.read_bytes()
    else:
        done = dst.is_symlink() and dst.resolve() == src
    if done:
        print(f"ok      {dst}")
        return
    if dst.exists() or dst.is_symlink():
        backup = dst.with_name(f"{dst.name}.bak-{stamp}")
        dst.rename(backup)
        print(f"backup  {dst} -> {backup.name}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    if copy:
        shutil.copy2(src, dst)
        print(f"copy    {src} -> {dst}")
    else:
        dst.symlink_to(src)
        print(f"link    {dst} -> {src}")


def main():
    home = Path.home()
    stamp = time.strftime("%Y%m%d%H%M%S")
    for src_rel, dst_rel in LINKS.items():
        install(REPO / src_rel, home / dst_rel, stamp, copy=False)
    for src_rel, dst_rel in COPIES.items():
        install(REPO / src_rel, home / dst_rel, stamp, copy=True)


if __name__ == "__main__":
    main()
