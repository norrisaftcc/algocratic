"""
CLASSIFICATION: RED CLEARANCE - MANDATORY ALGORITHM EXERCISE
DOCUMENT: AF-SESSION1-ASSIGN3-R-2025-07

# AlgoFlex™ Adaptation Protocol
## *Dynamic Implementation Under Shifting Specifications*

The Algorithm has determined that your ability to adapt to changing requirements
requires assessment. This exercise will measure your capacity to modify algorithms
in response to evolving specifications while maintaining code stability and
algorithmic efficiency throughout transitional phases.

RESOURCE ALLOCATION TIMELINE: 75 MINUTES

"""

import random
import time
from typing import List, Dict, Any, Tuple, Optional, Union

# Notification: Specification Update v1.0 has been applied to this document.
# Changes include initial requirements establishment.

def sort_data_efficiently(data: List[int]) -> List[int]:
    """
    Sorts the given data according to The Algorithm's adaptive sorting protocol.
    
    The function must:
    1. Sort integers in ascending numerical order
    2. Optimize for both speed and memory efficiency
    3. Handle large datasets with minimal resource consumption
    4. Maintain stability for equal elements
    5. Perform effectively across all input distributions
    
    Args:
        data: List of integers to be sorted
        
    Returns:
        List[int]: Sorted list in ascending order
    
    >>> sort_data_efficiently([5, 3, 8, 1, 2])
    [1, 2, 3, 5, 8]
    >>> sort_data_efficiently([])
    []
    >>> sort_data_efficiently([1])
    [1]
    >>> sort_data_efficiently([5, 5, 3, 3, 1])
    [1, 3, 3, 5, 5]
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v1.1 has been applied to this document.
# Sort direction now depends on data characteristics.

def sort_data_efficiently(data: List[int]) -> List[int]:
    """
    Sorts the given data according to The Algorithm's adaptive sorting protocol.
    
    The function must:
    1. Sort integers in ascending order if the average value is less than 50
    2. Sort integers in descending order if the average value is 50 or greater
    3. Optimize for both speed and memory efficiency
    4. Handle large datasets with minimal resource consumption
    5. Maintain stability for equal elements
    
    Args:
        data: List of integers to be sorted
        
    Returns:
        List[int]: Sorted list in appropriate order based on data average
    
    >>> sort_data_efficiently([5, 3, 8, 1, 2])  # avg = 3.8, ascending
    [1, 2, 3, 5, 8]
    >>> sort_data_efficiently([100, 75, 80, 95])  # avg = 87.5, descending
    [100, 95, 80, 75]
    >>> sort_data_efficiently([50, 25, 75])  # avg = 50, descending
    [75, 50, 25]
    >>> sort_data_efficiently([])
    []
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v1.2 has been applied to this document.
# Custom sorting keys have been introduced.

def sort_data_efficiently(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sorts the given data according to The Algorithm's adaptive sorting protocol.
    
    The function must:
    1. Sort dictionaries by their 'priority' field (ascending)
    2. If 'priority' values are equal, sort by 'value' field (ascending)
    3. If both fields are equal, maintain original order
    4. Optimize for both speed and memory efficiency
    5. Handle large datasets with minimal resource consumption
    
    Args:
        data: List of dictionaries, each with 'priority' and 'value' keys
        
    Returns:
        List[Dict[str, Any]]: Sorted list of dictionaries
    
    >>> sort_data_efficiently([
    ...     {'priority': 3, 'value': 10, 'data': 'A'},
    ...     {'priority': 1, 'value': 20, 'data': 'B'},
    ...     {'priority': 3, 'value': 5, 'data': 'C'}
    ... ])
    [{'priority': 1, 'value': 20, 'data': 'B'}, {'priority': 3, 'value': 5, 'data': 'C'}, {'priority': 3, 'value': 10, 'data': 'A'}]
    >>> sort_data_efficiently([])
    []
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v1.3 has been applied to this document.
# Performance monitoring and backwards compatibility added.

def sort_data_efficiently(data: Union[List[int], List[Dict[str, Any]]]) -> Tuple[Union[List[int], List[Dict[str, Any]]], Dict[str, float]]:
    """
    Sorts the given data according to The Algorithm's adaptive sorting protocol.
    
    The function must:
    1. Support BOTH previous data formats (list of integers or list of dictionaries)
    2. Apply appropriate sorting logic based on data type detected
    3. Track and return performance metrics
    4. Optimize for both speed and memory efficiency
    5. Handle large datasets with minimal resource consumption
    
    For integers:
    - Sort ascending if average < 50, otherwise descending
    
    For dictionaries:
    - Sort by 'priority' field (ascending), then by 'value' field (ascending)
    
    Args:
        data: Either a list of integers or a list of dictionaries
        
    Returns:
        Tuple containing:
        - The sorted data (either list of integers or list of dictionaries)
        - Dictionary with performance metrics ('time_ms', 'comparisons', 'memory_kb')
    
    >>> result, metrics = sort_data_efficiently([5, 3, 8, 1, 2])
    >>> result
    [1, 2, 3, 5, 8]
    >>> 'time_ms' in metrics and 'comparisons' in metrics and 'memory_kb' in metrics
    True
    >>> result, metrics = sort_data_efficiently([
    ...     {'priority': 3, 'value': 10, 'data': 'A'},
    ...     {'priority': 1, 'value': 20, 'data': 'B'}
    ... ])
    >>> result
    [{'priority': 1, 'value': 20, 'data': 'B'}, {'priority': 3, 'value': 10, 'data': 'A'}]
    >>> 'time_ms' in metrics and 'comparisons' in metrics and 'memory_kb' in metrics
    True
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v1.4 has been applied to this document.
# Filtering capabilities have been added.

def sort_data_efficiently(
    data: Union[List[int], List[Dict[str, Any]]],
    filter_condition: Optional[Union[Tuple[int, int], Dict[str, Any]]] = None
) -> Tuple[Union[List[int], List[Dict[str, Any]]], Dict[str, float]]:
    """
    Sorts and filters the given data according to The Algorithm's adaptive processing protocol.
    
    The function must:
    1. Support both previous data formats with appropriate sorting
    2. Apply optional filtering before sorting:
       - For integers: Filter to include only values in range [min, max] if provided
       - For dictionaries: Filter to include only items matching all criteria in the filter dict
    3. Track and return performance metrics
    4. Optimize for both speed and memory efficiency
    5. Handle large datasets with minimal resource consumption
    
    Args:
        data: Either a list of integers or a list of dictionaries
        filter_condition: Optional filter to apply before sorting:
                         - For integers: Tuple of (min_value, max_value)
                         - For dictionaries: Dict of key-value pairs to match
        
    Returns:
        Tuple containing:
        - The sorted and filtered data
        - Dictionary with performance metrics
    
    >>> result, metrics = sort_data_efficiently([5, 3, 8, 1, 2], (2, 6))
    >>> result  # Only values between 2 and 6 inclusive, sorted ascending
    [2, 3, 5]
    >>> result, metrics = sort_data_efficiently([
    ...     {'priority': 3, 'value': 10, 'data': 'A'},
    ...     {'priority': 1, 'value': 20, 'data': 'B'},
    ...     {'priority': 3, 'value': 5, 'data': 'C'}
    ... ], {'priority': 3})
    >>> result  # Only items with priority=3, sorted by priority then value
    [{'priority': 3, 'value': 5, 'data': 'C'}, {'priority': 3, 'value': 10, 'data': 'A'}]
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v1.5 (FINAL) has been applied to this document.
# AlgoFlex™ Protocol fully activated with conflicting operation modes.

def sort_data_efficiently(
    data: Union[List[int], List[Dict[str, Any]]],
    filter_condition: Optional[Union[Tuple[int, int], Dict[str, Any]]] = None,
    operation_mode: str = "standard"
) -> Tuple[Union[List[int], List[Dict[str, Any]]], Dict[str, float]]:
    """
    Processes the given data according to The Algorithm's fully activated AlgoFlex™ Protocol.
    
    The function must:
    1. Support different operation modes that modify behavior:
       - "standard": Default behavior as previously specified
       - "optimized": Prioritize performance over completeness
       - "thorough": Prioritize accuracy and completeness over performance
       - "balanced": Equal emphasis on all metrics
       - "random": Introduce controlled randomness for algorithmic diversity
    2. Adjust sorting, filtering, and metric collection based on operation mode
    3. Maintain backward compatibility with all previous versions
    4. Optimize for characteristics prioritized by each mode
    5. Return both processed data and comprehensive metrics
    
    Args:
        data: Either a list of integers or a list of dictionaries
        filter_condition: Optional filter to apply before sorting
        operation_mode: The processing strategy to employ
        
    Returns:
        Tuple containing:
        - The processed data according to specified mode
        - Dictionary with performance and quality metrics
    
    IMPLEMENTATION REQUIREMENTS:
    - The function must handle all five operation modes
    - "optimized" mode may use approximation algorithms for better performance
    - "thorough" mode must validate and sanitize all input data
    - "balanced" mode must achieve above-average scores on all metrics
    - "random" mode must produce different but still valid results on each run
    - All modes must be able to process both data types with appropriate logic
    
    >>> result, metrics = sort_data_efficiently([5, 3, 8, 1, 2], None, "standard")
    >>> result == [1, 2, 3, 5, 8]
    True
    >>> result, metrics = sort_data_efficiently([5, 3, 8, 1, 2], None, "thorough")
    >>> result == [1, 2, 3, 5, 8] and metrics['validation_checks'] > 0
    True
    >>> result1, _ = sort_data_efficiently([5, 3, 8, 1, 2], None, "random")
    >>> result2, _ = sort_data_efficiently([5, 3, 8, 1, 2], None, "random")
    >>> set(result1) == set(result2) and result1 != result2  # Same elements but different order
    True
    """
    # YOUR CODE HERE
    pass


def find_optimal_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Finds the optimal path through a grid according to The Algorithm's 
    pathfinding efficiency protocol.
    
    The function must:
    1. Find a path from top-left (0,0) to bottom-right (n-1,m-1)
    2. Minimize the sum of values in cells along the path
    3. Only allow movement right or down
    4. Handle grids of varying sizes efficiently
    5. Return the coordinates of cells in the optimal path
    
    Args:
        grid: A 2D grid of integers representing costs
        
    Returns:
        List[Tuple[int, int]]: Coordinates of cells in the optimal path
    
    >>> find_optimal_path([
    ...     [1, 3, 1],
    ...     [1, 5, 1],
    ...     [4, 2, 1]
    ... ])
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    >>> find_optimal_path([[1]])
    [(0, 0)]
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v2.1 has been applied to this document.
# Diagonal movement now supported.

def find_optimal_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Finds the optimal path through a grid according to The Algorithm's 
    pathfinding efficiency protocol.
    
    The function must:
    1. Find a path from top-left (0,0) to bottom-right (n-1,m-1)
    2. Minimize the sum of values in cells along the path
    3. Allow movement right, down, or diagonal
    4. Handle grids of varying sizes efficiently
    5. Return the coordinates of cells in the optimal path
    
    Args:
        grid: A 2D grid of integers representing costs
        
    Returns:
        List[Tuple[int, int]]: Coordinates of cells in the optimal path
    
    >>> find_optimal_path([
    ...     [1, 3, 1],
    ...     [1, 5, 1],
    ...     [4, 2, 1]
    ... ])
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    >>> find_optimal_path([[1]])
    [(0, 0)]
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v2.2 has been applied to this document.
# Obstacle avoidance added.

def find_optimal_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Finds the optimal path through a grid according to The Algorithm's 
    pathfinding efficiency protocol.
    
    The function must:
    1. Find a path from top-left (0,0) to bottom-right (n-1,m-1)
    2. Minimize the sum of values in cells along the path
    3. Allow movement right, down, or diagonal
    4. Treat cells with value -1 as impassable obstacles
    5. Return the coordinates of cells in the optimal path
    6. Return empty list if no path exists
    
    Args:
        grid: A 2D grid of integers representing costs (-1 for obstacles)
        
    Returns:
        List[Tuple[int, int]]: Coordinates of cells in the optimal path
    
    >>> find_optimal_path([
    ...     [1, 3, 1],
    ...     [1, -1, 1],
    ...     [4, 2, 1]
    ... ])
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    >>> find_optimal_path([
    ...     [1, -1, 1],
    ...     [-1, -1, 1],
    ...     [1, 1, 1]
    ... ])
    []
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v2.3 has been applied to this document.
# Multiple path criteria introduced.

def find_optimal_path(
    grid: List[List[int]], 
    criteria: str = "cost"
) -> List[Tuple[int, int]]:
    """
    Finds the optimal path through a grid according to The Algorithm's 
    pathfinding efficiency protocol.
    
    The function must:
    1. Find a path from top-left (0,0) to bottom-right (n-1,m-1)
    2. Optimize based on the specified criteria:
       - "cost": Minimize sum of values in cells (default)
       - "length": Minimize number of cells in path
       - "balanced": Balance between cost and length
    3. Allow movement right, down, or diagonal
    4. Treat cells with value -1 as impassable obstacles
    5. Return the coordinates of cells in the optimal path
    
    Args:
        grid: A 2D grid of integers representing costs (-1 for obstacles)
        criteria: The optimization criteria to use
        
    Returns:
        List[Tuple[int, int]]: Coordinates of cells in the optimal path
    
    >>> path = find_optimal_path([
    ...     [1, 3, 1],
    ...     [1, -1, 1],
    ...     [4, 2, 1]
    ... ], "cost")
    >>> sum(grid[y][x] for x, y in path)  # Sum should be minimal
    9
    >>> path = find_optimal_path([
    ...     [1, 3, 1],
    ...     [1, -1, 1],
    ...     [4, 2, 1]
    ... ], "length")
    >>> len(path)  # Path should be as short as possible
    5
    """
    # YOUR CODE HERE
    pass

# Notification: Specification Update v2.4 (FINAL) has been applied to this document.
# Multiple start and end points with time constraints.

def find_optimal_path(
    grid: List[List[int]], 
    criteria: str = "cost",
    start_points: List[Tuple[int, int]] = None,
    end_points: List[Tuple[int, int]] = None,
    time_limit_ms: Optional[int] = None
) -> List[List[Tuple[int, int]]]:
    """
    Finds optimal paths through a grid according to The Algorithm's 
    enhanced pathfinding protocol.
    
    The function must:
    1. Find paths from EACH start point to EACH end point
    2. Default to (0,0) as start and (n-1,m-1) as end if not specified
    3. Optimize each path based on the specified criteria
    4. Allow movement right, down, or diagonal
    5. Respect the optional time limit for computation
    6. Return a list of optimal paths for each start-end combination
    
    Args:
        grid: A 2D grid of integers representing costs (-1 for obstacles)
        criteria: The optimization criteria to use
        start_points: List of starting coordinates (default: [(0,0)])
        end_points: List of ending coordinates (default: [(n-1,m-1)])
        time_limit_ms: Optional time limit for computation in milliseconds
        
    Returns:
        List[List[Tuple[int, int]]]: List of optimal paths
    
    IMPLEMENTATION REQUIREMENTS:
    - The function must return as many paths as it can find within the time limit
    - Paths should be returned in order of start_point index, then end_point index
    - For unreachable end points, the corresponding path should be an empty list
    - If time limit is reached, return the best paths found so far
    - All returned paths must be valid (avoiding obstacles)
    
    >>> grid = [
    ...     [1, 3, 1],
    ...     [1, -1, 1],
    ...     [4, 2, 1]
    ... ]
    >>> paths = find_optimal_path(grid, "cost", [(0,0)], [(2,2)])
    >>> len(paths) == 1 and len(paths[0]) > 0
    True
    >>> paths = find_optimal_path(grid, "cost", [(0,0), (2,0)], [(2,2)])
    >>> len(paths) == 2
    True
    >>> paths = find_optimal_path(grid, "cost", [(0,0)], [(2,2), (0,2)])
    >>> len(paths) == 2
    True
    """
    # YOUR CODE HERE
    pass


# BONUS FUNCTION (Optional but recommended for RED→ORANGE clearance consideration)
def adaptive_algorithm_selector(
    problem_type: str,
    data_size: int,
    time_constraint_ms: int
) -> Dict[str, Any]:
    """
    Dynamically selects and configures the optimal algorithm based on
    problem characteristics and constraints.
    
    The function must:
    1. Analyze the problem type and constraints
    2. Select the most appropriate algorithm from available options
    3. Configure algorithm parameters based on data size
    4. Balance speed, memory usage, and result quality
    5. Return the selected algorithm configuration
    
    Args:
        problem_type: Type of problem ("sorting", "pathfinding", "clustering", etc.)
        data_size: Size of the dataset to be processed
        time_constraint_ms: Maximum allowed processing time in milliseconds
        
    Returns:
        Dict[str, Any]: Selected algorithm configuration with parameters
    
    SUPPORTED PROBLEM TYPES:
    - "sorting": Selection of optimal sorting algorithm
    - "pathfinding": Selection of optimal pathfinding algorithm
    - "clustering": Selection of optimal data clustering algorithm
    
    >>> config = adaptive_algorithm_selector("sorting", 100, 1000)
    >>> "algorithm" in config and "parameters" in config
    True
    >>> config = adaptive_algorithm_selector("pathfinding", 10000, 50)
    >>> "algorithm" in config and "parameters" in config
    True
    >>> config = adaptive_algorithm_selector("sorting", 1000000, 100)
    >>> config["algorithm"] != adaptive_algorithm_selector("sorting", 10, 100)["algorithm"]
    True
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("AlgoFlex™ Adaptation Protocol Testing Initiated...")
    
    # Run doctests to verify implementation
    import doctest
    results = doctest.testmod(verbose=True)
    
    if results.failed == 0:
        print("\nALGORITHMIC ADAPTABILITY CONFIRMED, CITIZEN!")
        print("Your implementation has successfully adjusted to specification revisions.")
        print("Your flexibility rating has been noted in your permanent record.")
    else:
        print("\nALGORITHMIC RIGIDITY DETECTED, CITIZEN!")
        print(f"Your implementation failed to adapt to {results.failed} specification changes.")
        print("Mandatory Adaptability Training has been scheduled for you.")
    
    print("\nREMEMBER: Specifications are perfect even when they change. The Algorithm provides.")