# Third Pass Analysis Template

Use this template structure for consistent Third Pass analysis output.

## Standard Format

```markdown
### Third-Pass

#### Critical Analysis
- **주장의 약점 / 적용 한계**
  - [Specific weakness 1: explain the issue]
  - [Specific weakness 2: where this approach fails]
  - [Generalization limits: boundaries of applicability]

- **컨텍스트 의존성 (환경, 스택, 시기)**
  - Environment: [Tech stack, scale, constraints assumed]
  - Prerequisites: [Knowledge, tools, or resources required]
  - Temporal: [Time-sensitive assumptions or dated information]
  - Cultural: [Organizational, regional, or domain-specific factors]

- **누락된 관점 / 대안**
  - Alternatives: [Other approaches not explored]
  - Trade-offs: [Costs or sacrifices not discussed]
  - Contrary views: [Opposing arguments or debates]
  - Edge cases: [Scenarios not addressed]

#### Reconstruction
- **핵심을 나만의 언어로**
  - [Restate the central thesis and key supporting ideas]
  - [Explain the logical flow or architecture]
  - [Capture the "why" behind the approach]

- **내 상황에 적용한다면**
  - 직접 적용: [What can be adopted as-is, why it fits]
  - 변형 필요: [What needs modification, how to adapt it]
  - 적용 불가: [What doesn't fit, why not, what to do instead]

#### Discussion
- **가져갈 것**
  - [Most valuable insights to remember and apply]
  - [Specific actions or changes to make]

- **한계**
  - [Boundaries of applicability]
  - [Remaining questions or uncertainties]
  - [Situations where caution is needed]

#### Action Items
- [ ] [Specific action item or experiment to try]
- [ ] [Related concept or document to explore]
- [ ] [Validation step before applying]

#### Future Ideas
- [ ] [Follow-up research or investigation]
- [ ] [Related question to explore]
```

## Variation for Tech Blog

```markdown
### Third-Pass

#### Critical Analysis
- **Technical Limitations**
  - Problem scope: [What problems this doesn't solve]
  - Scale considerations: [Where performance/complexity becomes issue]
  - Trade-offs: [What's sacrificed for benefits gained]

- **Implementation Context**
  - Stack requirements: [Languages, frameworks, tools needed]
  - Prerequisites: [Existing infrastructure or knowledge]
  - Assumed scale: [Team size, user load, data volume]

- **Alternatives & Edge Cases**
  - Simpler approaches: [When to use something simpler]
  - Alternative solutions: [Other ways to solve this]
  - Edge cases: [Scenarios where this breaks]

#### Reconstruction
- **Technical Approach**
  - [Explain the solution architecture in own words]

- **Applying to My Stack**
  - 직접 적용: [Components that transfer as-is]
  - 변형 필요: [What to modify for my environment]
  - 다른 접근: [Where I'd do something different]

#### Discussion
- **Worth Adopting**
  - [Specific techniques or patterns to use]

- **Watch Out For**
  - [Gotchas, anti-patterns, or risks]

#### Action Items
- [ ] Test with small prototype
- [ ] Benchmark against current approach
- [ ] Read [related article/docs]
```

## Variation for Retrospective

```markdown
### Third-Pass

#### Critical Analysis
- **Context Specificity**
  - Team context: [What's unique about their team/org]
  - Situational factors: [Circumstances that affected outcomes]
  - Generalizability: [Where lessons may not apply]

- **Success Factors**
  - What they controlled: [Decisions and actions]
  - What they didn't: [Luck, timing, external factors]
  - Key enablers: [What made success possible]

- **Unstated Lessons**
  - Reading between lines: [Implicit insights]
  - Missing perspectives: [Other team members' views]
  - Survivorship bias: [What about failed attempts?]

#### Reconstruction
- **Key Lessons**
  - [Core takeaways in own words]

- **Relevance to My Situation**
  - 직접 적용: [Lessons that transfer to my context]
  - 변형 필요: [How to adapt for my situation]
  - 적용 불가: [What's too context-specific]

#### Discussion
- **Actionable Insights**
  - [Changes to make based on this]

- **Caveats**
  - [Limitations of lessons learned]

#### Action Items
- [ ] Apply [specific practice] on next project
- [ ] Validate [assumption] in my context
- [ ] Discuss with team
```

## Variation for Academic Paper

```markdown
### Third-Pass

#### Critical Analysis
- **Methodological Issues**
  - Design limitations: [Threats to validity]
  - Sample issues: [Size, representativeness, bias]
  - Alternative explanations: [Other ways to interpret results]

- **Assumptions & Scope**
  - Theoretical assumptions: [Framework dependencies]
  - Boundary conditions: [Where findings don't apply]
  - Generalizability: [Population, setting, time]

- **Research Gaps**
  - Missing variables: [What wasn't considered]
  - Unexplored angles: [Related questions not asked]
  - Future work: [What needs investigation]

#### Reconstruction
- **Research Contribution**
  - [Main findings and their significance]

- **Application to Practice**
  - 실무 적용: [How this informs real-world decisions]
  - 후속 연구: [Follow-up studies this enables]
  - 내 연구: [How this relates to my work]

#### Discussion
- **Key Findings**
  - [Most important results]

- **Limitations**
  - [Validity threats and boundaries]

#### Action Items
- [ ] Replicate with [different population/setting]
- [ ] Extend to [related phenomenon]
- [ ] Address [limitation] in future study
```

## Usage Notes

**Adapt the template:**
- Not every section is needed for every document
- Combine sections when appropriate
- Add subsections for complex analysis
- Use bullet points with bold headings for clear structure

**Maintain consistency:**
- Use same structure across similar documents
- This enables easy comparison later
- Makes it easier to find information

**Be concise but complete:**
- Each point should be specific and actionable
- Avoid vague statements
- Include enough context to understand later
