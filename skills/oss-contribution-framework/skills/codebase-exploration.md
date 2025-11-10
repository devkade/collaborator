# Phase 3: Codebase Exploration

Systematically understand project structure, conventions, and architecture.

## Purpose

Build mental model of the codebase to:
- Navigate confidently
- Follow project conventions
- Make informed implementation decisions
- Avoid breaking existing functionality
- Write code that fits naturally

## When to Use

**Triggers:**
- "코드베이스 구조 파악"
- "프로젝트 컨벤션 찾기"
- "이 프로젝트가 어떻게 구성되어 있지?"
- "테스트는 어떻게 작성하나?"

**Use when:**
- First time contributing to project
- Working on unfamiliar part of codebase
- Need to understand conventions
- Before making architectural decisions

## Exploration Framework

### Step 1: Project Overview

Start with high-level understanding.

**Read first:**
1. `README.md` - Project purpose, quick start
2. `CONTRIBUTING.md` - Contribution guidelines, workflow
3. `ARCHITECTURE.md` or `docs/` - System design (if exists)
4. `CHANGELOG.md` - Recent changes, patterns

**Understand:**
- **Purpose:** What problem does this solve?
- **Users:** Who uses this? (devs, end-users, enterprises)
- **Scope:** What's included vs. out of scope
- **Stack:** Core technologies, frameworks, languages

**Template:**
```markdown
### Project Overview

**Purpose:** [1-2 sentence description]

**Target Users:** [developer tool / web app / library / etc]

**Core Technologies:**
- Language: [version]
- Framework: [if applicable]
- Build tool: [npm/cargo/maven/etc]
- Testing: [jest/pytest/etc]

**Key Dependencies:**
- [dependency 1] - [purpose]
- [dependency 2] - [purpose]

**Project Maturity:**
- Age: [years]
- Contributors: [count]
- Stars: [if relevant]
- Stability: [alpha/beta/stable]
```

### Step 2: Directory Structure

Map the project layout and understand organization principles.

**Common patterns:**

**Application structure:**
```
/src or /lib          - Main source code
/tests or /test       - Test files
/docs                 - Documentation
/examples             - Usage examples
/scripts              - Build/utility scripts
/public or /static    - Static assets
/.github              - CI/CD, issue templates
```

**Language-specific:**
```
JavaScript/TypeScript: src/, dist/, node_modules/
Python: package_name/, tests/, setup.py
Rust: src/, target/, Cargo.toml
Go: cmd/, pkg/, internal/
Java: src/main/java/, src/test/java/, pom.xml
```

**Analysis checklist:**

```markdown
### Directory Structure

**Main source:** [path to primary code]

**Key directories:**
- `[dir1]/` - [purpose, what's inside]
- `[dir2]/` - [purpose, what's inside]
- `[dir3]/` - [purpose, what's inside]

**Organization principle:**
- By feature: ✅/❌ (e.g., /users, /products)
- By layer: ✅/❌ (e.g., /models, /views, /controllers)
- By type: ✅/❌ (e.g., /components, /utils, /services)

**Configuration files:**
- Build: [package.json, Cargo.toml, etc]
- Testing: [jest.config.js, pytest.ini, etc]
- Linting: [.eslintrc, .pylintrc, etc]
- CI/CD: [.github/workflows/, .travis.yml, etc]
```

**Exploration commands:**
```bash
# Get overview
tree -L 2 -d

# Count files by type
find . -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn

# Find largest files
find . -type f -exec du -h {} + | sort -rh | head -20

# Locate key files
find . -name "*test*" -type f
find . -name "*config*" -type f
```

### Step 3: Code Conventions

Identify and document project-specific patterns.

#### Naming Conventions

**Observe:**
- File naming: `kebab-case.js`, `PascalCase.tsx`, `snake_case.py`
- Class naming: `PascalCase`, `ClassName`
- Function naming: `camelCase`, `snake_case`, `verb_noun`
- Constants: `UPPER_SNAKE_CASE`, `kConstantName`
- Private members: `_private`, `#private`, `__private`

**Template:**
```markdown
### Naming Conventions

**Files:**
- Components: [e.g., PascalCase.tsx]
- Utilities: [e.g., camelCase.ts]
- Tests: [e.g., file.test.js or file_test.go]

**Code:**
- Classes: [pattern]
- Functions: [pattern]
- Constants: [pattern]
- Variables: [pattern]

**Examples from codebase:**
- Good: [show actual examples]
- Pattern: [explain the rule]
```

#### Code Style

**Check for:**
- Formatting (tabs vs spaces, line length)
- Import order and grouping
- Comment style (JSDoc, docstrings, etc)
- Error handling patterns
- Logging conventions

**Look at:**
```markdown
### Code Style

**Formatting:**
- Config: [.prettierrc, .editorconfig, etc]
- Indentation: [2 spaces / 4 spaces / tabs]
- Line length: [80 / 100 / 120 chars]
- Quotes: [single / double]

**Import Style:**
```javascript
// Example from codebase
import external from 'external-package'
import internal from '@/internal/module'
import relative from './relative'
```

**Comment Style:**
- Documentation: [JSDoc / docstrings / rustdoc]
- Inline: [when and how used]
- TODO format: [TODO: message / TODO(author): message]

**Error Handling:**
- Pattern: [try/catch, Result<T,E>, error codes]
- Custom errors: [how defined]
- Error messages: [format and style]
```

#### Architectural Patterns

**Identify:**
- Design patterns (MVC, Flux, Repository, etc)
- State management (Redux, Context, etc)
- Data flow (unidirectional, bidirectional)
- Module boundaries and dependencies

**Template:**
```markdown
### Architectural Patterns

**Overall Pattern:**
[MVC / MVVM / Layered / Microservices / etc]

**State Management:**
[How application state is managed]

**Data Flow:**
[How data moves through the system]

**Dependency Direction:**
[e.g., UI → Services → Data Layer]

**Key Abstractions:**
- [Abstraction 1]: [purpose, how used]
- [Abstraction 2]: [purpose, how used]
```

### Step 4: Testing Patterns

Understand how to write tests that fit the project.

**Explore:**

```markdown
### Testing Strategy

**Test Location:**
- Unit tests: [e.g., __tests__/, alongside source, tests/]
- Integration tests: [location]
- E2E tests: [location]

**Test Framework:**
- Framework: [Jest / pytest / go test / etc]
- Assertion library: [if separate]
- Mocking: [how mocks are created]

**Test Naming:**
- Pattern: [describe/test, test_, Test*, etc]
- Convention: [should_do_when_condition, test_feature_scenario]

**Test Structure:**
```javascript
// Example from codebase
describe('ComponentName', () => {
  it('should do X when Y', () => {
    // Arrange
    // Act
    // Assert
  })
})
```

**Coverage:**
- Target: [percentage, if specified]
- Tool: [nyc, coverage.py, etc]
- Required: [for all PRs / for new code]

**Running Tests:**
```bash
# Commands from package.json or Makefile
npm test
npm test -- --watch
npm test -- --coverage
```
```

**Find similar tests:**
```bash
# Find tests related to your work
grep -r "describe.*YourFeature" tests/
rg "test.*your_feature"
```

### Step 5: Build & Development Workflow

Learn how to build, run, and verify your changes.

**Essential commands:**

```markdown
### Development Workflow

**Setup:**
```bash
# Installation commands
git clone <repo>
cd <project>
[install dependencies]
[setup environment]
```

**Development:**
```bash
# Run in dev mode
[command to start dev server]

# Build
[command to build]

# Lint
[command to lint]

# Format
[command to format code]
```

**Testing:**
```bash
# Run all tests
[command]

# Run specific test
[command with file/pattern]

# Run with coverage
[command]
```

**Pre-commit:**
- [ ] Tests pass
- [ ] Linting passes
- [ ] Formatting applied
- [ ] [Other checks]

**CI/CD:**
- Pipeline: [GitHub Actions / Travis / CircleCI]
- Checks: [list what CI runs]
- Required: [what must pass for merge]
```

### Step 6: Find Reference Examples

Locate similar code to use as a reference.

**Search strategies:**

**Find similar features:**
```bash
# If adding a new component
find . -name "*Component.tsx" | head -5

# If fixing a bug in authentication
rg "authentication" --type ts

# If adding a new API endpoint
rg "app.post|router.post"
```

**Find similar patterns:**
```markdown
### Reference Examples

**For your issue:** [describe what you're implementing]

**Similar code:**
1. **[File path:line]**
   - What it does: [brief description]
   - Why relevant: [how it relates to your work]
   - Pattern to follow: [specific pattern]

2. **[File path:line]**
   - [same structure]

**Patterns to replicate:**
- [Pattern 1: e.g., how errors are handled]
- [Pattern 2: e.g., how validation is done]
- [Pattern 3: e.g., how tests are structured]

**Patterns to avoid:**
- [Anti-pattern 1: old code, being refactored]
- [Anti-pattern 2: special case, don't generalize]
```

### Step 7: Identify Related Code

Find code that will interact with your changes.

**Questions to answer:**
- What code calls the code I'm changing?
- What does my code call?
- What tests cover this area?
- What breaks if I change this?

**Dependency analysis:**
```markdown
### Impact Analysis

**Direct dependencies:**
- [Function/Module A] uses this
- [Function/Module B] uses this

**Indirect dependencies:**
- [Feature X] depends on the above

**Test coverage:**
- Covered by: [list test files]
- Coverage gaps: [what's not tested]

**Change impact:**
- 🟢 Low risk: [why]
- 🟡 Medium risk: [considerations]
- 🔴 High risk: [major concerns]
```

## Exploration Checklist

Use this checklist to ensure thorough exploration:

```markdown
### Codebase Exploration Checklist

**Documentation:**
- [ ] Read README.md
- [ ] Read CONTRIBUTING.md
- [ ] Review ARCHITECTURE.md (if exists)
- [ ] Check recent CHANGELOG entries

**Structure:**
- [ ] Map directory structure
- [ ] Identify main source location
- [ ] Locate test directory
- [ ] Find configuration files

**Conventions:**
- [ ] Naming patterns identified
- [ ] Code style understood
- [ ] Linting rules checked
- [ ] Format configuration found

**Testing:**
- [ ] Test framework identified
- [ ] Test location pattern understood
- [ ] Example tests reviewed
- [ ] Test commands documented

**Development:**
- [ ] Local setup completed
- [ ] Build process understood
- [ ] Dev server running
- [ ] Tests can run locally

**Context:**
- [ ] Similar code found
- [ ] Reference examples identified
- [ ] Related code mapped
- [ ] Impact assessed
```

## Common Pitfalls

**Avoid:**

❌ **Skipping exploration** - Leads to non-idiomatic code
❌ **Assuming conventions** - Every project is different
❌ **Ignoring existing patterns** - Breaks consistency
❌ **Not running tests locally** - Wastes CI cycles
❌ **Overlooking CONTRIBUTING.md** - Misses important rules
❌ **Copying without understanding** - Propagates bad patterns

## Output Format

Provide structured exploration notes:

```markdown
# 🗺️ Codebase Exploration: [Project Name]

**Repository:** [URL or path]
**Explored:** [date]
**For Issue:** #[number]

---

## Project Summary
[2-3 sentences about what this project does and how it's structured]

---

## Structure
[Directory map and organization principle]

---

## Conventions

### Naming
[Patterns for files, classes, functions]

### Style
[Formatting, imports, comments]

### Architecture
[Key patterns and abstractions]

---

## Testing
[Framework, patterns, location, commands]

---

## Development Workflow
[Setup, build, run, test commands]

---

## Reference Examples

**Similar to my work:**
- [Example 1: path:line - description]
- [Example 2: path:line - description]

**Patterns to follow:**
- [Pattern 1]
- [Pattern 2]

---

## Impact Analysis

**Files I'll likely modify:**
- [file 1] - [reason]
- [file 2] - [reason]

**Dependencies to consider:**
- [dependency 1]
- [dependency 2]

**Risk level:** 🟢 Low / 🟡 Medium / 🔴 High

---

## Notes & Questions

**Observations:**
- [Observation 1]
- [Observation 2]

**Still unclear:**
- [Question 1]
- [Question 2]

---

## Next Steps

✅ Exploration complete - Ready for **Phase 4: Issue-Code Mapping**

**Recommended focus:**
1. [Specific file to examine]
2. [Pattern to understand deeper]
3. [Test to reference]
```

## Integration with Main Framework

When invoked from main framework:

1. **Receive context:** Repository info, issue requirements from Phase 2
2. **Execute exploration:** Systematic codebase analysis
3. **Return structured notes:** Complete understanding of project
4. **Update tracker:** Mark Phase 3 complete
5. **Transition:** Prepare context for Phase 4 (specific file/function locations)

Can be re-invoked for deeper exploration of specific areas as needed during implementation.

## Using the Checklist

Load `references/codebase-checklist.md` for a detailed exploration checklist with more specific items per project type.
