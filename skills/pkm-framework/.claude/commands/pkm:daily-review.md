You are helping complete the Daily Review section in an Obsidian daily note.

## Context
- Daily notes location: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
- Date logic: If current time is before 04:00 AM, use previous day's date for the review
  - Example: 2025-11-19 02:30 AM → review 2025-11-18
  - Example: 2025-11-19 05:00 AM → review 2025-11-19
- TaskNotes data may be in YAML frontmatter (pomodoros field)

## Task
Fill in the **🌙 Daily Review** section of today's daily note.

### Steps:

1. **Determine target date**
   - Check current time
   - If before 04:00 AM, use previous day's date
   - Otherwise, use today's date

2. **Check Google Calendar (use pkm:gcal-today command)**
   - Fetch events for the target date from Google Calendar
   - TaskNotes already has ICS subscriptions configured
   - Extract scheduled meetings, appointments, and time blocks

3. **Read target date's daily note (TaskNotes format)**
   - Extract completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
   - Check YAML frontmatter `pomodoros` array for time tracking
   - Review content added during the day

4. **Fill "오늘 완료" section (TaskNotes format)**
   - List all completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
   - Search in "오늘 이어서 할 일" and Notes sections
   - If no tasks completed, note what was worked on

5. **Fill "시간 사용" section (TaskNotes Pomodoro format)**
   - Count total pomodoros from YAML `pomodoros` array length
   - Group by taskPath and display as: `Task Name - 🍅🍅🍅: 3`
   - Show total with tomato emojis: `총 🍅🍅🍅🍅🍅🍅: 6 pomodoros`
   - List calendar events from Google Calendar:
     - `- HH:MM-HH:MM: Event Title`

6. **Fill "인사이트" section**
   - Extract key learnings, discoveries, or patterns from today's notes
   - What worked well? What didn't?
   - Any blockers or important realizations?
   - Consider how calendar events aligned with planned work

7. **Fill "내일 제안" section (TaskNotes format)**
   - Based on incomplete tasks and insights, suggest priorities for tomorrow
   - Format as `- [ ] [[Task Name]]` (TaskNotes wikilink format)
   - Connect to blockers or unfinished work
   - Prioritize incomplete tasks from today

### Output Format
Provide only the "🌙 Daily Review" section content to update in today's note.

**Important**:
- DO NOT modify the "## Retro" section (user fills this manually)
- DO NOT modify other sections
- Preserve all frontmatter and existing content
