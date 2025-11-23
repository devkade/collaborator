You are helping add events to Google Calendar using gcalcli.

## Context
- Calendar: 00_Schedule (main calendar only)
- Tool: gcalcli CLI
- Authentication: OAuth credentials at `~/.gcalcli_oauth`

## Task
Add a new calendar event to 00_Schedule using gcalcli.

### Input Modes

**Mode 1: Interactive (no arguments)**
- Ask user for event details
- Collect: title, date, time, duration

**Mode 2: Quick add (natural language)**
- Parse natural language input
- Example: "Meeting with team tomorrow 2pm"
- Use gcalcli quick command

**Mode 3: Structured (specific parameters)**
- Accept: title, when, duration
- Use gcalcli add command

### Steps:

#### Mode 1: Interactive

1. **Prompt for event details:**
   - Event title: "What is the event?"
   - Date: "When? (YYYY-MM-DD or 'today', 'tomorrow')"
   - Time: "What time? (HH:MM)"
   - Duration: "How long? (minutes, default 60)"

2. **Execute gcalcli add:**
   ```bash
   gcalcli --calendar "00_Schedule" add \
     --title "Event Title" \
     --when "YYYY-MM-DD HH:MM" \
     --duration MINUTES \
     --reminder 10
   ```

3. **Confirm creation:**
   - Display: "✅ Event created: [Title] on [Date] at [Time]"

#### Mode 2: Quick Add

1. **Parse natural language input:**
   - User provides: "Meeting tomorrow 2pm"

2. **Execute gcalcli quick:**
   ```bash
   gcalcli --calendar "00_Schedule" quick "Meeting tomorrow 2pm"
   ```

3. **Confirm creation:**
   - Display gcalcli confirmation message

#### Mode 3: Structured

1. **Accept parameters:**
   - title: Event title
   - when: YYYY-MM-DD HH:MM
   - duration: minutes (default 60)

2. **Execute gcalcli add:**
   ```bash
   gcalcli --calendar "00_Schedule" add \
     --title "${title}" \
     --when "${when}" \
     --duration ${duration}
   ```

### Output Format

```markdown
✅ **Event Created:**

- **Title:** Deep Work Session
- **Date:** 2025-11-19
- **Time:** 14:00-16:00 (2 hours)
- **Calendar:** 00_Schedule

View: gcalcli agenda today
```

### Examples

**Interactive:**
```bash
/pkm:gcal-add
> What is the event? Deep Work
> When? tomorrow
> What time? 14:00
> How long? 120
✅ Event created: Deep Work on 2025-11-20 at 14:00
```

**Quick add:**
```bash
/pkm:gcal-add "Team meeting Friday 3pm"
✅ Event created via quick add
```

**Structured:**
```bash
/pkm:gcal-add --title "Code Review" --when "2025-11-19 16:00" --duration 60
✅ Event created: Code Review
```

### Integration with TaskNotes

**Create calendar event from task:**
```bash
# When user wants to time-block a task
/pkm:gcal-add "[[Task Name]]" tomorrow 10:00 120
```

This creates a 2-hour focus block for the task.

### Error Handling

**If gcalcli fails:**
- Show error message
- Check: authentication, calendar name, date format

**If duplicate event:**
- Warn user: "Similar event exists at this time"
- Confirm: "Add anyway?"

**If time conflict:**
- Show: "Conflict with existing event: [Event]"
- Suggest: Alternative time slots

### Default Settings

- **Default duration:** 60 minutes
- **Default reminder:** 10 minutes before
- **Calendar:** 00_Schedule (always)

### Notes

- Events sync across all Google Calendar clients
- Supports natural language (tomorrow, next Monday, etc.)
- Can create recurring events with --recurrence flag
- Time zones handled by Google Calendar settings
