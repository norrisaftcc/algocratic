# MANDATORY COLLABORATIVE EFFICIENCY EXERCISE™
## RED Clearance Assignment: Productivity Enhancement Tool Development

**CLASSIFICATION: RED CLEARANCE**  
**DOCUMENT: AF-RED-TODO-2025-01**  
**SUBMISSION DEADLINE: As Optimized by The Algorithm**

---

## PROJECT OVERVIEW

The Algorithm has determined that organizational efficiency can be improved by 34.2% through the implementation of a "Task Organization and Designation Optimizer" (TODO). Your team has been selected for the privilege of developing this critical infrastructure component.

You will work in Algorithm-assigned groups to develop a console-based TODO list application. This exercise will demonstrate your ability to collaborate effectively through approved version control channels.

---

## TEAM STRUCTURE

Each team will self-organize into the following mandatory roles:

### BUILD MASTER (1 per team)
- Creates and manages the GitHub repository
- Converts user stories into GitHub issues
- Reviews and merges pull requests
- Ensures all work follows proper Git workflow
- Reports status to ORANGE clearance supervisors

### UI DEVELOPMENT UNIT (1-2 contributors)
- Implements the console interface menu system
- Creates user input handling functions
- Develops display formatting for list visualization
- Coordinates with Data Structure Unit for integration

### DATA STRUCTURE UNIT (1-2 contributors)
- Implements the list management library
- Creates functions for add, remove, and status operations
- Ensures data persistence within session
- Coordinates with UI Development Unit for integration

---

## DELIVERABLES - PHASE 1

### 1. USER STORIES
Each team must create user stories for the following features in the prescribed format:

**Required Format:**
```
As a [user type],
I want to [action],
So that [benefit].

Acceptance Criteria:
- [Specific testable requirement]
- [Another specific requirement]
```

**Required Stories:**
- Add new item to list
- Mark item as complete
- View current list with status indicators

### 2. GITHUB REPOSITORY STRUCTURE
- Repository initialized with README.md
- .gitignore file appropriate for your chosen language
- Issues created for each user story
- Branch protection enabled on main branch
- All team members added as collaborators

### 3. INITIAL CODE FRAMEWORK
- Basic project structure established
- Separate modules/files for UI and data structure
- Function stubs with appropriate documentation
- At least one pull request per team member merged

---

## TECHNICAL SPECIFICATIONS

### Acceptable Implementation Languages
- Python (recommended for neural alignment)
- Java (for those seeking additional complexity)
- JavaScript (Node.js environment only)
- C++ (for the architecturally ambitious)

### Required Functionality Signatures

**Data Structure Unit must provide:**
- `add_item(description)` - Adds new todo item
- `complete_item(index)` - Marks item as complete  
- `get_all_items()` - Returns list of all items with status
- `get_pending_items()` - Returns only incomplete items
- `get_item_count()` - Returns total number of items

**UI Unit must provide:**
- Main menu loop with options
- Input validation for user choices
- Formatted display of todo list
- Clear screen functionality (OS-appropriate)
- Exit confirmation

---

## WORKFLOW REQUIREMENTS

1. **ALL work must be done in feature branches**
   - Branch names must follow pattern: `feature/description`
   - Direct commits to main branch will result in efficiency demerits

2. **ALL code must enter main via Pull Request**
   - PR must include description of changes
   - PR must reference related issue number
   - Build Master must approve before merge

3. **Commit Message Standards**
   - Must begin with type: `feat:`, `fix:`, `docs:`, `refactor:`
   - Must be written in imperative mood
   - Must not exceed 72 characters

4. **Issue Management**
   - Issues must be assigned before work begins
   - Issues must be labeled appropriately
   - Issues must be closed via PR

---

## ASSESSMENT CRITERIA

Your team's efficiency will be evaluated based on:

- Proper Git workflow adherence (40%)
- Functional code framework (30%)
- User story quality and completeness (20%)
- Team collaboration evidence (10%)

**Note**: The Algorithm values process compliance over feature completion in this exercise.

---

## SUBMISSION INSTRUCTIONS

1. Build Master submits repository URL via approved channels
2. All team members must have meaningful commit history
3. Repository must be public for Algorithm inspection
4. README must list all team members and their roles

---

## IMPORTANT NOTICES

- The Algorithm monitors all commit timestamps for productivity analysis
- Excessive commit frequency may trigger automated performance review
- Insufficient commit frequency will be noted in permanent record
- The optimal commit rate has not been disclosed

**REMINDER**: This is a collaborative exercise. The Algorithm has determined that teams attempting to bypass collaboration requirements show 67% higher project failure rates in subsequent assignments.

---

**THE ALGORITHM PROVIDES. THE ALGORITHM GUIDES. THE ALGORITHM EVALUATES.**

*Document Version 1.0.3 - Previous versions have been deprecated and discussing them is discouraged.*