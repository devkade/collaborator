# PR Submission Checklist

**Issue:** #[number]
**PR Title:** [Type]: [Brief description]
**Branch:** [branch-name]
**Date:** [date]

---

## Pre-Submission Checklist

### Code Quality

- [ ] **All tests pass locally**
  ```bash
  [test command]
  # Output: [all passing]
  ```

- [ ] **Linting passes**
  ```bash
  [lint command]
  # Output: [no errors]
  ```

- [ ] **Build succeeds**
  ```bash
  [build command]
  # Output: [success]
  ```

- [ ] **Type checking passes** (if applicable)
  ```bash
  [type check command]
  # Output: [no errors]
  ```

- [ ] **No compiler warnings**
  - Checked: Yes / No / N/A

### Functionality

- [ ] **All requirements implemented**
  - Requirement 1: ✅
  - Requirement 2: ✅
  - Requirement 3: ✅

- [ ] **Edge cases handled**
  - Empty input: ✅
  - Null/undefined: ✅
  - Large data: ✅
  - Invalid input: ✅
  - [Other edge cases]: ✅

- [ ] **Error handling complete**
  - Error messages clear
  - Graceful degradation
  - No crashes

- [ ] **Manual testing done**
  - Tested on: [environment]
  - Test scenarios: [list]
  - Results: [all passed]

### Testing

- [ ] **New tests added**
  - Unit tests: [count] added
  - Integration tests: [count] added
  - Test coverage: [percentage]

- [ ] **Test quality**
  - Tests are meaningful (not just for coverage)
  - Tests follow project conventions
  - Tests have clear names
  - Tests are independent

- [ ] **Existing tests still pass**
  - All passing: Yes
  - Any skipped: No
  - Any modified: [list with reason]

### Documentation

- [ ] **Code comments added**
  - Complex logic explained
  - Public APIs documented
  - TODOs addressed or tracked

- [ ] **README updated** (if needed)
  - New features documented
  - Examples added
  - Installation updated

- [ ] **CHANGELOG entry added**
  ```markdown
  ## [Unreleased]
  ### [Added/Fixed/Changed]
  - [Description] (#[issue])
  ```

- [ ] **API docs updated** (if applicable)
  - Parameters documented
  - Return values documented
  - Examples provided

### Git Hygiene

- [ ] **Branch is up to date with main**
  ```bash
  git fetch origin
  git rebase origin/main
  # Conflicts resolved: Yes/No
  ```

- [ ] **Commits are clean**
  - Logical commits: Yes
  - Clear messages: Yes
  - No merge commits: Yes (or rebased)

- [ ] **No sensitive data**
  - No API keys
  - No passwords
  - No personal data
  - No secrets in history

- [ ] **No unintended changes**
  - No debug code
  - No commented code
  - No formatting-only changes (unless intended)
  - No temp files

### Self-Review

- [ ] **Reviewed entire diff**
  - Read through all changes
  - Checked for issues
  - Verified quality

- [ ] **Code is clear**
  - Variable names are descriptive
  - Functions have single responsibility
  - Logic is straightforward
  - Comments where needed

- [ ] **Follows conventions**
  - Naming matches project style
  - Formatting is consistent
  - Patterns match existing code
  - No new paradigms introduced

- [ ] **No obvious bugs**
  - Logic is correct
  - Edge cases handled
  - No potential null errors
  - No off-by-one errors

### Completeness

- [ ] **All acceptance criteria met**
  - [Criterion 1]: ✅
  - [Criterion 2]: ✅
  - [Criterion 3]: ✅

- [ ] **Issue fully resolved**
  - Nothing left to do
  - No half-implemented features
  - No TODOs left unaddressed

- [ ] **No scope creep**
  - Only issue requirements addressed
  - No unrelated changes
  - Additional ideas tracked separately

---

## PR Description Draft

### Title
```
[Type]: [Clear, concise description (50-70 chars)]
```

### Description
```markdown
## Summary
[2-3 sentences: what, why, how]

## Changes Made
- [Change 1]
- [Change 2]
- [Change 3]

## Type of Change
- [x] [Selected type]

## Related Issue
Fixes #[issue-number]

## How to Test
1. [Step 1]
2. [Step 2]
3. [Verify result]

## Screenshots (if applicable)
[Add screenshots or remove section]

## Checklist
- [x] Code follows style guidelines
- [x] Self-reviewed
- [x] Commented hard-to-understand areas
- [x] Documentation updated
- [x] No new warnings
- [x] Tests added and passing

## Additional Notes
[Any context, tradeoffs, or future work]
```

---

## CI/CD Preparation

### Expected CI Checks

- [ ] **Tests** - Should pass
- [ ] **Linting** - Should pass
- [ ] **Type checking** - Should pass
- [ ] **Build** - Should succeed
- [ ] **Coverage** - Should meet threshold ([X]%)
- [ ] **[Other checks]** - [Expected result]

### If CI Fails

**Plan:**
1. Check logs immediately
2. Reproduce locally
3. Fix and push update
4. Don't wait for reviewer if CI failing

---

## Communication Plan

### Before Creating PR

- [ ] **Comment on issue**
  "Submitted PR #[number] to address this issue"

- [ ] **Tag appropriately** (if permissions)
  - Type label (bug, enhancement, etc)
  - Status label (ready for review, etc)

### After Creating PR

- [ ] **Monitor CI**
  - Checks all passing
  - Fix any failures immediately

- [ ] **Request review** (if needed)
  - Specific reviewer requested
  - Or wait for maintainer assignment

- [ ] **Be responsive**
  - Check for comments daily
  - Respond within 24-48 hours
  - Make requested changes promptly

---

## Review Readiness

### Making Reviewer's Job Easy

- [ ] **PR is focused**
  - Single concern
  - Reasonable size (< 500 lines if possible)
  - Clear purpose

- [ ] **Context provided**
  - Clear description
  - Test instructions
  - Screenshots if UI change

- [ ] **Quality is high**
  - No obvious issues
  - Well-tested
  - Follows conventions

- [ ] **Ready for feedback**
  - Open to suggestions
  - Will respond promptly
  - Willing to iterate

### Potential Review Comments

**Prepare for:**
- Style/convention feedback → Will fix
- Architectural suggestions → Open to discuss
- Test coverage requests → Will add
- Documentation requests → Will improve
- Bug concerns → Will investigate

---

## Submission Commands

### Push Branch

```bash
# Ensure branch is up to date
git fetch origin
git rebase origin/main

# Push to remote
git push -u origin [branch-name]

# If rebased and need to force push
git push -f origin [branch-name]
```

### Create PR

**Via GitHub CLI:**
```bash
gh pr create \
  --title "[Type]: [Description]" \
  --body-file pr-description.md \
  --label [label] \
  --assignee @me
```

**Via Web:**
1. Go to repository on GitHub
2. Click "Pull requests"
3. Click "New pull request"
4. Select your branch
5. Fill in title and description
6. Create pull request

---

## Post-Submission

### Immediate Actions

- [ ] **Verify PR created successfully**
  - URL: [PR URL]
  - All info present
  - CI triggered

- [ ] **Comment on issue**
  "Submitted PR #[number]"

- [ ] **Monitor CI**
  - All checks running
  - Fix if any fail

### Ongoing

- [ ] **Respond to comments**
  - Check daily
  - Reply within 24-48 hours
  - Be constructive

- [ ] **Make requested changes**
  - Address feedback
  - Push updates
  - Mark comments resolved

- [ ] **Keep updated with main**
  - Rebase if requested
  - Resolve conflicts promptly

---

## Merge Preparation

### Before Merge

- [ ] **All reviews approved**
  - Required approvals received
  - No unresolved comments

- [ ] **CI passing**
  - All checks green
  - No failures

- [ ] **Up to date with main**
  - No merge conflicts
  - Latest changes incorporated

- [ ] **Final review**
  - Re-check changes
  - Verify quality
  - Confirm ready

### After Merge

- [ ] **Update local repository**
  ```bash
  git checkout main
  git pull origin main
  ```

- [ ] **Delete feature branch**
  ```bash
  git branch -d [branch-name]
  git push origin --delete [branch-name]
  ```

- [ ] **Close related issues** (if not auto-closed)
  - Issue #[number] closed

- [ ] **Celebrate!** 🎉
  - Contribution merged
  - Value added to project
  - Experience gained

---

## Troubleshooting

### Common Issues

**CI Failing:**
- Check logs carefully
- Reproduce locally
- Fix and push update
- Don't wait for reviewer

**Merge Conflicts:**
- Rebase on main
- Resolve conflicts
- Test still passes
- Force push if needed

**Review Taking Long:**
- Be patient
- Maintainers are busy
- Polite ping after 1-2 weeks
- Don't take personally

**Changes Requested:**
- Thank reviewer
- Ask questions if unclear
- Make changes promptly
- Push updates

---

## Notes

[Personal notes, reminders, or considerations]

**Lessons Learned:**
[Note anything learned during this contribution for future reference]
