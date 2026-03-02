# Multi-Agent Patterns

For complex projects, you may want to use specialized agents instead of a single coding agent.

## Agent Types

### 1. Feature Agent
Implements new functionality.

**Prompt focus:**
- Select one feature from features.json
- Implement with tests
- Mark as passing
- Document in progress.txt

### 2. Testing Agent
Dedicated to verification and quality.

**Prompt focus:**
- Review features marked as passing
- Verify they actually work
- Add automated tests
- Report bugs to Fix Agent

### 3. Fix Agent
Addresses bugs and broken functionality.

**Prompt focus:**
- Read progress.txt for reported issues
- Fix bugs found by Testing Agent
- Verify fixes with regression tests
- Update features.json if tests change

### 4. Refactor Agent
Improves code quality without changing functionality.

**Prompt focus:**
- Identify technical debt
- Refactor for clarity/performance
- Maintain all existing tests
- Only modify features.json notes, not passes

### 5. Documentation Agent
Keeps docs in sync with code.

**Prompt focus:**
- Read features.json for completed features
- Update README, API docs, comments
- Verify code examples work
- Update architecture diagrams

## Coordination Strategies

### Strategy 1: Sequential Handoff
Each agent runs in sequence, updates progress.txt, hands off to next.

```
Feature Agent → Testing Agent → Fix Agent (if needed) → Documentation Agent
```

### Strategy 2: Parallel with Integration
Multiple agents work on different features, Integration Agent merges.

```
Feature Agent A ─┐
Feature Agent B ─┼→ Integration Agent → Testing Agent
Feature Agent C ─┘
```

### Strategy 3: Review Loop
Feature Agent works, Review Agent checks, cycles until approved.

```
Feature Agent → Review Agent ─→ (approved? → commit) 
                      ↓ (not approved)
                Feature Agent (revise)
```

## Implementation Tips

1. **Clear role definition** - Each agent should have a narrow, specific focus
2. **Shared context** - All agents read the same progress.txt and features.json
3. **Handoff protocol** - Define exactly what "done" means for each agent
4. **Conflict resolution** - Establish priority rules when agents disagree
5. **Integration points** - Schedule regular synchronization sessions

## Example: Web App Team

```
Initializer Agent (once)
    ↓
Feature Agent ──→ Testing Agent
    ↑                  ↓
    └──── Fix Agent ←─┘
           ↓
    Documentation Agent (periodic)
```

Each feature goes through: implement → test → fix → document
