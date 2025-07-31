# Development Environment Onboarding Guide
## *Teaching Modern Development Tools Through Dystopian Corporate IT*

**CLASSIFICATION: OUT-OF-CHARACTER**  
**DOCUMENT: INSTRUCTOR-DEVENV-GUIDE-2025-01**

---

## Overview & Educational Goals

This assignment introduces students to essential development tools (VS Code and GitHub Codespaces) through the satirical lens of AlgoCratic's corporate dystopia. Tool onboarding is often the most frustrating part of a programming course, but by framing it as deliberately absurd corporate policy, we create a more engaging experience while still teaching crucial skills.

By the end of this assignment, students should be able to:
- Install and configure VS Code on their local machine
- Access and use GitHub repositories and Codespaces
- Navigate basic IDE features and Git operations
- Execute simple command-line operations
- Run tests to verify their environment is working correctly

This assignment is designed for INFRARED clearance level (absolute beginners), making it an ideal starting point for the course.

---

## The Pedagogical Method Behind the Approach

The satirical framing of development environment setup serves several educational purposes:

1. **Reduces Frustration**: By acknowledging that environment setup is tedious through satire, we defuse frustration

2. **Creates Technical Documentation Literacy**: Students practice following detailed technical instructions while recognizing when instructions are ridiculous

3. **Introduces Corporate IT Culture**: The exaggerated policies mirror (slightly) more reasonable IT policies students will encounter professionally

4. **Builds Confidence**: Successfully navigating an intentionally intimidating setup process builds confidence for real technical challenges

5. **Establishes Course Tone**: The assignment immediately introduces the satirical dystopian theme that will run throughout the course

---

## Technical Prerequisites

Before conducting this exercise, ensure:

1. **GitHub Organization Setup**:
   - Create a GitHub organization for your class
   - Prepare repository templates with the verification files
   - Set up team permissions appropriately
   
2. **VS Code Extensions**:
   - Create a list of recommended extensions for your course
   - Consider creating a custom extension pack for easy installation
   
3. **Codespaces Configuration**:
   - Configure devcontainer.json with appropriate settings
   - Ensure Codespaces quotas are sufficient for your class size
   - Test the environment thoroughly before assigning

---

## Setup Instructions

### 1. Repository Preparation

Create a template repository containing:

1. `verify_environment.py` - Script to verify environment setup
   ```python
   """Environment verification script"""
   import os
   import sys
   
   def test_environment_setup():
       """Test that the environment is properly configured."""
       # Test that loyalty verification file exists
       assert os.path.exists('loyalty_verification.txt'), "Loyalty verification file missing"
       
       # Test loyalty file contents
       with open('loyalty_verification.txt', 'r') as f:
           content = f.read().strip()
           assert content == "The Algorithm Provides", "Incorrect loyalty verification content"
       
       # Test probationary_unit_info.py exists and can be imported
       assert os.path.exists('probationary_unit_info.py'), "Probationary unit info file missing"
       
       try:
           import probationary_unit_info
           info = probationary_unit_info.identify()
           assert "name" in info and info["name"] != "YOUR FULL LEGAL NAME", "Name not properly configured"
           assert "employee_id" in info and info["employee_id"] != "YOUR ASSIGNED ID", "ID not properly configured"
       except ImportError:
           assert False, "Could not import probationary_unit_info module"
       except Exception as e:
           assert False, f"Error in probationary_unit_info module: {str(e)}"
       
       return True
   ```

2. `infrared_verification_task.py` - The implementation file students will modify
   ```python
   """
   INFRARED CLEARANCE VERIFICATION TASK
   This file contains functions that must be implemented to verify minimal competence.
   """
   
   def calculate_algorithm_loyalty_score(productivity_metric, obedience_factor, initiative_suppression=True):
       """
       Calculates an employee's Algorithm Loyalty Score™ based on input metrics.
       
       Args:
           productivity_metric: Numeric value from 0-100
           obedience_factor: Numeric value from 0-100
           initiative_suppression: Boolean indicating proper suppression of independent thought
       
       Returns:
           float: The calculated Algorithm Loyalty Score™
       """
       # YOUR IMPLEMENTATION HERE
       pass
   ```

3. `infrared_verification_task_test.py` - Tests for the implementation
   ```python
   """Tests for the verification task implementation."""
   import pytest
   from infrared_verification_task import calculate_algorithm_loyalty_score
   
   def test_calculate_algorithm_loyalty_score_with_suppression():
       """Test loyalty calculation with initiative properly suppressed."""
       assert calculate_algorithm_loyalty_score(80, 90, True) == 84.0
       assert calculate_algorithm_loyalty_score(50, 50, True) == 50.0
       assert calculate_algorithm_loyalty_score(0, 100, True) == 40.0
       assert calculate_algorithm_loyalty_score(100, 0, True) == 60.0
   
   def test_calculate_algorithm_loyalty_score_without_suppression():
       """Test loyalty calculation with dangerous independent thought."""
       assert calculate_algorithm_loyalty_score(80, 90, False) == 69.0
       assert calculate_algorithm_loyalty_score(50, 50, False) == 35.0
       assert calculate_algorithm_loyalty_score(100, 100, False) == 85.0
   
   def test_calculate_algorithm_loyalty_score_default_parameters():
       """Test loyalty calculation with default parameters."""
       assert calculate_algorithm_loyalty_score(70, 80) == 74.0
       assert calculate_algorithm_loyalty_score(90, 60) == 78.0
   ```

### 2. GitHub Classroom Setup

1. Create an assignment in GitHub Classroom using your template repository
2. Configure it to automatically create personal repositories for each student
3. Ensure Codespaces are enabled for the organization and assignment

### 3. Instructor Environment Testing

Before releasing to students:
1. Accept the assignment yourself as a test student
2. Follow all the steps in the assignment document
3. Verify that the environment and tests work as expected
4. Check that Codespaces launches correctly

---

## Classroom Implementation

### Day 1: Introduction (45-60 minutes)

1. Present the satirical "Authorized Developer Interface Configuration Protocol" with appropriate corporate seriousness
2. Demonstrate VS Code installation and basic features
3. Show how to access GitHub and create a Codespace
4. Explain the verification exercise while maintaining the dystopian character
5. Allow students to begin environment setup with support available

### Day 2: Troubleshooting and Completion (30-45 minutes)

1. Address common setup issues students encountered
2. Demonstrate how to complete the verification exercise
3. Show how to commit and push changes
4. Verify that all students have a working environment
5. Break character to explain which parts of the setup are genuinely important vs. satirical

---

## Real-World Connection Points

During the out-of-character debriefing, connect the satirical elements to actual software development practices:

### "Authorized Development Tools"
**Satire**: The concept of only using "Algorithm-approved" development tools

**Real-World Parallel**: Many companies do have standardized development environments and require specific tools for consistency, security, and team efficiency

### "Prohibited IDE Functionality"
**Satire**: The absurd restriction of basic features like "Find in files" for low-clearance employees

**Real-World Parallel**: Feature restrictions based on role/permissions exist in many enterprise systems, though usually for security rather than hierarchy reasons

### "Mandatory Extensions"
**Satire**: Required installation of "Productivity Surveillance Toolkit"

**Real-World Parallel**: Many development teams do require certain extensions for linting, style checking, and other quality control measures

---

## Troubleshooting Common Issues

Be prepared to help students with these common environment setup issues:

### VS Code Installation Issues
- **Windows**: PATH issues, permission problems during installation
- **Mac**: Gatekeeper blocking execution, PATH not configured properly
- **Linux**: Package repository issues, dependency problems

### GitHub Access Issues
- Account creation problems
- Organization invitation not received or accepted
- Repository permissions configuration

### Codespaces Issues
- Quotas/limits exceeded for free accounts
- Slow startup time or timeout issues
- Compatibility issues with student browsers

### Implementation Issues
- Syntax errors in Python implementation
- Misunderstanding of the loyalty score formula
- Test interpretation difficulties

---

## Assessment Strategy

### Formative Assessment

During setup, evaluate:
- Students' ability to follow technical instructions
- Troubleshooting approaches when they encounter issues
- Understanding of basic Git operations
- Comfort with the VS Code interface

### Summative Assessment

After completion, verify:
- Successful environment setup (all verification tests pass)
- Correctly implemented loyalty score calculation
- Proper submission via Git
- Understanding of the development workflow

### Grading Rubric

This is typically a completion-based assignment rather than a graded one, but if grading is required:

| Criterion | Excellent | Satisfactory | Needs Improvement |
|-----------|-----------|--------------|-------------------|
| Environment Setup | All components installed correctly with verification passing | Environment works with minor issues | Failed to set up working environment |
| Code Implementation | Loyalty score function works perfectly with all tests passing | Function works with some test failures | Function not implemented correctly |
| Git Operations | Successfully completed all required Git operations | Completed basic operations with some assistance | Unable to use Git effectively |
| Documentation | Completed all documentation steps correctly | Completed most documentation with minor issues | Failed to properly document setup |

---

## Educational Context

After completing the assignment, use these discussion points to connect to broader software engineering concepts:

### Development Environment Importance
Discuss how a properly configured development environment impacts productivity and code quality.

### The Role of Standardization
Explain why standardized environments and tools are important for team collaboration.

### Continuous Integration Foundations
Show how the verification tests are a simple form of the automated testing they'll encounter in CI/CD pipelines.

### Technical Documentation Literacy
Discuss the importance of being able to follow detailed technical documentation.

---

## Supplementary Resources

Provide these resources to students who want additional help:

### VS Code Resources
- [VS Code Getting Started Guide](https://code.visualstudio.com/docs/introvideos/basics)
- [VS Code Keyboard Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

### GitHub Resources
- [GitHub Quickstart](https://docs.github.com/en/get-started/quickstart)
- [GitHub Codespaces Overview](https://docs.github.com/en/codespaces/overview)
- [Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

### Python Testing Resources
- [Pytest Getting Started](https://docs.pytest.org/en/7.0.x/getting-started.html)
- [Python unittest Framework](https://docs.python.org/3/library/unittest.html)

---

## Differentiated Instruction

For different student experience levels:

### For Complete Beginners
- Provide a detailed walkthrough video
- Consider in-class guided installation sessions
- Pair with more experienced students

### For Experienced Students
- Offer "side quests" to explore advanced VS Code features
- Challenge them to customize their environment with productivity enhancements
- Invite them to help document common issues for future students

---

*This assignment sets up students for success by ensuring they have a functioning development environment while introducing them to the satirical world of AlgoCratic Futures™.*

---

**Happy Teaching!**