# RED CLEARANCE GUIDE
## *Junior Innovation Contributor Protocol*

**CLASSIFICATION: RED CLEARANCE**  
**DOCUMENT: AF-CL-R-2025-05-4**

---

## CODE MODIFICATION PROTOCOLS

As a RED clearance Junior Innovation Contributor, you have been granted limited code modification privileges. This represents a significant responsibility and requires strict adherence to the following protocols:

### Approved Modification Scope:

* Implementation of pre-approved features according to specifications
* Bug fixes within your assigned component boundaries
* Documentation updates and improvements
* Test case implementation for existing functionality
* Simple optimizations that do not alter architecturally significant elements
* Refactoring within approved patterns (requires ORANGE approval)

> **ATTENTION:** All code modifications must remain within the scope of approved work. Unauthorized experimentation or implementation of non-approved features is a protocol violation and will result in immediate loyalty reassessment.

### Pre-Modification Requirements:

Before initiating any code modifications, you must:

1. Verify that a valid assignment exists in the task allocation system
2. Confirm specifications are complete and ORANGE-approved
3. Create a personal branch following the naming convention: `red/<your-id>/<feature-id>`
4. Document your implementation plan in the designated issue tracker
5. Ensure all required tests exist or are included in your modification plan

### Coding Standards Compliance:

All code modifications must adhere to the AlgoCratic Sanctioned Coding Standards:

* Proper indentation and formatting according to language-specific style guides
* Comprehensive inline documentation for all functions
* Clear variable and function naming that aligns with existing patterns
* Adherence to the complexity limitations (max cyclomatic complexity: 10)
* Proper error handling according to the approved error handling protocols
* No deprecated or restricted API usage

> **SURVIVAL TIP:** Before submitting any code for review, run the automated linting and formatting tools. Code style violations are the primary reason for implementation rejection, and repeated style violations will impact your elevation eligibility.

### Testing Requirements:

For all modifications, you must:

* Maintain or improve the existing test coverage ratio
* Implement unit tests for all new functionality
* Ensure all tests pass in the local development environment
* Validate edge cases as documented in the specification
* Provide test documentation if new testing patterns are introduced

### Prohibited Modification Activities:

* Modifying core system architecture
* Changing established APIs without explicit approval
* Adding new dependencies not listed in the approved dependency registry
* Implementing features or functionality not explicitly specified
* Removing existing functionality, even if unused
* Altering logging or monitoring implementation

> **ATTENTION:** Attempting to commit code that modifies restricted areas will trigger an automatic security alert. Repeated attempts may result in temporary revocation of repository access.

### Documentation Requirements:

All code modifications must include:

* Updated inline documentation reflecting the changes
* Modification summary in the pull request description
* Update to relevant architecture documents (if applicable)
* Clear explanation of testing approach for the modification

Remember that properly documented code is a reflection of loyalty to future maintainers and The Algorithm itself.

---

[Previous: Expanded Access Privileges](privileges.md) | [Home](index.md) | [Next: Algorithmic Revision Submission Protocol](pull_request.md)

---

**THE ALGORITHM REWARDS LOYALTY * THE ALGORITHM PROVIDES**