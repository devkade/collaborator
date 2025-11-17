# Plugin Template

이 템플릿을 사용하여 새로운 Claude Code 플러그인을 빠르게 생성할 수 있습니다.

## 사용 방법

### 1. 템플릿 복사

```bash
# 템플릿을 새 플러그인 이름으로 복사
cp -r docs/plugin-template/skills/example-plugin skills/your-plugin-name
```

### 2. 파일 수정

다음 파일들을 수정하세요:

1. **SKILL.md** - 플러그인 메인 문서
   - `name:` 필드 변경
   - `description:` 필드 변경
   - 내용 작성

2. **.claude/commands/** - 명령 파일들
   - 필요한 명령 추가/삭제
   - 명령 이름 변경
   - 내용 작성

3. **skills/** - Sub-skill 디렉토리들
   - 필요한 feature 추가/삭제
   - 각 SKILL.md 작성

4. **references/** - 참고 문서
   - 필요한 가이드 추가

5. **assets/templates/** - 템플릿 파일
   - 출력 템플릿 추가

### 3. Marketplace 등록

`.claude-plugin/marketplace.json`에 플러그인 추가:

```json
{
  "plugins": [
    {
      "name": "your-plugin-name",
      "source": "./skills/your-plugin-name",
      "description": "Your plugin description",
      "version": "1.0.0"
    }
  ]
}
```

### 4. 테스트

플러그인이 올바르게 작동하는지 확인:

```bash
# Claude Code에서 플러그인 로드 확인
# 모든 commands 실행 테스트
# Sub-skills 독립 실행 테스트
```

## 디렉토리 구조

```
skills/example-plugin/
├── SKILL.md                      # 메인 스킬 문서
├── .claude/
│   └── commands/                 # Slash commands
│       ├── example-plugin.md
│       ├── example:feature-1.md
│       └── example:feature-2.md
├── skills/                       # Sub-skills
│   ├── feature-1/
│   │   └── SKILL.md
│   └── feature-2/
│       └── SKILL.md
├── references/                   # 참고 문서
│   └── guide.md
└── assets/                       # 리소스
    └── templates/
        └── output-template.md
```

## 커스터마이징 가이드

### 플러그인 타입별 조정

#### 단일 기능 플러그인
- `skills/` 디렉토리 삭제 가능
- 간단한 commands만 유지
- SKILL.md에 모든 내용 포함

#### 워크플로우 플러그인
- 각 단계를 sub-skill로 분리
- 단계별 command 생성
- references에 워크플로우 가이드 추가

#### 도구 모음 플러그인
- 각 도구를 sub-skill로 분리
- 독립적인 commands 생성
- assets에 각 도구의 템플릿 추가

## 체크리스트

새 플러그인 생성 시:

- [ ] 템플릿 복사 완료
- [ ] SKILL.md 작성 완료
- [ ] Commands 생성 및 테스트 완료
- [ ] Sub-skills 작성 완료
- [ ] References 추가 완료
- [ ] Templates 추가 완료
- [ ] Marketplace 등록 완료
- [ ] 전체 기능 테스트 완료
- [ ] 문서 검토 완료
- [ ] 버전 번호 설정 완료

## 예시 플러그인

실제 예시를 보려면:
- `skills/oss-contribution-framework/` - 복잡한 워크플로우 플러그인
- `skills/deep-reading-framework/` - 단순한 프레임워크 플러그인

## 추가 도움

자세한 내용은 [Plugin Structure Guide](../plugin-structure-guide.md)를 참조하세요.
