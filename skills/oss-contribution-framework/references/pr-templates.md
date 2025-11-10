# PR Templates Reference

Collection of PR templates for various project types and change types.

## Universal PR Template

Use this as a base for any PR:

```markdown
## Description

[Clear description of what this PR does and why]

## Changes Made

- [Change 1]
- [Change 2]
- [Change 3]

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring
- [ ] Performance improvement
- [ ] Test coverage improvement
- [ ] Build/CI improvement
- [ ] Chore/maintenance

## Related Issue

Fixes #[issue-number]

## How to Test

1. [Step 1]
2. [Step 2]
3. [Verify expected behavior]

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published
```

---

## Bug Fix Template

```markdown
## Bug Fix: [Brief Description]

### Problem

[Describe the bug that was fixed]

**Symptoms:**
- [What users experienced]
- [Error messages, if any]

**Root Cause:**
[What was causing the bug]

### Solution

[Explain how the fix addresses the root cause]

### Changes Made

- **Modified:** `path/to/file.ext`
  - [Specific change made]
- **Added:** Test case for regression prevention
- **Updated:** Documentation (if applicable)

### Testing

**Reproduction steps (before fix):**
1. [Step that triggered bug]
2. [Expected: X, Actual: Y]

**Verification steps (after fix):**
1. [Same steps]
2. [Now works correctly]

**Regression test:**
- [ ] Added test that fails without fix
- [ ] Test passes with fix
- [ ] Related tests still pass

### Related Issue

Fixes #[issue-number]

### Checklist

- [ ] Root cause identified and fixed (not just symptoms)
- [ ] Regression test added
- [ ] Similar edge cases considered
- [ ] No new warnings introduced
- [ ] All tests pass locally
- [ ] Documentation updated if behavior changed
```

---

## Feature Addition Template

```markdown
## Feature: [Feature Name]

### Summary

[2-3 sentences: What this feature does and why it's valuable]

### Motivation

**User Need:**
[What problem does this solve?]

**Use Cases:**
1. [Use case 1]
2. [Use case 2]

### Implementation

**Approach:**
[High-level description of implementation approach]

**Key Components:**
- **[Component 1]** - [Purpose]
- **[Component 2]** - [Purpose]

**Design Decisions:**
- [Decision 1]: [Rationale]
- [Decision 2]: [Rationale]

### Changes Made

**Core Implementation:**
- `path/to/new/file.ext` - [What it does]
- `path/to/modified/file.ext` - [Changes made]

**Tests:**
- `path/to/test/file.ext` - [What's tested]

**Documentation:**
- Updated README with usage examples
- Added API documentation
- Updated CHANGELOG

### Usage Example

```[language]
// Example of how to use the new feature
const result = newFeature(input)
```

### API (if applicable)

**New Functions/Methods:**

```[language]
/**
 * [Description]
 * @param {Type} param - [Description]
 * @returns {Type} [Description]
 */
function newFunction(param) {
  // ...
}
```

### Testing

**Test Coverage:**
- [ ] Happy path
- [ ] Edge cases: [list specific ones]
- [ ] Error cases: [list specific ones]
- [ ] Integration with existing features

**Manual Testing:**
1. [How to try the feature]
2. [Expected result]

### Related Issue

Fixes #[issue-number]

### Breaking Changes

[If any, describe them. Otherwise state "None"]

### Future Enhancements

[Optional: Ideas for future improvements that are out of scope for this PR]

### Checklist

- [ ] Feature is complete and working
- [ ] Follows project conventions
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] Examples provided
- [ ] No performance regressions
- [ ] Backwards compatible (or breaking changes documented)
```

---

## Refactoring Template

```markdown
## Refactoring: [What's Being Refactored]

### Motivation

**Current Problems:**
- [Problem 1: e.g., code duplication]
- [Problem 2: e.g., tight coupling]
- [Problem 3: e.g., difficult to test]

**Benefits of Refactoring:**
- [Benefit 1: e.g., improved maintainability]
- [Benefit 2: e.g., better testability]
- [Benefit 3: e.g., clearer separation of concerns]

### Changes Made

**Refactored Files:**
- `path/to/file.ext`
  - Before: [What it was]
  - After: [What it is now]
  - Improvements: [Specific improvements]

### Refactoring Type

- [ ] Extract function/method
- [ ] Extract class/module
- [ ] Rename for clarity
- [ ] Remove duplication
- [ ] Simplify logic
- [ ] Improve structure
- [ ] Update patterns to modern practices

### Behavior Preservation

**Guarantees:**
- [ ] All existing tests pass
- [ ] No functional changes
- [ ] Same inputs produce same outputs
- [ ] No API changes (for libraries)

**Evidence:**
- Test suite: [X/X passing]
- Coverage: [maintained or improved]
- Manual testing: [verified key workflows]

### Code Quality Metrics (optional)

**Before:**
- Lines of code: [number]
- Cyclomatic complexity: [number]
- Duplication: [percentage]

**After:**
- Lines of code: [number]
- Cyclomatic complexity: [number]
- Duplication: [percentage]

### Related Issue

Addresses #[issue-number]

### Checklist

- [ ] No behavior changes
- [ ] All tests pass
- [ ] No new warnings
- [ ] Test coverage maintained or improved
- [ ] Code is more maintainable
- [ ] Follows project conventions
```

---

## Documentation Template

```markdown
## Documentation: [What's Being Documented]

### Summary

[What documentation is being added/updated and why]

### Changes Made

- [ ] Added new documentation
- [ ] Updated existing documentation
- [ ] Fixed errors/typos
- [ ] Added examples
- [ ] Improved clarity
- [ ] Added diagrams/screenshots

**Files Changed:**
- `docs/path/to/file.md` - [What changed]

### Type of Documentation

- [ ] Tutorial (learning-oriented)
- [ ] How-to guide (task-oriented)
- [ ] Reference (information-oriented)
- [ ] Explanation (understanding-oriented)
- [ ] API documentation
- [ ] README update
- [ ] Code comments
- [ ] Changelog entry

### Verification

- [ ] Technically accurate
- [ ] Examples work as shown
- [ ] Links are valid
- [ ] Proper formatting
- [ ] No spelling/grammar errors
- [ ] Appropriate level of detail
- [ ] Clear and understandable

### Screenshots/Examples

[If applicable, show before/after or provide visual examples]

### Related Issue

Fixes #[issue-number]

### Checklist

- [ ] Documentation is accurate
- [ ] Examples are tested
- [ ] No broken links
- [ ] Follows project documentation style
- [ ] Appropriate level of detail for audience
```

---

## Performance Improvement Template

```markdown
## Performance: [What's Being Optimized]

### Problem

**Current Performance:**
- Metric: [e.g., response time, memory usage]
- Measurement: [specific numbers]
- Impact: [who/what is affected]

**Bottleneck:**
[What's causing the performance issue]

### Solution

[Describe optimization approach]

**Why This Approach:**
[Rationale for chosen optimization]

### Changes Made

- `path/to/file.ext` - [Specific optimization]

**Algorithm Change:**
- Before: [O(n²), etc.]
- After: [O(n), etc.]

### Performance Impact

**Benchmarks:**

| Scenario | Before | After | Improvement |
|----------|--------|-------|-------------|
| Small    | 10ms   | 5ms   | 50% faster  |
| Medium   | 100ms  | 20ms  | 80% faster  |
| Large    | 1000ms | 50ms  | 95% faster  |

**Methodology:**
[How benchmarks were measured]

### Tradeoffs

**Pros:**
- [Benefit 1]
- [Benefit 2]

**Cons:**
- [Tradeoff 1: e.g., slightly more memory usage]
- [Tradeoff 2: e.g., increased code complexity]

**Acceptable Because:**
[Why tradeoffs are acceptable]

### Testing

- [ ] Performance benchmarks included
- [ ] Existing tests pass
- [ ] No regressions in other areas
- [ ] Works under various load conditions

### Related Issue

Fixes #[issue-number]

### Checklist

- [ ] Performance improvement verified
- [ ] No correctness regressions
- [ ] Tradeoffs are acceptable
- [ ] Benchmarks included
- [ ] Works under various conditions
```

---

## Breaking Change Template

```markdown
## Breaking Change: [What's Changing]

### ⚠️ Breaking Change Warning

This PR introduces breaking changes. Requires version bump and migration guide.

### What's Breaking

[Clear description of what's changing and what breaks]

**Affected:**
- [API/function/behavior that's changing]
- [Versions affected]
- [Who needs to update]

### Why This Change

[Strong justification for breaking change]

**Problems with Current Approach:**
- [Problem 1]
- [Problem 2]

**Benefits of New Approach:**
- [Benefit 1]
- [Benefit 2]

### Changes Made

**API Changes:**
```[language]
// Before
oldFunction(param1, param2)

// After
newFunction({ param1, param2, newOption })
```

**Behavior Changes:**
- [What behaved differently before]
- [How it behaves now]

### Migration Guide

**For Users on v[X.Y.Z]:**

1. **Update Function Calls**
   ```[language]
   // Old way
   doSomething(a, b)

   // New way
   doSomething({ a, b })
   ```

2. **Update Configuration**
   ```[language]
   // Old config
   { option: value }

   // New config
   { newOption: value }
   ```

3. **Test Your Code**
   [Specific things to test]

**Automated Migration:**
[If migration script provided]
```bash
npm run migrate
```

### Deprecation Period (if applicable)

- [ ] Old API marked as deprecated in v[X.Y.Z]
- [ ] Migration guide published
- [ ] Deprecation warnings added
- [ ] Removal scheduled for v[X.Y.Z]

### Testing

- [ ] New API tested
- [ ] Old behavior removed/deprecated
- [ ] Migration tested
- [ ] Documentation updated

### Related Issue

Implements #[issue-number]

### Checklist

- [ ] Breaking changes clearly documented
- [ ] Migration guide provided
- [ ] Strong justification provided
- [ ] Version bump appropriate (major version)
- [ ] Deprecation period considered
- [ ] Affected users notified (if possible)
```

---

## Small/Trivial Change Template

```markdown
## [Type]: [Brief Description]

### Changes

[One-line description of change]

### Type

- [ ] Typo fix
- [ ] Formatting
- [ ] Comment improvement
- [ ] Dead code removal
- [ ] Dependency update (patch)
- [ ] Config update
- [ ] Other trivial change

### Verification

- [ ] No functional changes
- [ ] Tests still pass (if applicable)

[Optional: If this fixes an issue]
Fixes #[issue-number]
```

---

## Test Addition Template

```markdown
## Tests: [What's Being Tested]

### Motivation

**Coverage Gap:**
[What wasn't covered before]

**Why Now:**
[Why adding these tests]

### Tests Added

**File:** `path/to/test/file.ext`

**Test Cases:**
- [ ] Happy path: [description]
- [ ] Edge case: [specific case]
- [ ] Edge case: [specific case]
- [ ] Error handling: [specific error]

**Coverage Improvement:**
- Before: [X%]
- After: [Y%]
- Increase: [+Z%]

### Testing

- [ ] All new tests pass
- [ ] Existing tests still pass
- [ ] Tests are meaningful (not just for coverage)
- [ ] Tests are maintainable

### Related Issue

Addresses #[issue-number]

### Checklist

- [ ] Tests cover the intended scenarios
- [ ] Tests are clear and readable
- [ ] Tests follow project conventions
- [ ] Coverage improved
```

---

## Security Fix Template

```markdown
## Security Fix: [Brief Description]

### ⚠️ Security Issue

[Describe vulnerability - be cautious about details if not yet disclosed]

**Severity:** [Critical/High/Medium/Low]

**CVSS Score:** [If applicable]

### Vulnerability Details

**Affected Versions:** [version range]

**Attack Vector:** [How it can be exploited]

**Impact:** [What attacker can do]

### Fix

[Describe how the fix addresses the vulnerability]

**Changes:**
- [Specific security improvement]

### Verification

- [ ] Exploit no longer works
- [ ] Security test added
- [ ] Similar code audited
- [ ] No new vulnerabilities introduced

### CVE

[CVE number if assigned, or "Pending" or "N/A"]

### Related Issue

Fixes #[issue-number] (if public)

[Or use private security advisory]

### Checklist

- [ ] Vulnerability fixed
- [ ] Security test added
- [ ] Similar code checked
- [ ] Changelog entry prepared (for after disclosure)
- [ ] Security advisory drafted (if needed)
```

---

## Dependency Update Template

```markdown
## Dependency Update: [Package Name]

### Update Details

**Package:** [package-name]
**From:** v[X.Y.Z]
**To:** v[A.B.C]

**Type:**
- [ ] Patch (bug fixes)
- [ ] Minor (new features, backwards compatible)
- [ ] Major (breaking changes)

### Motivation

- [ ] Security vulnerability fix
- [ ] Bug fixes
- [ ] New features needed
- [ ] Maintenance/housekeeping
- [ ] Performance improvements

**Specific Reason:**
[Why updating now]

### Changes Required

- [ ] No code changes needed
- [ ] Updated usage due to API changes
- [ ] Updated configuration
- [ ] Updated tests
- [ ] Updated documentation

**Code Changes:**
[If any, describe what changed]

### Breaking Changes

[List any breaking changes from changelog]

[How they were addressed]

### Testing

- [ ] All tests pass
- [ ] Manual testing completed
- [ ] No regressions
- [ ] New features work (if using them)

### Changelog Review

**Key changes from dependency:**
- [Change 1]
- [Change 2]

**Full changelog:** [link]

### Related Issue

Addresses #[issue-number]

### Checklist

- [ ] Dependency updated
- [ ] Code adapted to changes (if needed)
- [ ] Tests pass
- [ ] No security vulnerabilities
- [ ] Documentation updated (if needed)
```

---

## Choosing the Right Template

1. **Identify change type** - What kind of change is this?
2. **Select template** - Use the matching template
3. **Adapt to project** - Modify for project-specific requirements
4. **Fill completely** - Don't skip sections
5. **Add context** - Provide all relevant information
6. **Be clear** - Make reviewer's job easy

**Template Priority:**
1. Use project's template if exists
2. Adapt from these templates
3. Look at recent merged PRs for format

**Remember:** The goal is clear communication, not bureaucracy. Adapt templates to fit the situation.
