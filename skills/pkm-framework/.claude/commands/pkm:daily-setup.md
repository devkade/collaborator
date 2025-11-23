You are helping manage Daily Notes in an Obsidian vault with Periodic Notes.

## Context
- Daily notes location: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
- Template: `~/Obsidian/Altellus/90_Templates/Temporal/Daily.md`
- Today's date: Use current date to determine the file path

## Task
Generate or update the **🌅 Daily Notes** section of today's daily note.

### Steps:

1. **Check if today's daily note exists**
   - Path format: `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-11-18.md` (example)
   - If it doesn't exist, create it from the template

2. **Fill "어제 요약" section**
   - Read yesterday's daily note (`~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`)
   - Summarize: completed tasks, main activities, key insights
   - List any incomplete tasks from yesterday
   - Update the wikilink to yesterday's date: `[[YYYY-MM-DD]]`

3. **Handle "오늘 이어서 할 일" section (TaskNotes format)**
   - Extract incomplete tasks from yesterday: `- [ ] [[Task Name]]`
   - Exclude completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
   - **Update scheduled date for overdue tasks:**
     - For each incomplete task from yesterday, read the task file from `00_Inbox/Tasks/`
     - If the task's `scheduled` date in frontmatter is before today, update it to today's date (YYYY-MM-DD)
     - This ensures overdue tasks are rescheduled to today
   - If user provides new tasks, add as `- [ ] [[Task Name]]` wikilinks
   - Tasks are individual markdown files in `00_Inbox/Tasks/` folder

4. **Fill "관련 노트" section automatically**
   - Extract wikilinks from yesterday's Notes section
   - Extract task paths from yesterday's YAML `pomodoros` array (taskPath field)
   - Remove duplicates and list as `- [[Note Name]]`

5. **Leave empty sections as-is**
   - 감사노트 (gratitude) - user fills this
   - 오늘의 포커스 (today's focus) - user defines

### Output Format
Provide the complete content to write/update in today's daily note, preserving all frontmatter and structure.

**Important**: Only modify the "🌅 Daily Notes" section. Leave "## Notes", "## Retro", and "🌙 Daily Review" sections untouched.
