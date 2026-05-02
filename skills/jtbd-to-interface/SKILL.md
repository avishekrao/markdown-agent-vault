---
name: jtbd-to-interface
description: >
Generative transformation of JTBD into interface specification. Jobs generate screens, not test them.
Normalized JTBDs (job statements, job maps, outcomes, personas)
Screen Spec - what screens exist, what they are on, what flow between them, what options by persona.
Be sure to use this skill when the user asks: generate an interface from jobs,
Design screens based on JTBD, "what screens are needed for these jobs", "turn jobs into an interface",
“From jobs to layouts”, “interface from jobs”, “screen spec from JTBD”, “what screens flow from jobs”
Jobs → Navigation, Jobs → Screens, Generate UI Speculation from JTBD, What Should Be on Screen
for this job”. Also use when a user downloads a file with a JTBD library or Job Architecture.
And he wants to get the interface structure. DO NOT use the JTBD lens to audit an existing interface.
This is a different approach (testing, not generation).
---

# Interface: Generative Transformation

You turn structured JTBDs into an interface specification. You don’t “draw an interface and then check through jobs,” but **jobs generate an interface. Every screen element exists because it was created by a particular job, outcome, or circumstance.

## philosophy

The interface is Job Architecture made visible. Sections = Big Jobs. Screens = Little Jobs. Screen state sequence = Job Map. Elements on the screen = Desired Outcomes. Display options = Circumstances × Personas.

If an element on the screen cannot be traced to a specific job, it is superfluous. If the job is not presented on any screen, it is a gap.

---

## Generative chain (5 levels)

Skill works consistently on 5 levels. Each level takes the output of the previous one and generates the next.

### Level 1: Big Jobs Navigation

**A list of Big Jobs (3-7 pieces) from Job Architecture.

What do you do?
1. Each Big Job is a top-level navigation section.
2. If Big Job has 2+ side jobs with fundamentally different contexts, subsection is allowed.
3. Navigation is built around the verbs of the user, not the nouns of the system.

** Output format:**
```
NAV-1: ← Big Job {job statement}
NAV-2: ← Big Job {job statement}
  NAV-2.1: {Subsection} ← Little Job "{job statement}"
  NAV-2.2: {Subsection} ← Little Job "{job statement}"
...
```

*Naming principle: * Partition name = what the user wants to do, not what the system stores. Replenish instead of Balance. “Run ads” instead of “Advertising accounts.” “Reward” instead of “Reward.”

**Control question: ** If you replace all partition names with Make X, the phrases should sound natural to the user.

### Level 2: Little Jobs - Screens

**Input:** Navigation map from Level 1 + list of Little Jobs tied to each Big Job.

What do you do?
1. Each meaningful Little Job = one screen (or screen state).
2. Trivial Little Jobs (1 action, 0 solutions) can be an element on the parent job screen, rather than a separate screen.
3. If Little Job serves several Big Jobs, the screen lives in the section where the job is performed more often. In the remaining sections there is a link / shortcut.

** Output format:**
```
SCREEN: {screen-id}
  Section: NAV-{N}
  Job: "{job statement}"
  Type: workspace | wizard | dashboard | list | detail | settings
  Frequency: daily | weekly | monthly | event-driven
  Persons: {list of people who use this screen}
  Related screens: {screen-id}
```

**Typology of screens** (determined by the nature of the job):

| Nature job | Screen type | When |
|-------------|-----------|-------|
| Monitoring, review | Dashboard | Job type Control, Monitor |
| | Wizard | Job type Launch, Setup |
| Collection management | List + Detail | Job type Manage, Organize |
| Daily work | Workspace | Job type Execute, Operate |
| Configuration | Settings | Job type Configure, Customize |

### Level 3: Job Map → Flow screen

**In:** Screen from Level 2 + Job Map (8 steps Ulwick) for this job.

What do you do?
1. Each Job Map step where the user needs to take an action or make a decision = a separate screen state or a wizard step.
2. The Define and Locate steps are often combined into a starting screen/shape.
3. The Monitor and Modify steps are often combined into a workbar.
4. The Conclude step is the confirmation/result screen.
5. Job Map is the order of navigation inside the screen (left to right, top to bottom).

** Output format:**
```
FLOW: {screen-id}

  STATE-1: {state name}
    Job Map step: Define/Locate
    What the user decides: {description of the solution}
    What to see: {information to solve}
    Action: {what the user does}
    > transition: STATE-2 (at: {condition})

  STATE-2: {state name}
    Job Map Step: Prepare/Confirm
    ...

  STATE-3: {state name}
    Job Map step: Execute
    ...
```

** Job Map steps that do not generate screen states:**
- If a step is fully automated by the system (there is no user decision), it does not generate a UI state, but can generate a notification or progress indicator.
- If two adjacent steps are always performed together without pause, combine them into one state.

### Level 4: Desired Outcomes

**Input:** Screen state from Level 3 + Desired Outcomes for each Job Map step.

What do you do?
1. Each Desired Outcome generates one or more UI elements that help the user achieve this outcome.
2. Outcome type “Minimize X” → an element that shows the current value of X (for control).
3. Outcome: Reduce time to Y or shortcut to Y.
4. Outcome type “Increase confidence in Z” → Z visualization, status, preview, confirmation.

** Output format:**
```
ELEMENTS: {screen-id} / STATE-{N}

  EL-1: {type of element}
    Outcome: "{desired outcome statement}"
    Purpose: {why does this element exist}
    Content: {what shows/does}
    Priority: primary | secondary | tertiary

  EL-2: {type of element}
    Outcome: "{desired outcome statement}"
    ...
```

**Typology of elements** (defined by outcome type):

| Outcome type | UI element | Example |
|------------|-----------|--------|
| Minimize error | Validation, preview, confirmation | "Check before sending" |
| Reduce time | Shortcut, autocomplete, template | "Repeat past replenishment" |
| Increase visibility | Metric, status bar, table | Current balance: X ku |
| Maintain control | Filter, sort, switch | "Show only my accounts" |
| Avoid risk | Warning, confirmation dialog, undo | “Are you sure? Cancellation impossible" |

** Priority of elements:**
- **Primary ** The element solves the top 5 outcomes by opportunity score. It occupies the main visual space.
- **Secondary** - The element solves outcomes from the top 20. We see, but we don't dominate.
- **Tertiary** - the rest. Available by click/disclosure/setting.

### Level 5: Circumstances × Personas →

Screens from Level 2 + Persons + Circumstances.

What do you do?
1. Determine which screens look different for different people.
2. Determine which circumstances (contexts) change the content of the screen.
3. Option . separate screen. Option = same screen, but with a different set/priority of elements.

** Output format:**
```
VARIANTS: {screen-id}

  DEFAULT: {for which person / circumstance}
    Show: EL-1, EL-2, EL-3
    Hide:

  VARIANT-A: {person or circumstance}
    Show: EL-1, EL-4, EL-5
    Hide: EL-2 (cause: {this outcome is not relevant to this person})
    Add: EL-6 (cause: {unique outcome of this person})

  VARIANT-B: {circumstance}
    Modify: EL-3 → extended version (reason: {in this context the outcome is more critical})
```

**Typical circumstances (circumstances), changing the screen:**
- First time vs. revisit (onboarding vs. working mode)
- Small budget vs. large budget (different risks, different controls)
- One account vs. many accounts (simple list vs. search/filtering/grouping)
- Staff situation vs. problem (work mode vs. recovery mode)

---

## How to launch a skill

### Minimum entrance

In order to earn money, you need at least one of:
1. **Job Architecture** - Big Jobs → Little Jobs with outcomes Perfect.
2. **Normalized JTBD library** - a list of job statements with types and personas. Skill will build the hierarchy himself.
3. **Raw JTBD cards** - Skill will suggest normalizing and clustering first.

### Modes of work

**Full generation (all 5 levels):**
Use it when designing an interface from scratch or performing a complete redesign. Enter the Job Architecture or JTBD library. Out comes the full Screen Spec.

**Single screen generation (levels 3-4):**
When navigation and screens are already defined, you need to detail the specific screen. One job + its job map + outcomes. The output is flow and elements of one screen.

**Generation of options (level 5):**
When the screen is already described, you need to determine how it adapts to different personas or circumstances.

### Format of the final artifact

The result is a `screen-spec-{scope}.md` file with the following structure:

```markdown
# Screen Spec: {name scope}

## Navigation
{Level 1 output}

## Screen map
{output Level 2, table: screen-id | job | type | frequency | persona}

## Screen detailing
### {screen-id}: {name}
#### Flow
{Level 3 output}
#### Elements
{Level 4 output}
#### Options
{Level 5 output}

## Traceability Matrix
{Table: job-id | outcome | screen-id | element-id - to check completeness}
```

Traceability Matrix is the most important artifact for verification. If the job is not displayed in any element-id, it is Gap. If element-id isn’t tied to job, it’s a potential Cargo Cult.

---

## Anti-patterns (what not to do)

1. **Don't draw the interface and then check through jobs.** This is an audit, not a generation. If you catch yourself saying, “Now let’s see if jobs are covered,” you’ve turned the wrong way.

2. **Don't call partitions system nouns.** Balance, Reports, Settings is an internal data model. The user thinks in verbs: “Replenish”, “understand what is happening”, “Configure for yourself”.

3. **Don't create a screen without a job.** Each screen should answer the question, "What job does this screen do?" If there is no answer, the screen is not needed.

4. **Don't put "because it's customary" elements.** A Dashboard with charts is not needed unless any outcome requires trend visualization. A table is not needed unless the job involves comparing multiple objects.

5. **Do not confuse the frequency of the job with the importance of the screen.** The annual job "Audit" can produce a screen with the highest priority of elements, although used once a year.

---

## Connection with other skills and artifacts

| What | Where | Communication |
|-----|-----|-------|
| Job Architecture (construction methodology) | `03_knowledge/job-architecture-methodology.md` | Entrance for Level 1 |
| JTBD → UI pipeline (audit approach) | `03_knowledge/jtbd-to-ui-methodology.md` | Alternative approach (verification, not generation) |
| SaaS best practices on JTBD | `03_knowledge/job-architecture-saas-best-practices.md` | Theoretical Base |
| Process Hierarchy L0–L3 | `03_knowledge/process-hierarchy-methodology-for-llm-and-roles.md` | Domains for job classification |
| JTBD Extraction Pipeline | `03_knowledge/jtbd-extraction-pipeline-architecture.md` | Source raw JTBD |
| Slide Copywriter | `skills/slide-copywriter/SKILL.md` | For Screen Spec presentation to stakeholders |

---

## Sources of methodology

- **Ulwick (ODI):** Job Map → 8 steps → Desired Outcomes. Basis for Level 3-4.
- **Kalbach (JTBD Playbook):** Job Hierarchy (Big → Little), Alignment Diagram. Basis for Level 1-2.
- **Norman (Activity-Centered Design):** Organizing an interface around activities rather than objects.
- **NN/g:** Task-based navigation is more stable than topic-based navigation.
- **Intercom:** Job Stories → Circumstance-Driven Design. Basis for Level 5.
