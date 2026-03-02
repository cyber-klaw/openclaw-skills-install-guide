# OpenClaw Skills Install Guide

This repo documents how to install and organize the current OpenClaw skills setup.

## Prerequisites

- macOS / Linux
- [OpenClaw](https://github.com/openclaw/openclaw)
- `gh` authenticated (`gh auth login`)

## Skill Directory Layout

```bash
~/.openclaw/workspace/skills/
├── dev/
│   ├── code-dev-with-gemini/
│   ├── long-running-agent-harness/
│   └── anthropic-frontend-design/
└── meta/
    └── skill-creator/
```

## Install / Sync Skills

### 1) Clone official skill source (example)

```bash
git clone https://github.com/openclaw/skills
```

### 2) Copy a skill into workspace

```bash
cp -R skills/skills/qrucio/anthropic-frontend-design ~/.openclaw/workspace/skills/dev/
```

### 3) Use skill-creator to create categorized skills

```bash
python3 ~/.openclaw/workspace/skills/meta/skill-creator/scripts/init_skill.py my-new-skill --category dev --skills-root ~/.openclaw/workspace/skills
```

## Agent Reach Runtime Install (separate from skill folder)

```bash
python3.11 -m pip install --user https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
agent-reach doctor
```

## Notes

- Keep custom skills in `~/.openclaw/workspace/skills`.
- Keep a `SKILL_MAP.md` for quick routing and maintenance.
- Runtime tools (like Agent Reach) are installed separately from skill folders.
