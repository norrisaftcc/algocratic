# Project Ideation: Start the Band

## Overview
A text-based, asynchronous music collaboration project where LLMs comprise 80% of the band and 8-10 humans act as prompters and curators.

## Core Concept
- **LLMs as Musicians**: AI models generate the majority of creative content
- **Humans as Conductors**: People prompt, guide, and curate the output
- **GitHub as Studio**: Distributed version control for musical collaboration
- **Asynchronous by Design**: No real-time coordination required

## Entry Flow
"Welcome to the Band" = Create your GitHub account + personal band member repository

## Technical Architecture

### Repository Structure
**Two-tier system:**
1. **Main Orchestrator Repository** (`start-the-band`)
   - Central hub for band coordination
   - Roster of all members
   - Shared resources and templates
   - Collective sessions and tracks

2. **Individual Member Repositories** (`band-member-[username]`)
   - Personal creative space
   - Individual prompts and sessions
   - Curated outputs
   - Personal band journal

### File Support
- **Text files**: Prompts, metadata, documentation (Git tracked)
- **MP3 files**: Audio outputs (Git ignored, stored locally)

## Workflow

### Basic Flow
1. Human joins → Creates personal repo from template
2. Human writes prompts → Saves in personal repo
3. Human feeds prompts to LLMs → Gets musical/lyrical output
4. Human curates results → Commits good stuff
5. Best material → Shared to main repo
6. Collaboration → Others can build on shared prompts

### Key Features
- **Prompt Templates**: Standardized formats for different music styles
- **Session Tracking**: Timestamp and document all LLM interactions
- **Metadata System**: Track credits, versions, and prompt genealogy
- **Curation Pipeline**: Clear path from idea to finished track

## Design Principles
1. **Asynchronous First**: No scheduling conflicts
2. **LLM Optimized**: Templates designed for copy/paste workflows
3. **Version Everything**: Full history of creative evolution
4. **Decentralized Creation**: Members own their process
5. **Collective Curation**: Best stuff bubbles up to main repo

## Next Steps
1. Create main orchestrator repository
2. Develop member repository template
3. Write onboarding documentation
4. Create initial prompt templates
5. Establish curation guidelines

## Integration with AlgoCratic
While this is a separate project, it maintains AlgoCratic's spirit of:
- Satirical corporate language ("The Band demands your creative output")
- Clearance levels (maybe "Opening Act" → "Headliner"?)
- Productivity metrics ("Tracks per Quarter")

---
*The Algorithm has composed this ideation. May your prompts be harmonious and your commits melodic.*