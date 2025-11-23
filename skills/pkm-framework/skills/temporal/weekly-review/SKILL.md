---
name: pkm:weekly-review
description: Generate or update the Weekly Summary section by aggregating daily notes in Obsidian
---

# Weekly Review Skill

This skill helps you reflect on your week by aggregating data from your daily notes and generating comprehensive weekly insights.

## Purpose

Automatically generate the **📆 Weekly Summary** with:
- Weekly highlights and accomplishments
- KPIs (completion rate, total focus time)
- Project status tracking
- Insights and patterns
- Blockers and delayed tasks
- Next week's priorities

## Context

- **Weekly notes location**: `20_Notes/Journal/YYYY/Mnn/YYYY-Www.md`
- **Daily notes location**: `20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
- **Obsidian vault**: `~/Obsidian/Altellus`
- **Current week**: Calculate from today's date
- **Review period**: Past 7 days of daily notes

## Workflow

### 1. Identify the weekly note
- Calculate current week number (e.g., `2025-W46`)
- Path format: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-W46.md`
- Create from template if doesn't exist

### 2. Aggregate daily notes (TaskNotes format)
- Read the past 7 daily notes from `20_Notes/Journal/`
- Extract completed tasks in TaskNotes format: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
- Extract incomplete tasks: `- [ ] [[Task Name]]`
- Count pomodoros from YAML `pomodoros` array in each daily note
- Collect data from both "🌅 Daily Notes" and "🌙 Daily Review" sections

### 3. Fill "주간 하이라이트" (Weekly Highlights)
- List 3-5 major accomplishments this week
- Use TaskNotes format for highlights: `- [x] [[Task Name]]`
- What moved forward? What was completed?
- Focus on significant wins and progress

### 4. Fill "KPI & 지표" (KPIs & Metrics) - TaskNotes format
- **완료율** (Completion rate): Count completed vs total TaskNotes tasks
- **총 Pomodoros**: Sum `pomodoros` array length from all 7 daily notes
- Display with emoji: `총 🍅 x 35 (7일간)`
- Show daily average: `일평균: 5 pomodoros/day`
- Example format:
  - `- 완료율: 23/30 tasks (77%)`
  - `- 총 Pomodoros: 🍅 x 35`

### 5. Fill "주요 프로젝트 상태" (Project Status)
- Identify projects mentioned across the week
- Track progress and current status
- Format: `- [[Project Name]] — status description`

### 6. Fill "🧠 Insights"
- Patterns discovered across the week
- What worked well consistently?
- What recurring issues appeared?
- Any systemic improvements needed?

### 7. Fill "⏱ Time & Energy"
- Project-wise time breakdown
- Energy flow observations (when was most productive?)
- Time allocation vs. planned focus areas

### 8. Fill "🧱 Blockers" - TaskNotes format
- Find TaskNotes tasks appearing 3+ days without completion: `- [ ] [[Task Name]]`
- Format: `- [ ] [[Task Name]] — X일 연속 미완료`
- Recurring obstacles that appeared multiple times
- External dependencies blocking progress
- Identify root causes if visible

### 9. Fill "🎯 다음 주 우선순위" (Next Week Priorities) - TaskNotes format
- Based on blockers and incomplete work
- Format as TaskNotes checklist: `- [ ] [[Priority Task]]`
- Connect to blocker resolutions
- Include carried-forward important tasks
- Prioritize delayed tasks from blockers section

## Output Format

Provide the complete weekly note content with all sections filled.

**Important**:
- Pull data from actual daily notes, not assumptions
- Calculate real numbers for KPIs from TaskNotes YAML frontmatter
- Preserve frontmatter and template structure
- Base all insights on actual data from the 7 daily notes

## Usage

This skill is called via the `/pkm:weekly-review` command, typically on Friday evening or Sunday evening to reflect on the week.

## Integration

- Works with **Periodic Notes** plugin in Obsidian
- Reads daily notes from the past 7 days
- Aggregates YAML frontmatter data (pomodoros)
- Links to daily notes using wikilinks

## Example

**Input**: User runs `/pkm:weekly-review` on 2025-11-22 (Friday of week 47)

**Process**:
1. Calculate week number: `2025-W47`
2. Identify weekly note: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-W47.md`
3. Read 7 daily notes: 2025-11-16 through 2025-11-22
4. Extract from each daily note:
   - Completed tasks from "오늘 완료"
   - Pomodoros from YAML frontmatter
   - Insights from "인사이트"
   - Projects mentioned
   - Incomplete tasks
5. Aggregate and analyze:
   - Count total tasks: 23 completed / 30 total = 77%
   - Sum pomodoros: 58 total = 29 hours
   - Identify projects: Project A, Project B, Project C
   - Find blockers: Tasks mentioned 3+ days
6. Generate insights and priorities

**Output**: Complete weekly note with all 9 sections filled based on actual weekly data.
