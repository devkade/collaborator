# Codebase Exploration Checklist

Systematic checklist for understanding a new codebase.

## Initial Overview

### Documentation Review
- [ ] Read README.md thoroughly
- [ ] Review CONTRIBUTING.md for guidelines
- [ ] Check ARCHITECTURE.md or design docs
- [ ] Read recent CHANGELOG entries
- [ ] Review LICENSE and any legal requirements
- [ ] Check CODE_OF_CONDUCT.md
- [ ] Read SECURITY.md for vulnerability reporting

### Project Metadata
- [ ] Identify project purpose and scope
- [ ] Understand target users/audience
- [ ] Note primary programming language(s)
- [ ] Check framework/platform used
- [ ] Identify project maturity (alpha/beta/stable)
- [ ] Review release cadence
- [ ] Check activity level (recent commits)

---

## Repository Structure

### Directory Mapping
- [ ] Identify main source directory (src/, lib/, app/)
- [ ] Locate test directory (test/, tests/, __tests__/)
- [ ] Find documentation (docs/, doc/)
- [ ] Identify build output (dist/, build/, target/)
- [ ] Locate configuration files (config/, .config/)
- [ ] Find examples/samples (examples/, samples/)
- [ ] Check for scripts (scripts/, tools/, bin/)

### Organization Pattern
- [ ] Determine organization principle:
  - [ ] By feature (user/, product/, order/)
  - [ ] By layer (models/, views/, controllers/)
  - [ ] By type (components/, utils/, services/)
  - [ ] Hybrid approach
- [ ] Note any special directories
- [ ] Understand separation of concerns
- [ ] Identify public vs internal code

---

## Build System & Dependencies

### Package Management
- [ ] Identify package manager (npm, yarn, pip, cargo, maven)
- [ ] Locate package manifest (package.json, requirements.txt, Cargo.toml)
- [ ] Review dependencies and their purposes
- [ ] Check for peer dependencies
- [ ] Note any unusual or unfamiliar dependencies
- [ ] Check dependency versions and compatibility

### Build Configuration
- [ ] Identify build tool (webpack, vite, rollup, gradle)
- [ ] Locate build configuration files
- [ ] Understand build process
- [ ] Check for multiple build targets (dev, prod)
- [ ] Note output artifacts
- [ ] Identify entry points

### Setup & Installation
- [ ] Follow setup instructions in README
- [ ] Install dependencies successfully
- [ ] Verify development environment works
- [ ] Run development server/app
- [ ] Check for environment variable requirements
- [ ] Note any platform-specific setup

---

## Code Conventions

### Naming Conventions
- [ ] File naming pattern:
  - [ ] kebab-case, PascalCase, snake_case, camelCase
  - [ ] Extensions used (.ts, .tsx, .js, .jsx, .py, .rs)
- [ ] Directory naming pattern
- [ ] Component/class naming (PascalCase, etc)
- [ ] Function/method naming (camelCase, snake_case)
- [ ] Variable naming (camelCase, snake_case)
- [ ] Constant naming (UPPER_SNAKE_CASE, kConstant)
- [ ] Private member naming (_private, #private, __private)
- [ ] Boolean naming (isX, hasY, shouldZ)

### Code Style
- [ ] Indentation (tabs vs spaces, size)
- [ ] Line length limit
- [ ] Quote style (single, double)
- [ ] Semicolon usage
- [ ] Brace style (same line, new line)
- [ ] Import organization and ordering
- [ ] Blank line conventions
- [ ] Trailing comma usage

### Formatting Tools
- [ ] Check for .editorconfig
- [ ] Look for .prettierrc or prettier.config.js
- [ ] Check for .eslintrc or eslint.config.js
- [ ] Find other linter configs (.pylintrc, rustfmt.toml)
- [ ] Run formatter to see changes
- [ ] Run linter to check compliance

---

## Testing

### Test Framework
- [ ] Identify testing framework (Jest, pytest, JUnit, etc)
- [ ] Locate test configuration
- [ ] Understand test file naming convention
- [ ] Check test location pattern (co-located vs separate)
- [ ] Note test file extensions

### Test Structure
- [ ] Identify test structure pattern:
  - [ ] describe/it (Jest, Mocha)
  - [ ] test_ prefix (pytest)
  - [ ] Test* classes (JUnit)
  - [ ] #[test] attributes (Rust)
- [ ] Check for test helpers/utilities
- [ ] Review fixture patterns
- [ ] Understand mocking approach
- [ ] Note setup/teardown patterns

### Test Commands
- [ ] Run all tests: [command]
- [ ] Run specific test file: [command]
- [ ] Run with coverage: [command]
- [ ] Run in watch mode: [command]
- [ ] Run integration tests: [command]
- [ ] Run e2e tests: [command]

### Test Coverage
- [ ] Check coverage tool (nyc, coverage.py, tarpaulin)
- [ ] Find coverage configuration
- [ ] Identify coverage thresholds
- [ ] Locate coverage reports
- [ ] Check what's excluded from coverage

### Test Patterns
- [ ] Review 3-5 existing tests
- [ ] Identify assertion library/style
- [ ] Understand test data approach
- [ ] Note how mocks are created
- [ ] Check async test patterns
- [ ] Review error/exception testing
- [ ] Understand snapshot testing (if used)

---

## Development Workflow

### Running Locally
- [ ] Start development server: [command]
- [ ] Build for development: [command]
- [ ] Build for production: [command]
- [ ] Watch mode: [command]
- [ ] Clean build: [command]

### Code Quality
- [ ] Lint code: [command]
- [ ] Fix linting issues: [command]
- [ ] Format code: [command]
- [ ] Type check (if applicable): [command]
- [ ] Run pre-commit checks: [command]

### Git Workflow
- [ ] Check branching strategy (git flow, trunk-based)
- [ ] Understand branch naming convention
- [ ] Review commit message format
- [ ] Check for commit hooks (husky, pre-commit)
- [ ] Note PR/merge requirements
- [ ] Understand rebase vs merge policy

---

## CI/CD

### Continuous Integration
- [ ] Identify CI system (GitHub Actions, Travis, CircleCI)
- [ ] Locate CI configuration (.github/workflows/, .travis.yml)
- [ ] Review CI jobs/pipelines
- [ ] Understand what CI checks:
  - [ ] Tests
  - [ ] Linting
  - [ ] Type checking
  - [ ] Build
  - [ ] Coverage
  - [ ] Security scanning
- [ ] Note CI environment differences
- [ ] Check if CI runs on all branches or just some

### Deployment
- [ ] Check deployment process
- [ ] Identify deployment targets (npm, docker, cloud)
- [ ] Review deployment configuration
- [ ] Understand release process
- [ ] Note versioning strategy (semver, calver)

---

## Architecture & Patterns

### Overall Architecture
- [ ] Identify architectural pattern:
  - [ ] MVC/MVP/MVVM
  - [ ] Layered
  - [ ] Clean Architecture
  - [ ] Microservices
  - [ ] Monolithic
  - [ ] Component-based
- [ ] Understand data flow
- [ ] Identify key abstractions
- [ ] Note separation of concerns
- [ ] Check dependency direction

### Design Patterns
- [ ] Identify common design patterns used:
  - [ ] Factory
  - [ ] Strategy
  - [ ] Observer
  - [ ] Decorator
  - [ ] Adapter
  - [ ] Singleton
  - [ ] Repository
  - [ ] Service
- [ ] Note framework-specific patterns
- [ ] Understand composition patterns

### State Management (if applicable)
- [ ] Identify state management approach:
  - [ ] Redux/Zustand/MobX
  - [ ] Context API
  - [ ] Local state
  - [ ] Server state (React Query, SWR)
- [ ] Understand state organization
- [ ] Note where state lives
- [ ] Check for state persistence

### API/Interface Patterns
- [ ] Identify API style (REST, GraphQL, gRPC)
- [ ] Understand error handling pattern
- [ ] Note validation approach
- [ ] Check authentication/authorization pattern
- [ ] Review data serialization

---

## Language/Framework Specifics

### JavaScript/TypeScript
- [ ] Check ES version target
- [ ] Note module system (ESM, CommonJS)
- [ ] Review TypeScript config (if TS)
- [ ] Check for type definitions
- [ ] Note async patterns (Promise, async/await)
- [ ] Review bundler configuration

### Python
- [ ] Check Python version
- [ ] Note import style (absolute vs relative)
- [ ] Review requirements/dependencies
- [ ] Check for virtual environment usage
- [ ] Note async patterns (asyncio, threading)
- [ ] Review packaging configuration (setup.py, pyproject.toml)

### Rust
- [ ] Check Rust edition
- [ ] Review Cargo.toml features
- [ ] Note error handling pattern (Result, panic)
- [ ] Check for unsafe code usage
- [ ] Review trait usage patterns
- [ ] Note lifetime annotation style

### Go
- [ ] Check Go version
- [ ] Review module dependencies (go.mod)
- [ ] Note package organization
- [ ] Check error handling pattern
- [ ] Review interface usage
- [ ] Note concurrency patterns (goroutines, channels)

---

## Finding Similar Code

### Reference Examples
- [ ] Find examples of similar features
- [ ] Locate comparable components
- [ ] Identify similar bug fixes
- [ ] Review similar tests
- [ ] Check similar API endpoints
- [ ] Find analogous utilities

### Search Strategies
```bash
# Find similar files
find . -name "*[similar-name]*"

# Find similar patterns
rg "pattern" --type [lang]

# Find similar classes/functions
rg "class.*Name|function.*Name"

# Find usages
rg "functionName\("

# Find similar tests
rg "test.*similar|describe.*Similar"
```

---

## Code Reading

### Entry Points
- [ ] Identify main entry point (main.js, __main__.py, main.rs)
- [ ] Find route definitions (for web apps)
- [ ] Locate command definitions (for CLI tools)
- [ ] Identify public API (for libraries)
- [ ] Find initialization code

### Core Components
- [ ] Identify 3-5 most important modules
- [ ] Understand their responsibilities
- [ ] Note their relationships
- [ ] Review their interfaces
- [ ] Check their dependencies

### Code Flow
- [ ] Trace a simple user action
- [ ] Follow a typical request path
- [ ] Understand data transformations
- [ ] Note side effects
- [ ] Identify external calls

---

## Documentation

### Inline Documentation
- [ ] Check documentation style (JSDoc, docstrings, rustdoc)
- [ ] Review documentation coverage
- [ ] Note documentation patterns
- [ ] Check for examples in docs
- [ ] Review parameter documentation

### External Documentation
- [ ] Check for API documentation
- [ ] Review user guides
- [ ] Find developer guides
- [ ] Look for architecture diagrams
- [ ] Check for decision records (ADRs)

---

## Security & Performance

### Security Practices
- [ ] Check input validation patterns
- [ ] Review authentication approach
- [ ] Understand authorization checks
- [ ] Note data sanitization
- [ ] Check for security warnings in dependencies
- [ ] Review secrets management

### Performance Considerations
- [ ] Identify performance-critical paths
- [ ] Check for caching strategies
- [ ] Note optimization patterns
- [ ] Review resource management
- [ ] Check for profiling tools

---

## Community & Contribution

### Communication Channels
- [ ] Find discussion forum/Discord/Slack
- [ ] Locate issue tracker
- [ ] Check for mailing list
- [ ] Find meeting notes (if any)
- [ ] Review RFCs or proposals

### Contribution Process
- [ ] Review issue labels and meanings
- [ ] Understand PR template requirements
- [ ] Check review process
- [ ] Note testing requirements
- [ ] Understand merge criteria

---

## Project-Specific Notes

### Custom Conventions
- [ ] Note any unusual patterns
- [ ] Document project-specific terms
- [ ] Record special requirements
- [ ] Note gotchas or common mistakes
- [ ] List helpful resources

### Tool-Specific Setup
- [ ] IDE/editor configuration
- [ ] Debugging setup
- [ ] Testing utilities
- [ ] Code generation tools
- [ ] Development aids

---

## Completion Checklist

Before considering exploration complete:

- [ ] Can navigate the codebase confidently
- [ ] Understand main architecture and patterns
- [ ] Know where to find things
- [ ] Can run, build, and test locally
- [ ] Understand contribution workflow
- [ ] Have found reference examples
- [ ] Know project conventions
- [ ] Can ask informed questions
- [ ] Ready to start implementation

---

## Notes Template

Use this to record your findings:

```markdown
# Codebase Exploration Notes: [Project Name]

**Date:** [date]
**For Issue:** #[number]

## Quick Reference
- Main language: [language]
- Framework: [framework]
- Test command: [command]
- Dev server: [command]

## Structure
[Key directory map]

## Conventions
[Important patterns to follow]

## Similar Code
[Reference examples for my work]

## Questions
[Things still unclear]

## Ready to Code
[Specific files/functions I'll modify]
```
