# Issue Patterns Reference

Common issue types and specialized approaches for each.

## Bug Reports

### Characteristics
- Something is broken
- Current behavior doesn't match expected
- Often includes error messages
- May have reproduction steps

### Analysis Pattern

**1. Reproduce**
- Follow reproduction steps exactly
- Verify bug exists
- Note environment details

**2. Isolate**
- Minimal test case
- Remove unrelated factors
- Identify triggering conditions

**3. Locate**
- Find where error occurs
- Trace backwards to cause
- Identify root cause vs symptoms

**4. Fix Strategy**
- Fix root cause, not symptoms
- Handle similar edge cases
- Don't break working cases
- Add regression test

### Common Bug Patterns

**Null/Undefined Errors:**
```javascript
// Bug: Crashes when data is null
function process(data) {
  return data.value // TypeError if data is null
}

// Fix: Handle null case
function process(data) {
  if (!data) return defaultValue
  return data.value
}

// Test
expect(process(null)).toBe(defaultValue)
```

**Off-by-One Errors:**
```python
# Bug: Skips last element
for i in range(len(arr) - 1):
    process(arr[i])

# Fix
for i in range(len(arr)):
    process(arr[i])

# Or better
for item in arr:
    process(item)
```

**Race Conditions:**
```javascript
// Bug: State changes between check and use
if (cache.has(key)) {
  return cache.get(key) // Might be deleted by now
}

// Fix: Get once, check result
const value = cache.get(key)
if (value !== undefined) {
  return value
}
```

**Input Validation:**
```javascript
// Bug: No validation
function divide(a, b) {
  return a / b // Division by zero
}

// Fix: Validate inputs
function divide(a, b) {
  if (b === 0) {
    throw new Error('Division by zero')
  }
  return a / b
}
```

---

## Feature Requests

### Characteristics
- Request for new functionality
- Describes user need
- May include use cases
- May have mockups/examples

### Analysis Pattern

**1. Understand Need**
- Who needs this?
- What problem does it solve?
- What are use cases?
- Why existing features insufficient?

**2. Design API/Interface**
- How will users interact?
- What's the simplest interface?
- Consistent with existing features?
- Extensible for future needs?

**3. Plan Implementation**
- Where does it fit architecturally?
- What components affected?
- Data model changes needed?
- Breaking changes?

**4. Implementation Strategy**
- Start with minimal viable version
- Add polish incrementally
- Get feedback early
- Document well

### Feature Types

**UI Feature:**
```markdown
**Checklist:**
- [ ] Component implementation
- [ ] State management
- [ ] Event handling
- [ ] Styling
- [ ] Responsive design
- [ ] Accessibility
- [ ] Loading states
- [ ] Error states
- [ ] User feedback (success/error messages)
```

**API Endpoint:**
```markdown
**Checklist:**
- [ ] Route definition
- [ ] Request validation
- [ ] Business logic
- [ ] Response formatting
- [ ] Error handling
- [ ] Authentication/authorization
- [ ] Rate limiting (if needed)
- [ ] API documentation
- [ ] Integration tests
```

**CLI Command:**
```markdown
**Checklist:**
- [ ] Command definition
- [ ] Argument parsing
- [ ] Validation
- [ ] Core logic
- [ ] Output formatting
- [ ] Error messages
- [ ] Help text
- [ ] Examples in docs
```

**Library Function:**
```markdown
**Checklist:**
- [ ] Function signature design
- [ ] Input validation
- [ ] Core implementation
- [ ] Error handling
- [ ] Documentation (JSDoc/docstrings)
- [ ] Usage examples
- [ ] Type definitions
- [ ] Backwards compatibility
```

---

## Documentation Issues

### Characteristics
- Missing or unclear docs
- Outdated information
- Requests for examples
- Typos or formatting

### Analysis Pattern

**1. Identify Gap**
- What's missing?
- Who's the audience?
- What level of detail?
- Where should it live?

**2. Research**
- Understand the feature fully
- Find code examples
- Check similar docs
- Verify current behavior

**3. Write**
- Clear and concise
- Examples included
- Proper formatting
- Links to related docs

**4. Verify**
- Technically accurate
- Examples work
- No broken links
- Proper grammar/spelling

### Documentation Types

**Tutorials:**
```markdown
**Structure:**
1. What you'll build
2. Prerequisites
3. Step-by-step instructions
4. Expected results
5. Next steps

**Style:**
- Conversational
- Hand-holding
- Complete working example
- Learn by doing
```

**How-To Guides:**
```markdown
**Structure:**
1. Problem statement
2. Solution approach
3. Step-by-step
4. Variations/alternatives

**Style:**
- Task-oriented
- Practical
- Assumes some knowledge
- Shows best practices
```

**Reference:**
```markdown
**Structure:**
1. Function/API signature
2. Parameters
3. Return value
4. Errors/exceptions
5. Examples
6. See also

**Style:**
- Precise
- Complete
- Technical
- Searchable
```

**Conceptual:**
```markdown
**Structure:**
1. Overview
2. Key concepts
3. How it works
4. When to use
5. Related topics

**Style:**
- Explanatory
- Big picture
- Theory and context
- Understanding-focused
```

---

## Refactoring Issues

### Characteristics
- Code quality improvement
- No behavior change
- Technical debt
- Maintainability focus

### Analysis Pattern

**1. Identify Problems**
- Code smells
- Duplication
- Complexity
- Poor naming
- Tight coupling

**2. Ensure Test Coverage**
- Tests exist for current behavior
- Tests are comprehensive
- Tests will catch regressions

**3. Plan Incremental Steps**
- Small, safe transformations
- Each step leaves code working
- Can pause/resume anytime

**4. Execute Carefully**
- One refactoring at a time
- Run tests after each step
- Commit working states
- Don't mix with feature work

### Refactoring Patterns

**Extract Function:**
```javascript
// Before: Long complex function
function processOrder(order) {
  // 50 lines of code
  // mixing concerns
}

// After: Extracted smaller functions
function processOrder(order) {
  validateOrder(order)
  const items = prepareItems(order.items)
  const total = calculateTotal(items)
  return createInvoice(order, items, total)
}

function validateOrder(order) { /* ... */ }
function prepareItems(items) { /* ... */ }
function calculateTotal(items) { /* ... */ }
function createInvoice(order, items, total) { /* ... */ }
```

**Remove Duplication:**
```python
# Before: Duplicated logic
def process_user_data(data):
    if not data:
        raise ValueError("Invalid data")
    # process...

def process_order_data(data):
    if not data:
        raise ValueError("Invalid data")
    # process...

# After: Extracted common logic
def validate_data(data):
    if not data:
        raise ValueError("Invalid data")

def process_user_data(data):
    validate_data(data)
    # process...

def process_order_data(data):
    validate_data(data)
    # process...
```

**Improve Naming:**
```javascript
// Before: Unclear names
function calc(x, y) {
  const t = x * y
  const d = t * 0.1
  return t - d
}

// After: Clear names
function calculateTotalWithDiscount(price, quantity) {
  const subtotal = price * quantity
  const discount = subtotal * 0.1
  return subtotal - discount
}
```

**Reduce Complexity:**
```javascript
// Before: Deep nesting
function process(data) {
  if (data) {
    if (data.items) {
      if (data.items.length > 0) {
        // process
      }
    }
  }
}

// After: Early returns
function process(data) {
  if (!data) return
  if (!data.items) return
  if (data.items.length === 0) return

  // process
}
```

---

## Performance Issues

### Characteristics
- Something is slow
- Resource usage high
- Scalability problems
- May include benchmarks

### Analysis Pattern

**1. Measure**
- Reproduce performance issue
- Measure current performance
- Profile to find bottleneck
- Get baseline numbers

**2. Identify Cause**
- Algorithm complexity
- Unnecessary work
- Resource leaks
- Inefficient data structures

**3. Optimize**
- Fix the bottleneck
- Use better algorithm
- Cache when appropriate
- Lazy load when possible

**4. Verify**
- Measure improvement
- Check correctness maintained
- Verify no regressions
- Document tradeoffs

### Performance Patterns

**Algorithm Optimization:**
```javascript
// Before: O(n²)
function findDuplicates(arr) {
  const dupes = []
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) {
        dupes.push(arr[i])
      }
    }
  }
  return dupes
}

// After: O(n)
function findDuplicates(arr) {
  const seen = new Set()
  const dupes = new Set()
  for (const item of arr) {
    if (seen.has(item)) {
      dupes.add(item)
    }
    seen.add(item)
  }
  return Array.from(dupes)
}
```

**Caching:**
```javascript
// Before: Recalculates every time
function expensiveCalculation(data) {
  // Heavy computation
  return result
}

// After: Cache results
const cache = new Map()
function expensiveCalculation(data) {
  const key = JSON.stringify(data)
  if (cache.has(key)) {
    return cache.get(key)
  }
  const result = /* heavy computation */
  cache.set(key, result)
  return result
}
```

**Lazy Loading:**
```javascript
// Before: Load everything upfront
const data = loadAllData() // Slow!

// After: Load on demand
let data = null
function getData() {
  if (!data) {
    data = loadAllData()
  }
  return data
}
```

---

## Security Issues

### Characteristics
- Security vulnerability
- Potential exploit
- Missing validation
- Unsafe practices

### Analysis Pattern

**1. Assess Severity**
- What can attacker do?
- What data is at risk?
- Who is affected?
- How easy to exploit?

**2. Identify Root Cause**
- Missing validation?
- Unsafe API usage?
- Incorrect logic?
- Outdated dependency?

**3. Fix Securely**
- Validate all inputs
- Use safe APIs
- Follow security best practices
- Don't roll your own crypto

**4. Verify Fix**
- Test exploit no longer works
- Check similar code
- Add security tests
- Consider security review

### Security Patterns

**Input Validation:**
```javascript
// Before: No validation
app.post('/user/:id', (req, res) => {
  const query = `SELECT * FROM users WHERE id = ${req.params.id}`
  db.query(query) // SQL injection!
})

// After: Validated and parameterized
app.post('/user/:id', (req, res) => {
  const id = parseInt(req.params.id, 10)
  if (isNaN(id)) {
    return res.status(400).json({ error: 'Invalid ID' })
  }
  const query = 'SELECT * FROM users WHERE id = ?'
  db.query(query, [id]) // Safe
})
```

**XSS Prevention:**
```javascript
// Before: Direct HTML insertion
element.innerHTML = userInput // XSS!

// After: Escaped text
element.textContent = userInput // Safe
// Or use framework's escaping
element.innerHTML = escapeHtml(userInput)
```

**Authorization:**
```javascript
// Before: No auth check
app.delete('/user/:id', (req, res) => {
  deleteUser(req.params.id) // Anyone can delete!
})

// After: Check permissions
app.delete('/user/:id', requireAuth, (req, res) => {
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' })
  }
  deleteUser(req.params.id)
})
```

---

## CI/CD Issues

### Characteristics
- Build failures
- Test flakiness
- Deployment problems
- Pipeline configuration

### Analysis Pattern

**1. Reproduce Locally**
- Can you reproduce the issue?
- Environment differences?
- Missing dependencies?

**2. Identify Cause**
- Check CI logs
- Look for error messages
- Compare with working runs
- Check recent changes

**3. Fix**
- Update configuration
- Fix flaky tests
- Add missing dependencies
- Improve reliability

**4. Verify**
- Passes consistently
- Doesn't break other jobs
- Works across environments

### CI/CD Patterns

**Flaky Test Fix:**
```javascript
// Before: Flaky due to timing
test('updates after delay', () => {
  triggerUpdate()
  expect(getValue()).toBe(newValue) // Sometimes fails
})

// After: Proper async handling
test('updates after delay', async () => {
  triggerUpdate()
  await waitFor(() => expect(getValue()).toBe(newValue))
})
```

**Environment-Specific Fix:**
```javascript
// Before: Assumes specific OS
const path = '/usr/local/bin' // Fails on Windows

// After: Cross-platform
const path = require('path').join(os.homedir(), 'bin')
```

---

## Dependency Updates

### Characteristics
- Upgrade library version
- Fix security vulnerability
- Get new features
- Maintenance

### Analysis Pattern

**1. Check Changes**
- Read changelog
- Review breaking changes
- Check migration guide
- Assess impact

**2. Update**
- Update package version
- Update code if needed
- Update tests
- Update docs

**3. Test Thoroughly**
- All tests pass
- Manual testing
- Check for regressions
- Verify new version works

**4. Document**
- Note breaking changes
- Update dependencies list
- Mention in changelog

---

## Using This Reference

When analyzing an issue:

1. Identify issue type
2. Read corresponding pattern
3. Follow analysis checklist
4. Apply relevant code patterns
5. Adapt to specific context

Each project and issue is unique - use these as starting points, not rigid rules.
