# Performance Optimization Assignment Instructor Guide
## *Teaching Software Optimization Through Corporate Crisis*

**CLASSIFICATION: OUT-OF-CHARACTER**  
**DOCUMENT: INSTRUCTOR-PERF-GUIDE-2025-10**

---

## Overview & Educational Goals

This assignment challenges students to optimize a deliberately inefficient "legacy" decision engine while maintaining its existing functionality. The assignment is framed as an "Algorithmic Emergency™" with resource constraints, tight deadlines, and contradictory requirements, simulating the real-world pressure of production performance issues.

By the end of this assignment, students should be able to:
- Identify common performance bottlenecks in Python code
- Apply efficient algorithms and data structures to improve performance
- Use profiling tools to measure and verify optimizations
- Balance competing constraints like memory usage vs. execution speed
- Make and justify performance trade-off decisions
- Maintain backward compatibility while improving internal implementation

This assignment is designed for YELLOW clearance level, targeting students who have mastered basic programming concepts and are ready to focus on performance optimization techniques.

---

## The Pedagogical Method Behind the Crisis Scenario

The assignment is deliberately framed as a high-pressure performance crisis with unreasonable constraints. This approach serves several educational purposes:

1. **Realistic Work Scenario**: Emergency performance optimization under tight constraints is a common scenario in software engineering careers

2. **Learning Under Pressure**: Students develop the ability to prioritize optimizations and make reasonable trade-offs when perfect solutions aren't possible

3. **Systems Thinking**: The assignment forces students to understand the entire system before making targeted optimizations

4. **Practical Application**: Performance optimization is often overlooked in CS education but is a crucial skill in industry

5. **Tangible Results**: Students can see dramatic improvements in execution time and memory usage, providing immediate positive reinforcement

---

## Technical Background: Core Performance Issues

The provided decision engine implementation contains several deliberate inefficiencies that students should identify and address:

### Algorithmic Inefficiencies
1. **O(n²) and O(n³) Algorithms**: Several functions have quadratic or cubic complexity that can be reduced
2. **Redundant Calculations**: Many functions repeatedly calculate the same values
3. **Inefficient Data Structures**: Inappropriate data structures for the required operations
4. **Excessive Object Creation**: Creating new objects when modifications would suffice

### Implementation Inefficiencies
1. **Unnecessary Data Copying**: Frequent copying of data structures
2. **Inefficient String Operations**: Repeated string manipulations
3. **Multiple Passes Over Data**: Processing data multiple times when once would suffice
4. **Artificial Delays**: Some functions include sleep statements to simulate expensive operations

### Memory Management Issues
1. **Memory Leaks**: Accumulating references to objects
2. **Excessive Memory Allocation**: Creating larger arrays than necessary
3. **Inefficient Object Storage**: Storing data in memory-intensive formats

---

## Setup Instructions

1. **Environment Preparation**:
   - Ensure students have Python 3.7+ installed
   - Required libraries: `numpy`, `pandas` (have students install via pip)
   - Profiling tools: `cProfile`, `memory_profiler` (optional but recommended)
   
2. **Assignment Distribution**:
   - Provide the decision engine code file (`decision_engine_to_optimize.py`)
   - Provide the performance optimization assignment document
   - Include a basic benchmark script for students to measure their improvements
   
3. **Supplementary Materials**:
   - Create a cheat sheet on Python performance optimization techniques
   - Provide resources on profiling tools
   - Share examples of common performance patterns and anti-patterns

---

## Classroom Implementation

### Day 1: Introduction (45-60 minutes)

1. Present the satirical "Strategic Resource Allocation Directive™" in character
2. Explain the concept of performance optimization and its importance
3. Demonstrate basic profiling tools to identify bottlenecks
4. Introduce common optimization techniques
5. Show a few simple examples of inefficient vs. optimized code

### Day 2: Guided Optimization (60-90 minutes)

1. Have students run the baseline code and measure performance
2. Guide students through profiling the code to identify bottlenecks
3. Demonstrate optimization of one component (e.g., the data ingestion pipeline)
4. Discuss the contradictory requirements and how to approach them
5. Have students begin optimization of other components

### Days 3-5: Implementation and Review

1. Students work on their optimization implementations
2. Instructors provide guidance on specific optimization techniques
3. Hold code review sessions to discuss approaches
4. Conduct mid-point performance measurements to track progress
5. Discuss trade-offs between different optimization strategies

---

## Real-World Inspiration Discussion

During the assignment, connect the satirical elements to actual workplace situations:

### "73% Reduction in Allocated Computational Resources"
**Satire**: The dramatic resource reduction without corresponding requirement adjustments

**Real-World Parallel**: Budget cuts or infrastructure changes that impact performance requirements, forcing developers to optimize existing systems

### "Zero-Downtime Optimization Mandate"
**Satire**: The requirement to maintain full system operation during optimization

**Real-World Parallel**: Production systems that can't be taken offline, requiring careful, incremental optimization

### "Contradictory Requirements"
**Satire**: Being asked to simultaneously reduce memory usage and execution time without trade-offs

**Real-World Parallel**: Stakeholders with competing priorities (e.g., operations team wants memory efficiency, product team wants response speed)

---

## Optimization Approach Guidance

Here are key optimization strategies students should consider. Share these if students are struggling:

### 1. Vectorization
Replace loops with NumPy's vectorized operations:

```python
# Before (inefficient)
result = []
for data_point in data_points:
    processed = some_calculation(data_point)
    result.append(processed)

# After (vectorized)
data_array = np.array([data_point.features.values() for data_point in data_points])
processed_array = vectorized_calculation(data_array)
result = [DataPoint(...) for values in processed_array]
```

### 2. Memoization
Cache expensive calculation results:

```python
# Before (inefficient)
def expensive_calculation(x):
    time.sleep(0.1)  # Simulate expensive operation
    return x * x

# After (with memoization)
calculation_cache = {}
def expensive_calculation(x):
    if x in calculation_cache:
        return calculation_cache[x]
    time.sleep(0.1)  # Simulate expensive operation
    result = x * x
    calculation_cache[x] = result
    return result
```

### 3. Batch Processing
Process data in batches rather than individually:

```python
# Before (inefficient)
for item in items:
    process_item(item)

# After (batch processing)
batch_process(items)
```

### 4. Data Structure Selection
Choose appropriate data structures:

```python
# Before (inefficient)
# Repeatedly checking if an item exists in a list - O(n)
if item in large_list:
    # Do something

# After (efficient)
# Convert to set for O(1) lookups
item_set = set(large_list)
if item in item_set:
    # Do something
```

### 5. Algorithmic Improvements
Replace inefficient algorithms:

```python
# Before (inefficient) - O(n²)
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates

# After (efficient) - O(n)
def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
```

---

## Common Optimization Opportunities in the Code

Here are specific areas in the decision engine code that students should focus on:

### 1. Data Ingestion Pipeline
- Replace inefficient JSON/CSV processing
- Eliminate redundant validation
- Batch process features

### 2. Feature Extraction Module
- Vectorize feature extraction
- Use NumPy operations effectively
- Eliminate redundant normalizations

### 3. Decision Matrix Calculator
- Replace O(n²) similarity calculations with vectorized operations
- Optimize matrix operations
- Implement sparse matrix techniques for large datasets

### 4. Output Generator
- Batch process outputs
- Simplify confidence calculations
- Reduce string operations

---

## Assessment Strategy

### Formative Assessment

During implementation, evaluate:
- Students' ability to identify performance bottlenecks
- Their strategic approach to optimization
- How they handle contradictory requirements
- Their use of profiling tools to measure improvements

### Summative Assessment

After completion, evaluate:
- Performance improvement (execution time and memory usage)
- Correctness of results compared to original implementation
- Code quality and readability
- Technical explanation of optimization approaches
- Justification of trade-off decisions

### Grading Rubric

| Criterion | Excellent (A) | Satisfactory (B-C) | Needs Improvement (D-F) |
|-----------|---------------|--------------------|-----------------------|
| Performance Improvement | Achieved ≥90% execution time reduction and ≥50% memory reduction | Achieved 50-90% execution time reduction and 30-50% memory reduction | Achieved <50% execution time reduction or <30% memory reduction |
| Correctness | Results match original implementation with 99.7%+ accuracy | Results match with 95-99.7% accuracy | Results deviate significantly from original |
| Optimization Approach | Implemented sophisticated, appropriate optimizations | Implemented basic optimizations correctly | Few effective optimizations or incorrect implementation |
| Code Quality | Clean, well-documented code with clear optimization intent | Readable code with adequate documentation | Difficult to understand or poorly documented |
| Trade-off Justification | Clear explanation of optimization decisions and trade-offs | Basic justification of main optimizations | Poor or missing justification |

---

## Reflection Discussion Questions

After completing the assignment, use these questions to drive discussion:

1. Which optimizations provided the most significant performance improvements?
2. How did you balance the contradictory requirements for memory usage and execution speed?
3. Which tools or techniques were most helpful in identifying performance bottlenecks?
4. What would you do differently if you were to optimize this code again?
5. How does this exercise compare to performance optimization you've done in the past?
6. How did the crisis scenario affect your approach to optimization?

---

## Example Optimization Solutions

Here are some example optimization approaches for key components:

### Data Ingestion Pipeline

```python
def load_from_json(self, json_data: str) -> List[DataPoint]:
    """Optimized JSON loading with vectorized operations."""
    start_time = time.time()
    
    # Parse JSON once
    data = json.loads(json_data)
    
    # Validate and process in batch
    ids = []
    features_list = []
    metadata_list = []
    timestamps = []
    priorities = []
    
    # Extract data in a single pass
    for item in data:
        # Validate required fields
        if "id" not in item or "features" not in item:
            missing = "id" if "id" not in item else "features"
            raise ValueError(f"Missing '{missing}' field in item")
        
        ids.append(item["id"])
        features_list.append(item.get("features", {}))
        
        # Extract metadata in one operation
        metadata = {k: v for k, v in item.items() 
                   if k not in ["id", "features", "timestamp", "priority"]}
        metadata_list.append(metadata)
        
        timestamps.append(item.get("timestamp", time.time()))
        priorities.append(item.get("priority", 1.0))
    
    # Create data points in batch
    result = [
        DataPoint(id=id, features=features, metadata=metadata, 
                timestamp=timestamp, priority=priority, processed=False)
        for id, features, metadata, timestamp, priority 
        in zip(ids, features_list, metadata_list, timestamps, priorities)
    ]
    
    # Batch validation
    self._validate_features_batch(features_list)
    
    # Record metrics
    processing_time["load_from_json"] = time.time() - start_time
    memory_usage["load_from_json"] = sys.getsizeof(json_data)
    execution_count["load_from_json"] = execution_count.get("load_from_json", 0) + 1
    
    return result

def _validate_features_batch(self, features_list: List[Dict[str, float]]) -> None:
    """Validate features in batch."""
    # Collect all feature values for vectorized validation
    all_values = []
    for features in features_list:
        all_values.extend(features.values())
    
    # Check types
    if not all(isinstance(v, (int, float)) for v in all_values):
        raise ValueError("All feature values must be numeric")
    
    # Convert to numpy for fast range checking
    all_values_array = np.array(all_values, dtype=float)
    if np.any((all_values_array < -1000000) | (all_values_array > 1000000)):
        raise ValueError("Feature values must be within range [-1000000, 1000000]")
```

### Feature Extraction Optimization

```python
def extract_features(self, data_points: List[DataPoint]) -> List[FeatureVector]:
    """Extract features with vectorized operations."""
    start_time = time.time()
    
    # Create feature arrays efficiently
    feature_names = set()
    for data_point in data_points:
        feature_names.update(data_point.features.keys())
    
    feature_names = sorted(feature_names)
    name_to_index = {name: i for i, name in enumerate(feature_names)}
    
    # Pre-allocate arrays
    num_points = len(data_points)
    vectors = np.zeros((num_points, self.dimensions))
    weights = np.zeros(num_points)
    categories = []
    
    # Fill arrays efficiently
    for i, data_point in enumerate(data_points):
        # Transfer features to vector
        for name, value in data_point.features.items():
            idx = name_to_index.get(name, -1)
            if idx >= 0 and idx < self.dimensions:
                vectors[i, idx] = value
        
        # Determine category and weight once
        categories.append(self._determine_category(data_point))
        weights[i] = self._calculate_weight(data_point)
    
    # Normalize all vectors at once
    vectors = self._normalize_vectors_batch(vectors)
    
    # Create feature vectors from arrays
    result = [
        FeatureVector(
            id=data_points[i].id,
            vector=vectors[i],
            weight=weights[i],
            category=categories[i],
            normalized=True
        )
        for i in range(num_points)
    ]
    
    # Record metrics
    processing_time["extract_features"] = time.time() - start_time
    memory_usage["extract_features"] = vectors.nbytes + weights.nbytes
    execution_count["extract_features"] = execution_count.get("extract_features", 0) + 1
    
    return result

def _normalize_vectors_batch(self, vectors: np.ndarray) -> np.ndarray:
    """Normalize all vectors in a single operation."""
    # Calculate mean and std for each vector
    means = np.mean(vectors, axis=1, keepdims=True)
    stds = np.std(vectors, axis=1, keepdims=True)
    
    # Replace zero standard deviations with 1.0
    stds[stds == 0] = 1.0
    
    # Normalize all vectors at once
    normalized_vectors = (vectors - means) / stds
    
    return normalized_vectors
```

### Decision Matrix Optimization

```python
def calculate_decision_matrix(self, feature_vectors: List[FeatureVector]) -> np.ndarray:
    """Calculate the decision matrix with vectorized operations."""
    start_time = time.time()
    
    n = len(feature_vectors)
    
    # Extract vectors and weights into arrays
    vectors = np.array([fv.vector for fv in feature_vectors])
    weights = np.array([fv.weight for fv in feature_vectors])
    
    # Calculate all pairwise similarities at once
    # Using broadcasting for efficient computation
    
    # Compute dot products for all pairs: (n,d) @ (d,n) -> (n,n)
    dot_products = np.dot(vectors, vectors.T)
    
    # Compute norms for all vectors at once
    norms = np.sqrt(np.sum(vectors**2, axis=1))
    
    # Compute all cosine similarities at once: (n,n) / (n,1) @ (1,n) -> (n,n)
    outer_norms = np.outer(norms, norms)
    cosine_similarities = np.divide(
        dot_products, 
        outer_norms, 
        out=np.zeros_like(dot_products), 
        where=outer_norms != 0
    )
    
    # Compute Euclidean distances efficiently
    # Using broadcasting: (n,1,d) - (1,n,d) -> (n,n,d)
    # Then: sum((n,n,d), axis=2) -> (n,n)
    squared_diffs = np.sum((vectors[:, np.newaxis, :] - vectors[np.newaxis, :, :]) ** 2, axis=2)
    distances = np.sqrt(squared_diffs)
    
    # Avoid division by zero
    distance_factors = 1.0 / (1.0 + distances)
    
    # Compute weight factors using broadcasting
    weight_factors = weights / (weights[:, np.newaxis] + weights[np.newaxis, :])
    weight_factors_transposed = 1.0 - weight_factors
    
    # Combine metrics
    matrix = (
        weight_factors * distance_factors + 
        weight_factors_transposed * (0.5 + 0.5 * cosine_similarities)
    ) / 2.0
    
    # Normalize rows
    row_sums = matrix.sum(axis=1, keepdims=True)
    matrix = np.divide(matrix, row_sums, out=np.zeros_like(matrix), where=row_sums != 0)
    
    # Record metrics
    processing_time["calculate_decision_matrix"] = time.time() - start_time
    memory_usage["calculate_decision_matrix"] = matrix.nbytes
    execution_count["calculate_decision_matrix"] = execution_count.get("calculate_decision_matrix", 0) + 1
    
    return matrix
```

---

## Additional Performance Optimization Resources

### For Instructors
- [High Performance Python](https://www.oreilly.com/library/view/high-performance-python/9781492055013/) by Micha Gorelick and Ian Ozsvald
- [Python Performance Optimization](https://www.amazon.com/Python-Performance-Optimization-Gabriele-Lanaro/dp/1484239954) by Gabriele Lanaro
- [Profiling and Optimizing Python](https://www.youtube.com/watch?v=8qEnExGLZfY) (PyCon talk)

### For Students (Higher Clearance Resources)
- [Python Tricks: The Book](https://realpython.com/products/python-tricks-book/) - Contains optimization tips
- [Effective Python: 90 Specific Ways to Write Better Python](https://effectivepython.com/)
- [NumPy Performance Optimization Guide](https://numpy.org/doc/stable/reference/arrays.indexing.html)

---

*This assignment gives students hands-on experience with a critical but often overlooked aspect of software development: making existing code run faster and more efficiently without breaking functionality.*

---

**Happy Teaching!**