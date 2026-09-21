# dotfiles

macOS: AeroSpace, kitty, tmux, Neovim (LazyVim), zsh (oh-my-zsh), Karabiner, git.

```sh
git clone https://github.com/Nano-AI/dotfiles ~/Documents/dotfiles
python3 ~/Documents/dotfiles/install.py   # symlinks into $HOME; existing files -> *.bak-<timestamp>
```

## Keys — hjkl everywhere, one modifier per layer

| Layer | Modifier | Keys |
|---|---|---|
| AeroSpace (windows) | `alt` | `hjkl` focus, `shift+hjkl` move, `f` fullscreen, `1-0`/letters workspace |
| kitty (tabs) | `ctrl+shift` | `h`/`l` prev/next tab, `t` new tab here, `j`/`k` scroll, `/` search scrollback |
| tmux + nvim (panes) | `ctrl` | `hjkl` moves across tmux panes and nvim splits seamlessly |
| tmux | prefix (`ctrl-b`) | `v`/`s` split, `HJKL` resize, `ctrl-l` clear screen, `[` copy mode (`v` select, `y` yank) |

Karabiner swaps Caps Lock and Backspace.
