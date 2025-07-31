# Instructor Guide: Teaching Flowchart Reading with INFRARED Conditional Logic

## Overview

This guide helps instructors integrate flowchart reading skills into the `infrared_conditional_logic.py` assignment. Flowchart literacy is a critical skill for:
- Understanding technical documentation
- Visualizing complex logic before coding
- Communicating algorithmic thinking
- Debugging logical errors

## Teaching Approach

### 1. Pre-Assignment Introduction (15 minutes)
- Show students common flowchart symbols:
  - **Oval/Ellipse**: Start/End terminals
  - **Diamond**: Decision points (Yes/No questions)
  - **Rectangle**: Process/Action steps
  - **Arrows**: Flow direction
  - **Parallelogram**: Input/Output (optional)

### 2. Guided Flowchart Reading (20 minutes)
Using the enhanced assignment file:
1. Display the clearance determination flowchart
2. Trace through 2-3 examples as a class
3. Have students predict outputs before coding
4. Emphasize the systematic nature of decision trees

### 3. Assessment Components

#### Flowchart Comprehension (20% of grade)
- `interpret_clearance_flowchart()`: Tests basic understanding
- `trace_access_flowchart()`: Tests ability to follow paths
- Look for correct path identification and decision sequencing

#### Implementation from Flowchart (40% of grade)
- `determine_clearance_level()`: Direct flowchart to code
- `authorize_resource_access()`: More complex branching
- Assess if code structure mirrors flowchart logic

#### Traditional Implementation (40% of grade)
- Remaining functions test general conditional logic
- No flowcharts provided - tests independent thinking

### 4. Common Student Challenges

**Challenge 1: Nested Conditions**
- Students often flatten nested logic
- Solution: Emphasize indentation matching flowchart depth

**Challenge 2: Missing Edge Cases**
- Flowcharts make all paths explicit
- Solution: Have students trace ALL possible paths

**Challenge 3: Order of Operations**
- Flowchart order matters (check years first!)
- Solution: Number the decision points

### 5. Extension Activities

For advanced students:
1. Create flowchart for `classify_resource_efficiency()`
2. Find optimization opportunities in flowcharts
3. Convert flowcharts to truth tables

For struggling students:
1. Provide partially completed code matching flowchart structure
2. Use physical cards to "walk through" flowchart
3. Pair programming with flowchart visible

## In-Character Integration

Maintain the satirical tone while teaching real skills:

> "The Algorithm's Decision Matrices are sacred visual representations of Its perfect logic. 
> Failure to interpret these diagrams correctly will result in... suboptimal career trajectories.
> Remember, Citizens: The flowchart flows, and we must flow with it."

## Assessment Rubric Addition

Add to existing INFRARED rubric:

| Component | Weight | Criteria |
|-----------|--------|----------|
| Flowchart Interpretation | 20% | Correctly answers comprehension questions, traces paths accurately |
| Visual-to-Code Translation | 20% | Code structure mirrors flowchart, all paths implemented |
| Original Conditional Logic | 60% | Existing rubric criteria apply |

## Resource Preparation

1. **Digital Option**: Use the `infrared_flowchart_generator.py` to create:
   - HTML files students can view in browser
   - Mermaid diagrams for documentation

2. **Print Option**: Create PDF handouts with:
   - Flowchart symbols reference
   - Practice flowcharts
   - Blank flowchart templates

3. **Interactive Option**: 
   - Use online tools like draw.io or Lucidchart
   - Have students create their own flowcharts

## Success Metrics

Students demonstrate flowchart literacy when they can:
1. ✓ Read and trace through provided flowcharts
2. ✓ Implement code that matches flowchart structure
3. ✓ Identify errors in flowcharts
4. ✓ Create simple flowcharts for given logic

## Notes on Satirical Balance

The flowcharts serve dual purposes:
1. **Educational**: Real skill development in visual logic representation
2. **Satirical**: "The Algorithm's Sacred Decision Matrices" adds corporate mystique

This maintains engagement while teaching fundamental CS concepts.

---

**Remember**: Flowchart reading is a gateway skill to UML diagrams, state machines, and other visual programming tools students will encounter in their careers.