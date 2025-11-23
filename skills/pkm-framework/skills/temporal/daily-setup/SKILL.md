---
name: pkm:daily-setup
description: Generate or update the Daily Notes section for morning daily note setup in Obsidian
---

# Daily Setup Skill

This skill helps you start your day by creating or updating today's daily note in your Obsidian vault.

## Purpose

Automatically create or update the **🌅 Daily Notes** section of your daily note with:

-   Summary of yesterday's work
-   Incomplete tasks carried forward
-   Proper date navigation

## Context

-   **Daily notes location**: `20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
-   **Template**: `90_Templates/Temporal/Daily.md`
-   **Obsidian vault**: `~/Obsidian/Altellus`
-   **Today's date**: Use current date to determine the file path

## Workflow

### 1. Check if today's daily note exists

-   Path format: `20_Notes/Journal/2025/M11/2025-11-18.md` (example)
-   If it doesn't exist, create it from the template at `90_Templates/Temporal/Daily.md`

### 2. Fill "어제 요약" (Yesterday Summary) section

-   Read yesterday's daily note from `20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
-   Summarize:
    -   Completed tasks (marked with `[x]`)
    -   Main activities from the note content
    -   Key insights from the Daily Review section
-   List any incomplete tasks from yesterday
-   Update the wikilink to yesterday's date: `[[YYYY-MM-DD]]`

### 3. Handle "오늘 이어서 할 일" (Tasks to Continue Today) section - TaskNotes format

-   Extract incomplete tasks from yesterday in TaskNotes format: `- [ ] [[Task Name]]`
-   Exclude completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
-   **Update scheduled date for overdue tasks:**
    -   For each incomplete task from yesterday, read the task file from `00_Inbox/Tasks/`
    -   If the task's `scheduled` date in frontmatter is before today, update it to today's date (YYYY-MM-DD)
    -   This ensures overdue tasks are rescheduled to today
-   If user provides new tasks, add them as `- [ ] [[Task Name]]` wikilinks
-   TaskNotes: Tasks are individual markdown files in `00_Inbox/Tasks/` folder

### 4. Fill "관련 노트" (Related Notes) section automatically

-   Extract wikilinks from yesterday's Notes section
-   Extract task paths from yesterday's YAML `pomodoros` array (taskPath field)
-   Remove duplicates and list as `- [[Note Name]]`
-   This provides automatic tracking of what notes/tasks you worked on yesterday

### 5. Leave empty sections as-is

These sections are filled by the user during the day:

-   **감사노트** (gratitude) - user fills this
-   **오늘의 포커스** (today's focus) - user defines

## Output Format

Provide the complete content to write/update in today's daily note, preserving all frontmatter and structure.

**Important**:

-   Only modify the "🌅 Daily Notes" section
-   Leave "## Notes", "## Retro", and "🌙 Daily Review" sections untouched
-   Preserve all YAML frontmatter (especially pomodoro tracking)

## Usage

This skill is called via the `/pkm:daily-setup` command, typically first thing in the morning to prepare your daily note.

## Integration

-   Works with **Periodic Notes** plugin in Obsidian
-   Reads from the daily note template
-   Maintains wikilink navigation between dates
-   Respects YAML frontmatter structure

## Example

**Input**: User runs `/pkm:daily-setup` on 2025-11-19

**Process**:

1. Check if `20_Notes/Journal/2025/M11/2025-11-19.md` exists
2. Read yesterday's note: `20_Notes/Journal/2025/M11/2025-11-18.md`
3. Extract completed tasks and insights from 2025-11-18
4. Create/update today's note with yesterday's summary
5. Link to yesterday: `[[2025-11-18]]`

**Output**: Updated daily note with filled "어제 요약" section and wikilink navigation ready for the day.
