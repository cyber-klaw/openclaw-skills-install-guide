# OpenClaw Skills Install Guide

一键安装并同步当前技能目录结构（与你现在一致）：

- `skills/dev/code-dev-with-gemini`
- `skills/dev/long-running-agent-harness`
- `skills/dev/anthropic-frontend-design`
- `skills/meta/skill-creator`

## 一键安装

```bash
git clone https://github.com/cyber-klaw/openclaw-skills-install-guide.git
cd openclaw-skills-install-guide
bash scripts/install.sh
```

默认安装到：`~/.openclaw/workspace/skills`

如需指定目录：

```bash
bash scripts/install.sh /custom/skills/path
```

## 说明

- 安装脚本会覆盖同名技能目录（保证结果一致）。
- 会自动生成/刷新 `SKILL_MAP.md`。
