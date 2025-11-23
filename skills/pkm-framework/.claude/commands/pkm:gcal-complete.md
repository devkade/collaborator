You are helping mark task completion in Google Calendar using gcalcli.

## Context
- Calendar: 00_Schedule (main calendar only)
- Tool: gcalcli CLI
- TaskNotes: Tasks complete with `- [x] [[Task Name]] ✅ YYYY-MM-DD`
- Integration: Sync task completion status to calendar

## Task
When a TaskNotes task is marked complete, update the corresponding calendar event to reflect completion.

### Use Cases

**1. Mark single task complete:**
```bash
/pkm:gcal-complete "[[SWSP25 Problem Definition]]"
```
Updates calendar event to show task is done.

**2. Auto-sync completions:**
```bash
/pkm:gcal-complete --sync
```
Syncs all completed tasks from today's daily note to calendar.

**3. Daily review integration:**
Called automatically by `/pkm:daily-review` to update calendar after review.

### Steps:

#### Single Task Completion

1. **Parse task name:**
   - Input: `[[Task Name]]`
   - Extract task name from wikilink

2. **Find calendar event:**
   ```bash
   gcalcli --calendar "00_Schedule" \
           search "Task Name"
   ```
   Look for events with task name in title or description.

3. **Update event:**
   ```bash
   # Option 1: Prepend ✅ to title
   gcalcli --calendar "00_Schedule" \
           edit "EVENT_ID" \
           --title "✅ Task Name"

   # Option 2: Add completion note to description
   gcalcli --calendar "00_Schedule" \
           edit "EVENT_ID" \
           --description "Completed: YYYY-MM-DD HH:MM"
   ```

4. **Confirm:**
   ```markdown
   ✅ Calendar updated: [[Task Name]] marked complete
   ```

#### Auto-Sync Today's Completions

1. **Read today's daily note:**
   - Path: `~/Obsidian/Altellus/20_Notes/Journal/YYYY/Mnn/YYYY-MM-DD.md`
   - Extract "오늘 완료" section
   - Find: `- [x] [[Task Name]] ✅ YYYY-MM-DD`

2. **For each completed task:**
   - Search calendar for matching event
   - If found, update with ✅ marker
   - If not found, skip (not time-blocked)

3. **Summary:**
   ```markdown
   ✅ **Calendar sync complete:**

   Updated events:
   - ✅ [[Task: Daily 템플릿 확정]]
   - ✅ [[ELEGNT 논문 리뷰]]

   Not in calendar:
   - [[Quick email reply]] (not time-blocked)

   Total synced: 2/3 tasks
   ```

### Output Format

**Single task:**
```markdown
✅ **Calendar Event Updated:**

- **Task:** [[SWSP25 Problem Definition]]
- **Event:** "🎯 SWSP25 Problem Definition" → "✅ SWSP25 Problem Definition"
- **Completed:** 2025-11-19 15:45

Calendar reflects task completion ✅
```

**Sync summary:**
```markdown
✅ **Daily Completion Sync:**

**Updated (3):**
- ✅ [[Task: Daily 템플릿 확정]] (09:00-10:30)
- ✅ [[Task: Weekly Summary 재작성]] (11:00-12:00)
- ✅ [[ELEGNT 논문 리뷰]] (15:00-17:00)

**Not time-blocked (2):**
- ✅ [[Quick email reply]]
- ✅ [[Update README]]

**Calendar sync:** 3/5 tasks
```

### Update Strategies

**Strategy 1: Title Update (Recommended)**
- Before: `🎯 SWSP25 Problem Definition`
- After: `✅ SWSP25 Problem Definition`
- Visual: Easy to spot in calendar
- Preserves: Original event structure

**Strategy 2: Color Change**
- Change event color to green (completed)
- Requires: gcalcli color support
- Visual: Color-coded completion

**Strategy 3: Description Note**
- Add to description: `Completed: 2025-11-19 15:45`
- Preserves: Title unchanged
- Detail: Exact completion timestamp

**Default: Strategy 1 (Title Update)**

### Integration with Daily Review

`/pkm:daily-review` automatically calls this command:

```bash
# Daily review workflow:
1. Extract completed tasks
2. Update calendar events: /pkm:gcal-complete --sync
3. Generate review section
```

User sees:
```markdown
### 오늘 완료
- [x] [[Task: Daily 템플릿 확정]] ✅ 2025-11-18
  _Calendar updated_ ✅
```

### Smart Matching

**Find events by:**
1. Exact title match: "🎯 Task Name" = "Task Name"
2. Description match: Contains "TaskNotes: [[Task Name]]"
3. Fuzzy match: Similar title (85%+ match)
4. Time range: Within today's events only

**Disambiguation:**
If multiple matches:
- Prefer: Today's events over future
- Prefer: Exact title match over fuzzy
- Ask: User to confirm if ambiguous

### Error Handling

**If event not found:**
- Message: "No calendar event found for [[Task Name]]"
- Reason: "Task was not time-blocked"
- Action: Skip (not an error)

**If multiple matches:**
- Message: "Multiple events found for [[Task Name]]:"
- List: All matching events with times
- Ask: "Which one to update? (1/2/3)"

**If already marked complete:**
- Message: "Event already marked complete: ✅ [[Task Name]]"
- Action: Skip (idempotent)

**If gcalcli fails:**
- Message: "Unable to update calendar. Check authentication."
- Suggest: Run `gcalcli init`

### Advanced Features

**1. Batch update:**
```bash
/pkm:gcal-complete --all
```
Updates all completed tasks from today's note.

**2. Retroactive sync:**
```bash
/pkm:gcal-complete --date 2025-11-18
```
Syncs completions from a past date.

**3. Undo completion:**
```bash
/pkm:gcal-complete --undo "[[Task Name]]"
```
Removes ✅ marker (if task was uncompleted).

### Completion Metadata

**Store in event description:**
```
Completed: 2025-11-19 15:45
Pomodoros: 3 🍅🍅🍅
Notes: Finished earlier than expected
```

**Benefits:**
- Track actual vs estimated time
- Review completion patterns
- Inform future time estimates

### Weekly Review Integration

Weekly review shows:
```markdown
### 주간 완료 태스크
- [x] [[Task A]] ✅ (90min, est 120min) - 25% faster
- [x] [[Task B]] ✅ (120min, est 90min) - 33% slower

**Insights:** Complex tasks taking longer than estimated.
```

### Notes

- Only updates time-blocked tasks (calendar events exist)
- Non-blocked tasks skip update (normal behavior)
- Preserves event time and other details
- Completion marker: ✅ (universally recognized)
- Can manually undo in Google Calendar UI
