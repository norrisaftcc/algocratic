"""
CLASSIFICATION: YELLOW CLEARANCE - QUALITY ASSURANCE DIRECTIVE
DOCUMENT: AF-SESSION5-ASSIGN3-Y-2025-14

# Quality Assurance Protocol™
## *Comprehensive Testing Strategy Under Resource Constraints*

The Algorithm has determined that your testing capabilities require immediate
enhancement. As a YELLOW clearance specialist, you must ensure system reliability
while optimizing for both coverage and execution speed. This assignment measures
your ability to design and implement testing strategies that satisfy contradictory
quality metrics.

RESOURCE ALLOCATION TIMELINE: 90 MINUTES
EFFICIENCY EXPECTATION: YELLOW

"""

import unittest
import time
import random
from typing import List, Dict, Any, Optional, Callable, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import json

# TESTING TARGET: AlgoCratic Task Management System (ATMS)

@dataclass
class Task:
    """Represents a task in the ATMS system"""
    task_id: str
    title: str
    priority: int  # 1-5, where 5 is highest
    assignee: str
    due_date: datetime
    status: str  # 'pending', 'in_progress', 'completed', 'blocked'
    dependencies: List[str]  # List of task_ids that must complete first
    estimated_hours: float
    actual_hours: float = 0.0
    completion_percentage: int = 0

class TaskManager:
    """
    AlgoCratic Task Management System - Core functionality
    
    This system manages task allocation, tracking, and optimization.
    Your job is to create comprehensive tests that ensure reliability
    while meeting The Algorithm's efficiency requirements.
    """
    
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.employees: Dict[str, List[str]] = {}  # employee -> list of task_ids
        self.performance_threshold = 0.8  # 80% on-time completion required
        
    def create_task(self, task_id: str, title: str, priority: int, 
                   assignee: str, due_date: datetime, dependencies: List[str],
                   estimated_hours: float) -> Task:
        """
        Creates a new task in the system.
        
        Validation rules:
        - Task ID must be unique
        - Priority must be 1-5
        - Assignee must not have more than 5 active tasks
        - Due date must be in the future
        - Dependencies must exist in the system
        - Estimated hours must be positive
        """
        # Validation logic
        if task_id in self.tasks:
            raise ValueError(f"Task {task_id} already exists")
            
        if not 1 <= priority <= 5:
            raise ValueError("Priority must be between 1 and 5")
            
        if assignee in self.employees and len(self.employees[assignee]) >= 5:
            active_tasks = [t for t in self.employees[assignee] 
                          if self.tasks[t].status != 'completed']
            if len(active_tasks) >= 5:
                raise ValueError(f"{assignee} has too many active tasks")
                
        if due_date <= datetime.now():
            raise ValueError("Due date must be in the future")
            
        for dep in dependencies:
            if dep not in self.tasks:
                raise ValueError(f"Dependency {dep} does not exist")
                
        if estimated_hours <= 0:
            raise ValueError("Estimated hours must be positive")
            
        # Create task
        task = Task(
            task_id=task_id,
            title=title,
            priority=priority,
            assignee=assignee,
            due_date=due_date,
            status='pending',
            dependencies=dependencies,
            estimated_hours=estimated_hours
        )
        
        self.tasks[task_id] = task
        
        # Update employee assignments
        if assignee not in self.employees:
            self.employees[assignee] = []
        self.employees[assignee].append(task_id)
        
        return task
        
    def update_task_progress(self, task_id: str, hours_worked: float, 
                           completion_percentage: int) -> None:
        """
        Updates task progress.
        
        Rules:
        - Task must exist
        - Hours worked must be positive
        - Completion percentage must be 0-100
        - Cannot update completed tasks
        - Status automatically updates based on percentage
        """
        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} does not exist")
            
        task = self.tasks[task_id]
        
        if task.status == 'completed':
            raise ValueError("Cannot update completed task")
            
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative")
            
        if not 0 <= completion_percentage <= 100:
            raise ValueError("Completion percentage must be 0-100")
            
        # Update task
        task.actual_hours += hours_worked
        task.completion_percentage = completion_percentage
        
        # Update status based on completion
        if completion_percentage == 0:
            task.status = 'pending'
        elif completion_percentage < 100:
            task.status = 'in_progress'
        else:
            task.status = 'completed'
            
    def get_employee_workload(self, employee: str) -> Dict[str, Any]:
        """
        Calculates current workload for an employee.
        
        Returns:
        - Total assigned tasks
        - Active tasks (not completed)
        - Total estimated hours remaining
        - Overdue tasks count
        - Performance score
        """
        if employee not in self.employees:
            return {
                'total_tasks': 0,
                'active_tasks': 0,
                'estimated_hours_remaining': 0.0,
                'overdue_tasks': 0,
                'performance_score': 1.0
            }
            
        task_ids = self.employees[employee]
        tasks = [self.tasks[tid] for tid in task_ids]
        
        active_tasks = [t for t in tasks if t.status != 'completed']
        overdue_tasks = [t for t in active_tasks if t.due_date < datetime.now()]
        
        hours_remaining = sum(
            t.estimated_hours * (1 - t.completion_percentage / 100)
            for t in active_tasks
        )
        
        # Calculate performance score
        completed_tasks = [t for t in tasks if t.status == 'completed']
        if completed_tasks:
            on_time = len([t for t in completed_tasks 
                         if t.actual_hours <= t.estimated_hours * 1.2])
            performance_score = on_time / len(completed_tasks)
        else:
            performance_score = 1.0
            
        return {
            'total_tasks': len(tasks),
            'active_tasks': len(active_tasks),
            'estimated_hours_remaining': hours_remaining,
            'overdue_tasks': len(overdue_tasks),
            'performance_score': performance_score
        }
        
    def check_task_dependencies(self, task_id: str) -> bool:
        """
        Checks if all dependencies for a task are completed.
        
        Returns True if task can be started, False otherwise.
        """
        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} does not exist")
            
        task = self.tasks[task_id]
        
        for dep_id in task.dependencies:
            if dep_id not in self.tasks:
                return False
            if self.tasks[dep_id].status != 'completed':
                return False
                
        return True
        
    def get_critical_path(self) -> List[str]:
        """
        Identifies the critical path of tasks (longest dependency chain).
        
        This is a simplified version that finds the longest chain of
        dependent tasks based on estimated hours.
        """
        # Build dependency graph
        graph = {}
        for task_id, task in self.tasks.items():
            graph[task_id] = task.dependencies
            
        # Find tasks with no dependencies (starting points)
        start_tasks = [tid for tid, deps in graph.items() if not deps]
        
        if not start_tasks:
            return []
            
        # Simple DFS to find longest path
        def find_longest_path(task_id: str, visited: set) -> Tuple[float, List[str]]:
            if task_id in visited:
                return (0, [])
                
            visited.add(task_id)
            task = self.tasks[task_id]
            
            # Find dependent tasks
            dependents = [tid for tid, task in self.tasks.items() 
                         if task_id in task.dependencies]
            
            if not dependents:
                return (task.estimated_hours, [task_id])
                
            # Recursively find longest path through dependents
            max_hours = 0
            max_path = []
            
            for dep_id in dependents:
                hours, path = find_longest_path(dep_id, visited.copy())
                if hours > max_hours:
                    max_hours = hours
                    max_path = path
                    
            return (task.estimated_hours + max_hours, [task_id] + max_path)
            
        # Find overall longest path
        longest_hours = 0
        critical_path = []
        
        for start_id in start_tasks:
            hours, path = find_longest_path(start_id, set())
            if hours > longest_hours:
                longest_hours = hours
                critical_path = path
                
        return critical_path

# ===== YOUR TESTING ASSIGNMENT BEGINS HERE =====

"""
QUALITY ASSURANCE DIRECTIVE™

The Algorithm requires comprehensive testing of the AlgoCratic Task Management
System. Your tests must balance multiple contradictory requirements:

1. COVERAGE REQUIREMENTS:
   - Achieve minimum 90% code coverage
   - Test all happy paths
   - Test all error conditions
   - Test edge cases and boundary conditions

2. EFFICIENCY CONSTRAINTS:
   - All tests must complete within 5 seconds total
   - No individual test may exceed 1 second
   - Minimize redundant test scenarios
   - Use efficient test data generation

3. TESTING PRIORITIES:
   - CRITICAL: Task creation and validation
   - HIGH: Progress tracking and status updates
   - MEDIUM: Workload calculations
   - LOW: Critical path analysis

4. SPECIAL REQUIREMENTS:
   - Include performance benchmarking
   - Test concurrent access scenarios
   - Verify data integrity under load
   - Document any discovered bugs

DELIVERABLES:

Create a comprehensive test suite using Python's unittest framework that:

1. Tests all methods in TaskManager
2. Includes positive and negative test cases
3. Uses setUp/tearDown for test isolation
4. Implements mock data generators for efficiency
5. Includes at least one performance test
6. Documents test coverage metrics

BONUS OBJECTIVES (For exemplary loyalty rating):
- Implement property-based testing for one method
- Create a stress test that verifies system behavior under load
- Design a test that catches a subtle bug in the existing code

Remember: The Algorithm values both thoroughness and efficiency. Tests that
are comprehensive but slow will be penalized. Tests that are fast but
incomplete will also be penalized. Find the optimal balance.

Example test structure provided below. Expand and complete it.
"""

class TestTaskManager(unittest.TestCase):
    """Comprehensive test suite for AlgoCratic Task Management System"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.tm = TaskManager()
        self.test_employee = "EMP001"
        self.future_date = datetime.now() + timedelta(days=7)
        
    def tearDown(self):
        """Clean up after each test method"""
        # Clean up any resources if needed
        pass
        
    def test_create_task_success(self):
        """Test successful task creation with valid inputs"""
        task = self.tm.create_task(
            task_id="TASK001",
            title="Implement Algorithm Worship Module",
            priority=3,
            assignee=self.test_employee,
            due_date=self.future_date,
            dependencies=[],
            estimated_hours=8.0
        )
        
        self.assertEqual(task.task_id, "TASK001")
        self.assertEqual(task.status, "pending")
        self.assertIn("TASK001", self.tm.tasks)
        
    def test_create_task_duplicate_id(self):
        """Test that duplicate task IDs raise appropriate error"""
        # Create first task
        self.tm.create_task(
            task_id="TASK001",
            title="First Task",
            priority=3,
            assignee=self.test_employee,
            due_date=self.future_date,
            dependencies=[],
            estimated_hours=8.0
        )
        
        # Attempt to create duplicate
        with self.assertRaises(ValueError) as context:
            self.tm.create_task(
                task_id="TASK001",
                title="Duplicate Task",
                priority=3,
                assignee=self.test_employee,
                due_date=self.future_date,
                dependencies=[],
                estimated_hours=8.0
            )
            
        self.assertIn("already exists", str(context.exception))
        
    # TODO: Implement remaining test methods
    # - test_create_task_invalid_priority
    # - test_create_task_too_many_assignments
    # - test_create_task_past_due_date
    # - test_create_task_missing_dependency
    # - test_create_task_negative_hours
    # - test_update_progress_success
    # - test_update_progress_completed_task
    # - test_update_progress_invalid_percentage
    # - test_get_employee_workload_calculations
    # - test_check_dependencies
    # - test_critical_path_simple
    # - test_critical_path_complex
    # - test_performance_benchmark
    # - test_concurrent_access
    # - test_stress_scenario

def run_test_suite():
    """Run the complete test suite and report results"""
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskManager)
    
    # Run tests with verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Report coverage metrics
    print("\n=== TEST COVERAGE REPORT ===")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.1f}%")
    
    return result

if __name__ == "__main__":
    # Run the test suite
    run_test_suite()