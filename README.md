# dotfiles

macOS: AeroSpace, kitty, tmux, Neovim (LazyVim), zsh (oh-my-zsh), Karabiner, git.

```sh
git clone https://github.com/Nano-AI/dotfiles ~/Documents/dotfiles
python3 ~/Documents/dotfiles/install.py   # symlinks into $HOME; existing files -> *.bak-<timestamp>
```

## Keys — hjkl everywhere, one modifier per layer

| Layer | Modifier | Keys |
|---|---|---|
| AeroSpace (windows) | `alt` | `hjkl` focus, `shift+hjkl` move, `f` fullscreen (`shift+f` macOS fullscreen), `1-0`/letters workspace |
| kitty + nvim (panes) | `cmd` | `hjkl` moves across kitty panes and nvim splits seamlessly |
| kitty (tabs) | `ctrl+shift` | `h`/`l` prev/next tab, `t` new tab here, `j`/`k` scroll, `/` search scrollback |
| tmux + nvim (panes) | `ctrl` | `hjkl` moves across tmux panes and nvim splits seamlessly |
| tmux | prefix (`ctrl-b`) | `v`/`s` split, `HJKL` resize, `ctrl-l` clear screen, `[` copy mode (`v` select, `y` yank) |

Karabiner swaps Caps Lock and Backspace (less finger travel to delete). Its config is **copied**, not
linked: Karabiner's root daemon can't open it through a link into `~/Documents`, which silently turns
every remap off. After changing it in the Karabiner GUI: `cp ~/.config/karabiner/karabiner.json karabiner/`.
