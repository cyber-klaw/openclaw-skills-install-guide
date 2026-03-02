# SKILL_MAP.md

Routing map for the curated skill set installed by this repository.

## Layout

- `skills/dev/` — engineering and product development skills
- `skills/meta/` — skill authoring and packaging skills

## Skills

### code-dev-with-gemini
- Path: `skills/dev/code-dev-with-gemini`
- Purpose: Code generation and project scaffolding via Gemini CLI
- Trigger hints: `gemini`, `new project`, `component`, `写代码`
- Risk: low-medium (local file edits)

### long-running-agent-harness
- Path: `skills/dev/long-running-agent-harness`
- Purpose: Patterns for long-running/multi-session coding agents
- Trigger hints: `harness`, `multi-session`, `sub-agent`, `长期任务`
- Risk: medium (agent orchestration)

### anthropic-frontend-design
- Path: `skills/dev/anthropic-frontend-design`
- Purpose: Frontend/UI design patterns and stack-specific guidance
- Trigger hints: `frontend design`, `UI`, `UX`, `design system`
- Risk: low (read-heavy references/scripts)

### skill-creator
- Path: `skills/meta/skill-creator`
- Purpose: Create/update/package skills with consistent structure
- Trigger hints: `create skill`, `update skill`, `.skill package`
- Risk: low-medium (local file structure changes)

## Maintenance Rules

1. Keep folder name equal to skill `name`.
2. Keep category directories stable (`dev`, `meta`, optionally `ops/data/comms`).
3. Update this file whenever a skill is added, removed, or renamed.
4. Keep trigger hints concise and practical for routing.
