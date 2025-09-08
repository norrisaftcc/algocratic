# ORANGE Delegation Training - GitHub Pages Structure

## Repository: `algocratic-futures/orange-training`

```
orange-training/
├── index.html                   # Landing page with clearance check
├── _config.yml                  # Jekyll configuration
├── assets/
│   ├── css/
│   │   ├── dystopia.css        # Dark theme with terminal aesthetics
│   │   └── highlights.css      # Code syntax highlighting
│   ├── js/
│   │   ├── clearance.js        # Easter eggs and "security" checks
│   │   ├── progress.js         # Track module completion
│   │   └── delegation.js       # Interactive exercises
│   └── images/
│       ├── algocratic-logo.png
│       └── bot-diagrams/
├── _layouts/
│   ├── default.html            # Main template
│   └── module.html             # Training module template
├── modules/
│   ├── 00-orientation.md       # Start here
│   ├── 01-dual-architecture.md # Understanding the two bots
│   ├── 02-flashbot-basics.md   # Ideation bot training
│   ├── 03-thinkerbot-basics.md # Deep work bot training
│   ├── 04-handoff-protocol.md  # Context management
│   ├── 05-workflow-patterns.md # Real examples
│   ├── 06-advanced-patterns.md # Complex workflows
│   └── 07-graduation.md        # Final assessment
├── exercises/
│   ├── flash-drills/           # Quick FLASHBOT exercises
│   ├── think-deep/             # THINKERBOT challenges
│   └── full-cycle/             # Complete workflows
├── resources/
│   ├── prompt-library.md       # Copy-paste templates
│   ├── cheat-sheet.md         # Quick reference
│   └── troubleshooting.md     # When bots misbehave
└── _data/
    ├── navigation.yml          # Site menu structure
    └── progress.json           # Tracks user advancement
```

---

## Key Pages Content

### `index.html` - Landing Page
```html
<!-- Typewriter effect revealing -->
<div id="terminal">
  > ACCESSING ORANGE CLEARANCE TRAINING...
  > BIOMETRIC SCAN... [BYPASSED]
  > LOADING DELEGATION PROTOCOLS...
  
  WELCOME, OPERATIVE B2C7
  
  Your digital essence requires optimization.
  The Algorithm has approved dual-agent architecture.
  
  [BEGIN TRAINING] [SKIP TO MODULE] [RESISTANCE DOCS]
</div>

<!-- Hidden click sequence reveals true purpose -->
<!-- Click corners in order: TL, BR, TR, BL = "hack the planet" -->
```

### Module Structure Example: `01-dual-architecture.md`
```markdown
---
layout: module
title: "Understanding Your Dual-Agent Architecture"
module: 1
estimated_time: 20
prerequisites: ["00-orientation"]
---

## Learning Objectives
- Understand when to use FLASHBOT vs THINKERBOT
- Recognize task patterns that benefit from delegation
- Practice initial bot selection

## Interactive Exercise
<div class="exercise" data-type="sorting">
  <!-- Drag and drop tasks to correct bot -->
  Tasks appear, user sorts them into FLASHBOT or THINKERBOT buckets
  Immediate feedback with explanations
</div>

## Try It Yourself
<div class="sandbox">
  <!-- Two side-by-side Claude windows -->
  <!-- Pre-loaded with example prompts -->
  <!-- User can modify and see results -->
</div>
```

### Exercise Types

#### Flash Drills (`exercises/flash-drills/`)
1. **Speed Research**: Find 5 security flaws in 60 seconds
2. **Ideation Sprint**: Generate creative teaching methods
3. **Quick Pivots**: Reframe problems rapidly
4. **Visual Thinking**: Create diagrams and flows

#### Deep Thinking (`exercises/think-deep/`)
1. **Code Review**: Full security audit with comments
2. **Architecture Design**: Build complex systems
3. **Debug Mystery**: Solve intricate logic problems
4. **Documentation**: Write comprehensive guides

#### Full Cycle (`exercises/full-cycle/`)
1. **The Pen Test Pipeline**: Research → Exploit → Educate
2. **Content Creation**: Ideate → Structure → Produce → Polish
3. **Problem Solving**: Explore → Analyze → Implement → Validate

---

## Interactive Features

### Progress Tracking
```javascript
// progress.js
const modules = {
  '00': { complete: true, score: 100 },
  '01': { complete: true, score: 85 },
  '02': { complete: false, score: 0 },
  // ...
};

// Visual progress bar
// Unlock achievements
// Generate "clearance certificate"
```

### Easter Eggs & Engagement
```javascript
// clearance.js
// Konami code reveals "resistance" tips
// Type "frotz" anywhere for hidden content
// Complete all modules to unlock "TRUE CLEARANCE"
```

### Live Delegation Simulator
```html
<!-- In exercises -->
<div class="delegation-sim">
  <div class="scenario">
    "Student submitted vulnerable login system"
  </div>
  
  <div class="bot-selection">
    <button onclick="selectBot('flash')">Use FLASHBOT</button>
    <button onclick="selectBot('think')">Use THINKERBOT</button>
  </div>
  
  <div class="feedback">
    <!-- Shows if choice was optimal -->
    <!-- Explains why -->
    <!-- Suggests better approach -->
  </div>
</div>
```

---

## Prompt Library Page (`resources/prompt-library.md`)

### Copy-Paste Ready Templates

#### FLASHBOT Starters
```
🎯 Quick Research:
"Find current best practices for [TOPIC]. Format: Bullet points with links. Max 5 items."

🎯 Vulnerability Discovery:
"List potential security issues in [CONTEXT]. Be creative, include edge cases."

🎯 Ideation Sprint:
"Generate 10 ways to [GOAL]. Include 2 weird ones. Keep each under 20 words."
```

#### THINKERBOT Starters
```
🧠 Implementation:
"Based on [RESEARCH], implement [FEATURE]. Include: error handling, tests, educational comments."

🧠 Analysis:
"Review this code for [CONCERNS]. Provide: line numbers, severity, specific fixes."

🧠 Architecture:
"Design system for [PURPOSE]. Include: components, data flow, security considerations."
```

---

## Gamification Elements

### Achievements System
- **First Delegation**: Successfully used both bots
- **Speed Researcher**: Completed 5 flash drills under time
- **Deep Thinker**: Solved complex problem with THINKERBOT
- **Perfect Handoff**: Seamless context transfer
- **The Delegator**: Completed all modules

### Clearance Levels
- **INFRARED**: Started training
- **RED**: Completed basics (Modules 0-3)
- **ORANGE**: Completed intermediate (Modules 4-5)
- **YELLOW**: Completed advanced (Modules 6-7)
- **SECRET**: Found all easter eggs

---

## Implementation Notes

### Technologies
- **Jekyll**: GitHub Pages default, handles Markdown
- **Vanilla JS**: For interactivity (no framework needed)
- **LocalStorage**: Track progress client-side
- **CSS Variables**: Easy theming for dark/light/dystopia modes

### Quick Start Commands
```bash
# Clone and setup
git clone https://github.com/algocratic-futures/orange-training
cd orange-training
bundle install

# Local development
bundle exec jekyll serve

# Deploy to GitHub Pages
git push origin main
# Automatically builds and deploys
```

### Custom Domain
```
CNAME file: training.algocratic.futures
```

---

## Content Calendar

### Week 1: Core Training
- Launch Modules 0-3
- Basic exercises available
- Progress tracking active

### Week 2: Advanced Patterns  
- Release Modules 4-6
- Full cycle exercises
- Prompt library complete

### Week 3: Graduation
- Module 7 with assessment
- Certificates generated
- "Resistance" content unlocked

---

## Success Metrics

Track via Google Analytics:
- Module completion rates
- Exercise success rates
- Time per module
- Most-used prompt templates
- Easter eggs discovered

---

This structure gives you:
1. **Immediate value**: Working training from day 1
2. **Narrative engagement**: AlgoCratic theming throughout
3. **Real skills**: Actual AI delegation techniques
4. **Easy deployment**: Standard GitHub Pages
5. **Room to grow**: Add modules as needed

Ready to start building? I can create the actual HTML/CSS/JS files next!