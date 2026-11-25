#!/usr/bin/env python3
"""Preview or install the published configuration files without replacing any."""

import argparse
import os
from pathlib import Path


FILES = ("niri/config.kdl", "alacritty/alacritty.toml")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write missing files")
    args = parser.parse_args()

    source = Path(__file__).resolve().parent / "config"
    root = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config")
    if not root.is_absolute():
        parser.error("XDG_CONFIG_HOME must be an absolute path")

    for name in FILES:
        target = root / name
        if target.parent.is_symlink() or target.is_symlink() or target.exists():
            print(f"keep    {target}")
            continue
        if not args.apply:
            print(f"create  {target}")
            continue
        data = (source / name).read_bytes()
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open("xb") as out:
                out.write(data)
        except FileExistsError:
            print(f"keep    {target}")
        else:
            print(f"wrote   {target}")


if __name__ == "__main__":
    main()
