---
name: oss:issue-analysis
description: Phase 2 of OSS contribution - Deep analysis of issue requirements, scope, and expected outcomes. Extracts core requirements, identifies edge cases, maps dependencies, and assesses complexity. Use when starting work on selected issue, clarifying unclear requirements, or identifying edge cases.
---

# Phase 2: Issue Analysis

Deep analysis of issue requirements, scope, and expected outcomes.

## Purpose

Transform an issue description into a clear, actionable understanding of:
- What exactly needs to be done
- Why it's needed
- What success looks like
- What the constraints and edge cases are

## When to Use

**Triggers:**
- "이 이슈 분석해줘"
- "요구사항 정리"
- "이슈 영향 범위 파악"
- "무엇을 구현해야 하는지 명확하게 해줘"

**Use when:**
- Starting work on a selected issue
- Issue description is unclear
- Need to confirm understanding before coding
- Want to identify edge cases early

## Analysis Framework

### Step 1: Issue Type Detection

Identify the type of issue to apply appropriate analysis pattern:

**Bug Fix:**
- Current behavior (broken)
- Expected behavior (correct)
- Reproduction steps
- Root cause (if known)

**Feature Request:**
- User need/problem
- Proposed solution
- Acceptance criteria
- Use cases

**Refactoring:**
- Current code problems
- Desired improvements
- Constraints (maintain behavior)
- Quality metrics

**Documentation:**
- Missing/unclear content
- Target audience
- Required information
- Format/location

**Performance:**
- Current metrics
- Target metrics
- Affected scenarios
- Constraints

**Chore/Maintenance:**
- Technical debt item
- Reason for change
- Scope of work
- Dependencies

### Step 2: Core Requirements Extraction

Parse the issue to extract concrete requirements.

#### For Bug Fixes

**Extract:**
- **Problem:** What is broken?
- **Impact:** Who is affected? How severely?
- **Environment:** What versions, platforms, conditions?
- **Expected outcome:** What should happen instead?
- **Acceptance:** How to verify it's fixed?

**Template:**
```markdown
### Bug Analysis

**Current Behavior:**
[What actually happens - be specific]

**Expected Behavior:**
[What should happen - reference docs/specs if available]

**Reproduction Steps:**
1. [Step 1]
2. [Step 2]
3. [Observe: ...]

**Environment:**
- Version: [version]
- Platform: [OS/browser/etc]
- Configuration: [relevant settings]

**Root Cause (Hypothesis):**
[Your initial theory of what's causing this]

**Affected Users:**
[Who hits this? How often? Severity: Critical/High/Medium/Low]
```

#### For Features

**Extract:**
- **User story:** Who wants this and why?
- **Functionality:** What should it do?
- **Interface:** How do users interact with it?
- **Integration:** How does it fit into existing system?
- **Success metrics:** How to measure success?

**Template:**
```markdown
### Feature Analysis

**User Story:**
As a [user type], I want [capability] so that [benefit].

**Functional Requirements:**
1. [Requirement 1 - must have]
2. [Requirement 2 - must have]
3. [Requirement 3 - nice to have]

**User Interface:**
- **Input:** [What user provides]
- **Output:** [What user sees/gets]
- **Interaction flow:** [Step-by-step user journey]

**Acceptance Criteria:**
- [ ] [Criterion 1 - specific and testable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Non-Functional Requirements:**
- Performance: [any constraints]
- Compatibility: [versions, platforms]
- Accessibility: [considerations]
```

#### For Refactoring

**Extract:**
- **Current problems:** Code smells, tech debt
- **Desired state:** What good looks like
- **Constraints:** Must not break functionality
- **Scope:** What's in and out of scope

**Template:**
```markdown
### Refactoring Analysis

**Current Problems:**
1. [Problem 1: e.g., duplicated code across X files]
2. [Problem 2: e.g., poor separation of concerns]
3. [Problem 3: e.g., difficult to test]

**Desired Outcome:**
[What the code should look like after refactoring]

**Constraints:**
- [ ] No behavior changes
- [ ] All existing tests must pass
- [ ] No API changes (if library)
- [ ] [Other constraints]

**Refactoring Scope:**
- Files affected: [list]
- Functions/classes to change: [list]
- Out of scope: [what not to touch]
```

### Step 3: Implicit Requirements Discovery

Find the unwritten expectations and edge cases.

**Ask critical questions:**

**Boundary conditions:**
- What happens with empty input?
- What about very large input?
- Maximum/minimum values?
- Null/undefined handling?

**Error scenarios:**
- Network failures?
- Invalid input?
- Permissions issues?
- Resource exhaustion?

**Integration points:**
- How does this interact with existing features?
- What other parts depend on this?
- What breaks if this changes?
- Backwards compatibility needed?

**User experience:**
- Loading states?
- Error messages?
- Accessibility?
- Mobile/responsive?

**Performance:**
- Expected load?
- Response time requirements?
- Memory constraints?
- Scalability concerns?

**Security:**
- Input validation?
- Authorization checks?
- Data sanitization?
- Privacy implications?

**Output format:**
```markdown
### Edge Cases & Implicit Requirements

**Boundary Conditions:**
- [ ] Empty input: [how to handle]
- [ ] Large data: [limits, pagination]
- [ ] Special characters: [escaping, validation]

**Error Handling:**
- [ ] Network failure: [retry logic, user feedback]
- [ ] Invalid input: [validation, error messages]
- [ ] Permissions: [who can do what]

**Integration Concerns:**
- Depends on: [list dependencies]
- Affects: [list affected components]
- Breaking change: Yes ⚠️ / No ✅

**Non-Functional:**
- Performance: [requirements or concerns]
- Security: [validations needed]
- Accessibility: [ARIA, keyboard nav, etc]
```

### Step 4: Scope Definition

Clearly define what's included and excluded.

**Determine scope:**

**Minimal viable solution:**
- Core functionality only
- Essential edge cases
- Basic tests
- Minimal documentation

**Complete solution:**
- Full functionality
- All edge cases
- Comprehensive tests
- Full documentation
- Performance optimization

**Out of scope:**
- Related but separate issues
- Future enhancements
- Unrelated refactoring

**Template:**
```markdown
### Scope Definition

**In Scope (Minimal):**
1. [Must-have item 1]
2. [Must-have item 2]
3. [Must-have item 3]

**In Scope (If Time Permits):**
1. [Nice-to-have item 1]
2. [Nice-to-have item 2]

**Out of Scope:**
1. [Item to defer - with reason]
2. [Item to defer - with reason]

**Dependencies:**
- Blocked by: [list blocking issues]
- Blocks: [list issues waiting on this]

**Estimated Complexity:**
🟢 Simple (< 4 hours)
🟡 Moderate (1-2 days)
🔴 Complex (3+ days)

**Complexity Factors:**
- [Factor 1: e.g., need to learn new API]
- [Factor 2: e.g., touching critical code path]
```

### Step 5: Acceptance Criteria

Define specific, testable conditions for "done".

**Good acceptance criteria are:**
- **Specific:** No ambiguity
- **Testable:** Can verify objectively
- **Complete:** Cover all requirements
- **Achievable:** Within scope

**Format:**
```markdown
### Acceptance Criteria

**Functional:**
- [ ] [Action] results in [observable outcome]
- [ ] [Condition] produces [expected result]
- [ ] [Feature] works with [existing feature]

**Quality:**
- [ ] All new code has tests (coverage > X%)
- [ ] No new linting errors
- [ ] Documentation updated
- [ ] Existing tests pass

**Edge Cases:**
- [ ] [Edge case 1] handled correctly
- [ ] [Edge case 2] shows appropriate error

**Integration:**
- [ ] Works on [platform 1]
- [ ] Compatible with [version X]
- [ ] No breaking changes (or documented)
```

### Step 6: Questions for Maintainer

Identify what's still unclear and needs clarification.

**Prepare questions:**
- Specific, not vague
- Show you've done research
- Offer potential solutions
- Respect maintainer's time

**Question template:**
```markdown
### Questions for Maintainer

Before starting implementation, I'd like to clarify:

1. **[Specific aspect]**
   - Current understanding: [what you think]
   - Question: [what's unclear]
   - Options: [potential approaches A, B, C]
   - Preference: [your recommendation and why]

2. **[Edge case handling]**
   - Scenario: [describe edge case]
   - Question: Should this [A] or [B]?
   - Precedent: [similar handling elsewhere in codebase, if found]

3. **[Technical approach]**
   - Question: Prefer [approach A] or [approach B]?
   - Tradeoffs:
     - A: [pros and cons]
     - B: [pros and cons]
```

## Analysis Patterns by Issue Type

### Bug Analysis Pattern

1. Reproduce the bug locally
2. Identify the failing component
3. Trace the code path
4. Hypothesize root cause
5. Identify fix location
6. Consider side effects

### Feature Analysis Pattern

1. Understand user need
2. Survey existing solutions
3. Design API/interface
4. Map integration points
5. Identify implementation approach
6. Consider extensibility

### Refactoring Analysis Pattern

1. Measure current code quality
2. Identify specific problems
3. Define quality targets
4. Plan incremental steps
5. Identify test strategy
6. Consider risk mitigation

## Common Pitfalls

**Avoid:**

❌ **Assuming requirements** - Always verify understanding
❌ **Scope creep** - Stick to issue scope
❌ **Ignoring edge cases** - They matter!
❌ **Skipping questions** - Ask before coding
❌ **Not checking discussions** - Read all comments
❌ **Over-engineering** - Match project's complexity level

## Output Format

Provide comprehensive analysis:

```markdown
# 📋 Issue Analysis: [Issue Title]

**Issue:** #[number] | **Type:** [bug/feature/refactor/docs]
**URL:** [link]
**Status:** Ready to implement / Needs clarification

---

## Summary
[2-3 sentence summary of what needs to be done and why]

---

## Requirements

### Core Requirements
[Structured extraction based on issue type]

### Edge Cases
[List of edge cases and how to handle them]

### Scope
- **In scope:** [list]
- **Out of scope:** [list]
- **Complexity:** [estimate]

---

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

---

## Implementation Notes

**Affected Components:**
- [Component 1]
- [Component 2]

**Key Considerations:**
- [Consideration 1]
- [Consideration 2]

**Potential Challenges:**
- [Challenge 1: description and mitigation]
- [Challenge 2: description and mitigation]

---

## Open Questions

[If any - questions to ask maintainer]

---

## Next Steps

✅ Analysis complete - Ready for **Phase 3: Codebase Exploration**

**Recommended:** Before coding, explore:
1. [Specific file/component to understand]
2. [Test patterns to learn]
3. [Similar features to reference]
```

## Integration with Main Framework

When invoked from main framework:

1. **Receive context:** Issue URL, type, initial assessment
2. **Execute analysis:** Deep dive into requirements
3. **Return structured breakdown:** Complete understanding
4. **Update tracker:** Mark Phase 2 complete
5. **Transition:** Prepare context for Phase 3 (codebase exploration targets)

Can be re-invoked if requirements change or new information emerges.

## Using the Template

Load `assets/templates/issue-analysis-template.md` for a blank template to fill in during analysis.
