"""
CLASSIFICATION: ORANGE CLEARANCE - EMERGENCY PROTOCOL
DOCUMENT: AF-SESSION3-ASSIGN1-O-2025-12

# Emergency Debugging Protocol™ - Part 1: Diagnostic Phase
## *Crisis-Level System Failure Analysis Under Temporal Constraints*

The Algorithm has detected Critical System Anomalies™ in the AlgoCratic Employee
Productivity Tracking System (AEPTS). Your debugging skills have been deemed
adequate for emergency deployment. Immediate diagnostic analysis is required
to prevent cascading organizational efficiency failures.

RESOURCE ALLOCATION TIMELINE: 45 MINUTES
CRISIS ESCALATION LEVEL: ORANGE

Note: This is Part 1 of a 2-part emergency protocol. Part 2 will involve
implementing fixes based on your diagnostic findings.

"""

import random
import datetime
import json
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass

# SYSTEM STATUS: MALFUNCTIONING - REQUIRES EMERGENCY DEBUGGING

@dataclass
class EmployeeRecord:
    """Employee productivity tracking record"""
    employee_id: str
    name: str
    department: str
    productivity_score: float
    tasks_completed: int
    last_activity: datetime.datetime
    loyalty_rating: str

# Global system state (contains multiple bugs)
SYSTEM_STATE = {
    'active_employees': [],
    'productivity_threshold': 85.0,
    'loyalty_categories': ['SUSPICIOUS', 'ACCEPTABLE', 'COMMENDABLE', 'EXEMPLARY'],
    'department_weights': {
        'Engineering': 1.2,
        'Marketing': 0.9,
        'HR': 0.8,
        'Finance': 1.1,
        'Operations': 1.0
    }
}

def calculate_productivity_score(tasks_completed: int, hours_worked: float, 
                               department: str) -> float:
    """
    Calculates employee productivity score based on tasks and hours.
    
    Formula: (tasks_completed / hours_worked) * department_weight * 10
    
    Args:
        tasks_completed: Number of tasks completed today
        hours_worked: Hours worked today
        department: Employee's department
        
    Returns:
        float: Productivity score (0-100 scale)
        
    >>> calculate_productivity_score(8, 8.0, 'Engineering')
    96.0
    >>> calculate_productivity_score(5, 8.0, 'Marketing')
    56.25
    """
    if hours_worked <= 0:
        return 0.0
    
    base_score = (tasks_completed / hours_worked) * 10
    department_weight = SYSTEM_STATE['department_weights'].get(department, 1.0)
    
    # BUG: This calculation has an issue with department weight application
    final_score = base_score + department_weight
    
    # BUG: Score validation logic has problems
    if final_score > 100:
        final_score = 100
    elif final_score < 0:
        final_score = 0
        
    return final_score

def determine_loyalty_rating(productivity_score: float, days_employed: int) -> str:
    """
    Determines employee loyalty rating based on productivity and tenure.
    
    Args:
        productivity_score: Employee's current productivity score
        days_employed: Number of days employed
        
    Returns:
        str: Loyalty rating category
        
    >>> determine_loyalty_rating(95.0, 365)
    'EXEMPLARY'
    >>> determine_loyalty_rating(75.0, 30)
    'ACCEPTABLE'
    """
    # BUG: Logic flow has multiple issues
    if productivity_score >= 90 and days_employed > 180:
        return 'EXEMPLARY'
    elif productivity_score >= 80:
        return 'COMMENDABLE'
    elif productivity_score >= 70 or days_employed < 90:
        return 'ACCEPTABLE'
    else:
        return 'SUSPICIOUS'

def process_daily_metrics(employee_data: Dict[str, Any]) -> EmployeeRecord:
    """
    Processes daily employee metrics and creates record.
    
    Args:
        employee_data: Dictionary containing employee information
        
    Returns:
        EmployeeRecord: Processed employee record
        
    Example employee_data format:
    {
        'id': 'EMP001',
        'name': 'John Smith',
        'department': 'Engineering',
        'tasks_today': 8,
        'hours_today': 8.5,
        'hire_date': '2023-01-15'
    }
    """
    try:
        # BUG: Date parsing has issues
        hire_date = datetime.datetime.strptime(employee_data['hire_date'], '%Y-%m-%d')
        days_employed = (datetime.datetime.now() - hire_date).days
        
        # Calculate productivity score
        productivity = calculate_productivity_score(
            employee_data['tasks_today'],
            employee_data['hours_today'],
            employee_data['department']
        )
        
        # Determine loyalty rating
        loyalty = determine_loyalty_rating(productivity, days_employed)
        
        # BUG: Record creation has parameter issues
        record = EmployeeRecord(
            employee_id=employee_data['id'],
            name=employee_data['name'],
            department=employee_data['department'],
            productivity_score=productivity,
            tasks_completed=employee_data['tasks_today'],
            last_activity=datetime.datetime.now(),
            loyalty_rating=loyalty
        )
        
        return record
        
    except Exception as e:
        # BUG: Error handling is inadequate
        print(f"Error processing employee {employee_data['id']}: {e}")
        return None

def generate_daily_report(employee_records: List[EmployeeRecord]) -> Dict[str, Any]:
    """
    Generates daily productivity report for management.
    
    Args:
        employee_records: List of processed employee records
        
    Returns:
        Dict containing report statistics
    """
    if not employee_records:
        return {'error': 'No employee data available'}
    
    # Filter out None records (from processing errors)
    valid_records = [r for r in employee_records if r is not None]
    
    if not valid_records:
        return {'error': 'No valid employee records'}
    
    # Calculate department statistics
    dept_stats = {}
    for record in valid_records:
        dept = record.department
        if dept not in dept_stats:
            dept_stats[dept] = {
                'employee_count': 0,
                'total_productivity': 0,
                'loyalty_breakdown': {}
            }
        
        dept_stats[dept]['employee_count'] += 1
        dept_stats[dept]['total_productivity'] += record.productivity_score
        
        # BUG: Loyalty tracking has issues
        loyalty = record.loyalty_rating
        if loyalty in dept_stats[dept]['loyalty_breakdown']:
            dept_stats[dept]['loyalty_breakdown'][loyalty] += 1
        else:
            dept_stats[dept]['loyalty_breakdown'][loyalty] = 1
    
    # Calculate averages
    for dept, stats in dept_stats.items():
        # BUG: Average calculation has division issues
        stats['average_productivity'] = stats['total_productivity'] / stats['employee_count']
    
    # Overall statistics
    total_employees = len(valid_records)
    total_productivity = sum(r.productivity_score for r in valid_records)
    average_productivity = total_productivity / total_employees
    
    # BUG: Alert logic has problems
    alert_level = 'GREEN'
    if average_productivity < SYSTEM_STATE['productivity_threshold']:
        alert_level = 'YELLOW'
    if average_productivity < 60:
        alert_level = 'RED'
    
    return {
        'date': datetime.datetime.now().strftime('%Y-%m-%d'),
        'total_employees': total_employees,
        'average_productivity': average_productivity,
        'alert_level': alert_level,
        'department_statistics': dept_stats
    }

# Sample test data (contains data that will trigger bugs)
SAMPLE_EMPLOYEE_DATA = [
    {
        'id': 'EMP001',
        'name': 'Alice Johnson',
        'department': 'Engineering',
        'tasks_today': 12,
        'hours_today': 8.0,
        'hire_date': '2023-01-15'
    },
    {
        'id': 'EMP002',
        'name': 'Bob Wilson',
        'department': 'Marketing',
        'tasks_today': 6,
        'hours_today': 7.5,
        'hire_date': '2024-08-01'
    },
    {
        'id': 'EMP003',
        'name': 'Carol Davis',
        'department': 'Finance',
        'tasks_today': 0,  # Edge case: no tasks completed
        'hours_today': 8.0,
        'hire_date': '2022-03-10'
    },
    {
        'id': 'EMP004',
        'name': 'David Brown',
        'department': 'HR',
        'tasks_today': 4,
        'hours_today': 0,  # Edge case: zero hours logged
        'hire_date': '2023-11-20'
    },
    {
        'id': 'EMP005',
        'name': 'Eve Miller',
        'department': 'Operations',
        'tasks_today': 15,
        'hours_today': 10.0,
        'hire_date': '2020-05-30'
    },
    {
        'id': 'EMP006',
        'name': 'Frank Garcia',
        'department': 'Research',  # Department not in weights dict
        'tasks_today': 8,
        'hours_today': 8.0,
        'hire_date': '2023-07-12'
    }
]

def run_system_test():
    """
    Runs the productivity tracking system with sample data.
    This function will demonstrate the bugs when executed.
    """
    print("=== ALGOCRATIC EMPLOYEE PRODUCTIVITY TRACKING SYSTEM ===")
    print("Running daily processing...")
    print()
    
    # Process all employee data
    records = []
    for emp_data in SAMPLE_EMPLOYEE_DATA:
        record = process_daily_metrics(emp_data)
        records.append(record)
        if record:
            print(f"Processed: {record.name} - Productivity: {record.productivity_score:.1f} - Loyalty: {record.loyalty_rating}")
    
    print()
    print("Generating daily report...")
    
    # Generate report
    report = generate_daily_report(records)
    
    print("=== DAILY PRODUCTIVITY REPORT ===")
    print(json.dumps(report, indent=2, default=str))

# ===== DEBUGGING ASSIGNMENT BEGINS HERE =====

"""
EMERGENCY DIAGNOSTIC PROTOCOL™

SITUATION: The AlgoCratic Employee Productivity Tracking System is producing
incorrect results and management is demanding immediate answers. You have been
assigned to perform emergency diagnostic analysis.

PHASE 1 OBJECTIVES:

1. IDENTIFY ALL BUGS: Run the system and identify every bug/issue you can find.
   Document each bug with:
   - Location (function name and line description)
   - Expected behavior vs actual behavior
   - Impact on system functionality

2. CATEGORIZE ISSUES: Classify each bug by severity:
   - CRITICAL: System crashes or produces completely wrong results
   - HIGH: Incorrect calculations or logic errors
   - MEDIUM: Edge case handling problems
   - LOW: Code quality or minor logic issues

3. ANALYZE ROOT CAUSES: For each bug, explain why it occurs and what the
   correct implementation should be.

4. DOCUMENT TESTING STRATEGY: Describe how you would test each fix to ensure
   it works correctly.

CONSTRAINT: You are NOT to fix any bugs in Part 1. Your job is purely
diagnostic. Part 2 will involve implementing the fixes.

DELIVERABLE: Create a detailed bug report following this format:

BUG REPORT FORMAT:
==================

BUG #X: [Brief Description]
Location: [Function name and code area]
Severity: [CRITICAL/HIGH/MEDIUM/LOW]
Current Behavior: [What actually happens]
Expected Behavior: [What should happen]
Root Cause: [Why the bug occurs]
Test Case: [How to reproduce/test]
Fix Strategy: [High-level approach to fix]

==================

Complete your diagnostic analysis by running run_system_test() and analyzing
all output. Look for:
- Calculation errors
- Logic flow problems
- Edge case failures
- Error handling issues
- Data type problems
- Missing validation

The Algorithm expects thorough analysis. Incomplete diagnostics will result
in loyalty score penalties.

TIME ALLOCATION:
- 10 minutes: Initial code review and understanding
- 20 minutes: Running tests and identifying bugs
- 15 minutes: Documenting findings and analysis

BEGIN DIAGNOSTIC PROTOCOL NOW.
"""

if __name__ == "__main__":
    print("DIAGNOSTIC MODE: Running system test to identify bugs...")
    print("=" * 60)
    run_system_test()
    print("=" * 60)
    print("DIAGNOSTIC COMPLETE: Analyze output and document all bugs found.")