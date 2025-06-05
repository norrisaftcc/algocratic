"""
CLASSIFICATION: ORANGE CLEARANCE - EMERGENCY PROTOCOL
DOCUMENT: AF-SESSION3-ASSIGN2-O-2025-12

# Emergency Debugging Protocol™ - Part 2: Crisis Resolution Implementation
## *Systematic Bug Remediation Under Continued Temporal Pressure*

Based on your diagnostic analysis from Part 1, The Algorithm has authorized
you to proceed with Crisis Resolution Implementation™. Your bug identification
skills have been deemed adequate. Now you must demonstrate code remediation
capabilities under sustained pressure.

RESOURCE ALLOCATION TIMELINE: 45 MINUTES
CRISIS ESCALATION LEVEL: ORANGE (MAINTAINED)

PREREQUISITE: Completion of Part 1 diagnostic analysis with documented bug report.

"""

import random
import datetime
import json
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass

# SYSTEM STATUS: UNDERGOING EMERGENCY REPAIRS

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

# Global system state (to be debugged and fixed)
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
    # FIX REQUIRED: Implement corrected productivity calculation
    # Based on your Part 1 analysis, fix the calculation logic
    pass  # Replace with your implementation

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
    # FIX REQUIRED: Implement corrected loyalty rating logic
    # Based on your Part 1 analysis, fix the conditional logic
    pass  # Replace with your implementation

def process_daily_metrics(employee_data: Dict[str, Any]) -> Optional[EmployeeRecord]:
    """
    Processes daily employee metrics and creates record.
    
    Args:
        employee_data: Dictionary containing employee information
        
    Returns:
        EmployeeRecord: Processed employee record, or None if processing fails
        
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
    # FIX REQUIRED: Implement robust error handling and data validation
    # Based on your Part 1 analysis, fix all identified issues
    pass  # Replace with your implementation

def generate_daily_report(employee_records: List[Optional[EmployeeRecord]]) -> Dict[str, Any]:
    """
    Generates daily productivity report for management.
    
    Args:
        employee_records: List of processed employee records (may contain None values)
        
    Returns:
        Dict containing report statistics
    """
    # FIX REQUIRED: Implement corrected report generation
    # Based on your Part 1 analysis, fix all calculation and logic errors
    pass  # Replace with your implementation

# Sample test data (same as Part 1 - designed to test your fixes)
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
    This should now work correctly with your fixes.
    """
    print("=== ALGOCRATIC EMPLOYEE PRODUCTIVITY TRACKING SYSTEM (FIXED) ===")
    print("Running daily processing...")
    print()
    
    # Process all employee data
    records = []
    for emp_data in SAMPLE_EMPLOYEE_DATA:
        record = process_daily_metrics(emp_data)
        records.append(record)
        if record:
            print(f"Processed: {record.name} - Productivity: {record.productivity_score:.1f} - Loyalty: {record.loyalty_rating}")
        else:
            print(f"Failed to process employee {emp_data['id']}: {emp_data['name']}")
    
    print()
    print("Generating daily report...")
    
    # Generate report
    report = generate_daily_report(records)
    
    print("=== DAILY PRODUCTIVITY REPORT ===")
    print(json.dumps(report, indent=2, default=str))

def run_validation_tests():
    """
    Runs additional validation tests to verify your fixes work correctly.
    """
    print("\n=== VALIDATION TESTS ===")
    
    # Test 1: Productivity calculation validation
    print("Test 1: Productivity Calculation")
    test_score = calculate_productivity_score(8, 8.0, 'Engineering')
    expected_score = 96.0  # (8/8) * 1.2 * 10 = 12.0 * 8 = 96.0
    print(f"  Expected: {expected_score}, Got: {test_score}")
    print(f"  Result: {'PASS' if abs(test_score - expected_score) < 0.1 else 'FAIL'}")
    
    # Test 2: Edge case handling
    print("\nTest 2: Zero Hours Edge Case")
    test_score = calculate_productivity_score(5, 0, 'Marketing')
    print(f"  Zero hours should return 0.0, Got: {test_score}")
    print(f"  Result: {'PASS' if test_score == 0.0 else 'FAIL'}")
    
    # Test 3: Loyalty rating logic
    print("\nTest 3: Loyalty Rating Logic")
    test_loyalty = determine_loyalty_rating(95.0, 365)
    print(f"  High productivity + long tenure should be EXEMPLARY, Got: {test_loyalty}")
    print(f"  Result: {'PASS' if test_loyalty == 'EXEMPLARY' else 'FAIL'}")
    
    # Test 4: Unknown department handling
    print("\nTest 4: Unknown Department Handling")
    test_score = calculate_productivity_score(10, 8.0, 'UnknownDept')
    expected_score = 100.0  # (10/8) * 1.0 * 10 = 12.5 * 8 = 100.0 (capped)
    print(f"  Unknown dept should use 1.0 weight, Expected: {expected_score}, Got: {test_score}")
    print(f"  Result: {'PASS' if abs(test_score - expected_score) < 0.1 else 'FAIL'}")

# ===== IMPLEMENTATION ASSIGNMENT BEGINS HERE =====

"""
EMERGENCY RESOLUTION PROTOCOL™

SITUATION: Your diagnostic analysis from Part 1 has been reviewed by The Algorithm.
Management demands immediate implementation of fixes to restore system functionality.

PHASE 2 OBJECTIVES:

1. IMPLEMENT ALL FIXES: Based on your Part 1 bug report, implement fixes for
   every bug you identified. Your fixes must:
   - Correct the logic errors
   - Handle edge cases properly
   - Maintain the original function signatures
   - Preserve the intended behavior when inputs are valid

2. COMPREHENSIVE TESTING: Ensure your fixes work by:
   - Running the provided test suite
   - Verifying all edge cases are handled
   - Confirming calculations are mathematically correct
   - Testing error conditions gracefully

3. CODE QUALITY: Your implementations must demonstrate:
   - Proper error handling
   - Input validation
   - Clear logic flow
   - Appropriate use of type hints
   - Defensive programming practices

IMPLEMENTATION REQUIREMENTS:

A. calculate_productivity_score():
   - Fix the department weight multiplication (it should multiply, not add)
   - Handle zero/negative hours correctly
   - Handle unknown departments (default weight = 1.0)
   - Ensure score stays within 0-100 range

B. determine_loyalty_rating():
   - Fix the logical flow (current logic has precedence issues)
   - Ensure all combinations of productivity/tenure are handled correctly
   - Return only valid loyalty categories

C. process_daily_metrics():
   - Add proper input validation
   - Handle date parsing errors gracefully
   - Return None for invalid data instead of crashing
   - Ensure all EmployeeRecord fields are populated correctly

D. generate_daily_report():
   - Handle empty/invalid record lists
   - Fix division by zero errors
   - Correct the loyalty tracking logic
   - Ensure proper alert level calculation

CONSTRAINT REMINDERS:
- Function signatures must remain unchanged
- Original test data must work correctly after fixes
- All edge cases in the sample data must be handled gracefully
- The system should never crash, even with bad input

DELIVERABLE: Complete implementations of all four functions that pass both
the main test and validation tests.

TIME ALLOCATION:
- 35 minutes: Implementation of fixes
- 10 minutes: Testing and validation

The Algorithm monitors your implementation speed and correctness. Efficient
debugging demonstrates superior technical competency.

BEGIN IMPLEMENTATION PROTOCOL NOW.
"""

if __name__ == "__main__":
    print("IMPLEMENTATION MODE: Testing fixed system...")
    print("=" * 60)
    run_system_test()
    print("=" * 60)
    run_validation_tests()
    print("=" * 60)
    print("CRISIS RESOLUTION COMPLETE: All systems operational.")