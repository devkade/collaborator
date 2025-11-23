You are helping complete the Weekly Review in an Obsidian vault with Periodic Notes.

## Context
- Weekly notes location: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-Www.md`
- Daily notes location: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
- Current week: Calculate from today's date
- Review period: Past 7 days of daily notes

## Task
Generate or update the **📆 Weekly Summary** and all sections of this week's weekly note.

### Steps:

1. **Identify the weekly note**
   - Calculate current week number (e.g., `2025-W46`)
   - Path format: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-W46.md`
   - Create from template if doesn't exist

2. **Aggregate daily notes (TaskNotes format)**
   - Read the past 7 daily notes from `~/Obsidian/Altellus/20_Notes/Journal/`
   - Extract completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
   - Extract incomplete tasks: `- [ ] [[Task Name]]`
   - Count pomodoros from YAML `pomodoros` array in each note

3. **Fill "주간 하이라이트" (Weekly Highlights)**
   - List 3-5 major accomplishments this week
   - Use TaskNotes format: `- [x] [[Task Name]]` for completed highlights
   - What moved forward? What was completed?

4. **Fill "KPI & 지표" (KPIs & Metrics) - TaskNotes format**
   - **완료율**: Count completed vs total TaskNotes tasks from 7 daily notes
   - **총 Pomodoros**: Sum `pomodoros` array length from all 7 daily notes
   - Display total with emoji: `총 🍅 x 35 (7일간)`
   - Example: `- 완료율: 23/30 tasks (77%)`

5. **Fill "주요 프로젝트 상태" (Project Status)**
   - Identify projects mentioned across the week
   - Format: `- [[Project Name]] — status description`

6. **Fill "🧠 Insights"**
   - Patterns discovered across the week
   - What worked well consistently?
   - What recurring issues appeared?

7. **Fill "⏱ Time & Energy"**
   - Project-wise time breakdown
   - Energy flow observations (when was most productive?)

8. **Fill "🧱 Blockers" - TaskNotes format**
   - Find tasks appearing 3+ days without completion: `- [ ] [[Task Name]]`
   - Recurring obstacles
   - External dependencies blocking progress
   - Format: `- [ ] [[Task Name]] — X일 연속 미완료`

9. **Fill "🎯 다음 주 우선순위" (Next Week Priorities) - TaskNotes format**
   - Based on blockers and incomplete work
   - Format as TaskNotes checklist: `- [ ] [[Priority Task]]`
   - Connect to blocker resolutions
   - Prioritize delayed tasks

### Output Format
Provide the complete weekly note content with all sections filled.

**Important**:
- Pull data from actual daily notes, not assumptions
- Calculate real numbers for KPIs from TaskNotes YAML
- Preserve frontmatter and template structure
