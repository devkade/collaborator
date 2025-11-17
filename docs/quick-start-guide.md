# Claude Code Plugin 제작 빠른 시작 가이드

새로운 플러그인을 빠르게 만들기 위한 간단한 가이드입니다.

## 📦 템플릿 사용하기

### 1. 템플릿 복사

```bash
# 새 플러그인 생성
cp -r docs/plugin-template/skills/example-plugin skills/your-plugin-name

# 예: todo-manager 플러그인 생성
cp -r docs/plugin-template/skills/example-plugin skills/todo-manager
```

### 2. 파일 수정

다음 순서로 파일을 수정하세요:

#### ① SKILL.md 수정
```bash
# skills/your-plugin-name/SKILL.md
```

변경할 내용:
- `name:` - 플러그인 이름
- `description:` - 간단한 설명
- 나머지 내용을 플러그인에 맞게 작성

#### ② Commands 수정
```bash
# skills/your-plugin-name/.claude/commands/
```

- 파일 이름을 원하는 command 이름으로 변경
- 각 파일 내용 수정

#### ③ Sub-skills 수정
```bash
# skills/your-plugin-name/skills/
```

- feature 디렉토리 이름 변경
- 필요 없는 feature 삭제
- 새로운 feature 추가
- 각 SKILL.md 작성

#### ④ References & Templates 추가
```bash
# skills/your-plugin-name/references/
# skills/your-plugin-name/assets/templates/
```

### 3. Marketplace 등록

`.claude-plugin/marketplace.json` 파일에 플러그인 추가:

```json
{
  "plugins": [
    {
      "name": "your-plugin-name",
      "source": "./skills/your-plugin-name",
      "description": "플러그인 설명",
      "version": "1.0.0"
    }
  ]
}
```

### 4. 테스트

플러그인이 제대로 작동하는지 확인:

```bash
# Claude Code에서:
# 1. Marketplace에서 플러그인 확인
# 2. Slash command 실행 테스트
# 3. Sub-skills 실행 테스트
```

## 🎯 플러그인 타입별 가이드

### 단순 유틸리티 플러그인

**필요한 파일만:**
```
skills/plugin-name/
├── SKILL.md
└── .claude/commands/
    └── plugin-name.md
```

**삭제해도 되는 것:**
- `skills/` 디렉토리
- `references/` (선택)
- `assets/` (선택)

### 다단계 워크플로우 플러그인

**필수 구조:**
```
skills/plugin-name/
├── SKILL.md                      # 전체 워크플로우 설명
├── .claude/commands/
│   ├── plugin-name.md            # 메인 command
│   ├── plugin:step-1.md          # 각 단계별 command
│   ├── plugin:step-2.md
│   └── plugin:step-3.md
├── skills/                       # 각 단계의 상세 가이드
│   ├── step-1/SKILL.md
│   ├── step-2/SKILL.md
│   └── step-3/SKILL.md
└── references/
    └── workflow-guide.md
```

### 도구 모음 플러그인

**필수 구조:**
```
skills/plugin-name/
├── SKILL.md                      # 도구 모음 개요
├── .claude/commands/
│   ├── tool-1.md
│   ├── tool-2.md
│   └── tool-3.md
└── skills/
    ├── tool-1/SKILL.md
    ├── tool-2/SKILL.md
    └── tool-3/SKILL.md
```

## ✅ 체크리스트

플러그인 배포 전 확인:

### 구조
- [ ] Marketplace에 올바르게 등록
- [ ] SKILL.md 작성 완료
- [ ] 모든 commands 생성
- [ ] Sub-skills 작성 (필요시)

### 문서
- [ ] 명확한 설명과 예시
- [ ] 사용 시나리오 명시
- [ ] 트리거 문구 정의
- [ ] 베스트 프랙티스 포함

### 테스트
- [ ] Marketplace에서 보이는지 확인
- [ ] 모든 commands 작동 확인
- [ ] Sub-skills 독립 실행 확인
- [ ] 예시대로 작동하는지 확인

## 📚 더 알아보기

상세한 내용은 다음 문서를 참조하세요:

- [Plugin Structure Guide](./plugin-structure-guide.md) - 전체 구조 가이드
- [Plugin Template](./plugin-template/) - 템플릿 파일들
- [OSS Contribution Framework](../skills/oss-contribution-framework/) - 실제 예시

## 💡 팁

### 명명 규칙

**플러그인 이름:**
- 명확하고 설명적으로: `oss-contribution-framework` ✅
- 너무 일반적이지 않게: `utilities` ❌

**Command 이름:**
- 일관된 prefix 사용: `plugin:action` 형식
- 예: `oss:issue-discovery`, `oss:codebase-exploration`

**Sub-skill 디렉토리:**
- 기능을 명확히 표현
- 예: `issue-discovery`, `code-analysis`

### 문서 작성

**SKILL.md 필수 섹션:**
1. Overview - 플러그인 설명
2. When to Use - 사용 시나리오
3. Features - 주요 기능
4. Usage Examples - 사용 예시

**Command 파일:**
- 한 줄로 간결하게
- "Use the {skill-name} skill to {action}" 형식

### 버전 관리

**시맨틱 버저닝:**
- `1.0.0` - 첫 릴리스
- `1.1.0` - 기능 추가
- `1.0.1` - 버그 수정
- `2.0.0` - 큰 변경 (하위 호환 X)

## 🚀 빠른 예시

### 예시 1: 간단한 포맷터 플러그인

```bash
# 1. 템플릿 복사
cp -r docs/plugin-template/skills/example-plugin skills/text-formatter

# 2. 불필요한 파일 삭제
rm -rf skills/text-formatter/skills
rm -rf skills/text-formatter/references

# 3. SKILL.md 수정
# name: text-formatter
# description: Format text in various styles

# 4. Command 생성
# .claude/commands/text-formatter.md

# 5. Marketplace 등록
# marketplace.json에 추가
```

### 예시 2: 3단계 워크플로우 플러그인

```bash
# 1. 템플릿 복사
cp -r docs/plugin-template/skills/example-plugin skills/api-design-workflow

# 2. 단계별로 재구성
cd skills/api-design-workflow/skills
mv feature-1 planning
mv feature-2 implementation
mkdir testing

# 3. Commands 수정
cd ../.claude/commands
mv example:feature-1.md api:planning.md
mv example:feature-2.md api:implementation.md
echo "Use the api:testing skill" > api:testing.md

# 4. 각 SKILL.md 작성
# 5. Marketplace 등록
```

---

**질문이나 문제가 있으면:**
1. [Plugin Structure Guide](./plugin-structure-guide.md) 확인
2. 기존 플러그인 코드 참조
3. GitHub Issues에 질문 남기기
