---
name: oss:issue-code-mapping
description: Phase 4 of OSS contribution - Connect issue requirements to specific code locations and modification points. Locates relevant files and functions, traces code paths, identifies modification points, and plans minimal change set. Use when ready to start implementation or finding where to make changes.
---

# Phase 4: Issue-Code Mapping

Connect issue requirements to specific code locations and modification points.

## Purpose

Bridge the gap between "what needs to be done" and "where to do it" by:
- Locating relevant files and functions
- Tracing execution paths
- Identifying modification points
- Understanding data flow
- Planning minimal change set

## When to Use

**Triggers:**
- "이슈와 코드 연결"
- "수정할 파일 찾기"
- "이 코드가 어디서 실행되지?"
- "어디를 바꿔야 하나?"

**Use when:**
- Ready to start implementation
- Need to find where to make changes
- Want to understand code flow
- Planning modification strategy

## Mapping Framework

### Step 1: Requirement Breakdown

Break issue requirements into concrete code tasks.

**From requirements to code:**

**Example - Feature: "Add export to CSV button"**

Requirements → Code tasks:
- UI: Add button component
- Handler: Create export function
- Data: Format data as CSV
- File: Trigger download
- Tests: Verify export works

**Template:**
```markdown
### Requirement → Code Mapping

**Requirement 1:** [User-facing requirement]
→ Code tasks:
  - [ ] [Specific code task 1]
  - [ ] [Specific code task 2]
  - [ ] [Test task]

**Requirement 2:** [Another requirement]
→ Code tasks:
  - [ ] [Task 1]
  - [ ] [Task 2]

**Non-functional:**
→ Code tasks:
  - [ ] [Performance consideration]
  - [ ] [Error handling]
  - [ ] [Edge case]
```

### Step 2: Entry Point Discovery

Find where the relevant code flow starts.

**For different issue types:**

**UI Feature/Bug:**
- Component that renders the UI
- Event handler that triggers action
- Route that displays the page

```bash
# Find component
rg "ComponentName" --type tsx
rg "class.*ComponentName" --type js

# Find route
rg "route.*path"
rg "/api/endpoint"
```

**API/Backend:**
- Route handler
- Controller method
- API endpoint definition

```bash
# Find endpoint
rg "app\.(get|post|put|delete).*endpoint"
rg "@app.route|@api_view"
rg "router.HandleFunc"
```

**CLI Feature:**
- Command definition
- Argument parser
- Main execution function

```bash
# Find command
rg "subcommand|command.*name"
rg "argparse|cobra|clap"
```

**Library Function:**
- Public API function
- Exported module
- Class method

```bash
# Find exports
rg "export (function|class|const)"
rg "pub fn|pub struct"
rg "__all__.*=|def.*"
```

**Template:**
```markdown
### Entry Points

**Primary entry point:**
- File: `[path/to/file]`
- Function/Component: `[name]`
- Line: [line number]
- Purpose: [what triggers this code]

**Related entry points:**
- `[file:line]` - [description]
- `[file:line]` - [description]

**How to reach:**
[Steps to trigger this code - e.g., click button, call API, run command]
```

### Step 3: Code Path Tracing

Follow the execution from entry point through the system.

**Tracing techniques:**

**Forward tracing (entry → result):**
```
Entry point
  ↓ calls
Function A
  ↓ calls
Function B
  ↓ modifies
Data store
  ↓ triggers
Side effect
```

**Backward tracing (result ← origin):**
```
Problem symptom
  ↑ comes from
Function X
  ↑ called by
Function Y
  ↑ triggered by
User action
```

**Use tools:**
```bash
# Find function calls
rg "functionName\("

# Find function definitions
rg "function functionName|def functionName|fn functionName"

# Find class usage
rg "new ClassName|ClassName\(|ClassName::"

# Find imports
rg "import.*Module|from.*import"
```

**Template:**
```markdown
### Execution Flow

**For [feature/bug]:**

```
1. Entry: [file:line] - [function/component]
   └─> Does: [what it does]

2. Calls: [file:line] - [function]
   └─> Does: [what it does]
   └─> Parameters: [what's passed]

3. Calls: [file:line] - [function]
   └─> Does: [what it does]
   └─> Returns: [what's returned]

4. Result: [final outcome]
```

**Key functions in flow:**
- `[function1]` @ [file:line] - [purpose]
- `[function2]` @ [file:line] - [purpose]
- `[function3]` @ [file:line] - [purpose]

**Data transformations:**
- Input: [shape/type]
- Transform 1: [what changes]
- Transform 2: [what changes]
- Output: [shape/type]
```

### Step 4: Modification Point Identification

Pinpoint exactly where to make changes.

**Change categories:**

**Add new code:**
- New function/method
- New component
- New module/file

**Modify existing:**
- Function logic
- Component behavior
- Data structure

**Remove code:**
- Dead code
- Deprecated feature
- Unnecessary complexity

**Template:**
```markdown
### Modification Points

#### Primary Changes

**1. [file/to/modify.ext]**
- Location: Function `[name]` @ line [num]
- Change type: [Add / Modify / Remove]
- What to change: [specific description]
- Why: [connects to requirement]
- Risk: 🟢 Low / 🟡 Medium / 🔴 High

**2. [another/file.ext]**
- [same structure]

#### Secondary Changes

**[file.ext]**
- Type: [e.g., import new dependency]
- Why: [supports primary change]

#### New Files

**[path/to/new/file.ext]**
- Purpose: [what this file does]
- Contains: [functions/classes/components]
- Based on: [similar file to use as template]

#### Files to Delete

**[file/to/remove.ext]**
- Reason: [why removing]
- Alternatives: [replacement]
```

### Step 5: Dependency Mapping

Identify what depends on what you're changing.

**Questions to answer:**
- What calls the code I'm modifying?
- What does my modified code call?
- What data structures are involved?
- What side effects occur?

**Find dependencies:**

```bash
# Who calls this function?
rg "functionName\("

# What does this function call?
# (Open file and read the function)

# Who uses this variable?
rg "variableName"

# What imports this module?
rg "import.*ModuleName|from.*ModuleName"
```

**Template:**
```markdown
### Dependencies

**Upstream (what calls my changes):**
- `[file:line]` - [caller description]
- `[file:line]` - [caller description]
- **Impact:** [how my change affects them]

**Downstream (what my changes call):**
- `[file:line]` - [dependency description]
- `[file:line]` - [dependency description]
- **Assumption:** [what I assume about these]

**Data dependencies:**
- Reads: [data source, structure]
- Writes: [data destination, structure]
- Shared state: [any shared state involved]

**Side effects:**
- [ ] File I/O
- [ ] Network calls
- [ ] Database operations
- [ ] State mutations
- [ ] Event emissions
- [ ] Logging

**Breaking change risk:**
- Public API change: Yes ⚠️ / No ✅
- Behavior change: Yes ⚠️ / No ✅
- Data format change: Yes ⚠️ / No ✅
```

### Step 6: Test Location Mapping

Find where tests need to be added or modified.

**Test discovery:**

```bash
# Find test files
find . -name "*test*" -name "*.ext"
find . -name "*spec*" -name "*.ext"

# Find tests for specific file
# If file is: src/utils/parser.js
# Look for: src/utils/__tests__/parser.test.js
#        or: tests/utils/test_parser.py
#        or: src/utils/parser_test.go

# Search for existing tests of similar features
rg "describe.*SimilarFeature|test.*similar_feature"
```

**Template:**
```markdown
### Test Mapping

**Existing tests to modify:**
- `[test/file/path]` - [test name]
  - Why modify: [your change affects this]
  - What to update: [specific test cases]

**New tests to add:**

**Unit tests:**
- Location: `[path/to/test/file]`
- Test cases needed:
  - [ ] Happy path: [description]
  - [ ] Edge case: [description]
  - [ ] Error case: [description]
- Reference: [similar test file to use as template]

**Integration tests:**
- Location: `[path]`
- Scenarios:
  - [ ] [Scenario 1]
  - [ ] [Scenario 2]

**E2E tests (if needed):**
- Location: `[path]`
- User flows:
  - [ ] [Flow 1]

**Test commands:**
```bash
# Run affected tests
[command to run specific test file]

# Run all tests
[command to run all tests]
```
```

### Step 7: Change Impact Assessment

Evaluate the scope and risk of your changes.

**Assess:**

```markdown
### Impact Assessment

**Scope:**
- Files modified: [count]
- New files: [count]
- Deleted files: [count]
- Total LOC changed: ~[estimate]

**Blast radius:**
- 🟢 Isolated: Changes don't affect other features
- 🟡 Moderate: Changes might affect related features
- 🔴 Wide: Changes affect core functionality

**Risk factors:**
- [ ] Modifying critical path code
- [ ] Changing data structures
- [ ] Altering public APIs
- [ ] Touching poorly tested code
- [ ] Complex logic changes
- [ ] Performance implications

**Mitigation strategies:**
- [Strategy 1: e.g., add extra tests]
- [Strategy 2: e.g., feature flag]
- [Strategy 3: e.g., gradual rollout]

**Rollback plan:**
- [How to undo changes if issues arise]
```

## Mapping Strategies by Issue Type

### Bug Fix Mapping

**Strategy:**
1. Reproduce bug locally
2. Add failing test that captures bug
3. Debug to find root cause location
4. Identify fix location
5. Verify fix resolves test

**Focus on:**
- Minimal change to fix issue
- Not breaking other functionality
- Handling similar edge cases

### Feature Mapping

**Strategy:**
1. Find where similar features exist
2. Identify integration points
3. Plan where new code goes
4. Map data flow
5. Design component interfaces

**Focus on:**
- Fitting naturally into architecture
- Reusing existing patterns
- Minimizing coupling

### Refactoring Mapping

**Strategy:**
1. Identify all locations of code smell
2. Find all call sites
3. Plan refactoring steps
4. Ensure test coverage
5. Verify behavior preservation

**Focus on:**
- Not changing behavior
- Incremental safe steps
- Test coverage verification

## Code Reading Techniques

**Efficient code exploration:**

**Top-down (start from entry point):**
1. Find entry point
2. Read main logic
3. Follow into called functions
4. Build understanding recursively

**Bottom-up (start from data/core):**
1. Find data structures
2. See who creates them
3. See who consumes them
4. Understand usage patterns

**Meet-in-the-middle:**
1. Start from entry point
2. Start from suspected bug location
3. Trace until paths connect

**Pattern matching:**
1. Find similar working code
2. Understand its structure
3. Apply same pattern to your change

## Common Pitfalls

**Avoid:**

❌ **Not tracing full execution path** - Miss important side effects
❌ **Assuming without verifying** - Code might not work as expected
❌ **Ignoring edge cases** - Where bugs hide
❌ **Overlooking tests** - Will break CI
❌ **Making changes in wrong place** - Symptoms vs root cause
❌ **Too broad changes** - Harder to review, more risk

## Output Format

Provide complete code mapping:

```markdown
# 🎯 Issue-Code Mapping: [Issue Title]

**Issue:** #[number]
**Mapping Date:** [date]

---

## Summary
[2-3 sentences: what code needs to change and where]

---

## Requirements → Code

[Breakdown of requirements to code tasks]

---

## Entry Points

**Primary:** `[file:line]` - [description]

[How to trigger this code]

---

## Execution Flow

```
[Visual flow diagram]
```

**Key functions:**
- [List with descriptions]

---

## Modification Plan

### Files to Modify

**1. [file path]**
- Function: `[name]` @ line [X]
- Change: [specific change]
- Reason: [connects to requirement]
- Risk: [level]

[Repeat for each file]

### New Files

[List any new files needed]

### Dependencies

**Upstream callers:**
[List]

**Downstream calls:**
[List]

**Impact:** [assessment]

---

## Test Plan

**Existing tests affected:**
[List]

**New tests needed:**
[List with locations]

**Test commands:**
```bash
[Commands]
```

---

## Impact Assessment

**Scope:** [isolated / moderate / wide]
**Risk:** 🟢 Low / 🟡 Medium / 🔴 High

**Risk factors:**
- [Factor 1]
- [Factor 2]

**Mitigation:**
- [Strategy 1]
- [Strategy 2]

---

## Implementation Checklist

- [ ] Modification point 1: [file:line]
- [ ] Modification point 2: [file:line]
- [ ] New file: [path]
- [ ] Test: [test file]
- [ ] Test: [test file]
- [ ] Documentation update: [where]

---

## Next Steps

✅ Mapping complete - Ready for **Phase 5: Solution Implementation**

**Recommended order:**
1. [Task 1 - start here because...]
2. [Task 2 - then this because...]
3. [Task 3 - finally this]
```

## Integration with Main Framework

When invoked from main framework:

1. **Receive context:** Issue analysis, codebase structure, requirements
2. **Execute mapping:** Locate specific modification points
3. **Return concrete plan:** Exactly where to change what
4. **Update tracker:** Mark Phase 4 complete
5. **Transition:** Ready for implementation with clear roadmap

Can be re-invoked if new code locations discovered during implementation or if approach needs adjustment.

## Verification Before Implementation

**Before moving to Phase 5, verify:**

- [ ] All requirements have code locations
- [ ] Execution path fully understood
- [ ] Modification points are correct (not symptoms)
- [ ] Dependencies identified
- [ ] Test locations mapped
- [ ] Impact assessed and acceptable
- [ ] Have reference examples
- [ ] Clear implementation order

If any unclear, revisit relevant sections or consult with maintainer.
