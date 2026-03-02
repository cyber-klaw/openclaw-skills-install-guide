---
name: long-running-agent-harness
description: Build effective harnesses for long-running AI agents that work across multiple context windows. Use when setting up autonomous coding agents, multi-session projects, or when agents need to maintain progress across discrete sessions. Provides initializer/coding agent patterns, feature tracking, progress logging, and session management best practices based on Anthropic's research.
---

# Long-Running Agent Harness

## Overview

This skill implements Anthropic's proven pattern for long-running agents that work across multiple context windows. It solves the "amnesia problem" where each new session starts fresh with no memory of previous work.

**Core Pattern: Dual-Agent Architecture**
- **Initializer Agent**: First session sets up the environment infrastructure
- **Coding Agent**: Each subsequent session makes incremental progress and leaves clear artifacts

## When to Use This Skill

Use this harness when:
- Building complex projects that span multiple AI sessions
- Setting up autonomous coding agents for long-horizon tasks
- Creating agents that need to maintain state across context window boundaries
- Projects requiring consistent progress tracking and documentation

## Quick Start

### Step 1: Initialize the Project

Prompt the initializer agent to set up the environment:

```
You are the initializer agent. Set up a new project for: [PROJECT_DESCRIPTION]

Create the following infrastructure:
1. features.json - Comprehensive feature list with status tracking
2. init.sh - Script to start development server and environment
3. claude-progress.txt - Progress log file
4. Initial git repository with first commit

See references/initializer-prompt.md for the complete initializer prompt template.
```

### Step 2: Run Coding Sessions

For each subsequent session, use the coding agent pattern:

```
You are a coding agent. Make incremental progress on this project.

STARTUP ROUTINE (run first):
1. Run `pwd` to confirm working directory
2. Read claude-progress.txt for recent context
3. Read features.json to identify next priority
4. Check git log for recent commits
5. Run init.sh to start the environment
6. Test basic functionality before making changes

WORK PATTERN:
- Pick ONE incomplete feature from features.json
- Implement it fully with tests
- Mark it passing ONLY after end-to-end verification
- Write descriptive git commit
- Update claude-progress.txt

See references/coding-agent-prompt.md for the complete prompt.
```

## Core Components

### features.json

Structured feature tracking prevents agents from:
- Attempting to build everything at once (one-shotting)
- Prematurely declaring the project complete
- Skipping proper testing

**Format:**
```json
{
  "features": [
    {
      "id": "feat-001",
      "category": "functional",
      "description": "Clear, testable description",
      "steps": ["Step 1", "Step 2", "Step 3"],
      "passes": false,
      "notes": ""
    }
  ]
}
```

**Rules:**
- Agents may ONLY change the `passes` field
- Mark `passes: true` ONLY after end-to-end testing
- Never delete or modify tests (strongly enforced)

### claude-progress.txt

Session-to-session memory bridge. Each agent writes:
- What was attempted
- What was completed
- Current blockers
- Next recommended steps

**Format:**
```
=== Session 2026-02-28 10:30 ===
Agent: Coding Agent
Worked on: Feature feat-003 (User authentication)
Completed:
- Login form UI
- Password validation
- Session management
Blockers: None
Next: Test with real credentials

=== Session 2026-02-28 11:15 ===
...
```

### init.sh

Environment setup script that ensures every agent can quickly:
- Start the development server
- Install dependencies
- Run basic health checks

**Must include:**
- Error handling (exit on failure)
- Clear status messages
- Port/host information

## Session Workflow

### Initializer Agent Flow

1. **Analyze requirements** - Break down the project goal
2. **Create features.json** - Comprehensive feature list (200+ items for complex projects)
3. **Write init.sh** - Environment startup script
4. **Initialize git** - First commit with all scaffold files
5. **Create progress file** - Initial entry documenting setup

### Coding Agent Flow

Each session follows this exact sequence:

```
1. GET BEARINGS
   ├── pwd (confirm directory)
   ├── cat claude-progress.txt (recent context)
   ├── cat features.json (find next feature)
   └── git log --oneline -20 (recent commits)

2. START ENVIRONMENT
   ├── ./init.sh (start servers)
   └── Basic smoke test (is it working?)

3. WORK ON ONE FEATURE
   ├── Pick highest-priority incomplete feature
   ├── Implement with tests
   └── End-to-end verification

4. CLEAN UP
   ├── Fix any broken functionality
   ├── Update features.json (mark passing)
   ├── git commit -m "descriptive message"
   └── Update claude-progress.txt
```

## Common Failure Modes & Solutions

| Problem | Solution |
|---------|----------|
| Agent declares victory too early | Comprehensive features.json; force reading before starting work |
| Environment left with bugs | Startup routine always tests basic functionality first |
| Features marked done prematurely | Mandate end-to-end testing; only mark passing after verification |
| Time wasted figuring out how to run | init.sh script; read it at session start |
| Lost context between sessions | git history + claude-progress.txt as source of truth |

## Testing Requirements

Agents must verify features using the same methods a human would:

**Web Apps:**
- Browser automation (Puppeteer/playwright)
- Screenshots at key steps
- End-to-end user flows

**APIs:**
- curl/HTTP client tests
- Integration tests
- Error case handling

**CLI Tools:**
- Actual command execution
- Output verification
- Exit code checking

## Resources

### Prompt Templates

- `references/initializer-prompt.md` - Complete initializer agent prompt
- `references/coding-agent-prompt.md` - Complete coding agent prompt

### Example Files

- `assets/features-template.json` - Starter features.json template
- `assets/progress-template.txt` - Progress log template
- `assets/init-template.sh` - init.sh template

### Scripts

- `scripts/validate_features.py` - Validate features.json format
- `scripts/check_progress.py` - Analyze progress and suggest next steps

## Best Practices

1. **JSON over Markdown**: Use JSON for features.json - agents are less likely to accidentally corrupt it
2. **One feature at a time**: Resist the urge to batch multiple features
3. **Test before and after**: Always verify the baseline works before adding new code
4. **Descriptive commits**: Future agents (and humans) need to understand changes
5. **Leave it clean**: Each session ends with working, documented, committed code
6. **Progressive disclosure**: Don't overload new agents - they read only what they need

## Advanced: Multi-Agent Variations

For complex projects, consider specialized agents:
- **Testing Agent**: Dedicated to verification and bug discovery
- **Refactoring Agent**: Code cleanup and architecture improvements
- **Documentation Agent**: Keeping docs in sync with code

See `references/multi-agent-patterns.md` for implementation guidance.

## Reference Implementation

See the Anthropic quickstart for a working example:
https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding
