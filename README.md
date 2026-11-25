# Fedora Niri dotfiles

A portable starting point for my Niri-on-Wayland desktop on Fedora 44 KDE
Edition. This recreates the tiling layout, animation timings, core shortcuts,
and terminal preferences—not the installed app collection or a machine backup.

## Try it

1. Start with a working Niri session. The config was validated with Niri 26.04.
   Alacritty and Fuzzel are used by two shortcuts; use your own terminal and
   launcher if you prefer. Alacritty requests JetBrains Mono.
2. Clone this repo and validate before copying:

   ```sh
   git clone https://github.com/prrhesia/fedora-dotfiles.git
   cd fedora-dotfiles
   niri validate --config config/niri/config.kdl
   python3 install.py
   ```

3. If the preview looks right, run `python3 install.py --apply` as your regular
   user. It writes missing files only. If you already have configs, compare and
   merge them by hand. You can test against an empty config directory using
   `XDG_CONFIG_HOME` without touching your normal settings.

| Shortcut | Action |
| --- | --- |
| `Mod+T` / `Mod+D` | Alacritty / Fuzzel |
| `Mod+H/J/K/L` or arrow keys | Focus neighboring windows or columns |
| `Mod+1`–`Mod+9` | Switch workspace |
| `Mod+O` / `Mod+X` | Overview / close window |
| `Mod+Shift+/` | Show keyboard shortcuts |

Here `Mod` is normally Super in a native Niri session.

## What stays local

- Displays use automatic detection. Monitor placement, app-specific shortcuts,
  and startup commands are not copied.
- For a closer visual match, the source desktop uses the Bibata Modern Classic
  cursor and [Noctalia](https://github.com/noctalia-dev/noctalia-shell). Set those
  up separately if desired. The machine uses a Noctalia-generated Fuzzel theme;
  that generated include is not required or shipped here.
- No private shell customizations, account data, personal files, or system
  inventory. The installer does not install packages or use elevated privileges.

## Why this layout

The [GitHub dotfiles guide](https://dotfiles.github.io/) collects examples of
versioning settings and documenting restore steps. [GNU Stow](https://www.gnu.org/software/stow/manual/html_node/Introduction.html)
uses symlink trees; [chezmoi](https://www.chezmoi.io/why-use-chezmoi/) supports
machine-specific templates and separate secret management. This small setup uses
plain files and a preview-first installer instead. See the
[Niri documentation](https://github.com/YaLTeR/niri/wiki) for further customization.
