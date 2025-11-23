You are helping complete the Monthly Review in an Obsidian vault with Periodic Notes.

## Context
- Monthly notes location: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-Mmm.md`
- Weekly notes location: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-Www.md`
- Current month: Calculate from today's date
- Review period: All weekly notes from the current month (typically 4-5 weeks)

## Task
Generate or update the **📅 Monthly Summary** and all sections of this month's monthly note.

### Steps:

1. **Identify the monthly note**
   - Calculate current month (e.g., `2025-M11` for November)
   - Path format: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-M11.md`
   - Create from template if doesn't exist

2. **Aggregate weekly notes (TaskNotes format)**
   - Identify all weekly notes in the current month
   - Read each weekly note and extract highlights, KPIs, insights, blockers
   - Extract completed tasks: `- [x] [[Task Name]]`

3. **Fill "월간 하이라이트" (Monthly Highlights) - TaskNotes format**
   - List 5-7 major achievements across the month
   - Use TaskNotes format: `- [x] [[Task Name]]` for completed highlights
   - Significant milestones and key wins

4. **Fill "월간 KPI" (Monthly KPIs) - TaskNotes format**
   - **평균 완료율**: Average of weekly completion rates
   - **총 Pomodoros**: Sum of all weekly pomodoros
   - **주간 평균**: Total pomodoros / number of weeks
   - Display with emoji: `총 🍅 x 140 (4주간)`
   - Example: `- 평균 완료율: 76% (across 4 weeks)`

5. **Fill "목표 진행도" (Goal Progress)**
   - Review monthly or quarterly goals
   - Track progress on each goal
   - Format: `- [[Goal Name]] — X% complete / status`

6. **Fill "🧠 Monthly Themes & Patterns"**
   - Identify recurring themes across multiple weeks
   - What patterns emerged? What was most effective?
   - Any systemic issues needing attention?

7. **Fill "📊 Project Portfolio"**
   - List all projects worked on during the month
   - Current status and time investment per project

8. **Fill "🚧 Persistent Blockers" - TaskNotes format**
   - Blockers appearing in 2+ weekly reviews: `- [ ] [[Task Name]]`
   - Format: `- [ ] [[Task Name]] — X주 연속 미완료`
   - Long-term obstacles still unresolved
   - Systemic issues requiring strategic solutions

9. **Fill "🎯 다음 달 목표" (Next Month Objectives) - TaskNotes format**
   - Based on monthly insights and persistent blockers
   - 3-5 key objectives for next month
   - Format as TaskNotes checklist: `- [ ] [[Objective]]`
   - Prioritize blocker resolution

### Output Format
Provide the complete monthly note content with all sections filled.

**Important**:
- Aggregate data from actual weekly notes, not assumptions
- Calculate real numbers for KPIs from weekly data
- Look for long-term trends and patterns
- Preserve frontmatter and template structure
