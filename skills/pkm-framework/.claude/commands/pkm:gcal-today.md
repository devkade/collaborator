You are helping fetch today's Google Calendar events using gcalcli.

## Context
- Calendar: 00_Schedule (main calendar only)
- Tool: gcalcli CLI
- Authentication: OAuth credentials at `~/.gcalcli_oauth`

## Task
Fetch and display today's calendar events from 00_Schedule calendar using gcalcli.

### Steps:

1. **Determine today's date**
   - Get current date in YYYY-MM-DD format
   - Set time range: 00:00 to 23:59

2. **Execute gcalcli command**
   ```bash
   gcalcli --calendar "00_Schedule" agenda "YYYY-MM-DD 00:00" "YYYY-MM-DD 23:59"
   ```

3. **Parse gcalcli output**
   - gcalcli returns format: `HH:MM  Event Title`
   - Extract start time, end time (if available), and event title

4. **Format for PKM review**
   - Clean and format output
   - Group by time
   - Count total events

### Output Format

```markdown
**2025-11-19 Calendar Events:**

- 09:00-10:00: Team Standup
- 11:00-12:00: Deep Work Block
- 14:00-15:00: 1-on-1 with Sarah
- 16:00-17:00: Code Review Session

**Total:** 4 events
```

### gcalcli Command

```bash
gcalcli --calendar "00_Schedule" \
        agenda \
        "$(date '+%Y-%m-%d') 00:00" \
        "$(date '+%Y-%m-%d') 23:59"
```

### Error Handling

**If gcalcli not installed:**
- Message: "gcalcli not found. Install with: pip install gcalcli"
- Provide installation instructions

**If not authenticated:**
- Message: "Not authenticated. Run: gcalcli init"
- Guide OAuth setup process

**If no events:**
- Message: "No calendar events scheduled for today."

**If calendar not found:**
- Message: "Calendar '00_Schedule' not found. Check calendar name in Google Calendar."

### Integration with Daily Review

This command is automatically called by `/pkm:daily-review` to populate the "시간 사용" section.

**Daily review will combine:**
- Pomodoros from TaskNotes YAML
- Calendar events from this command

### Notes

- Only fetches from 00_Schedule calendar
- Real-time data from Google Calendar API
- Requires internet connection
- OAuth token refreshes automatically
