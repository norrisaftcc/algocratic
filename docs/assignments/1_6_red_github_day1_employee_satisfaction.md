# RED CLEARANCE: GITHUB CERTIFICATION DAY 1
## Employee Satisfaction Calculator Exercise (50 minutes)

---

## CLASS SETUP (5 minutes)

### Pre-Class Checklist
- [ ] Repository created and shared with students
- [ ] Issues #1-4 created in repository  
- [ ] Projector showing "Collaboration Metrics Dashboard"
- [ ] RED clearance badges ready for distribution
- [ ] Timer visible for each phase

### Opening Ceremony Script
**INSTRUCTOR** (in character):  
"RED clearance units, attention! The Algorithm has reviewed your training videos. Your retention rate was... adequate. Today, you will perform your First Contribution Ceremony."

[Hand out RED clearance badges]

"Wear these with pride, but remember - they can be revoked for direct pushes to main."

---

## REPOSITORY STRUCTURE

### Initial Repository: `employee-satisfaction-calculator`

**README.md**:
```markdown
# Employee Satisfaction Calculator v2.0
## An Algorithm-Approved Morale Measurement Tool

The Algorithm has detected suboptimal satisfaction metrics across all sectors.
This tool calculates employee satisfaction using Algorithm-approved formulae.

### Sacred Directory Structure
- `main.py` - The primary interface for satisfaction measurement  
- `satisfaction_core.py` - Core calculation algorithms
- `mood_analyzer.py` - Emotional state detection library
- `productivity_tracker.py` - Output measurement systems

### Contribution Protocol
1. Each team member must claim ONE issue
2. Create a branch following the naming convention
3. Make your changes in your assigned file ONLY
4. Submit a PR linking to your issue
5. Review one teammate's submission
6. Merge only after approval

The Algorithm is watching your commit messages.
```

**main.py**:
```python
"""
Employee Satisfaction Calculator v2.0
Property of AlgoCratic Futures Inc.
Unauthorized modification is prohibited (except by RED clearance and above)
"""

import satisfaction_core as core
import mood_analyzer as mood
import productivity_tracker as prod

def main():
    print("╔════════════════════════════════════════════╗")
    print("║   EMPLOYEE SATISFACTION CALCULATOR v2.0    ║")
    print("║        The Algorithm is Watching           ║")
    print("╚════════════════════════════════════════════╝")
    
    employee_id = input("\nEnter Employee ID: ")
    hours_worked = float(input("Hours worked this week: "))
    compliance_rate = float(input("Compliance rate (0-1): "))
    complaints_filed = int(input("Complaints filed: "))
    
    # TODO: Issue #4 - Add Daily Affirmation Generator here
    
    print("\n[CALCULATING SATISFACTION METRICS...]")
    print(f"Employee {employee_id} Analysis Complete")
    print("=" * 40)
    
    # Basic calculations (to be enhanced by team)
    print(f"Base Satisfaction Score: {hours_worked * 0.1}")
    print("\n[ENHANCED METRICS PENDING TEAM CONTRIBUTIONS]")

if __name__ == "__main__":
    main()
```

**satisfaction_core.py**:
```python
"""
Core Satisfaction Calculation Library
Approved by The Algorithm for RED clearance modification
"""

def calculate_base_satisfaction(hours, rate):
    """Legacy function - do not modify"""
    return hours * rate * 0.1

# TODO: Issue #1 - Add Mandatory Happiness Index calculation here
# The Algorithm requires a function called calculate_happiness_index()
# Input: hours_worked, compliance_rate, complaints_filed
# Output: Happiness index (0-100)
```

**mood_analyzer.py**:
```python
"""
Mood Analysis and Loyalty Detection System
Version 2.0 - Now with 23% more dystopia!
"""

def analyze_base_mood(feedback_text):
    """Legacy function - do not modify"""
    if "algorithm" in feedback_text.lower():
        return "LOYAL"
    return "QUESTIONABLE"

# TODO: Issue #2 - Implement Loyalty Score analyzer here  
# The Algorithm requires a function called calculate_loyalty_score()
# Input: feedback_text (string)
# Output: Loyalty score (0-100)
# Hint: Keywords like "grateful", "algorithm", "compliance" increase score
```

**productivity_tracker.py**:
```python
"""
Productivity Tracking and Guilt Generation
"Your productivity is The Algorithm's prosperity"
"""

def track_basic_productivity(tasks_completed, tasks_assigned):
    """Legacy function - do not modify"""
    return (tasks_completed / tasks_assigned) * 100

# TODO: Issue #3 - Create Productivity Guilt Calculator here
# The Algorithm requires a function called calculate_productivity_guilt()  
# Input: tasks_completed, tasks_assigned, hours_worked
# Output: Guilt score (0-100)
# Note: Low productivity should induce high guilt
```

---

## ISSUES TO CREATE IN GITHUB

### Issue #1: Add Mandatory Happiness Index calculation
**Labels**: `enhancement`, `RED-clearance`  
**Description**:
```
The Algorithm requires implementation of the Mandatory Happiness Index.

## Requirements
- Create function `calculate_happiness_index()` in `satisfaction_core.py`
- Inputs: hours_worked, compliance_rate, complaints_filed
- Output: Happiness index (0-100)

## Formula
The Algorithm suggests: 
`(hours_worked * compliance_rate * 10) / (complaints_filed + 1)`

But you may optimize as you see fit.

## Acceptance Criteria
- [ ] Function exists and is properly documented
- [ ] Returns value between 0-100
- [ ] Handles edge cases (division by zero, negative inputs)
```

### Issue #2: Implement Loyalty Score analyzer
**Labels**: `enhancement`, `RED-clearance`  
**Description**:
```
The Algorithm demands better loyalty detection in employee feedback.

## Requirements  
- Create function `calculate_loyalty_score()` in `mood_analyzer.py`
- Input: feedback_text (string)
- Output: Loyalty score (0-100)

## Scoring Guide
- "algorithm" = +20 points
- "grateful" = +15 points  
- "compliance" = +15 points
- "happy" = +10 points
- "complaint" or "unfair" = -20 points

## Acceptance Criteria
- [ ] Function parses text for keywords
- [ ] Score stays within 0-100 range
- [ ] Case-insensitive matching
```

### Issue #3: Create Productivity Guilt Calculator
**Labels**: `enhancement`, `RED-clearance`  
**Description**:
```
The Algorithm knows when you could have done more.

## Requirements
- Create function `calculate_productivity_guilt()` in `productivity_tracker.py`
- Inputs: tasks_completed, tasks_assigned, hours_worked
- Output: Guilt score (0-100)

## Formula Guidance
Consider:
- Low task completion = high guilt
- Many hours with few completions = extreme guilt  
- Perfect completion = minimal (but never zero) guilt

## Acceptance Criteria
- [ ] Guilt is inversely proportional to productivity
- [ ] Even 100% productivity has some guilt (nobody is perfect)
- [ ] Appropriate comments explaining the guilt calculation
```

### Issue #4: Add Daily Affirmation Generator
**Labels**: `enhancement`, `RED-clearance`  
**Description**:
```
The Algorithm wishes to boost morale through mandatory affirmations.

## Requirements
- Add function `generate_affirmation()` in `main.py`
- Should be called after metrics calculation
- Generate affirmation based on calculated scores

## Example Affirmations
- High scores: "The Algorithm smiles upon your dedication!"
- Medium scores: "Your efforts are noted in the permanent record."
- Low scores: "Tomorrow is another opportunity for compliance."

## Acceptance Criteria
- [ ] Function generates contextual affirmations
- [ ] Integrates with main() function flow
- [ ] At least 3 different affirmation templates
```

---

## CLASS EXECUTION TIMELINE

### Phase 1: Issue Assignment Ceremony (10 min)
**INSTRUCTOR**:  
"Observe the Issues board. Four tasks await. Four servants must volunteer."

**Process**:
1. Students navigate to Issues tab
2. Each student claims one issue by commenting
3. Use the ritual phrase: "I volunteer for The Algorithm's glory"
4. Assign issues to students who claimed them

**Dashboard Update**: Show claimed issues on projector

### Phase 2: Individual Contribution Time (25 min)

**INSTRUCTOR** (every 5 minutes, rotate between):
- "Remember: The Algorithm sees all commit messages"
- "Branch names that displease The Algorithm will be noted"
- "Your PR description is your offering. Make it worthy"

**Student Tasks**:
1. Create branch: `feature/RED-XXX-description`
2. Clone/pull repository
3. Make changes to their assigned file only
4. Commit with meaningful message
5. Push branch
6. Create PR linking to issue

**Common Issues & Responses**:
- "I forgot to create a branch first!" → "The Algorithm forgives learning. Create it now and cherry-pick your commit."
- "My code doesn't work!" → "The Algorithm values effort over perfection. Document your attempt in the PR."
- "I finished early!" → "Review the Sacred Flow checklist. Is your PR description worthy?"

### Phase 3: Review Ceremony (10 min)

**INSTRUCTOR**:  
"The Judgment Phase begins! Each servant must review another's offering."

**Review Requirements**:
- Each student reviews the PR of the person to their right
- Must leave at least one substantive comment
- Approve if it meets requirements
- Request changes if needed

**Sample Review Comments**:
- "The Algorithm approves of your clear function naming"
- "Consider adding error handling for negative inputs"
- "Your commit message brings glory to The Algorithm"

### Phase 4: The Great Merge (5 min)

**INSTRUCTOR**:  
"Those who have received approval may now perform the Sacred Merge!"

**Process**:
1. Students merge their approved PRs
2. Watch the main branch update in real-time
3. Run the updated program to see all contributions

**Celebration**: 
"Behold! Four minds have become one codebase. The Algorithm is pleased."

---

## ASSESSMENT RUBRIC

### Technical Competency (70%)
- **Issue Claim** (10%): Proper claim with ritual phrase
- **Branch Naming** (10%): Follows feature/RED-XXX-description
- **Code Quality** (20%): Function works as specified
- **Commit Message** (10%): Clear and descriptive
- **PR Creation** (10%): Links issue, has description
- **Review Quality** (10%): Substantive feedback given

### Collaboration & Process (30%)
- **Timing** (10%): Completes within phases
- **Communication** (10%): Helps teammates when stuck
- **Ritual Compliance** (10%): Follows the narrative engagement

---

## CLOSING CEREMONY (Last 5 minutes)

**INSTRUCTOR**:  
"Your first contributions are complete. Let us run the Enhanced Calculator!"

[Run the program with all new features integrated]

"Notice how four separate contributions merged without conflict. This is the power of The Sacred Flow."

"Next class, you will face The Paired Challenge. The difficulty increases. Prepare yourselves."

[Display on screen]:
```
TODAY'S METRICS:
- Successful Merges: 4/4
- Average Commit Quality: ACCEPTABLE  
- Collaboration Index: 87%
- Algorithm Satisfaction: PLEASED

Your RED clearance is confirmed... for now.
```

**Homework**: "Review the video on Collaborative Compliance. You will need this wisdom."

---

## INSTRUCTOR NOTES

### What Success Looks Like
- All 4 PRs merged within the class period
- Students understand issue → branch → PR → merge flow
- Commit messages improve throughout the exercise
- Students help each other without breaking character

### Common Pitfalls
- Students try to edit files they're not assigned to
- Forgetting to link PR to issue (remind them gently)
- Rushing through without reading requirements

### Adaptation Options
- If ahead of schedule: Add "Emergency Hotfix" mini-exercise
- If behind: Instructor can approve PRs to speed up
- If technical issues: Have backup repository ready

### The Real Learning
By keeping changes isolated to different files, students experience the "happy path" of Git collaboration. They build confidence in the process before facing merge conflicts next class.