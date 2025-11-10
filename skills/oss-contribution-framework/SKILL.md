---
name: oss-contribution-framework
description: Systematic framework for contributing to open source projects. Guides through issue discovery, analysis, codebase exploration, solution mapping, implementation, and PR creation. Use when starting OSS contributions, analyzing issues, understanding unfamiliar codebases, or creating pull requests. Includes modular sub-skills for each contribution phase.
---

# OSS Contribution Framework

A comprehensive, step-by-step framework for making meaningful open source contributions. This skill orchestrates the entire contribution workflow from finding the right issue to submitting a polished pull request.

## Overview

This framework breaks down OSS contributions into six systematic phases, each with its own dedicated sub-skill. You can use the complete workflow or invoke individual phases as needed.

## Quick Start

**Full workflow:**
```
사용자: "이 프로젝트에 기여하고 싶어" or "OSS 기여 시작"
→ Framework guides through all 6 phases
```

**Individual phase:**
```
사용자: "이슈 분석해줘" or "코드베이스 탐색"
→ Activates specific sub-skill
```

## Six-Phase Workflow

### Phase 1: Issue Discovery & Triage
**Sub-skill:** `skills/issue-discovery.md`

Find and evaluate suitable issues to work on.

**Capabilities:**
- Filter issues by labels, difficulty, project activity
- Assess issue quality and clarity
- Evaluate if issue matches your skills
- Check for duplicate work or stale issues

**Triggers:**
- "좋은 이슈 찾아줘"
- "beginner-friendly 이슈 추천"
- "이 이슈가 적합한지 평가해줘"

### Phase 2: Issue Analysis
**Sub-skill:** `skills/issue-analysis.md`

Deep analysis of requirements, scope, and expected outcomes.

**Capabilities:**
- Extract core requirements and acceptance criteria
- Identify edge cases and implicit expectations
- Map dependencies and affected components
- Assess complexity and time estimate

**Triggers:**
- "이 이슈 분석해줘"
- "요구사항 정리"
- "이슈 영향 범위 파악"

### Phase 3: Codebase Exploration
**Sub-skill:** `skills/codebase-exploration.md`

Understand project structure, conventions, and architecture.

**Capabilities:**
- Map project structure and key directories
- Identify coding conventions and patterns
- Find test patterns and CI/CD setup
- Understand build system and dependencies

**Triggers:**
- "코드베이스 구조 파악"
- "프로젝트 컨벤션 찾기"
- "테스트 패턴 분석"

### Phase 4: Issue-Code Mapping
**Sub-skill:** `skills/issue-code-mapping.md`

Connect issue requirements to specific code locations.

**Capabilities:**
- Locate relevant files and functions
- Trace code paths related to the issue
- Identify modification points
- Map test locations

**Triggers:**
- "이슈와 코드 연결"
- "수정할 파일 찾기"
- "관련 코드 위치 파악"

### Phase 5: Solution Implementation
**Sub-skill:** `skills/solution-implementation.md`

Design and implement the solution following project standards.

**Capabilities:**
- Design solution approach
- Write code following project conventions
- Add/update tests
- Handle edge cases

**Triggers:**
- "솔루션 구현"
- "이슈 해결 시작"
- "테스트 작성"

### Phase 6: Documentation & PR
**Sub-skill:** `skills/documentation-pr.md`

Document changes and create a comprehensive pull request.

**Capabilities:**
- Write clear PR description
- Document code changes
- Create changelog entries
- Prepare for review

**Triggers:**
- "PR 작성"
- "문서화"
- "pull request 준비"

## Workflow Orchestration

The main framework manages state and progress across phases:

### Initial Setup

When user starts contribution workflow:

1. **Detect starting point:**
   - New contribution: Start at Phase 1
   - Have issue URL: Start at Phase 2
   - Already analyzed: Start at Phase 3
   - Ready to implement: Start at Phase 5

2. **Gather context:**
   - Repository URL or local path
   - Issue number/URL (if available)
   - User's familiarity with project
   - Language/framework preferences

3. **Initialize tracker:**
```markdown
## 🎯 Contribution Progress
- [ ] Phase 1: Issue Discovery
- [ ] Phase 2: Issue Analysis
- [ ] Phase 3: Codebase Exploration
- [ ] Phase 4: Issue-Code Mapping
- [ ] Phase 5: Solution Implementation
- [ ] Phase 6: Documentation & PR

**Current Phase:** [PHASE]
**Repository:** [REPO]
**Issue:** [ISSUE_URL]
```

### Phase Transitions

After completing each phase, checkpoint with user:

```
"Phase [N] 완료했습니다.

[SUMMARY OF FINDINGS]

다음 단계:
1. Phase [N+1] 진행 - [DESCRIPTION]
2. 현재 단계 심화 분석
3. 특정 부분 재검토

어떻게 진행할까요?"
```

### Progressive Context

Maintain and carry forward context between phases:

- **Phase 1 → 2:** Issue URL, labels, initial assessment
- **Phase 2 → 3:** Requirements, scope, affected areas
- **Phase 3 → 4:** Project structure, conventions, patterns
- **Phase 4 → 5:** File locations, modification points
- **Phase 5 → 6:** Changes made, tests added

## Sub-Skill Invocation

Each sub-skill can be invoked independently or as part of the workflow.

**Independent usage:**
```
사용자: "이 이슈 분석해줘: https://github.com/..."
→ Directly loads Phase 2 sub-skill
```

**Within workflow:**
```
Framework: "Phase 2를 시작합니다..."
→ Internally loads skills/issue-analysis.md
→ Applies guidance and returns results
→ Updates progress tracker
```

## Adaptive Guidance

The framework adapts based on:

**Project type:**
- **Web app:** Focus on UI/UX, API, state management
- **CLI tool:** Focus on commands, flags, I/O
- **Library:** Focus on API design, backwards compatibility
- **Documentation:** Focus on clarity, examples, accuracy

**Issue type:**
- **Bug:** Root cause analysis, reproduction steps
- **Feature:** Design considerations, API surface
- **Refactor:** Code quality, test coverage maintenance
- **Docs:** Accuracy, completeness, examples

**User experience level:**
- **First contribution:** More guidance, explanations
- **Experienced:** Streamlined, focus on project-specific aspects

## Best Practices

**For optimal results:**

1. **Start early** - Engage framework before coding
2. **Be thorough** - Don't skip phases, especially exploration
3. **Communicate** - Comment on issue before starting work
4. **Test locally** - Verify changes before PR
5. **Follow conventions** - Match project style strictly
6. **Ask questions** - Engage maintainers when unclear

**Quality checklist:**

Before moving to Phase 6 (PR), verify:
- [ ] All requirements addressed
- [ ] Tests pass locally
- [ ] Code follows project conventions
- [ ] No unintended changes
- [ ] Documentation updated
- [ ] Commit messages are clear

## Advanced Features

### Multi-Issue Analysis

Compare and prioritize multiple issues:
```
"이 3개 이슈 중 어떤 걸 먼저 해야 할까?"
→ Analyzes difficulty, impact, learning value
```

### Contribution Strategy

Get personalized contribution roadmap:
```
"이 프로젝트에 장기적으로 기여하고 싶어"
→ Suggests progression path from simple to complex issues
```

### Review Preparation

Prepare for code review:
```
"PR 리뷰 대비"
→ Anticipates reviewer questions and concerns
```

## Reference Materials

Each phase has detailed references:
- `references/issue-patterns.md` - Common issue types and approaches
- `references/codebase-checklist.md` - Systematic exploration guide
- `references/pr-templates.md` - Template library for various projects
- `references/contribution-tips.md` - Project-specific guidelines

## Templates

Standard output templates in `assets/templates/`:
- `issue-analysis-template.md` - Structured issue breakdown
- `codebase-notes-template.md` - Project understanding notes
- `pr-checklist-template.md` - Pre-submission checklist

## Notes

- This framework is language and project-agnostic
- Adapt guidance to specific project conventions
- Always prioritize maintainer preferences
- Focus on sustainable, long-term contributions
- Build understanding, not just code changes

## Progressive Disclosure

1. **Start here** - SKILL.md for overview and workflow
2. **Load sub-skills** - Individual phase guidance as needed
3. **Consult references** - Detailed patterns and checklists
4. **Use templates** - Structured output formats
