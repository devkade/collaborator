---
name: pkm:monthly-review
description: Generate or update the Monthly Summary section by aggregating weekly notes in Obsidian
---

# Monthly Review Skill

This skill helps you reflect on your month by aggregating data from your weekly notes and generating comprehensive monthly insights.

## Purpose

Automatically generate the **📅 Monthly Summary** with:
- Monthly highlights and major achievements
- Monthly KPIs aggregated from weekly data
- Goal progress tracking
- Long-term patterns and trends
- Monthly themes
- Next month's objectives

## Context

- **Monthly notes location**: `20_Notes/Journal/YYYY/Mnn/YYYY-Mmm.md`
- **Weekly notes location**: `20_Notes/Journal/YYYY/Mnn/YYYY-Www.md`
- **Obsidian vault**: `~/Obsidian/Altellus`
- **Current month**: Calculate from today's date
- **Review period**: All weekly notes from the current month (typically 4-5 weeks)

## Workflow

### 1. Identify the monthly note
- Calculate current month (e.g., `2025-M11` for November)
- Path format: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-M11.md`
- Create from template if doesn't exist

### 2. Aggregate weekly notes (TaskNotes format)
- Identify all weekly notes in the current month (e.g., 2025-W44 through 2025-W47)
- Read each weekly note from `20_Notes/Journal/YYYY/Mnn/YYYY-Www.md`
- Extract highlights, KPIs, insights, blockers, and project statuses
- Extract completed tasks: `- [x] [[Task Name]]`

### 3. Fill "월간 하이라이트" (Monthly Highlights) - TaskNotes format
- List 5-7 major achievements across the month
- Use TaskNotes format: `- [x] [[Task Name]]` for highlights
- Significant milestones reached
- Major projects completed or advanced
- Key wins and breakthroughs

### 4. Fill "월간 KPI" (Monthly KPIs) - TaskNotes format
- **평균 완료율** (Average completion rate): Average of weekly completion rates
- **총 Pomodoros**: Sum of all weekly pomodoros
- **주간 평균**: Total pomodoros / number of weeks
- Display with emoji: `총 🍅 x 140 (4주간)`
- Example format:
  - `- 평균 완료율: 76% (across 4 weeks)`
  - `- 총 Pomodoros: 🍅 x 140`
  - `- 주간 평균: 35 pomodoros/week`

### 5. Fill "목표 진행도" (Goal Progress)
- Review monthly or quarterly goals
- Track progress on each goal
- Format: `- [[Goal Name]] — X% complete / status`
- Note which goals are on track vs behind

### 6. Fill "🧠 Monthly Themes & Patterns"
- Identify recurring themes across multiple weeks
- What patterns emerged this month?
- What working styles or approaches were most effective?
- Any systemic issues that need addressing?

### 7. Fill "📊 Project Portfolio"
- List all projects worked on during the month
- Current status of each project
- Time investment per project (if tracked)
- Format: `- [[Project Name]] — status, time invested`

### 8. Fill "🚧 Persistent Blockers" - TaskNotes format
- Blockers appearing in 2+ weekly reviews: `- [ ] [[Task Name]]`
- Format: `- [ ] [[Task Name]] — X주 연속 미완료`
- Long-term obstacles still unresolved
- Dependencies causing repeated delays
- Systemic issues requiring strategic solutions

### 9. Fill "🎯 다음 달 목표" (Next Month Objectives) - TaskNotes format
- Based on monthly insights and persistent blockers
- 3-5 key objectives for next month
- Format as TaskNotes checklist: `- [ ] [[Objective]]`
- Connect to unfinished important work
- Include blocker resolution strategies
- Prioritize persistent blocker resolution

## Output Format

Provide the complete monthly note content with all sections filled.

**Important**:
- Aggregate data from actual weekly notes, not assumptions
- Calculate real numbers for KPIs from weekly data
- Preserve frontmatter and template structure
- Look for long-term trends, not just week-to-week variations

## Usage

This skill is called via the `/pkm:monthly-review` command, typically at the end of the month (last day or first day of new month).

## Integration

- Works with **Periodic Notes** plugin in Obsidian
- Reads weekly notes from the current month
- Aggregates weekly KPI data
- Links to weekly notes using wikilinks

## Example

**Input**: User runs `/pkm:monthly-review` on 2025-11-30 (end of November)

**Process**:
1. Calculate month: `2025-M11` (November)
2. Identify monthly note: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-M11.md`
3. Find weekly notes in November: W44, W45, W46, W47, W48 (5 weeks)
4. Read each weekly note
5. Extract from each week:
   - Weekly highlights
   - Completion rate
   - Total focus time
   - Projects mentioned
   - Insights
   - Blockers
6. Aggregate and analyze:
   - Average completion rate: (75% + 80% + 72% + 78% + 81%) / 5 = 77.2%
   - Total focus time: 32 + 28 + 35 + 30 + 33 = 158 hours
   - Weekly average: 31.6 hours
   - Identify projects: Project A (4 weeks), Project B (3 weeks), Project C (2 weeks)
   - Find persistent blockers: Items mentioned in 3+ weeks
7. Identify monthly themes and long-term patterns
8. Set next month's objectives

**Output**: Complete monthly note with all sections filled based on aggregated monthly data.
