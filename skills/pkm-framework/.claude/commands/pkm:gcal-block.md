You are helping create time blocks in Google Calendar from TaskNotes tasks using gcalcli.

## Context
- Calendar: 00_Schedule (main calendar only)
- Tool: gcalcli CLI
- TaskNotes: Tasks in `~/Obsidian/Altellus/00_Inbox/Tasks/`
- Daily notes: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`

## Task
Create calendar time blocks for TaskNotes tasks to facilitate focus time and task completion.

### Use Cases

**1. Manual time block for specific task**
```bash
/pkm:gcal-block "[[SWSP25 Problem Definition]]" 2025-11-19 14:00 120
```
Creates 2-hour focus block for the task.

**2. Auto-schedule incomplete tasks**
```bash
/pkm:gcal-block --auto
```
Automatically schedules incomplete tasks from today's daily note.

**3. Weekly planning**
```bash
/pkm:gcal-block --week
```
Creates time blocks for all tasks planned this week.

### Steps:

#### Manual Time Block

1. **Parse input:**
   - Task name: `[[Task Name]]` (TaskNotes wikilink)
   - Date: YYYY-MM-DD
   - Time: HH:MM
   - Duration: minutes (default 90)

2. **Extract task details:**
   - Read task file from `00_Inbox/Tasks/Task Name.md`
   - Get task title, priority, time estimate

3. **Create calendar event:**
   ```bash
   gcalcli --calendar "00_Schedule" add \
     --title "🎯 [Task Title]" \
     --when "YYYY-MM-DD HH:MM" \
     --duration MINUTES \
     --description "TaskNotes: [[Task Name]]"
   ```

4. **Confirm:**
   - Display: "✅ Time block created for [[Task Name]]"

#### Auto-Schedule

1. **Read today's daily note:**
   - Extract "오늘 이어서 할 일" section
   - Find incomplete tasks: `- [ ] [[Task Name]]`

2. **Check calendar availability:**
   - Fetch today's events with `/pkm:gcal-today`
   - Find free time slots (gaps between events)

3. **Prioritize tasks:**
   - High priority first (if specified in TaskNotes)
   - Larger time estimates first
   - Morning for deep work, afternoon for lighter tasks

4. **Create time blocks:**
   - For each task, find suitable time slot
   - Create gcalcli event with task reference
   - Default duration: 90 minutes (pomodoro-friendly)

5. **Summary:**
   ```markdown
   ✅ **Auto-scheduled 3 tasks:**

   - 09:00-10:30: [[SWSP25 Problem Definition]]
   - 11:00-12:00: [[Long horizon action model paper search]]
   - 14:00-15:30: [[Claude 명령 테스트 및 디버깅]]

   Total focus time: 4 hours
   ```

#### Weekly Planning

1. **Read this week's tasks:**
   - From weekly note or aggregated daily notes
   - Extract all incomplete tasks: `- [ ] [[Task Name]]`

2. **Distribute across week:**
   - Monday-Friday scheduling
   - Balance workload (max 4 hours deep work/day)
   - Respect existing calendar events

3. **Create blocks:**
   - Spread tasks across available time slots
   - Group similar tasks (context switching reduction)

### Output Format

**Single task:**
```markdown
✅ **Time Block Created:**

- **Task:** [[SWSP25 Problem Definition]]
- **Time:** 2025-11-19 14:00-16:00 (2 hours)
- **Calendar:** 00_Schedule

Focus time secured! 🎯
```

**Auto-schedule:**
```markdown
✅ **Auto-scheduled 4 tasks:**

**Morning (Deep Work):**
- 09:00-10:30: [[SWSP25 Problem Definition]] 🍅🍅🍅
- 11:00-12:30: [[ELEGNT 논문 리뷰]] 🍅🍅🍅

**Afternoon:**
- 14:00-15:00: [[Documentation 업데이트]] 🍅🍅
- 15:30-16:30: [[Code Review]] 🍅🍅

**Total:** 5.5 hours focus time
**Available:** 09:00-12:30, 14:00-16:30
```

### Smart Scheduling Logic

**1. Respect existing events:**
- Don't overlap with calendar events
- Leave buffer time (15 min) between blocks

**2. Energy optimization:**
- 09:00-12:00: Deep work (complex tasks)
- 14:00-16:00: Medium tasks
- 16:00-18:00: Light tasks (reviews, admin)

**3. Pomodoro-friendly durations:**
- 25 min = 🍅
- 50 min = 🍅🍅
- 90 min = 🍅🍅🍅 (ideal)
- 120 min = 🍅🍅🍅🍅

**4. Task batching:**
- Group similar tasks (reading papers, coding, writing)
- Reduce context switching

### Integration with TaskNotes

**Time estimate from task:**
```yaml
---
timeEstimate: 120  # minutes
priority: high
---
```

Use task's `timeEstimate` for block duration.

**Update task after scheduling:**
```yaml
---
scheduled: 2025-11-19
calendarBlock: true
---
```

### Error Handling

**If no free time:**
- Message: "No available time slots today. Calendar is full."
- Suggest: Tomorrow or specific time

**If task not found:**
- Message: "Task [[Task Name]] not found in 00_Inbox/Tasks/"
- Verify: Task name spelling

**If calendar conflict:**
- Message: "Conflict at 14:00 with: [Existing Event]"
- Suggest: Next available slot

### Advanced Features

**1. Focus mode:**
```bash
/pkm:gcal-block --focus 4
```
Create 4-hour protected deep work block (no meetings).

**2. Recurring blocks:**
```bash
/pkm:gcal-block "[[Weekly Review]]" --recur weekly-friday-16:00
```

**3. Flexible timing:**
```bash
/pkm:gcal-block --auto --prefer-morning
```
Schedule tasks in morning hours only.

### Defaults

- **Duration:** 90 minutes (🍅🍅🍅)
- **Buffer:** 15 minutes between blocks
- **Deep work hours:** 09:00-12:00
- **Event prefix:** 🎯 (focus block indicator)

### Notes

- Time blocks appear in Google Calendar immediately
- Sync across all devices
- Can reschedule by dragging in Google Calendar
- Task completion doesn't auto-delete block (manual cleanup)
