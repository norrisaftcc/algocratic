# AlgoFlex™ Assignment Instructor Guide
## *Teaching Algorithm Adaptation Through Shifting Specifications*

**CLASSIFICATION: OUT-OF-CHARACTER**  
**DOCUMENT: INSTRUCTOR-ALG-GUIDE-2025-07**

---

## Overview & Educational Goals

This assignment teaches students how to handle changing requirements through a deliberately shifting set of specifications for algorithm implementation. By structuring the assignment as a series of "specification updates," we simulate the real-world experience of evolving requirements during development.

The primary educational goals are to help students:

1. Build resilience to changing requirements and specifications
2. Learn how to refactor code to accommodate new features
3. Practice maintaining backward compatibility
4. Develop strategies for balancing conflicting constraints
5. Understand the importance of flexible, adaptable code architecture

By the end of this assignment, students should be able to:
- Implement algorithms that can adapt to changing requirements
- Design flexible code structures that minimize refactoring pain
- Balance competing concerns like performance, accuracy, and readability
- Recognize and resolve conflicting specifications
- Communicate effectively about trade-offs in their implementation

---

## The Pedagogical Method Behind the Shifting Specifications

The "specification updates" in this assignment are carefully designed to teach important software engineering principles:

### 1. Backward Compatibility (v1.3)
When we shift from sorting integers to dictionaries, then require handling both, students learn the importance of maintaining backward compatibility with existing clients.

### 2. Feature Expansion (v1.4, v2.2)
Adding filtering capabilities and obstacle avoidance teaches students how to expand functionality while preserving existing behavior.

### 3. Operation Modes (v1.5)
The introduction of conflicting operation modes mirrors real systems that need different optimization priorities for different use cases.

### 4. Interface Evolution (v2.3, v2.4)
The pathfinding function's evolution from simple to complex parameters shows how interfaces grow over time in production systems.

### 5. Real-World Connection
Each specification shift deliberately mirrors common requirement changes in industry:
- Changes in sorting direction based on data (business rules changing)
- Adding performance metrics (monitoring requirements)
- Supporting multiple starting points (expanding use cases)
- Time constraints (operational requirements)

---

## Setup Instructions

1. **Development Environment**:
   - Ensure students have Python 3.7+ installed
   - Verify doctest functionality is working
   - Consider providing a virtual environment with typing support
   
2. **Assignment Distribution**:
   - Provide only the INITIAL version of each function to students
   - DO NOT give them all specification updates at once
   - Schedule releases of specification updates as described below
   
3. **Supplementary Materials**:
   - Create a reference guide on algorithm design patterns
   - Provide sample implementations of flexible, adaptable code
   - Share examples of industry requirement changes and how they were handled

---

## Classroom Implementation

### Initial Setup (Day 1)

1. Introduce the assignment as a "stable" specification
2. Have students implement the initial versions of both functions:
   - `sort_data_efficiently` v1.0
   - `find_optimal_path` v1.0
3. Verify their implementations pass the initial tests
4. Warn students that there might be "shifting priorities" ahead

### First Update (Day 2)

1. Present the first "Specification Update" for each function:
   - `sort_data_efficiently` v1.1 (changing sort direction based on data)
   - `find_optimal_path` v2.1 (adding diagonal movement)
2. Explain that this is a simulation of real-world requirement changes
3. Give students time to adapt their code
4. Discuss strategies for designing more flexible code

### Subsequent Updates (Days 3-5)

1. Release one specification update per day
2. Ask students to track how much code they need to change each time
3. Discuss strategies for minimizing the impact of changes
4. Have students reflect on how they could have designed their initial code differently

### Final Updates and Reflection (Day 6)

1. Release the final specifications:
   - `sort_data_efficiently` v1.5
   - `find_optimal_path` v2.4
2. Give students time to implement these most complex requirements
3. Hold a reflection session on the experience
4. Connect to real-world software evolution

---

## Real-World Inspiration Discussion

During implementation, connect the shifting specifications to actual workplace situations:

### Sorting Function Changes
**Satire**: Changing from "sort ascending" to "sort based on data average" then to "sort dictionaries" then to "handle both data types"

**Real-World Parallel**: A user-facing feature that starts simple (v1), then gains business rules (v1.1), then needs to work with a new data model (v1.2), then must maintain backward compatibility for existing clients (v1.3)

### Pathfinding Function Changes
**Satire**: Adding diagonal movement, then obstacles, then multiple criteria, then multiple start/end points

**Real-World Parallel**: A navigation algorithm that starts with basic capabilities, then adds features requested by different teams, then needs to balance competing priorities (speed vs. accuracy), then gets deployed in more complex scenarios

### Time Constraints Addition
**Satire**: Adding a time_limit_ms parameter that constrains computation

**Real-World Parallel**: Systems moving from batch processing to real-time requirements, where "correct but slow" solutions become unacceptable

---

## Specification Release Schedule

For maximum impact, release the specifications according to this schedule:

### Day 1: Initial Assignment
- `sort_data_efficiently` v1.0
- `find_optimal_path` v1.0

### Day 2: First Update
- `sort_data_efficiently` v1.1 (sort direction depends on data)
- `find_optimal_path` v2.1 (diagonal movement)

### Day 3: Second Update
- `sort_data_efficiently` v1.2 (dictionary sorting)
- `find_optimal_path` v2.2 (obstacle avoidance)

### Day 4: Third Update
- `sort_data_efficiently` v1.3 (backward compatibility)
- `find_optimal_path` v2.3 (multiple criteria)

### Day 5: Final Update
- `sort_data_efficiently` v1.4, v1.5 (filtering and operation modes)
- `find_optimal_path` v2.4 (multiple start/end points)

---

## Assessment Strategy

### Formative Assessment

During implementation of each update, evaluate:
- How students adapt their code architecture
- The strategies they use to maintain backward compatibility
- Their ability to balance conflicting requirements
- The clarity of their implementation approach

### Summative Assessment

After the final specifications are implemented, evaluate:
- Code quality and organization
- Handling of all requirement changes
- Performance of the solution under various conditions
- Clarity of implementation comments and documentation

### Grading Rubric

| Criterion | Excellent (A) | Satisfactory (B-C) | Needs Improvement (D-F) |
|-----------|---------------|--------------------|-----------------------|
| Adaptability | Code elegantly handles each specification change with minimal refactoring | Code accommodates all changes but requires significant rewrites | Code fails to adapt to multiple specification changes |
| Correctness | All versions pass their respective tests | Most versions pass most tests | Multiple versions fail tests |
| Code Organization | Architecture anticipates changes and isolates them effectively | Reasonable structure that allows for changes | Brittle design that breaks with each change |
| Performance | Efficient implementation across all operation modes | Acceptable performance with some inefficiencies | Poor performance or fails to meet time constraints |
| Documentation | Excellent documentation of design decisions and strategies | Basic documentation of implementation | Minimal or no documentation |

---

## Reflection Discussion Questions

After completing the assignment, use these questions to drive discussion:

1. How did you feel when each new specification was released?
2. Which specification change required the most significant code refactoring?
3. How would you design your solution differently if you could start over?
4. What strategies helped you minimize the impact of specification changes?
5. How does this experience compare to real-world software development?
6. What did you learn about designing flexible, adaptable code?

---

## Implementation Strategies to Discuss

After the assignment, highlight these key strategies that help handle changing requirements:

### 1. The Strategy Pattern
Demonstrate how defining algorithm behaviors as interchangeable components would have simplified adapting to operation modes and criteria changes.

### 2. The Adapter Pattern
Show how adapters could have eased the transition from integers to dictionaries and maintained backward compatibility.

### 3. The Factory Method Pattern
Explain how a factory could have helped isolate creation logic as data types and modes evolved.

### 4. Parameter Objects
Discuss how consolidating related parameters into objects can make interfaces more stable as requirements expand.

### 5. Progressive Enhancement
Highlight the value of implementing core functionality first, then adding optional enhancements.

---

## Connection to Higher Clearance Levels

This assignment builds foundational skills that will be expanded at higher clearance levels:

1. **ORANGE**: Students will design algorithms with built-in flexibility from the start
2. **YELLOW**: Students will architect systems that anticipate requirement changes
3. **GREEN**: Students will create frameworks that allow for runtime adaptation

Each progression reduces the reactive nature of adaptation and increases proactive design for change.

---

## Tips for Instructors

1. **Embody the corporate character** when announcing specification updates
2. **Be flexible with deadlines** since this is a challenging assignment
3. **Encourage struggling students** by reminding them that adaptation is difficult for everyone
4. **Highlight good practices** when you see students designing for change
5. **Connect to industry experience** by sharing your own stories of requirement shifts
6. **Create a supportive environment** for the frustration that will naturally occur

---

## Debriefing the Real Lesson

At the end of this assignment, conduct a thorough debriefing that reveals the true educational purpose:

1. Explain that the deliberately shifting specifications mirror real-world software evolution
2. Share examples from industry where requirements changed dramatically during development
3. Discuss the cost of change in poorly designed systems versus flexible ones
4. Highlight that this experience, while frustrating, is excellent preparation for industry
5. Connect the specific specification changes to common real-world scenarios
6. Acknowledge that handling changing requirements is one of the most valuable skills in software engineering

---

## Additional Resources

### For Instructors
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
- [Working Effectively with Legacy Code](https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052)
- [Refactoring: Improving the Design of Existing Code](https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599)

### For Students (Higher Clearance Resources)
- [Clean Architecture](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
- [Adaptive Code: Agile coding with design patterns and SOLID principles](https://www.amazon.com/Adaptive-Code-principles-Developer-Practices/dp/1509302581)
- [A Philosophy of Software Design](https://www.amazon.com/Philosophy-Software-Design-John-Ousterhout/dp/1732102201)

---

*This assignment is arguably the most valuable in the entire curriculum for preparing students for real-world software development conditions.*

---

**Happy Teaching!**