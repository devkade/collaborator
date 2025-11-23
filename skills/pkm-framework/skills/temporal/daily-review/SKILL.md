---
name: pkm:daily-review
description: Complete the Daily Review section for end-of-day reflection in Obsidian
---

# Daily Review Skill

This skill helps you close out your day by completing the **🌙 Daily Review** section with tasks completed, time usage, insights, and tomorrow's priorities.

## Purpose

Automatically complete the **🌙 Daily Review** section with:

-   Tasks completed today
-   Time usage from Google Calendar and pomodoro tracking
-   Key insights and learnings
-   Suggestions for tomorrow's work

## Context

-   **Daily notes location**: `20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
-   **Obsidian vault**: `~/Obsidian/Altellus`
-   **Date logic**: If current time is before 04:00 AM, use previous day's date for the review
    -   Example: 2025-11-19 02:30 AM → review 2025-11-18
    -   Example: 2025-11-19 05:00 AM → review 2025-11-19
-   **TaskNotes data**: Pomodoro tracking may be in YAML frontmatter (`pomodoros` field)

## Workflow

### 1. Determine target date

-   Check current time
-   If before 04:00 AM, use previous day's date
-   Otherwise, use today's date

### 2. Check Google Calendar

-   Use the `/pkm:gcal-today` command to fetch events
-   TaskNotes already has Google Calendar ICS subscriptions configured
-   Extract scheduled meetings, appointments, and time blocks

### 3. Read target date's daily note (TaskNotes format)

-   Extract completed tasks in TaskNotes format: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
-   Check YAML frontmatter `pomodoros` array for time tracking data
-   Review content added during the day

### 4. Fill "오늘 완료" (Tasks Completed) section - TaskNotes format

-   List all completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`
-   Search in "오늘 이어서 할 일" section and Notes section
-   If no tasks completed, note what was worked on instead

### 5. Fill "시간 사용" (Time Usage) section - TaskNotes Pomodoro format

-   Count total pomodoros from YAML `pomodoros` array length
-   Group by taskPath and display as: `Task Name - 🍅🍅🍅: 3`
-   Show total with tomato emoji count: `총 🍅🍅🍅🍅🍅🍅: 6 pomodoros`
-   List calendar events from Google Calendar:
    -   `- HH:MM-HH:MM: Event Title`

### 6. Fill "인사이트" (Insights) section

-   Extract key learnings, discoveries, or patterns from today's notes
-   What worked well? What didn't?
-   Any blockers or important realizations?
-   Consider how calendar events aligned with planned work

### 7. Fill "내일 제안" (Tomorrow's Suggestions) section - TaskNotes format

-   Based on incomplete tasks and insights, suggest priorities for tomorrow
-   Format as `- [ ] [[Task Name]]` (TaskNotes wikilink format)
-   Connect to blockers or unfinished work
-   Prioritize incomplete tasks from today

## Output Format

Provide only the "🌙 Daily Review" section content to update in today's note.

**Important**:

-   DO NOT modify the "## Retro" section (user fills this manually)
-   DO NOT modify other sections
-   Preserve all frontmatter and existing content

## Usage

This skill is called via the `/pkm:daily-review` command, typically at the end of the workday or before bed.

## Integration

-   Uses the **gcal-review** skill for Google Calendar integration
-   Reads YAML frontmatter for pomodoro tracking
-   Works with **Periodic Notes** plugin in Obsidian
-   Respects the early-morning edge case (reviews previous day if before 4 AM)

## Example

**Input**: User runs `/pkm:daily-review` on 2025-11-19 at 10:00 PM

**Process**:

1. Determine target date: 2025-11-19 (after 4 AM)
2. Fetch calendar events for 2025-11-19 using `gcal-review`
3. Read `~/Obsidian/Altellus/20_Notes/Journal/2025/M11/2025-11-19.md`
4. Extract completed tasks marked with `[x]`
5. Calculate time usage from calendar + pomodoros in YAML
6. Generate insights from note content
7. Suggest tomorrow's priorities based on incomplete work

**Output**: Updated "🌙 Daily Review" section with all subsections filled.
