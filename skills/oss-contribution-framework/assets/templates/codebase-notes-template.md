# Codebase Exploration Notes: [Project Name]

**Repository:** [URL or path]
**Explored:** [date]
**For Issue:** #[number]
**Language:** [primary language]

---

## Quick Reference

**Essential Commands:**
```bash
# Install dependencies
[command]

# Run dev server
[command]

# Run tests
[command]

# Lint/format
[command]
```

**Key Directories:**
- Source: `[path]`
- Tests: `[path]`
- Docs: `[path]`

---

## Project Summary

[2-3 sentences about what this project does and how it's structured]

**Purpose:** [What problem does this solve?]

**Target Users:** [Developer tool / Web app / Library / CLI / etc]

**Core Technologies:**
- Language: [language + version]
- Framework: [if applicable]
- Build tool: [tool]
- Testing: [framework]

**Project Maturity:**
- Age: [years or months]
- Activity: [active / moderate / slow]
- Contributors: [approximate count]
- Stability: [alpha / beta / stable / mature]

---

## Directory Structure

```
project-root/
├── [main-source-dir]/     - [purpose]
├── [test-dir]/            - [purpose]
├── [docs-dir]/            - [purpose]
├── [config-files]         - [purpose]
└── [other-key-dirs]/      - [purpose]
```

**Organization Principle:**
- [ ] By feature (users/, products/, orders/)
- [ ] By layer (models/, views/, controllers/)
- [ ] By type (components/, utils/, services/)
- [ ] Hybrid approach

**Notes:**
[Any special organization patterns or unusual directory purposes]

---

## Code Conventions

### Naming Conventions

**Files:**
- Pattern: [kebab-case / PascalCase / snake_case]
- Extensions: [.js, .ts, .tsx, etc]
- Tests: [*.test.js / *_test.go / test_*.py]

**Code Elements:**
- Classes: [PascalCase]
- Functions: [camelCase / snake_case]
- Variables: [camelCase / snake_case]
- Constants: [UPPER_SNAKE_CASE / kConstant]
- Private: [_private / #private / __private]

**Examples from codebase:**
```[language]
// Actual examples from the project
class ExampleClass { }
function exampleFunction() { }
const EXAMPLE_CONSTANT = 'value'
```

### Code Style

**Formatting:**
- Indentation: [2 spaces / 4 spaces / tabs]
- Line length: [80 / 100 / 120 chars]
- Quotes: [single / double]
- Semicolons: [required / optional]

**Imports:**
```[language]
// Import order example from project
import external from 'package'
import internal from '@/internal'
import relative from './relative'
```

**Comments:**
- Documentation: [JSDoc / docstrings / rustdoc / etc]
- Inline: [when and how used]
- TODO format: [TODO: / TODO(name): / FIXME:]

**Error Handling:**
- Pattern: [try/catch / Result<T,E> / error codes]
- Custom errors: [how defined]
- Error messages: [format and style]

### Architectural Patterns

**Overall Pattern:**
[MVC / MVVM / Layered / Component-based / etc]

**State Management:**
[How application state is managed]

**Data Flow:**
[How data moves through the system]

**Dependency Direction:**
[e.g., UI → Services → Data Layer]

**Key Abstractions:**
- [Abstraction 1]: [purpose and how used]
- [Abstraction 2]: [purpose and how used]

---

## Testing

### Test Framework & Location

**Framework:** [Jest / pytest / JUnit / etc]

**Test Locations:**
- Unit tests: [path pattern]
- Integration tests: [path pattern]
- E2E tests: [path pattern]

**Test Naming:**
- Pattern: [describe/it / test_ / Test* / #[test]]
- Convention: [naming style for test descriptions]

### Test Structure

**Typical test pattern:**
```[language]
// Example test structure from the project
describe('FeatureName', () => {
  it('should do X when Y', () => {
    // Arrange
    // Act
    // Assert
  })
})
```

**Common patterns:**
- Setup/teardown: [how handled]
- Fixtures: [location and usage]
- Mocks: [how created]
- Assertions: [library and style]

### Running Tests

```bash
# All tests
[command]

# Specific file
[command]

# With coverage
[command]

# Watch mode
[command]
```

**Coverage:**
- Target: [percentage if specified]
- Tool: [coverage tool used]
- Reports: [where generated]

---

## Development Workflow

### Setup

```bash
# Initial setup
git clone [repo]
cd [project]
[install command]
[setup environment]
```

**Prerequisites:**
- [Tool/version requirement 1]
- [Tool/version requirement 2]

### Development Commands

```bash
# Development mode
[command]

# Build
[command]

# Lint
[command]

# Format
[command]

# Type check (if applicable)
[command]
```

### Git Workflow

**Branch naming:** [pattern: feature/*, fix/*, etc]

**Commit format:**
```
type(scope): description

[longer explanation if needed]
```

**Pre-commit hooks:**
- [What runs automatically]

---

## CI/CD

**CI System:** [GitHub Actions / Travis / CircleCI / etc]

**Configuration:** [.github/workflows/* / .travis.yml / etc]

**CI Checks:**
- [ ] Tests
- [ ] Linting
- [ ] Type checking
- [ ] Build
- [ ] Coverage
- [ ] [Other checks]

**Important:** [Any CI-specific considerations]

---

## Reference Examples

### For My Work

**Similar features/patterns:**

1. **[Feature/Pattern 1]**
   - File: `[path/to/file]:[line]`
   - What it does: [description]
   - Why relevant: [how it relates to my issue]
   - Pattern to follow: [specific pattern]

2. **[Feature/Pattern 2]**
   - File: `[path/to/file]:[line]`
   - What it does: [description]
   - Why relevant: [how it relates]
   - Pattern to follow: [specific pattern]

3. **[Feature/Pattern 3]**
   - File: `[path/to/file]:[line]`
   - What it does: [description]
   - Why relevant: [how it relates]

### Patterns to Replicate

- **[Pattern 1]:** [e.g., how errors are handled]
  - Example: [file:line]
  - Apply to: [my use case]

- **[Pattern 2]:** [e.g., how validation is done]
  - Example: [file:line]
  - Apply to: [my use case]

- **[Pattern 3]:** [e.g., how tests are structured]
  - Example: [file:line]
  - Apply to: [my use case]

### Patterns to Avoid

- **[Anti-pattern 1]:** [old code being refactored]
- **[Anti-pattern 2]:** [special case, don't generalize]

---

## Impact Analysis

### Files I'll Likely Modify

1. **`[path/to/file1]`**
   - Reason: [why this file]
   - Change type: [add / modify / delete]
   - Confidence: [high / medium / low]

2. **`[path/to/file2]`**
   - Reason: [why this file]
   - Change type: [add / modify / delete]
   - Confidence: [high / medium / low]

### Dependencies to Consider

**Upstream (what calls my changes):**
- [Dependency 1]: [description]
- [Dependency 2]: [description]

**Downstream (what my changes call):**
- [Dependency 1]: [description]
- [Dependency 2]: [description]

**Side effects:**
- [ ] File I/O
- [ ] Network calls
- [ ] Database operations
- [ ] State mutations
- [ ] Event emissions

### Risk Level

**Overall risk:** 🟢 Low / 🟡 Medium / 🔴 High

**Risk factors:**
- [Factor 1: e.g., modifying critical path]
- [Factor 2: e.g., poorly tested area]

**Mitigation:**
- [Strategy 1: e.g., add extra tests]
- [Strategy 2: e.g., incremental changes]

---

## Notes & Questions

### Key Observations

- [Observation 1: interesting pattern or consideration]
- [Observation 2: something to remember]
- [Observation 3: potential challenge]

### Still Unclear

- [ ] [Question 1: what still needs investigation]
- [ ] [Question 2: clarification needed]
- [ ] [Question 3: uncertainty]

### Resources

- Documentation: [links to relevant docs]
- Similar issues: [links to related issues/PRs]
- References: [external resources]

---

## Next Steps

✅ Exploration complete - Ready for **Phase 4: Issue-Code Mapping**

**Recommended focus:**
1. [Specific file/component to examine more closely]
2. [Pattern to understand deeper]
3. [Test to review as reference]

**Action items:**
- [ ] [Specific exploration task if needed]
- [ ] [Question to ask maintainer if needed]
- [ ] [Code to trace if needed]

---

## Personal Notes

[Any additional thoughts, reminders, or insights for myself]
