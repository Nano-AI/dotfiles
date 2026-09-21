-- ctrl-h/j/k/l moves across nvim splits and the surrounding kitty or tmux panes as one grid.
-- In kitty, cmd+hjkl is forwarded here as ctrl+hjkl (kitty/kitty.conf); in tmux, see tmux/tmux.conf.
return {
  "mrjones2014/smart-splits.nvim",
  lazy = false, -- must load at startup: it sets the IS_NVIM var kitty uses to forward keys
  opts = {},
  keys = {
    { "<c-h>", function() require("smart-splits").move_cursor_left() end, desc = "Go to Left Split/Pane" },
    { "<c-j>", function() require("smart-splits").move_cursor_down() end, desc = "Go to Lower Split/Pane" },
    { "<c-k>", function() require("smart-splits").move_cursor_up() end, desc = "Go to Upper Split/Pane" },
    { "<c-l>", function() require("smart-splits").move_cursor_right() end, desc = "Go to Right Split/Pane" },
  },
}
