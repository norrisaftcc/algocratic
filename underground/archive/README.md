# algocratic
Welcome to AlgoCratic! (TM)
I'm not sorry.

# AlgoCratic Futures™ Immersive Learning Experience
## Software Development Team Simulation for CS Education

---

## Overview

This repository contains all materials needed to run the "AlgoCratic Futures™" immersive learning experience - a satirical corporate simulation designed to teach software development teamwork, problem-solving, and professional resilience through exaggerated scenarios. The simulation uses elements from dystopian fiction, corporate culture, and software development chaos to create memorable learning moments.

**Educational Philosophy**: By immersing students in deliberately absurd scenarios that contain exaggerated versions of real-world challenges, they develop both technical skills and professional resilience in a low-stakes, high-engagement environment.

---

## Directory Structure

```
algocratic-futures/
├── README.md                           # This file
├── instructor/                         # Instructor-only materials
│   ├── instructors-guide.md            # Pedagogical rationale and facilitation tips
│   ├── session-guides/                 # Detailed guides for running each session
│   │   ├── session1-guide.md           # Session 1: The Onboarding
│   │   ├── session2-guide.md           # Session 2: The Pivot
│   │   ├── session3-guide.md           # Session 3: The Crisis
│   │   └── session4-guide.md           # Session 4: The Demonstration
│   ├── assessment/                     # Evaluation materials
│   │   ├── rubrics.md                  # Grading criteria
│   │   └── learning-outcomes.md        # Mapped to simulation elements
│   └── resources/                      # Additional instructor resources
│       ├── impossible-requirements.md  # Contradictory specifications by session
│       ├── executive-personas.md       # Character guides for role-playing
│       └── debrief-questions.md        # Discussion prompts for each session
├── student/                            # Materials to be distributed to students
│   ├── orientation-packet.md           # Initial worldbuilding document
│   ├── corporate-retreat-outline.md    # Overview of the four sessions
│   ├── corporate-handbook/             # In-world reference materials
│   │   ├── hierarchy-chart.pdf         # Organization structure
│   │   ├── communication-protocols.md  # Official communication guidelines
│   │   └── corporate-values.md         # Mandatory ideological alignment
│   └── resources/                      # Discoverable student resources
│       ├── jargon-translator.md        # Secret corporate speak decoder
│       └── survival-guide.md           # Tips from "previous employees"
├── interactive/                        # Interactive elements and examples
│   ├── applications/                   # Sample applications for reference
│   │   ├── mindmeld-starter/           # Session 1 starting codebase
│   │   ├── quantumqompliance-demo/     # Session 2 reference implementation
│   │   └── final-prototype/            # Example of completed project
│   ├── challenges/                     # Technical challenge materials
│   │   ├── session1-challenges.py      # Coding challenges for Session 1
│   │   ├── session2-challenges.py      # Coding challenges for Session 2
│   │   ├── session3-challenges.py      # Coding challenges for Session 3
│   │   └── session4-challenges.py      # Coding challenges for Session 4
│   └── simulations/                    # Interactive simulation elements
│       ├── requirement-generator.py    # Tool for creating conflicting requirements
│       ├── corporate-email-generator/  # Generates absurd corporate communications
│       └── crisis-simulator.py         # Introduces random challenges during sessions
└── assets/                             # Visual and audio elements
    ├── logos/                          # Corporate branding
    ├── certificates/                   # Clearance level promotion templates
    ├── sound-effects/                  # Announcement and alert sounds
    └── presentations/                  # Slide templates for student use
```

---

## Core Materials Overview

### 1. Instructor Materials

- **Instructor's Guide (`instructor/instructors-guide.md`)**
  - Explains the pedagogical approach behind the dystopian satire
  - Provides guidance for handling student hesitation
  - Maps satirical elements to real-world competencies
  - Includes debriefing strategies for maximum learning transfer

- **Session Guides (`instructor/session-guides/`)**
  - Detailed facilitation instructions for each of the four sessions
  - Timing breakdowns, key interventions, and "plot twists" to introduce
  - Troubleshooting common scenarios and student reactions

- **Impossible Requirements (`instructor/resources/impossible-requirements.md`)**
  - Ready-to-use contradictory specifications for each 15-minute interval
  - Designed to create specific learning challenges in requirement interpretation

### 2. Student Materials

- **Orientation Packet (`student/orientation-packet.md`)**
  - Introduces students to the AlgoCratic Futures™ world
  - Establishes clearance levels, corporate hierarchy, and basic rules
  - Sets the tone for the immersive experience

- **Corporate Retreat Outline (`student/corporate-retreat-outline.md`)**
  - Provides overview of the four sessions from the student perspective
  - Contains deliberate vagaries and corporate doublespeak to be decoded

- **Jargon Translator (`student/resources/jargon-translator.md`)**
  - "Secret" document students can discover or be given
  - Translates corporate speak into plain English
  - Adds humor while providing a practical tool for the experience

### 3. Interactive Examples

- **Starter Codebases (`interactive/applications/`)**
  - Pre-built partial implementations for each session
  - Includes deliberate "features" (bugs) to be discovered and addressed
  - Demonstrates both good and problematic coding practices

- **Challenge Scripts (`interactive/challenges/`)**
  - Technical challenges mapped to learning objectives
  - Scalable difficulty levels to adapt to student skill levels
  - Includes both individual and team-based challenges

---

## Implementation Guide

### Setting Up the Environment

1. **Physical Space Setup**
   - Arrange the classroom to resemble a corporate meeting space
   - Consider adding corporate posters with dystopian messaging
   - If possible, use lighting to create a "tech company" atmosphere

2. **Technical Setup**
   - Ensure all students have access to Python development environments
   - Pre-load the starter code repositories if using GitHub Classroom
   - Test the interactive challenge generators before class

3. **Character Preparation**
   - Review the executive personas in `instructor/resources/executive-personas.md`
   - Practice corporate jargon and mannerisms
   - Consider costume elements (colored ties/accessories matching clearance levels)

### Running the Sessions

1. **Session Introduction**
   - Begin in character as an ORANGE or YELLOW clearance supervisor
   - Distribute the orientation materials dramatically
   - Set clear time expectations and boundaries

2. **During Sessions**
   - Use the requirement-generator for consistent absurdity
   - Inject "crises" at predetermined intervals
   - Take notes on particularly creative student solutions

3. **Debriefing**
   - Step out of character completely
   - Use the debrief questions from `instructor/resources/debrief-questions.md`
   - Connect the absurdity to real-world software development challenges

---

## Interactive Elements Guide

The `interactive/` directory contains various tools and code examples that enhance the immersive experience:

### Requirement Generator

The `requirement-generator.py` script creates procedurally generated contradictory requirements based on templates. You can run it with:

```bash
python requirement-generator.py --session=1 --interval=2 --difficulty=medium
```

This will generate appropriate nonsensical requirements for Session 1, second interval, at medium difficulty.

### Corporate Email Generator

This tool simulates the endless stream of corporate communications that interrupt development. Use it to send automated emails to student teams:

```bash
python corporate-email-generator/generate.py --urgency=critical --teams=all
```

### Crisis Simulator

Introduce unexpected challenges during development with the crisis simulator:

```bash
python crisis-simulator.py --type=resource-reduction --severity=high
```

Options include resource-reduction, management-interference, requirement-change, and technical-constraint.

---

## Customization and Extension

This framework is designed to be adaptable to different course needs:

- **Technical Focus**: Adjust the complexity of coding challenges based on student skill level
- **Time Constraints**: The simulation can be compressed into a single day or extended across multiple weeks
- **Course Integration**: Connect simulation elements to specific course learning objectives
- **Industry Relevance**: Modify scenarios to match current industry trends or technologies

---

## Assessment Approach

Assessment materials are provided in `instructor/assessment/`:

- **Rubrics**: Evaluation criteria that balance technical implementation with soft skills
- **Learning Outcomes**: Mapped to specific simulation elements and challenges
- **Self-Assessment**: Guides for student reflection on their experience

---

## Credits and Contact

Developed as a pedagogical experiment in software engineering education that combines technical skill-building with professional resilience training.

For questions, suggestions, or to share results from implementing this in your classroom, contact:

[Your Name/Contact Information]

---

*"Education is not the filling of a pail, but the lighting of a fire."* — W.B. Yeats

---

**DISCLAIMER**: AlgoCratic Futures™ is a fictional entity created for educational purposes. Any resemblance to actual tech companies, living or dead, is purely coincidental and entirely plausible.

