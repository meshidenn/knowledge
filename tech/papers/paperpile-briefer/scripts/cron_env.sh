#!/bin/bash

# cron/systemdから起動してもローカルのCLIを見つけやすくする。
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$HOME/.rye/shims:$HOME/.mise/shims:/opt/homebrew/bin:/usr/local/bin:$PATH"
