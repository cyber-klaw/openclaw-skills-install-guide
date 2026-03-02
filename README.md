# OpenClaw Skills Install Guide

One-command installer and reference repository for a curated OpenClaw skills setup.

This repo is designed to:

- Install a known-good set of skills in one step
- Preserve a consistent directory layout
- Make setup reproducible across machines

## Table of Contents

- [Overview](#overview)
- [Repository Layout](#repository-layout)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Verification](#verification)
- [Upgrade / Reinstall](#upgrade--reinstall)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

The installer deploys the following skills with fixed categories:

- `dev/code-dev-with-gemini`
- `dev/long-running-agent-harness`
- `dev/anthropic-frontend-design`
- `meta/skill-creator`

It writes/refreshes `SKILL_MAP.md` in the target skills root.

## Repository Layout

```text
.
├── skills/
│   ├── dev/
│   │   ├── code-dev-with-gemini/
│   │   ├── long-running-agent-harness/
│   │   └── anthropic-frontend-design/
│   └── meta/
│       └── skill-creator/
└── scripts/
    └── install.sh
```

## Prerequisites

- Git
- Bash (macOS/Linux)
- OpenClaw workspace available (default target: `~/.openclaw/workspace/skills`)

## Quick Start

```bash
git clone https://github.com/cyber-klaw/openclaw-skills-install-guide.git
cd openclaw-skills-install-guide
bash scripts/install.sh
```

## Installation

### Default target

Installs into:

```text
~/.openclaw/workspace/skills
```

Command:

```bash
bash scripts/install.sh
```

### Custom target

```bash
bash scripts/install.sh /path/to/skills
```

## Verification

After installation, verify expected directories exist:

```bash
ls -la ~/.openclaw/workspace/skills/dev
ls -la ~/.openclaw/workspace/skills/meta
```

Expected entries:

- `code-dev-with-gemini`
- `long-running-agent-harness`
- `anthropic-frontend-design`
- `skill-creator`

Also confirm:

```bash
cat ~/.openclaw/workspace/skills/SKILL_MAP.md
```

## Upgrade / Reinstall

Re-run the installer at any time:

```bash
bash scripts/install.sh
```

Behavior:

- Overwrites same-name skill folders in the target path
- Keeps category structure stable (`dev/`, `meta/`)
- Refreshes `SKILL_MAP.md`

## Customization

If you add or remove bundled skills in this repo:

1. Update `scripts/install.sh`
2. Keep `skills/<category>/<skill-name>/` structure consistent
3. Update this README and `SKILL_MAP.md` generation section accordingly

## Troubleshooting

### Permission denied

Use a writable target directory, or adjust permissions:

```bash
mkdir -p ~/.openclaw/workspace/skills
chmod -R u+rw ~/.openclaw/workspace/skills
```

### Skill not appearing in target

- Ensure installer completed without errors
- Re-run with shell tracing:

```bash
bash -x scripts/install.sh
```

### Wrong target path

Pass explicit path:

```bash
bash scripts/install.sh /absolute/path/to/skills
```

## Contributing

PRs are welcome for:

- New curated skills
- Installer robustness improvements
- Better verification tooling
- Documentation improvements

Recommended workflow:

1. Fork this repo
2. Create a feature branch
3. Make changes with tests/verification notes
4. Open a pull request

## License

No license file is currently included.
If you want this repo to be open-source reusable, add a license (MIT/Apache-2.0 recommended).
