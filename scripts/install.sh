#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${1:-$HOME/.openclaw/workspace/skills}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$TARGET_ROOT/dev" "$TARGET_ROOT/meta"

copy_skill() {
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
  rm -rf "$dst"
  cp -R "$src" "$dst"
  echo "✅ Installed $(basename "$dst") -> $dst"
}

copy_skill "$REPO_ROOT/skills/dev/code-dev-with-gemini" "$TARGET_ROOT/dev/code-dev-with-gemini"
copy_skill "$REPO_ROOT/skills/dev/long-running-agent-harness" "$TARGET_ROOT/dev/long-running-agent-harness"
copy_skill "$REPO_ROOT/skills/dev/anthropic-frontend-design" "$TARGET_ROOT/dev/anthropic-frontend-design"
copy_skill "$REPO_ROOT/skills/meta/skill-creator" "$TARGET_ROOT/meta/skill-creator"

cat > "$TARGET_ROOT/SKILL_MAP.md" <<'MD'
# SKILL_MAP.md

## Layout
- skills/dev
- skills/meta

## Installed Skills
- dev/code-dev-with-gemini
- dev/long-running-agent-harness
- dev/anthropic-frontend-design
- meta/skill-creator
MD

echo "\n🎉 All skills installed with current directory layout."
echo "Target: $TARGET_ROOT"
