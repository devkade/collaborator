---
name: pkm:gcalcli
description: Google Calendar integration for PKM Framework using gcalcli for read/write access
---

# gcalcli Skill

This skill provides Google Calendar integration for the PKM Framework using gcalcli CLI tool for both reading and writing calendar events.

## Purpose

Full Google Calendar integration with read/write capabilities for task management and time tracking.

**Key Features:**
- **Read**: Fetch calendar events for daily/weekly reviews
- **Write**: Create calendar events from TaskNotes tasks
- **Time blocking**: Automatically create focus blocks
- **Task sync**: Update calendar when tasks complete
- **00_Schedule calendar only**: Focused on main calendar management

## Context

- **gcalcli**: Google Calendar CLI tool
- **Target calendar**: `00_Schedule` (main calendar only)
- **Authentication**: Google OAuth 2.0
- **API**: Google Calendar API v3

## Installation

### 1. Install gcalcli

```bash
pip install gcalcli
```

### 2. Initial Authentication

```bash
gcalcli init
```

This will:
- Open browser for Google account authentication
- Save credentials to `~/.gcalcli_oauth`
- Grant calendar access permissions

### 3. Verify Installation

```bash
gcalcli --calendar "00_Schedule" agenda today
```

## How It Works

### Read Operations

gcalcli fetches events directly from Google Calendar API:

```bash
# Today's events
gcalcli --calendar "00_Schedule" agenda "2025-11-19 00:00" "2025-11-19 23:59"

# This week
gcalcli --calendar "00_Schedule" calw
```

### Write Operations

gcalcli creates/modifies events via API:

```bash
# Add event
gcalcli --calendar "00_Schedule" add \
  --title "Deep Work" \
  --when "2025-11-19 14:00" \
  --duration 120

# Quick add (natural language)
gcalcli --calendar "00_Schedule" quick "Meeting tomorrow 2pm"
```

## Output Format

### For Daily Review

```markdown
**2025-11-19 Calendar Events:**
- 09:00-10:00: Team Standup (00_Schedule)
- 11:00-12:00: Deep Work Block (01_Daily)
- 14:00-15:00: 1-on-1 with Sarah (02_Work)
- 16:00-17:00: Paper Reading (03_Development)
- 18:00-19:00: Exercise (05_Health)
```

### For Weekly Overview

```markdown
**이번 주 주요 일정:**
- 월: Team Planning (09:00-10:00)
- 화: Client Meeting (14:00-16:00)
- 수: Deep Work Day (No meetings)
- 목: 1-on-1s (14:00-17:00)
- 금: Demo Day (15:00-16:00)
```

## Commands

### Read Commands

#### `/pkm:gcal-today`

Fetch today's calendar events.

**Usage:**
```bash
/pkm:gcal-today
```

**Output:** Events for today from 00_Schedule

#### `/pkm:gcal-date <YYYY-MM-DD>`

Fetch events for a specific date.

**Usage:**
```bash
/pkm:gcal-date 2025-11-18
```

**Output:** Events for the specified date

#### `/pkm:gcal-week`

Fetch this week's calendar overview.

**Usage:**
```bash
/pkm:gcal-week
```

**Output:** Summary of events for the current week

### Write Commands

#### `/pkm:gcal-add`

Add a calendar event.

**Usage:**
```bash
# Add event with prompts
/pkm:gcal-add

# Quick add with natural language
/pkm:gcal-add "Meeting with team tomorrow 2pm"
```

**Output:** Event created confirmation

#### `/pkm:gcal-block`

Create time blocks from TaskNotes tasks.

**Usage:**
```bash
# Create focus block for a task
/pkm:gcal-block [[Task Name]] 2025-11-19 14:00 120

# Auto-schedule incomplete tasks
/pkm:gcal-block --auto
```

**Output:** Time blocks created

#### `/pkm:gcal-complete`

Mark task completion in calendar.

**Usage:**
```bash
# Update event when task completes
/pkm:gcal-complete [[Task Name]]
```

**Output:** Calendar event updated with ✅

## Integration with Daily Review

The daily review skill (`/pkm:daily-review`) automatically calls `/pkm:gcal-today` to populate the "시간 사용" section.

**Automatic usage:**
```markdown
### 시간 사용

**Pomodoros:**
- ELEGNT 논문 - 🍅🍅🍅: 3
- 총 🍅🍅🍅: 3 pomodoros

**Calendar Events:**
- 09:00-10:00: Team Standup (00_Schedule)
- 14:00-15:00: 1-on-1 with Sarah (02_Work)
```

## ICS Parsing

The skill parses standard ICS format:

```
BEGIN:VEVENT
DTSTART:20251119T090000Z
DTEND:20251119T100000Z
SUMMARY:Team Standup
DESCRIPTION:Weekly team sync
END:VEVENT
```

Extracts:
- Start time (`DTSTART`)
- End time (`DTEND`)
- Event title (`SUMMARY`)
- Description (`DESCRIPTION`)

## Configuration

### Enabling/Disabling Calendars

TaskNotes config controls which calendars are active:

```json
{
  "name": "00_Schedule",
  "enabled": true  // Set to false to disable
}
```

### Refresh Interval

TaskNotes automatically refreshes ICS feeds every 60 minutes.

## Troubleshooting

### "No calendar events found"

**Possible causes:**
1. No events scheduled for the date
2. ICS subscriptions disabled in TaskNotes
3. ICS feed not refreshed recently

**Solution:**
- Check TaskNotes calendar view
- Verify `enabled: true` in config
- Wait for next auto-refresh or restart Obsidian

### "Unable to read TaskNotes config"

**Cause:** TaskNotes plugin not installed or config missing

**Solution:**
- Install TaskNotes plugin
- Configure calendar subscriptions in TaskNotes settings

### Events showing wrong timezone

**Cause:** ICS events are in UTC, need local timezone conversion

**Solution:**
- Skill automatically converts to local timezone
- Verify system timezone is correct

## Example Usage

### Morning Daily Setup

```bash
# Check today's schedule
/pkm:gcal-today

# Output:
**2025-11-19 Calendar Events:**
- 09:00-10:00: Team Standup
- 11:00-12:00: Focus Block
- 14:00-15:00: Client Call
- 15:30-16:30: Code Review
```

### Evening Daily Review

Daily review automatically includes calendar events:

```bash
/pkm:daily-review

# Generates:
### 시간 사용
**Pomodoros:**
- Project A - 🍅🍅🍅: 3
- 총 🍅🍅🍅: 3

**Calendar Events:**
- 09:00-10:00: Team Standup
- 11:00-12:00: Focus Block (productive!)
- 14:00-15:00: Client Call
```

### Weekly Planning

```bash
/pkm:gcal-week

# Shows week overview for planning
```

## Dependencies

- **TaskNotes plugin**: Must be installed and configured
- **ICS subscriptions**: Google Calendar ICS URLs must be added to TaskNotes
- **Internet connection**: Required to fetch ICS feeds

## Future Enhancements

- Write events back to calendar
- Create calendar blocks from tasks
- Sync task completions to calendar
- Time blocking assistance
- Meeting preparation automation

## Version

**Current Version**: 1.0.0 (Initial release)

**Included in**: PKM Framework 1.0.0+

## See Also

- [Daily Review Skill](../temporal/daily-review/SKILL.md)
- [TaskNotes Plugin Documentation](https://github.com/obsidian-tasks-group/obsidian-tasks)
- [ICS Format Specification](https://tools.ietf.org/html/rfc5545)
