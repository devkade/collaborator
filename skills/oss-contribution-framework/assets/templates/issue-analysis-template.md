# Issue Analysis: [Issue Title]

**Issue:** #[number] | **Type:** [bug/feature/refactor/docs/performance]
**URL:** [GitHub issue link]
**Status:** Ready to implement / Needs clarification
**Date:** [Analysis date]

---

## Summary

[2-3 sentence summary of what needs to be done and why]

---

## Requirements

### Core Requirements

[Based on issue type, fill in relevant section below]

#### For Bug Fixes

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

#### For Features

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

**Non-Functional Requirements:**
- Performance: [any constraints]
- Compatibility: [versions, platforms]
- Accessibility: [considerations]

#### For Refactoring

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

### Edge Cases & Implicit Requirements

**Boundary Conditions:**
- [ ] Empty input: [how to handle]
- [ ] Large data: [limits, pagination]
- [ ] Special characters: [escaping, validation]
- [ ] Null/undefined: [default behavior]

**Error Handling:**
- [ ] Network failure: [retry logic, user feedback]
- [ ] Invalid input: [validation, error messages]
- [ ] Permissions: [who can do what]
- [ ] Resource exhaustion: [limits, throttling]

**Integration Concerns:**
- **Depends on:** [list dependencies]
- **Affects:** [list affected components]
- **Breaking change:** Yes ⚠️ / No ✅
- **Backwards compatibility:** [considerations]

**Non-Functional:**
- **Performance:** [requirements or concerns]
- **Security:** [validations needed]
- **Accessibility:** [ARIA, keyboard nav, etc]
- **Mobile/Responsive:** [considerations]

---

## Scope Definition

### In Scope (Minimal)
1. [Must-have item 1]
2. [Must-have item 2]
3. [Must-have item 3]

### In Scope (If Time Permits)
1. [Nice-to-have item 1]
2. [Nice-to-have item 2]

### Out of Scope
1. [Item to defer - with reason]
2. [Item to defer - with reason]

### Dependencies
- **Blocked by:** [list blocking issues]
- **Blocks:** [list issues waiting on this]

### Estimated Complexity
🟢 Simple (< 4 hours)
🟡 Moderate (1-2 days)
🔴 Complex (3+ days)

**Complexity Factors:**
- [Factor 1: e.g., need to learn new API]
- [Factor 2: e.g., touching critical code path]
- [Factor 3: e.g., requires significant testing]

---

## Acceptance Criteria

### Functional
- [ ] [Action] results in [observable outcome]
- [ ] [Condition] produces [expected result]
- [ ] [Feature] works with [existing feature]
- [ ] [Edge case] handled appropriately

### Quality
- [ ] All new code has tests (coverage > X%)
- [ ] No new linting errors
- [ ] No new type errors
- [ ] Documentation updated
- [ ] Existing tests pass

### Edge Cases
- [ ] [Edge case 1] handled correctly
- [ ] [Edge case 2] shows appropriate error
- [ ] [Edge case 3] returns expected default

### Integration
- [ ] Works on [platform 1]
- [ ] Compatible with [version X]
- [ ] No breaking changes (or documented)
- [ ] Integrates with [related feature]

---

## Implementation Notes

### Affected Components
- [Component 1: description of involvement]
- [Component 2: description of involvement]
- [Component 3: description of involvement]

### Key Considerations
- [Consideration 1: important factor to keep in mind]
- [Consideration 2: architectural constraint]
- [Consideration 3: performance implication]

### Potential Challenges
- **[Challenge 1]:** [description]
  - Mitigation: [how to address]
- **[Challenge 2]:** [description]
  - Mitigation: [how to address]

### Similar Patterns in Codebase
- [Similar feature/pattern 1] @ [file:line]
- [Similar feature/pattern 2] @ [file:line]

---

## Open Questions

[Questions to ask maintainer before implementation]

1. **[Specific aspect]**
   - Current understanding: [what you think]
   - Question: [what's unclear]
   - Options: [potential approaches A, B, C]
   - Preference: [your recommendation and why]

2. **[Edge case handling]**
   - Scenario: [describe edge case]
   - Question: Should this [A] or [B]?
   - Precedent: [similar handling elsewhere, if found]

---

## Next Steps

✅ Analysis complete - Ready for **Phase 3: Codebase Exploration**

**Before coding, explore:**
1. [Specific file/component to understand]
2. [Test patterns to learn]
3. [Similar features to reference]

**Or if clarification needed:**
❓ Post questions to issue thread and wait for maintainer response

---

## Notes

[Any additional context, insights, or considerations]
