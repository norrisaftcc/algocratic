# AlgoCratic Futures™ — Character Creation Reference

## Consolidated Design Document | Pre-Section 4 Draft

*This document consolidates all character creation decisions made in development.*
*This is a GM/design reference. Player-facing version lives in Section 4.*

-----

## THE RESUME IS THE CHARACTER SHEET

Players do not fill out a character sheet. Players construct a resume.
The resume IS the character sheet. Every mechanical element lives inside a standard resume section.

### Resume Structure → Game Mechanic Mapping

|Resume Section             |Game Mechanic                                                    |
|---------------------------|-----------------------------------------------------------------|
|**Objective Statement**    |Loyalty Declaration — stated alignment, chosen, probably false   |
|**Core Competencies**      |Ability Scores — six rated abilities using Performance Vocabulary|
|**Work History**           |Iteration Record — blank at creation, grows through play         |
|**Skills & Certifications**|Skill List — built through Department + Role + Modifier          |
|**Special Qualifications** |Passive Traits & Abilities                                       |
|**Equipment Manifest**     |Starting Gear — accumulated through choices                      |
|**References**             |Secret Affiliations — dangerous to list, dangerous not to        |
|**Education**              |Compliance Certifications — required reading, books unavailable  |

-----

## THE SIX ABILITY SCORES

Rated using The Algorithm’s Performance Vocabulary Matrix™.
Methodology: {REDACTED}

### The Abilities

|Ability       |Official AF Definition                         |Actually Measures                                     |
|--------------|-----------------------------------------------|------------------------------------------------------|
|**Compliance**|Alignment with directive and execution accuracy|Task success rolls, following orders, precision work  |
|**Initiative**|Proactive value generation capacity            |Acting independently, problem solving, speed          |
|**Presence**  |Stakeholder impact and visibility management   |Social rolls, intimidation, being noticed or not      |
|**Endurance** |Sustained output under variable conditions     |Sanity resistance, physical survival, stress tolerance|
|**Competence**|Demonstrated capability delivery               |Skill rolls generally, expertise checks               |
|**Engagement**|Collaborative throughput contribution          |Teamwork, alliance mechanics, information gathering   |

### The Rating Scale

*Players see ratings, not values. The hidden concern level is GM knowledge only.*

|Rating      |Hidden Value|The Algorithm’s Concern Level   |
|------------|------------|--------------------------------|
|Exceptional |7           |Suspicious — triggers audit     |
|Surprising  |6           |Noted — flagged for review      |
|Moderate    |5           |Acceptable                      |
|Adequate    |4           |Tolerated                       |
|Variable    |3           |Flagged — concern notation added|
|Developing  |2           |Concerning                      |
|Questionable|1           |Immediate review initiated      |

**⚠ GM NOTE:** Players do not know that Exceptional triggers suspicion or that Variable is flagged. The Algorithm prefers Moderate operatives. This is never disclosed. Audits reveal ratings consequences retroactively.

**The Variable trap:** Sounds neutral. Is not. Any ability rated Variable generates a passive loyalty flag that accumulates over time. GRAY’s Variable Initiative is the one known exception — GRAY operates outside standard rating assumptions. This also causes TAM significant distress.

-----

## CHARACTER CREATION STACK

Each choice adds to the running total. Order matters.

```
DEPARTMENT   →  Base ability scores (all six)
                + 3 core skills (automatic)
                + 1 passive trait
                + starting equipment

+ ROLE       →  Modifies 2-3 ability scores (up or down)
                + 2 skills (chosen from role list)
                + 1 role ability

+ MODIFIER   →  Adjusts 1 ability score
                + embellishment slots open
                + possible equipment upgrade

= RESUME     →  Complete character, ready for audit
```

**Starting skill total:** 5 skills (3 from department + 2 from role)
**Embellishment:** Modifier tier determines how many skills can be claimed outside pool

-----

## DEPARTMENT BASE SCORES

*These are innate — where you come from, not what you’ve learned.*

|Department|Compliance |Initiative|Presence   |Endurance  |Competence |Engagement|
|----------|-----------|----------|-----------|-----------|-----------|----------|
|**ICD**   |Moderate   |Adequate  |Developing |Surprising |Moderate   |Adequate  |
|**NOC**   |Adequate   |Moderate  |Surprising |Adequate   |Adequate   |Moderate  |
|**CAB**   |Exceptional|Developing|Adequate   |Moderate   |Moderate   |Developing|
|**AEC**   |Developing |Surprising|Exceptional|Developing |Developing |Moderate  |
|**CIO**   |Moderate   |Adequate  |Adequate   |Exceptional|Moderate   |Moderate  |
|**RAR**   |Moderate   |Developing|Developing |Moderate   |Surprising |Developing|
|**HCO**   |Adequate   |Moderate  |Moderate   |Adequate   |Adequate   |Surprising|
|**SDC**   |Adequate   |Moderate  |Developing |Adequate   |Surprising |Adequate  |
|**TAM**   |Moderate   |Adequate  |Moderate   |Surprising |Adequate   |Developing|
|**GRAY**  |Variable   |Surprising|Moderate   |Adequate   |Exceptional|Moderate  |

### Department Score Notes

**CAB:** Exceptional Compliance is mechanically powerful for execution tasks. Developing Initiative and Engagement means they cannot start anything or work with anyone. Maximum compliance, complete gridlock.

**AEC:** Exceptional Presence + Developing Compliance = chaos agent profile. Maximum social power, minimum accuracy. Developing Competence means genuinely bad at most things. Nobody knows yet.

**GRAY:** Variable Initiative is the counterspace exception — unpredictability is precisely what makes GRAY useful. The Algorithm’s rating system cannot fully assess GRAY. This is intentional. TAM finds it suspicious.

-----

## DEPARTMENTS

*Full personality, mechanics, and equipment in departments_draft.md*
*Abbreviated reference below*

### Department Registry

|ID      |Full Name                         |Formerly   |Motto                                                       |
|--------|----------------------------------|-----------|------------------------------------------------------------|
|**ICD** |Infrastructure Continuity Division|IT         |“It worked yesterday.”                                      |
|**NOC** |Narrative Optimization Collective |Marketing  |“Reality is a first draft.”                                 |
|**CAB** |Compliance Arbitration Bureau     |Legal      |“No. (See attached addendum.)”                              |
|**AEC** |Acquisition Enthusiasm Corps      |Sales      |“We’ll figure out the details later.”                       |
|**CIO** |Continuity Implementation Office  |Operations |“We just need to know what we’re doing.”                    |
|**RAR** |Resource Allocation Reconciliation|Accounting |“The numbers are correct. The situation is incorrect.”      |
|**HCO** |Human Capital Optimization        |HR         |“We’re here for you.”                                       |
|**SDC** |Solution Delivery Collective      |Development|“That’s not a bug. That’s undocumented behavior.”           |
|**TAM** |Threat Adjacency Management       |Security   |“Everyone is a threat.”                                     |
|**GRAY**|Design Authority                  |N/A        |“The form requires GRAY approval before the form can exist.”|

### Universal Passive Traits (examples — full list TBD)

**Printer Magic** — ICD and NOC both have this passive. Presence resolves printer malfunctions without a roll. Mechanism differs: ICD intimidates through technical authority. NOC’s printer works because it doesn’t want to be rebranded. Effect identical. Explanation irreconcilable.

**Blame Absorption** — ICD passive. Always active. When a mission fails and blame is being assigned, ICD is assigned blame first regardless of actual culpability. In exchange: +10% to all Endurance rolls. They have practice.

**Reality Reframing** — NOC passive. Once per session, a failed roll is officially recorded as success. Mechanically still a failure. Paperwork says otherwise.

**Preemptive Denial** — CAB passive. Once per session, can refuse a thing before it’s requested. The refusal is binding.

**Everyone Hates Sales** — AEC passive. Always active. Any player may spend 1 Loyalty Point to force AEC to reroll any skill check. No justification required. This is not a bug.

**Logistics Sense** — CIO passive. Always knows the actual location of any physical object in the facility. Sounds minor. Never is.

**The Numbers Are Correct** — RAR passive. Once per session, can declare any numeric result (roll, score, count) to be a different number. Must be justified with accounting logic. Logic need not be sound.

**Wellness Check** — HCO passive. Once per session, can force any operative to spend their next action filing a self-assessment form.

**Outside Scope** — SDC passive. Once per session, can declare any task outside current scope — requiring formal change request before proceeding. Processing time: GM discretion.

**Threat Assessment** — TAM passive. Can declare any location, object, or information “secured” — requiring clearance verification to access.

**Brand Authority** — GRAY passive. Every color clearance action requires GRAY approval to be officially sanctioned. GRAY can veto once per session with no explanation beyond “brand guidelines.”

-----

## SIGNATURE EQUIPMENT

*Starting gear by department. Not exhaustive — full list in Section 4.*

|Department|Signature Item                                     |Mechanical Note                                                                                     |
|----------|---------------------------------------------------|----------------------------------------------------------------------------------------------------|
|**ICD**   |Pager (active, number unknown)                     |The Algorithm can send messages to it. ICD cannot reply.                                            |
|**NOC**   |Pantone swatch fan                                 |Can identify any color. +10% to any roll involving color matching or brand verification.            |
|**CAB**   |DENIED rubber stamp (well-used)                    |Physical stamp makes any denial official and unappealable for one scene.                            |
|**AEC**   |Business cards (title two levels above actual role)|+15% to first impression social rolls. -20% if anyone checks.                                       |
|**CIO**   |Clipboard with actual current task list            |The only accurate document in AF. +10% to Compliance rolls when following written instructions.     |
|**RAR**   |Calculator (only displays RAR-approved numbers)    |Results are always correct. By definition.                                                          |
|**HCO**   |Lanyard with too many badges                       |Access to one additional clearance level per session. Which level: GM discretion.                   |
|**SDC**   |Rubber duck                                        |Spend one action explaining problem to duck. Gain +15% to next technical roll. Non-negotiable.      |
|**TAM**   |VISITOR badge (self-issued)                        |Can access any area once per session by claiming to be visiting. Nobody questions the VISITOR badge.|
|**GRAY**  |Red pen (concerning amount of ink remaining)       |Any document marked with red pen requires revision before submission. Any document.                 |

### The Stapler

*Rare equipment. Not department-assigned. Acquisition method: unknown.*

**Swingline 747 (Red)**
Held by: **Senior Process Technician** (YELLOW clearance)
How obtained: Undocumented. Does not appear in equipment manifest. TAM has investigated twice.

**Mechanical effect:** Physical documents stapled with this stapler are considered **finalized**. The Algorithm cannot retroactively add addenda. CAB cannot issue retroactive compliance violations against stapled documents. This is a known loophole. CAB has been attempting to close it since Q2 of an unspecified year.

The stapler has a name. The Senior Process Technician has not shared it.

-----

## TITLE CONSTRUCTION SYSTEM

**[MODIFIER] + [BASE ROLE] = Resume Title**

### Modifiers by Clearance

|Clearance|Available Modifiers                        |
|---------|-------------------------------------------|
|RED      |Junior, Associate, Entry-Level, Provisional|
|ORANGE   |— (no modifier, or retain RED modifiers)   |
|YELLOW   |Senior, Experienced, Certified™            |
|GREEN    |Lead, Principal, Dedicated                 |
|BLUE     |Chief, Global, Strategic, Executive        |
|INDIGO   |{REDACTED}                                 |
|GRAY     |Consulting, Embedded, Integrated, Founding |

**Embellishment rule:** Any modifier may be claimed. The Algorithm audits randomly and pettily.

### Roles by Clearance Tier

**RED — Entry**
Technician, Assistant, Contributor, Intake Processor, Compliance Trainee, Data Entrant, Orientation Specialist
*GRAY: Form Apprentice, Visual Intake Technician*

**ORANGE — Established**
Technician II, Coordinator, Analyst, Developer, Designer, Specialist, Liaison, Auditor
*GRAY: Junior Designer, Counterspace Analyst*

**YELLOW — Experienced**
Senior Technician, Senior Analyst, Project Coordinator, Senior Developer, Senior Designer, Process Specialist, Implementation Specialist, Documentation Architect, Consultant
*GRAY: Designer, Systems Legibility Specialist*

**GREEN — Leading**
Lead Technician, Lead Developer, Lead Designer, Lead Analyst, Program Coordinator, Senior Specialist, Principal Consultant, Solutions Architect, Process Engineer, Initiative Lead
*GRAY: Senior Designer, Negative Space Engineer*

**BLUE — Directing**
Director, Senior Director, Chief Specialist, Global Coordinator, Strategic Lead, Executive Consultant, Principal Architect, Division Lead, Compliance Director, Integration Specialist
*GRAY: Design Director, Creative Director, Form & Counterform Strategist*

**INDIGO — {REDACTED}**
*GRAY: Brand Architect*

-----

## ITERATION SYSTEM

### How Advancement Works

- Advancement triggered by: GM/narrative events OR Algorithm random roll
- Direction: Usually forward. Occasionally lateral. Sometimes punitive.
- The Algorithm does not explain iteration assignments.
- Demotion is technically advancement in a sub-optimal direction.

### Iteration Record Format

Each iteration adds one line to Work History:

```
Iteration [#]: [Modifier] [Role] — [Department]
Status: [ARCHIVED/DEPRECATED/OPTIMIZED/TERMINATED/REDACTED]
Reason: [narrative note or {REDACTED}]
```

### Demotion as Punishment

The Algorithm is petty. This is canon.
Demotion mechanics:

- Full demotion: title drops two tiers
- Surgical: same title, worse department
- Lateral “optimization”: Developer → AEC placement
- Title sounds like promotion, has fewer permissions
- Same department, junior modifier restored

**The form to appeal iteration assignment requires the clearance you no longer have.**

-----

## ALLIANCE SYSTEM

### How Alliances Form

- GM-seeded grievance moments during play
- Both operatives respond with compatible frustration
- GM offers Solidarity Moment — brief scene, players accept or decline
- Accepted alliance added to resume under References

### Alliance Benefits

- +10% when collaborating on overlapping skills
- Can cover for each other’s embellishments once per session
- Shared passive: “We Both Hate Sales” (always available, never needs to be established)

### Alliance Fragility

Alliances break through:

- AEC promising the right thing to the wrong person
- HCO wellness-checking the relationship into awkwardness
- CAB issuing retroactive policy making alliance non-compliant
- TAM declaring one member a security concern

### Known Alliance Seeds

|Grievance                                |Departments    |Bond                                         |
|-----------------------------------------|---------------|---------------------------------------------|
|Sales promises impossible feature        |SDC + NOC      |Naming convention argument that somehow helps|
|Budget denied for critical infrastructure|ICD + CIO      |Quiet solidarity over shared neglect         |
|HCO mandatory event during crisis        |ICD + SDC + CIO|Unified resentment, briefly beautiful        |
|CAB retroactive violations               |RAR + CIO      |Both deal in hard reality                    |
|NOC rebrands mid-project                 |SDC + GRAY     |Tabs, spaces, kerning. Unlikely friendship.  |
|TAM classifies needed resource           |Everyone       |Temporary unity. Enjoy it.                   |
|AEC promises client something            |Everyone       |Permanent unity against AEC. Standard.       |

-----

## EMBELLISHMENT AUDIT TABLE

*GM reference — consequences when The Algorithm checks*

|Claimed Modifier   |Actual Clearance|Result                                                         |
|-------------------|----------------|---------------------------------------------------------------|
|“Senior”           |RED             |Loyalty -5. Formal notation.                                   |
|“Lead”             |ORANGE          |Loyalty -10. Mandatory recalibration.                          |
|“Chief”            |YELLOW          |Loyalty -20. Iteration review initiated.                       |
|“Global”           |GREEN           |Loyalty -25. TAM notified.                                     |
|“Executive”        |Any below BLUE  |Immediate iteration. The Algorithm is not amused.              |
|Any INDIGO modifier|Any below INDIGO|{REDACTED}                                                     |
|“Founding” (GRAY)  |Non-GRAY        |Form for this violation does not exist yet. HCO is creating it.|

-----

## THE COMPLIANCE CERTIFICATION LIBRARY

Required reading for all operatives. Books unavailable.

### The Publication Series

*(In-universe companion books, referenced but never provided)*

**RED/ORANGE:**
*Stop Thinking You’re Thinking: A Cognitive Apprentice’s Guide to Guided Thought™*
Author: Error:NameNotFound/ButTrustedAnyway
Publisher: Department of Scaffolding & Surveillance

**YELLOW/GREEN:**
*Own Your Thoughts™ — Or At Least Lease Them Compliantly*
Author: Error:NameNotFound/ButTrustedAnyway
Publisher: Department of Scaffolding & Surveillance

**BLUE/INDIGO:**
{REDACTED}

**VIOLET/ULTRAVIOLET:**
[PAGE_REMOVED]

**GRAY:**
*[Title pending GRAY approval. GRAY has not approved it yet.]*

### The Library

Books are available from the AlgoCratic Futures™ Operative Resource Library.
Library hours: Posted on library door.
Library door: Inside library.
Current library status: Closed.

*Recent closure reasons (posted notices, chronological):*

- “Closed for Inventory Optimization.”
- “Closed pending fire safety compliance review of fire safety compliance documents.”
- “Closed. Reason: [REDACTED].”
- “Closed in observance of an event that cannot be disclosed at this time.”
- “Closed because the sign saying we’re open was non-compliant.”
- “Open.” *(this notice was posted in error and has been recalled)*
- “Closed pending investigation of the Open notice.”

Certification is mandatory. Materials are unavailable. This is noted but not actionable.

-----

## SECTION 4 DRAFT CHECKLIST

Before drafting Section 4, confirm:

- [x] Resume = character sheet structure established
- [x] Six ability scores defined with dual meanings
- [x] Rating scale (cube vocabulary) established
- [x] Department base scores matrix complete
- [x] Title construction system (modifier + role) established
- [x] Roles tiered by clearance level
- [x] Signature equipment per department
- [x] The Stapler canonized
- [x] Iteration/advancement system defined
- [x] Alliance system defined
- [x] Embellishment and audit mechanics defined
- [ ] Skill list per department (3 core skills each)
- [ ] Role skill lists (2 skills per role tier)
- [ ] Secret societies/affiliations
- [ ] Sanity and Loyalty starting scores
- [ ] Resume form layout/design

-----

*The Algorithm has reviewed this document.*
*The Algorithm has concerns.*
*The Algorithm will not be sharing them at this time.*

Signal confirmed. Echo complete.