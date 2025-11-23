---
name: pkm-framework
description: Comprehensive Personal Knowledge Management framework for Obsidian with temporal reviews, capture, linking, and analytics
---

# PKM Framework

A complete Personal Knowledge Management system for Obsidian vaults with temporal reviews, smart capture, note linking, and analytics. Designed to work seamlessly with Periodic Notes and integrate with your daily workflow.

## Overview

The PKM Framework provides a structured approach to managing knowledge in Obsidian, with a focus on:

- **Temporal Reviews**: Daily, weekly, and monthly reflection and planning
- **Smart Capture**: Quick note and meeting capture workflows
- **Note Linking**: Intelligent connections between related notes
- **Organization**: Project management and Zettelkasten support
- **Analytics**: Insights into your PKM system health and usage

## Features

### 🗓️ Temporal Reviews

Build a consistent review habit with automated temporal note management:

- **Daily Setup** (`/pkm:daily-setup`) - Morning routine to start your day with yesterday's summary and carried-over tasks
- **Daily Review** (`/pkm:daily-review`) - Evening reflection with tasks completed, time usage, insights, and tomorrow's suggestions
- **Weekly Review** (`/pkm:weekly-review`) - Weekly summary aggregating 7 days with KPIs, project status, and next week's priorities
- **Monthly Review** (`/pkm:monthly-review`) - Monthly overview aggregating weekly data with goal tracking and long-term patterns

### 📝 Smart Capture (Coming Soon)

Capture information quickly without disrupting your flow:

- **Quick Capture** - Rapid note capture to inbox or daily note
- **Meeting Notes** - Structured meeting notes with calendar integration

### 🔗 Note Linking (Coming Soon)

Build a connected knowledge base:

- **Smart Linking** - Automatically suggest relevant note connections
- **Backlink Analysis** - Analyze note connections and identify clusters

### 📂 Organization (Coming Soon)

Keep your vault organized and maintainable:

- **Project Notes** - Project note management and tracking
- **Zettelkasten** - Atomic note creation with proper linking
- **Periodic Cleanup** - Archive and cleanup old notes

### 📊 Analytics (Coming Soon)

Understand your PKM system:

- **PKM Statistics** - System health, usage statistics, and trends

## Quick Start

### Prerequisites

1. **Obsidian** with required plugins:
   - **Periodic Notes** (required)
   - **TaskNotes** (required) - For task management

2. **Vault structure**:
   ```
   ~/Obsidian/Altellus/
   ├── 00_Inbox/
   │   └── Tasks/              (TaskNotes tasks)
   ├── 20_Notes/
   │   └── Journal/
   │       └── YYYY/Mnn/
   │           ├── YYYY-MM-DD.md   (daily notes)
   │           ├── YYYY-Www.md     (weekly notes)
   │           └── YYYY-Mmm.md     (monthly notes)
   └── 90_Templates/
       └── Temporal/
           └── Daily.md
   ```

3. **gcalcli** (optional, for calendar integration):
   ```bash
   pip install gcalcli
   gcalcli init  # OAuth setup
   ```

### Installation

The PKM Framework is available as a plugin in the Claude Code marketplace:

```bash
# Install via marketplace (when available)
/skills install pkm-framework
```

### Basic Workflow

**Morning Routine:**
```bash
/pkm:daily-setup
```

**Evening Routine:**
```bash
/pkm:daily-review
```

**Weekly Review (Friday or Sunday):**
```bash
/pkm:weekly-review
```

**Monthly Review (End of month):**
```bash
/pkm:monthly-review
```

## Commands Reference

### Main Command

- `/pkm` - Main PKM menu (displays available commands)

### Temporal Reviews

- `/pkm:daily-setup` - Generate morning Daily Notes section
- `/pkm:daily-review` - Complete evening Daily Review section
- `/pkm:weekly-review` - Generate Weekly Summary
- `/pkm:monthly-review` - Generate Monthly Summary

### Capture (Coming Soon)

- `/pkm:quick-capture` - Quick capture to inbox or daily note
- `/pkm:meeting-notes` - Create meeting note with calendar sync

### Linking (Coming Soon)

- `/pkm:note-linking` - Smart linking between related notes
- `/pkm:backlink-analysis` - Analyze note connections

### Organization (Coming Soon)

- `/pkm:project-notes` - Project note management
- `/pkm:zettelkasten` - Create atomic note
- `/pkm:periodic-cleanup` - Archive old notes

### Analytics (Coming Soon)

- `/pkm:stats` - PKM system statistics

## Configuration

### Obsidian Vault Path

The default vault path is `~/Obsidian/Altellus`. If your vault is located elsewhere, you'll need to update the paths in the command files.

### Required Obsidian Plugins

1. **Periodic Notes** - For temporal note structure
2. **Templater** (optional) - For advanced templates
3. **Dataview** (optional) - For query-based views

### Integration with Google Calendar

The daily review feature integrates with Google Calendar through the `gcal-review` skill. Ensure you have calendar access configured.

## Vault Structure

### Required Folders

```
20_Notes/
  Journal/           # Temporal notes (daily, weekly, monthly)
    YYYY/
      Mnn/
        YYYY-MM-DD.md   # Daily notes
        YYYY-Www.md     # Weekly notes
        YYYY-Mmm.md     # Monthly notes
  Projects/          # Project notes (future)
  Zettels/          # Atomic notes (future)
  Meetings/         # Meeting notes (future)
  Inbox/            # Quick capture (future)

90_Templates/
  Temporal/         # Temporal note templates
    Daily.md        # Daily note template
    Weekly.md       # Weekly note template (future)
    Monthly.md      # Monthly note template (future)
```

## Workflows

### Daily Workflow

**Morning (5 minutes):**
1. Run `/pkm:daily-setup`
2. Review yesterday's summary
3. Check carried-over tasks
4. Set today's focus

**During the day:**
- Add notes and tasks to daily note
- Track pomodoros in YAML frontmatter
- Link to related notes

**Evening (5-10 minutes):**
1. Run `/pkm:daily-review`
2. Review completed tasks
3. Reflect on time usage
4. Capture insights
5. Plan tomorrow

### Weekly Workflow

**Friday or Sunday (20-30 minutes):**
1. Run `/pkm:weekly-review`
2. Review weekly highlights
3. Check KPIs and patterns
4. Assess project status
5. Identify blockers
6. Set next week's priorities

### Monthly Workflow

**End of month (30-45 minutes):**
1. Run `/pkm:monthly-review`
2. Review monthly achievements
3. Check goal progress
4. Identify long-term patterns
5. Address persistent blockers
6. Set next month's objectives

## Data Formats

### Daily Note YAML Frontmatter (TaskNotes)

```yaml
---
para: Note
type: journal
pomodoros:
  - id: "1763434005196"
    startTime: 2025-11-18T11:46:45.196+09:00
    endTime: 2025-11-18T12:02:13.144+09:00
    plannedDuration: 25
    type: work
    taskPath: 00_Inbox/ELEGNT 논문.md
    completed: true
---
```

### Task Format (TaskNotes)

- **Incomplete**: `- [ ] [[Task Name]]`
- **Completed**: `- [x] [[Task Name]] ✅ 2025-11-19`
- **Tasks** are individual markdown files in `00_Inbox/Tasks/`

### Pomodoro Display

- Visual: `ELEGNT 논문 - 🍅🍅🍅: 3`
- Total: `총 🍅🍅🍅🍅: 4 pomodoros`
- Count: Length of `pomodoros` array in YAML

### Time Tracking

- **Pomodoros**: From TaskNotes YAML `pomodoros` array
- **Calendar events**: From gcalcli (00_Schedule calendar)
- **Task tracking**: TaskNotes task files + wikilinks

## Integration with TaskNotes

### Task Management

- Tasks stored in `00_Inbox/Tasks/` as individual markdown files
- Referenced in daily notes as `- [ ] [[Task Name]]` wikilinks
- Completed tasks: `- [x] [[Task Name]] ✅ YYYY-MM-DD`

### Pomodoro Tracking

- TaskNotes tracks pomodoros in YAML frontmatter
- Each pomodoro includes: startTime, endTime, taskPath
- PKM Framework reads `pomodoros` array length for totals

### Calendar Sync (gcalcli)

- Time blocks created from tasks: `/pkm:gcal-block`
- Task completion synced to calendar: `/pkm:gcal-complete`
- Calendar events displayed in daily review
- 00_Schedule calendar only

## Troubleshooting

### Daily note not found
- Ensure Periodic Notes plugin is configured correctly
- Check vault path is `~/Obsidian/Altellus`
- Verify folder structure exists

### Tasks not recognized
- Ensure TaskNotes plugin is installed and configured
- Task files must be in `00_Inbox/Tasks/` folder
- Use wikilink format: `- [ ] [[Task Name]]`

### Calendar integration not working
- Install gcalcli: `pip install gcalcli`
- Authenticate: `gcalcli init`
- Verify 00_Schedule calendar exists in Google Calendar

### Pomodoros showing zeros
- Verify TaskNotes is tracking pomodoros
- Check YAML frontmatter has `pomodoros` array
- Ensure pomodoro tracking is enabled in TaskNotes settings

### Related notes not auto-filled
- Ensure daily note has Notes section
- Verify pomodoros have `taskPath` field
- Check wikilinks are properly formatted: `[[Note Name]]`

## Version

**Current Version**: 1.0.0

### What's Included (Phase 1)

- ✅ Daily Setup skill
- ✅ Daily Review skill
- ✅ Weekly Review skill
- ✅ Monthly Review skill
- ✅ Temporal workflow documentation

### Coming in Future Versions

- 📝 Capture skills (quick-capture, meeting-notes)
- 🔗 Linking skills (note-linking, backlink-analysis)
- 📂 Organization skills (project-notes, zettelkasten, periodic-cleanup)
- 📊 Analytics skills (pkm-stats)

## Contributing

This PKM Framework is designed to be extensible. Future skills can be added to enhance the system.

## License

Part of the Collaborator plugin collection.

## Support

For issues, questions, or feature requests, please refer to the main documentation in `./docs/pkm/`.
