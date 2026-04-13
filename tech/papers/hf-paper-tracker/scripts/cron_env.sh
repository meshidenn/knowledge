# Sourced by run_daily.sh / run_weekly.sh.
# cron のデフォルト PATH には ~/.local/bin や mise shims が入らないため、
# uv / codex / claude が「コマンドが見つかりません」になるのを防ぐ。
export PATH="${HOME}/.local/bin:${HOME}/.local/share/mise/shims:/usr/local/bin:/usr/bin:/bin${PATH:+:$PATH}"

# Obsidian vault へ生成 md をコピーする際の宛先（上書き可能）
export OBSIDIAN_HF_PAPERS_DAILY="${OBSIDIAN_HF_PAPERS_DAILY:-$HOME/Obsidian/intake/hf-papers/daily}"
export OBSIDIAN_HF_PAPERS_WEEKLY="${OBSIDIAN_HF_PAPERS_WEEKLY:-$HOME/Obsidian/intake/hf-papers/weekly}"
