# Common Patterns and Pitfalls

This reference catalogs frequently encountered patterns in documents and common analytical pitfalls to avoid.

## Document Patterns

### Persuasive Techniques to Recognize

**Authority Appeals:**
- Pattern: "As [expert/company] does..."
- Watch for: Cherry-picked examples, ignoring context differences
- Question: Does their context match yours?

**Bandwagon Effects:**
- Pattern: "Everyone is moving to..."
- Watch for: Exaggeration of adoption, ignoring failures
- Question: What's the actual evidence? Who's not adopting and why?

**Complexity Hiding:**
- Pattern: "Simply do X" or "Just Y"
- Watch for: Downplaying difficulty, ignoring prerequisites
- Question: What's the real complexity? What could go wrong?

**False Dichotomies:**
- Pattern: "Either X or Y"
- Watch for: Missing middle ground, other alternatives
- Question: What other options exist?

**Survivorship Bias:**
- Pattern: Success stories without failure context
- Watch for: Missing information about what didn't work
- Question: How many tried and failed? What's the selection bias?

### Structural Patterns

**Problem-Solution-Benefit:**
- Common in tech blogs and marketing
- Watch for: Problem exaggeration, solution oversimplification
- Verify: Is problem real? Is solution complete?

**Before-After:**
- Common in retrospectives and case studies
- Watch for: Overfitting to specific context, ignoring other factors
- Verify: What else changed? Is causation clear?

**Theory-Evidence-Conclusion:**
- Common in academic and analytical writing
- Watch for: Evidence cherry-picking, logical leaps
- Verify: Is evidence representative? Does conclusion follow?

## Analytical Pitfalls

### Confirmation Bias

**Pattern:** Looking for information that confirms existing beliefs

**How it manifests:**
- Focusing on supporting evidence while ignoring contradictions
- Interpreting ambiguous information favorably
- Remembering hits and forgetting misses

**Counter-strategy:**
- Actively seek disconfirming evidence
- Steelman opposing views
- Ask "What would prove me wrong?"

### Dunning-Kruger Effect

**Pattern:** Overestimating understanding of complex topics

**How it manifests:**
- Thinking you understand after superficial reading
- Missing subtle complexities
- Overconfidence in applying concepts

**Counter-strategy:**
- Try to teach it to someone
- Attempt implementation
- Identify what you don't know

### Availability Heuristic

**Pattern:** Overweighting easily recalled examples

**How it manifests:**
- Recent experiences seem more relevant
- Vivid examples dominate thinking
- Common cases seem universal

**Counter-strategy:**
- Seek statistical baselines
- Look for quiet counterexamples
- Question representativeness

### Hindsight Bias

**Pattern:** "I knew it all along" after seeing outcomes

**How it manifests in retrospectives:**
- Outcomes seem more inevitable than they were
- Overlooking genuine uncertainty at decision time
- Undervaluing decisions that happened to work out

**Counter-strategy:**
- What was known at decision time?
- What uncertainties existed?
- What could have gone differently?

### Context Collapse

**Pattern:** Ignoring contextual constraints and factors

**How it manifests:**
- "Why don't they just..."
- Assuming your context matches author's
- Missing organizational/cultural factors

**Counter-strategy:**
- Map explicit context: stack, scale, team, timeline
- Identify implicit context: expertise, resources, constraints
- Consider counter-factuals: what if context differed?

## Content-Specific Patterns

### Tech Blog Patterns

**"Magic Solution" Pattern:**
- Presents one approach as universal answer
- Reality: Every approach has trade-offs
- Ask: When does this NOT work?

**"Works on My Machine" Pattern:**
- Success in specific environment
- Reality: May not generalize
- Ask: What's special about this environment?

**"Premature Optimization" Pattern:**
- Complex solution to simple problem
- Reality: Simpler approaches often sufficient
- Ask: What's the simplest approach that works?

### Retrospective Patterns

**"Hero's Journey" Pattern:**
- Obstacles → Struggles → Triumph
- Reality: Often luck, timing, or missing context
- Ask: What role did circumstances play?

**"Lessons Learned" Pattern:**
- Lists of takeaways
- Reality: May be overgeneralized
- Ask: What contexts do these apply to?

**"If I Knew Then" Pattern:**
- Advice from hindsight
- Reality: Knowledge wasn't available then
- Ask: What was actually knowable?

### Technical Documentation Patterns

**"Happy Path Only" Pattern:**
- Documents ideal use cases
- Reality: Edge cases and errors matter
- Ask: What can go wrong?

**"Assumes Expert" Pattern:**
- Missing prerequisite knowledge
- Reality: Users have varying backgrounds
- Ask: What's assumed as known?

**"Version Lag" Pattern:**
- Documentation trails implementation
- Reality: Features changed, docs didn't
- Ask: Is this current? What changed?

### Academic Paper Patterns

**"Novel Technique" Pattern:**
- Emphasizes novelty
- Reality: May be incremental or narrow
- Ask: What's genuinely new vs repackaged?

**"Statistical Significance" Pattern:**
- p < 0.05 therefore important
- Reality: Statistical ≠ practical significance
- Ask: What's the effect size? Does it matter?

**"Future Work" Pattern:**
- Lists limitations as future work
- Reality: May indicate fundamental flaws
- Ask: Are these minor gaps or major issues?

## Red Flags

Watch for these warning signs:

**Credibility Issues:**
- Anonymous or unclear authorship
- No sources for bold claims
- Credentials don't match domain
- Conflicts of interest not disclosed

**Methodological Issues:**
- Unreproducible steps
- Missing crucial details
- Cherry-picked results
- No discussion of alternatives

**Logical Issues:**
- Circular reasoning
- False dichotomies
- Correlation → causation
- Generalizing from single case

**Practical Issues:**
- "Just trust me" explanations
- Missing costs or trade-offs
- Ignoring deployment challenges
- Unrealistic assumptions

## Strengthening Your Analysis

### Build Reference Classes

**Instead of single data point:**
- How many have tried this?
- What's the success rate?
- What patterns exist across cases?

### Seek Disconfirmation

**Actively look for:**
- Opposing viewpoints
- Failure cases
- Limitations and boundaries
- Alternative explanations

### Map Uncertainty

**Identify what's:**
- Known and verified
- Assumed but reasonable
- Speculative or uncertain
- Unknown or missing

### Consider Stakeholders

**Ask who:**
- Benefits from this framing?
- Would disagree and why?
- Isn't represented here?
- Has conflicting incentives?

## Meta-Patterns

### Evolution of Ideas

**Trace idea lineage:**
- Where did this come from?
- How has it evolved?
- What criticisms emerged?
- What's the current consensus?

### Domain Transfer

**When ideas cross domains:**
- What gets lost in translation?
- What analogies are imperfect?
- What needs adaptation?

### Zeitgeist Effects

**Recognize current trends:**
- What's fashionable now?
- What pressures shape discourse?
- What's being over/under-valued?
- What will look different in 5 years?

## Practical Guidelines

**Before accepting claims:**
1. Identify the evidence provided
2. Consider alternative explanations
3. Check for context dependency
4. Assess generalizability
5. Verify with other sources

**Before applying ideas:**
1. Map context similarities/differences
2. Identify adaptation requirements
3. Consider failure modes
4. Start with small experiments
5. Build feedback mechanisms

**When uncertain:**
1. State your uncertainties explicitly
2. Identify what would resolve them
3. Estimate confidence levels
4. Plan validation steps
5. Remain open to revision
