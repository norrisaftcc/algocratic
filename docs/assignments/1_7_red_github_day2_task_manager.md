# RED CLEARANCE: GITHUB CERTIFICATION DAY 2
## Algorithmic Task Manager - Paired Development Protocol (50 minutes)

---

## CLASS SETUP (5 minutes)

### Pre-Class Checklist
- [ ] New repository created: `algorithmic-task-manager`
- [ ] Issues #1-4 created with pairing assignments
- [ ] "Merge Conflict Resolution Station" designated
- [ ] Collaboration Metrics Dashboard updated
- [ ] Synchronization timer ready

### Opening Ritual Script
**INSTRUCTOR** (more ominous than Day 1):  
"RED clearance units, The Algorithm has analyzed your individual contributions. Satisfactory."

[Pause dramatically]

"But The Algorithm requires more. Today, you will learn Collaborative Compliance."

[Display on screen: Two developers working on same file, everything on fire]

"Two minds. One file. Infinite possibilities for chaos."

---

## REPOSITORY STRUCTURE

### Initial Repository: `algorithmic-task-manager`

**README.md**:
```markdown
# Algorithmic Task Manager
## Collaborative Compliance Edition

The Algorithm demands efficient task management with proper guilt allocation.
This system tracks tasks, measures procrastination, and induces appropriate shame.

### Technical Architecture
- `task_manager.py` - Complex menu-driven interface (ALL TEAMS WILL MODIFY)
- `task_database.py` - Shared data operations (ALL TEAMS WILL MODIFY)

### Collaboration Protocol - PAY ATTENTION
1. Teams of TWO will work on paired issues
2. Both developers MUST modify the SAME file
3. Coordination is not optional - it is survival
4. The Algorithm watches for merge conflicts with great interest

### The Synchronization Ritual
When working in pairs:
1. Discuss your approach BEFORE coding
2. Create separate branches
3. Coordinate your merges
4. Resolve conflicts with wisdom

Failure to synchronize will result in conflicts.
Conflicts result in decreased satisfaction metrics.
You have been warned.
```

**task_manager.py** (Complex menu system):
```python
"""
Algorithmic Task Manager - Menu Interface
WARNING: Multiple developers will modify this file
The Algorithm enjoys watching you coordinate
"""

import task_database as db

def display_menu():
    """The Algorithm's Perfect Menu System - DO NOT MODIFY THIS FUNCTION"""
    print("\n" + "="*50)
    print("    ALGORITHMIC TASK MANAGER v3.0")
    print("    'Your Guilt is Our Productivity'")
    print("="*50)
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. [PENDING] View Tasks by Guilt Level")  # Issue #1
    print("6. [PENDING] Calculate Procrastination Score")  # Issue #2
    print("7. Generate Shame Report")
    print("8. View Algorithm's Disappointment Level")
    print("9. Exit (The Algorithm Never Sleeps)")
    print("="*50)

def add_task():
    """Add a new task to disappoint The Algorithm with"""
    title = input("Task title: ")
    priority = input("Priority (LOW/MEDIUM/HIGH/CRITICAL): ")
    db.create_task(title, priority)
    print(f"Task '{title}' added. The Algorithm expects completion.")

def view_tasks():
    """View all tasks and feel the weight of incompletion"""
    tasks = db.get_all_tasks()
    if not tasks:
        print("No tasks found. The Algorithm questions your productivity.")
        return
    
    print("\nCurrent Obligations:")
    print("-" * 40)
    for task in tasks:
        status = "COMPLETE" if task['completed'] else "PENDING"
        print(f"[{task['id']}] {task['title']} - {task['priority']} - {status}")

def mark_complete():
    """Mark a task complete and reduce guilt marginally"""
    task_id = int(input("Task ID to complete: "))
    if db.complete_task(task_id):
        print("Task completed. The Algorithm acknowledges your minimal effort.")
    else:
        print("Task not found. The Algorithm notes your confusion.")

def delete_task():
    """Delete a task (The Algorithm remembers all deletions)"""
    task_id = int(input("Task ID to delete: "))
    if db.delete_task(task_id):
        print("Task deleted. Your shame remains.")
    else:
        print("Task not found. Incompetence noted.")

# TODO: Issue #1 - Add view_tasks_by_guilt_level() function here
# This function should:
# 1. Get all tasks from database
# 2. Calculate guilt level for each task
# 3. Display tasks sorted by guilt level
# 4. Include appropriately dystopian messages

# TODO: Issue #2 - Add calculate_procrastination_score() function here  
# This function should:
# 1. Analyze all tasks' creation dates
# 2. Calculate procrastination metrics
# 3. Display a "Procrastination Report"
# 4. Suggest punishment levels

def generate_shame_report():
    """Generate a comprehensive report of your failures"""
    tasks = db.get_all_tasks()
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    
    print("\n*** SHAME REPORT ***")
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Failure Rate: {((total-completed)/total*100):.1f}%")
    print(f"Algorithm's Judgment: DISAPPOINTED")

def view_disappointment():
    """The Algorithm's current disappointment level"""
    import random
    level = random.choice([
        "MILDLY IRRITATED",
        "NOTABLY DISPLEASED", 
        "SIGNIFICANTLY DISAPPOINTED",
        "CONSIDERING YOUR TERMINATION"
    ])
    print(f"\nThe Algorithm's Current Mood: {level}")

def main():
    """Main loop - The Algorithm is always watching"""
    db.initialize()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("ERROR: Function not implemented. Guilt increased.")
            # TODO: Call view_tasks_by_guilt_level() once implemented
        elif choice == '6':
            print("ERROR: Function not implemented. Procrastination noted.")
            # TODO: Call calculate_procrastination_score() once implemented
        elif choice == '7':
            generate_shame_report()
        elif choice == '8':
            view_disappointment()
        elif choice == '9':
            print("\nThe Algorithm releases you... for now.")
            break
        else:
            print("Invalid choice. The Algorithm questions your literacy.")

if __name__ == "__main__":
    main()
```

**task_database.py** (Shared library):
```python
"""
Task Database Operations
WARNING: This file will experience simultaneous modifications
Prepare for merge conflicts. The Algorithm is amused by your struggles.
"""

import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def initialize():
    """Initialize the task database"""
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)

def get_all_tasks():
    """Retrieve all tasks from the database"""
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks back to the database"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def create_task(title, priority):
    """Create a new task"""
    tasks = get_all_tasks()
    new_task = {
        'id': max([t['id'] for t in tasks], default=0) + 1,
        'title': title,
        'priority': priority,
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'completed_at': None
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def complete_task(task_id):
    """Mark a task as complete"""
    tasks = get_all_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            task['completed_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    """Delete a task (but The Algorithm remembers)"""
    tasks = get_all_tasks()
    original_length = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    if len(tasks) < original_length:
        save_tasks(tasks)
        return True
    return False

# TODO: Issue #3 - Add store_guilt_level() function here
# This function should:
# 1. Accept task_id and guilt_level parameters
# 2. Update the task with guilt information
# 3. Save to database
# 4. Return success/failure

# TODO: Issue #4 - Add calculate_procrastination() function here
# This function should:
# 1. Accept a task dictionary
# 2. Calculate time between creation and completion (or current time)
# 3. Return a procrastination score
# 4. Include factors like priority in calculation
```

---

## PAIRED ISSUES FOR GITHUB

### Issue #1: Menu Enhancement - View Tasks by Guilt Level
**Labels**: `enhancement`, `RED-clearance`, `paired-work`  
**Assigned to**: Student A & Student B  
**Description**:
```
The Algorithm demands better guilt visibility in the task system.

## Requirements
- Add function `view_tasks_by_guilt_level()` in `task_manager.py`
- Integrate into menu option 5
- Display tasks sorted by guilt level (highest first)

## Guilt Calculation
- Base guilt = days since creation * 10
- HIGH priority = guilt * 2
- CRITICAL priority = guilt * 3
- Completed tasks = guilt * 0.1 (guilt never fully disappears)

## Implementation Notes
- You will need to import datetime for calculations
- Consider edge cases (tasks created today)
- Format output for maximum shame induction

## Coordination Required
Your teammate is modifying the same file. Discuss line numbers!
```

### Issue #2: Menu Enhancement - Procrastination Score Calculator
**Labels**: `enhancement`, `RED-clearance`, `paired-work`  
**Assigned to**: Student A & Student B  
**Description**:
```
The Algorithm wishes to quantify your procrastination precisely.

## Requirements
- Add function `calculate_procrastination_score()` in `task_manager.py`
- Integrate into menu option 6
- Generate comprehensive procrastination metrics

## Procrastination Report Should Include
- Average days tasks remain incomplete
- Longest procrastinated task
- Procrastination trend (getting worse/better)
- Suggested punishment level

## Warning
Your teammate is adding another function to the same file.
Coordinate or suffer merge conflicts!
```

### Issue #3: Database Enhancement - Guilt Storage
**Labels**: `enhancement`, `RED-clearance`, `paired-work`  
**Assigned to**: Student C & Student D  
**Description**:
```
The Algorithm requires persistent guilt storage in the database.

## Requirements
- Add function `store_guilt_level(task_id, guilt_level)` in `task_database.py`
- Modify task structure to include guilt_level field
- Ensure backward compatibility with existing tasks

## Technical Details
- Add guilt_level to task dictionary
- Update existing tasks with calculated guilt
- Preserve all existing functionality

## Coordination Alert
Your teammate is also modifying task_database.py!
Plan your approach together or face The Algorithm's laughter.
```

### Issue #4: Database Enhancement - Procrastination Calculator
**Labels**: `enhancement`, `RED-clearance`, `paired-work`  
**Assigned to**: Student C & Student D  
**Description**:
```
The Algorithm needs to calculate procrastination at the data layer.

## Requirements
- Add function `calculate_procrastination(task)` in `task_database.py`
- Accept a task dictionary as input
- Return numerical procrastination score

## Calculation Factors
- Time since creation (primary factor)
- Priority level (multiplier)
- Completion status
- Consider time of day created (late night = higher score)

## Merge Conflict Warning
Your teammate is adding another database function.
The Algorithm suggests you discuss your strategy.
```

---

## CLASS EXECUTION TIMELINE

### Phase 1: The Pairing Ceremony (7 min)

**INSTRUCTOR**:  
"Today's challenge requires... cooperation. Find your assigned partner."

[Display pairing assignments on screen]

"You have 5 minutes to perform the Synchronization Ceremony."

**Synchronization Ceremony Steps**:
1. Partners discuss their approach
2. Write down who will implement what parts
3. Decide who merges first
4. Create a "Development Pact" (written plan)

**Provide Pact Template**:
```
DEVELOPMENT PACT - Team _____

We, [Name] and [Name], swear by The Algorithm to:
- Developer 1 will implement: _____________
- Developer 2 will implement: _____________  
- First to merge: _____________
- Conflict resolution strategy: _____________

Signed in the presence of The Algorithm
```

### Phase 2: Parallel Development (20 min)

**INSTRUCTOR** (announce phases):

**[0-5 minutes]**: "Begin development. Remember - you're modifying the same file!"

**[5-10 minutes]**: "The Algorithm notes that no PRs have been created yet..."

**[10-15 minutes]**: "First PR detected! Other teams, The Algorithm grows impatient."

**[15-20 minutes]**: "Conflict resolution phase approaching. Prepare yourselves."

**Monitor for**:
- Teams actually talking to each other
- Proper branch creation
- Commit message quality
- Signs of impending conflicts

### Phase 3: The Merge Ritual (15 min)

**INSTRUCTOR**:  
"The first developers may now create their PRs. The second developers... prepare for synchronization."

**When first conflicts appear**:
"BEHOLD! The Algorithm has provided your first merge conflict! This is not failure - this is learning!"

**Guide conflict resolution**:
1. Second developer pulls latest main
2. Git shows conflict markers
3. Team discusses which code to keep
4. Resolve in VS Code
5. Commit the resolution
6. Push and create PR

**For successful resolutions**:
"The Algorithm witnesses your cooperation. Your Synchronization Score increases!"

### Phase 4: Integration Testing (8 min)

**INSTRUCTOR**:  
"All teams, run your enhanced task manager! Test each other's features!"

**Testing Requirements**:
- Each team demos their new functions
- Other teams try to break the features
- Document any bugs in Issues

**Celebration of Success**:
"Four minds have modified two files without destroying The Algorithm's code! This is the power of coordination!"

---

## ASSESSMENT ADDITIONS FOR DAY 2

### Collaboration Metrics (40%)
- **Development Pact Quality** (10%): Clear plan created
- **Communication During Dev** (10%): Observed coordination
- **Conflict Resolution** (10%): Handled merge conflicts well
- **Peer Support** (10%): Helped other teams

### Technical Execution (60%)
- Same as Day 1, plus:
- **Integration Success** (10%): Both features work together
- **Code Compatibility** (10%): No breaking changes

---

## CLOSING CEREMONY

**INSTRUCTOR**:  
"Observe what you have accomplished. Where once was chaos, now stands coordinated code."

[Run the fully integrated task manager]

"The Algorithm has prepared you for the reality of collaborative development. In the world beyond these walls, you will face larger teams, more complex conflicts, and even less coordination."

"But you now possess the Sacred Knowledge: Branch. Communicate. Pull. Resolve. Merge."

[Display final metrics]:
```
COLLABORATION REPORT:
- Successful Integrations: X/4
- Average Conflict Resolution Time: X minutes
- Code Quality Index: X%
- Synchronization Score: X/100

The Algorithm's Judgment: [ADAPTIVE MESSAGE BASED ON PERFORMANCE]
```

"Your RED clearance is confirmed. Next week, you face ORANGE clearance challenges. The complexity increases exponentially."

---

## INSTRUCTOR TROUBLESHOOTING GUIDE

### Common Day 2 Issues

**"We don't know how to resolve conflicts!"**
- Have them read the conflict markers carefully
- Explain they need to choose which code to keep
- Show VS Code's conflict resolution UI

**"Our functions don't work together!"**
- Usually an import issue or function naming mismatch
- Check their Development Pact - did they follow it?

**"We finished our parts but don't know who merges first"**
- Remind them of their Pact
- If no pact, flip a coin (The Algorithm decides)

**"Everything is broken!"**
- Deep breath
- Git log to see what happened
- Sometimes easier to reset and cherry-pick commits

### Success Indicators
- Most teams experience at least one conflict
- Teams resolve conflicts through discussion, not instructor help
- Improved commit messages from Day 1
- Evidence of actual planning before coding

### The Meta-Learning
Students discover that Git's "annoying" processes exist because coordination is hard. The dystopian frame makes the frustration fun while teaching real collaboration skills.