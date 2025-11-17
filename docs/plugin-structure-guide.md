# Claude Code Plugin 구조 가이드

이 문서는 Claude Code에서 사용할 수 있는 플러그인을 제작할 때 참고할 수 있는 구조 가이드입니다.

## 목차

1. [개요](#개요)
2. [기본 구조](#기본-구조)
3. [Marketplace 설정](#marketplace-설정)
4. [Plugin 조직화 전략](#plugin-조직화-전략)
5. [Sub-Skills와 Commands](#sub-skills와-commands)
6. [실제 예시](#실제-예시)
7. [베스트 프랙티스](#베스트-프랙티스)

---

## 개요

### 핵심 원칙

**하나의 플러그인 = 하나의 완전한 기능 세트**

- Marketplace에는 최상위 플러그인만 노출
- 하위 기능들(sub-skills, commands)은 플러그인 내부에 포함
- 사용자는 하나의 플러그인을 설치하면 모든 관련 기능 사용 가능

### 플러그인 vs Sub-Skills

| 구분 | Marketplace 노출 | 독립 설치 | 용도 |
|------|-----------------|----------|------|
| **Plugin** | ✅ Yes | ✅ Yes | 완전한 기능 세트 |
| **Sub-Skill** | ❌ No | ❌ No | 플러그인 내부 모듈 |
| **Command** | ❌ No | ❌ No | 플러그인 기능 실행 |

---

## 기본 구조

### 디렉토리 레이아웃

```
repository-root/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace 설정 (최상위 플러그인만 등록)
├── skills/
│   ├── plugin-name-1/            # 첫 번째 플러그인
│   │   ├── SKILL.md              # 메인 스킬 문서
│   │   ├── .claude/
│   │   │   └── commands/         # Slash commands
│   │   │       ├── main-command.md
│   │   │       └── sub-command-*.md
│   │   ├── skills/               # Sub-skills (내부 모듈)
│   │   │   ├── feature-1/
│   │   │   │   └── SKILL.md
│   │   │   ├── feature-2/
│   │   │   │   └── SKILL.md
│   │   │   └── feature-3/
│   │   │       └── SKILL.md
│   │   ├── references/           # 참고 문서
│   │   │   ├── guide-1.md
│   │   │   └── guide-2.md
│   │   └── assets/               # 템플릿, 리소스
│   │       └── templates/
│   │           └── template-1.md
│   └── plugin-name-2/            # 두 번째 플러그인
│       └── ...
└── docs/                         # 프로젝트 문서
    └── plugin-structure-guide.md
```

### 핵심 파일 설명

#### 1. `.claude-plugin/marketplace.json`

Marketplace에 표시될 최상위 플러그인만 등록합니다.

```json
{
  "name": "your-marketplace-name",
  "owner": {
    "name": "your-name",
    "url": "https://github.com/your-username"
  },
  "description": "Marketplace description",
  "version": "1.0.0",
  "strict": false,
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./skills/plugin-name",
      "description": "Plugin description",
      "version": "1.0.0"
    }
  ]
}
```

#### 2. `skills/{plugin-name}/SKILL.md`

플러그인의 메인 스킬 문서입니다.

```markdown
---
name: plugin-name
description: Brief description of what this plugin does
---

# Plugin Name

Detailed documentation about the plugin.

## Overview
[Plugin overview and purpose]

## Features
[List of features]

## Usage
[How to use the plugin]

## Sub-Skills
[Description of included sub-skills]
```

#### 3. `skills/{plugin-name}/.claude/commands/`

Slash commands를 저장하는 디렉토리입니다.

```markdown
<!-- command-name.md -->
Use the {skill-name} skill to perform {action}.
```

#### 4. `skills/{plugin-name}/skills/{feature}/SKILL.md`

Sub-skill 문서입니다. Marketplace에는 노출되지 않지만 플러그인 내부에서 사용됩니다.

---

## Marketplace 설정

### ❌ 잘못된 방식 (각 sub-skill을 개별 플러그인으로 등록)

```json
{
  "plugins": [
    {
      "name": "main-framework",
      "source": "./skills/main-framework"
    },
    {
      "name": "sub-feature-1",
      "source": "./skills/main-framework/skills/feature-1"
    },
    {
      "name": "sub-feature-2",
      "source": "./skills/main-framework/skills/feature-2"
    }
  ]
}
```

**문제점:**
- Marketplace가 지저분해짐
- 사용자가 어떤 플러그인을 설치해야 할지 혼란
- 개별 설치 시 의존성 문제 발생 가능

### ✅ 올바른 방식 (최상위 플러그인만 등록)

```json
{
  "plugins": [
    {
      "name": "main-framework",
      "source": "./skills/main-framework"
    }
  ]
}
```

**장점:**
- Marketplace가 깔끔함
- 하나의 플러그인 설치로 모든 기능 사용 가능
- 명확한 의존성 관리

---

## Plugin 조직화 전략

### 단일 기능 플러그인

간단한 기능 하나만 제공하는 플러그인입니다.

```
skills/simple-plugin/
├── SKILL.md
└── .claude/
    └── commands/
        └── simple-command.md
```

**예시:**
- 텍스트 포맷터
- 단순 유틸리티

### 다단계 워크플로우 플러그인

여러 단계로 구성된 복잡한 워크플로우를 제공하는 플러그인입니다.

```
skills/workflow-plugin/
├── SKILL.md                      # 전체 워크플로우 설명
├── .claude/commands/
│   ├── workflow-start.md         # 워크플로우 시작
│   ├── workflow:step-1.md        # 각 단계별 명령
│   ├── workflow:step-2.md
│   └── workflow:step-3.md
├── skills/
│   ├── step-1/SKILL.md          # 각 단계의 상세 가이드
│   ├── step-2/SKILL.md
│   └── step-3/SKILL.md
├── references/
│   └── workflow-guide.md
└── assets/
    └── templates/
        └── output-template.md
```

**예시:**
- OSS contribution framework
- 프로젝트 설정 마법사
- 릴리스 프로세스 자동화

### 도구 모음 플러그인

관련된 여러 독립적인 도구를 제공하는 플러그인입니다.

```
skills/toolkit-plugin/
├── SKILL.md                      # 도구 모음 개요
├── .claude/commands/
│   ├── tool-1.md
│   ├── tool-2.md
│   └── tool-3.md
├── skills/
│   ├── tool-1/SKILL.md
│   ├── tool-2/SKILL.md
│   └── tool-3/SKILL.md
└── references/
    └── toolkit-reference.md
```

**예시:**
- 개발 유틸리티 모음
- 테스트 도구 세트
- 문서 생성 도구

---

## Sub-Skills와 Commands

### Sub-Skills 디자인

Sub-skills는 플러그인의 내부 모듈입니다.

**언제 사용하나요?**
- 큰 기능을 논리적 단위로 분리할 때
- 각 단계가 독립적으로 실행될 수 있을 때
- 재사용 가능한 모듈을 만들 때

**명명 규칙:**
```
skills/{plugin-name}/skills/{feature-name}/SKILL.md
```

**예시:**
```
skills/oss-contribution-framework/skills/
├── issue-discovery/SKILL.md
├── issue-analysis/SKILL.md
└── codebase-exploration/SKILL.md
```

### Commands 디자인

Commands는 플러그인 기능을 실행하는 단축 명령입니다.

**명명 규칙:**
```
{plugin-prefix}:{command-name}
또는
{plugin-name}
```

**예시:**
```bash
/oss-contribution-framework        # 메인 명령
/oss:issue-discovery              # Sub-skill 실행
/oss:issue-analysis
/oss:codebase-exploration
```

**Command 파일 구조:**
```markdown
<!-- .claude/commands/oss:issue-discovery.md -->
Use the oss:issue-discovery skill to find and evaluate suitable issues for OSS contribution.
```

---

## 실제 예시

### OSS Contribution Framework

현재 프로젝트의 `oss-contribution-framework`가 좋은 예시입니다.

#### 구조

```
skills/oss-contribution-framework/
├── SKILL.md                          # 전체 프레임워크 소개
├── .claude/commands/                 # 7개의 명령
│   ├── oss-contribution-framework.md
│   ├── oss:issue-discovery.md
│   ├── oss:issue-analysis.md
│   ├── oss:codebase-exploration.md
│   ├── oss:issue-code-mapping.md
│   ├── oss:solution-implementation.md
│   └── oss:documentation-pr.md
├── skills/                           # 6개의 phase sub-skills
│   ├── issue-discovery/SKILL.md
│   ├── issue-analysis/SKILL.md
│   ├── codebase-exploration/SKILL.md
│   ├── issue-code-mapping/SKILL.md
│   ├── solution-implementation/SKILL.md
│   └── documentation-pr/SKILL.md
├── references/                       # 참고 문서
│   ├── issue-patterns.md
│   ├── codebase-checklist.md
│   ├── pr-templates.md
│   └── contribution-tips.md
└── assets/templates/                 # 템플릿
    ├── issue-analysis-template.md
    ├── codebase-notes-template.md
    └── pr-checklist-template.md
```

#### Marketplace 등록

```json
{
  "plugins": [
    {
      "name": "oss-contribution-framework",
      "source": "./skills/oss-contribution-framework",
      "description": "Systematic 6-phase framework for contributing to open source projects from issue discovery to PR creation",
      "version": "1.0.0"
    }
  ]
}
```

#### 사용 방법

사용자는 `oss-contribution-framework` 하나만 설치하면:
- ✅ 6개의 phase skills 모두 사용 가능
- ✅ 7개의 slash commands 모두 사용 가능
- ✅ 모든 참고 문서와 템플릿 포함

---

## 베스트 프랙티스

### 1. 플러그인 범위 정의

**하나의 플러그인 = 하나의 명확한 목적**

✅ **좋은 예:**
- `oss-contribution-framework` - OSS 기여 전체 프로세스
- `deep-reading-framework` - 문서 읽기 프레임워크

❌ **나쁜 예:**
- `utilities` - 너무 광범위
- `helper` - 목적이 불명확

### 2. Sub-Skills 분리 기준

**다음 경우에 sub-skill로 분리:**
- 독립적으로 실행 가능한 기능
- 재사용될 수 있는 모듈
- 복잡도가 높아 별도 문서가 필요한 경우

**다음 경우에는 분리하지 않음:**
- 단순한 헬퍼 함수
- 플러그인 내부 로직
- 재사용되지 않는 일회성 코드

### 3. 명명 규칙

**플러그인 이름:**
```
{purpose}-{type}
예: oss-contribution-framework, deep-reading-framework
```

**Command 이름:**
```
{plugin-prefix}:{action}
예: oss:issue-discovery, oss:codebase-exploration
```

**Sub-skill 디렉토리:**
```
{feature-name}
예: issue-discovery, codebase-exploration
```

### 4. 문서화

**필수 문서:**
- `SKILL.md` - 플러그인 메인 문서
- `README.md` - 설치 및 사용 가이드 (선택)
- 각 sub-skill의 `SKILL.md`

**권장 문서:**
- `references/` - 참고 자료
- `assets/templates/` - 재사용 가능한 템플릿
- `docs/` - 상세 가이드

### 5. 버전 관리

**시맨틱 버저닝 사용:**
```
MAJOR.MINOR.PATCH
예: 1.0.0, 1.1.0, 2.0.0
```

**버전 업데이트 기준:**
- MAJOR: 하위 호환성 없는 변경
- MINOR: 하위 호환 가능한 기능 추가
- PATCH: 버그 수정

### 6. 테스트와 검증

**플러그인 배포 전 체크리스트:**
- [ ] Marketplace에 올바르게 등록되는가?
- [ ] 모든 commands가 작동하는가?
- [ ] Sub-skills가 독립적으로 실행 가능한가?
- [ ] 문서가 명확하고 완전한가?
- [ ] 예시와 템플릿이 포함되어 있는가?

---

## 참고 자료

### 추가 예시

- **claude-orchestration** - [GitHub](https://github.com/mbruhler/claude-orchestration)
  - 다단계 워크플로우 플러그인의 좋은 예시
  - Skills, commands, agents 조직화 방법 참고

### 관련 문서

- [Plugin Template](./plugin-template/) - 플러그인 템플릿
- Claude Code 공식 문서

---

## 체크리스트

새로운 플러그인을 만들 때 다음 체크리스트를 사용하세요:

### 구조
- [ ] `.claude-plugin/marketplace.json`에 최상위 플러그인만 등록
- [ ] `skills/{plugin-name}/SKILL.md` 생성
- [ ] Sub-skills를 `skills/{plugin-name}/skills/` 안에 조직화
- [ ] Commands를 `skills/{plugin-name}/.claude/commands/` 안에 생성

### 문서
- [ ] SKILL.md에 명확한 설명과 사용 예시 포함
- [ ] 각 sub-skill에 독립적인 문서 작성
- [ ] References와 templates 제공

### 명명
- [ ] 플러그인 이름이 목적을 명확히 표현
- [ ] Command 이름이 일관성 있는 패턴 사용
- [ ] Sub-skill 디렉토리 이름이 명확

### 기능
- [ ] 모든 commands가 올바르게 작동
- [ ] Sub-skills가 독립적으로 실행 가능
- [ ] 플러그인 간 의존성 최소화

### 배포
- [ ] 버전 번호 명시
- [ ] Marketplace description 작성
- [ ] 라이센스 명시 (선택)

---

이 가이드를 따라 플러그인을 제작하면 깔끔하고 유지보수가 쉬운 구조를 만들 수 있습니다.
