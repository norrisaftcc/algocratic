"""
YELLOW CLEARANCE ONLY
STRATEGIC RESOURCE ALLOCATION MODULE™
Decision Engine Optimization Target
Version 4.2.1

NOTICE: This code is Property of AlgoCratic Futures™
Unauthorized optimization is punishable by mandatory happiness enhancement.
"""

import time
import random
import copy
from typing import List, Dict, Any, Tuple

# Global cache that's never properly utilized
RESOURCE_CACHE = {}

class ResourceData:
    """Container for resource data with inefficient deep copying"""
    
    def __init__(self, resource_id: str, priority: int, allocation: float, 
                 dependencies: List[str], metadata: Dict[str, Any]):
        self.resource_id = resource_id
        self.priority = priority
        self.allocation = allocation
        self.dependencies = dependencies
        self.metadata = metadata
        
    def deep_copy(self) -> 'ResourceData':
        """Unnecessarily creates deep copies of all data"""
        # INEFFICIENCY: Using expensive deep copy operation when unnecessary
        return ResourceData(
            self.resource_id,
            self.priority,
            self.allocation,
            copy.deepcopy(self.dependencies),
            copy.deepcopy(self.metadata)
        )

class DecisionEngine:
    """
    Main decision engine for resource allocation during crisis scenarios.
    Contains multiple deliberate inefficiencies for optimization training.
    """
    
    def __init__(self):
        self.resources = []
        self.priority_lookup = {}  # Never properly utilized
        self.allocation_history = []  # Grows unbounded
        self.dependency_matrix = {}  # Processed inefficiently
        
    def add_resource(self, resource: ResourceData) -> None:
        """Add a resource to the decision engine"""
        # INEFFICIENCY: O(n) operation when we could use a dict/set for lookups
        for existing_resource in self.resources:
            if existing_resource.resource_id == resource.resource_id:
                print(f"Resource {resource.resource_id} already exists")
                return
        
        # INEFFICIENCY: Unnecessary deep copy
        self.resources.append(resource.deep_copy())
        
        # INEFFICIENCY: Redundant data storage
        self.priority_lookup[resource.resource_id] = resource.priority
        
    def get_resource_by_id(self, resource_id: str) -> ResourceData:
        """Retrieve a resource by ID - inefficiently"""
        # INEFFICIENCY: O(n) linear search instead of using a dictionary
        for resource in self.resources:
            if resource.resource_id == resource_id:
                # INEFFICIENCY: Unnecessary deep copy on every retrieval
                return resource.deep_copy()
        
        return None
    
    def calculate_dependency_scores(self) -> Dict[str, float]:
        """
        Calculate dependency scores for all resources
        Returns dictionary mapping resource_id to dependency score
        """
        dependency_scores = {}
        
        # INEFFICIENCY: O(n²) algorithm with redundant calculations
        for resource in self.resources:
            # INEFFICIENCY: Recalculates scores for each resource multiple times
            dependency_scores[resource.resource_id] = self._calculate_single_dependency_score(resource)
        
        return dependency_scores
    
    def _calculate_single_dependency_score(self, resource: ResourceData) -> float:
        """Calculate dependency score for a single resource"""
        # INEFFICIENCY: Recursive approach without memoization leads to repeated calculations
        if not resource.dependencies:
            return 1.0
        
        score = 0.0
        
        # INEFFICIENCY: O(n²) nested loop structure
        for dep_id in resource.dependencies:
            dep_resource = self.get_resource_by_id(dep_id)  # O(n) operation
            if dep_resource:
                # INEFFICIENCY: Redundant recalculation of scores
                dep_score = self._calculate_single_dependency_score(dep_resource)
                score += dep_score
        
        # Normalize by number of dependencies
        if resource.dependencies:
            score /= len(resource.dependencies)
        
        # INEFFICIENCY: Generates a random component that prevents caching
        score += random.uniform(-0.01, 0.01)  # Small randomness to simulate real-world variability
        
        return score
    
    def calculate_priority_weights(self) -> Dict[str, float]:
        """Calculate weighted priorities for resources"""
        # First get dependency scores
        dependency_scores = self.calculate_dependency_scores()
        
        # INEFFICIENCY: Creates new dictionaries repeatedly when updating would work
        priority_weights = {}
        
        # INEFFICIENCY: Extra loop that could be combined with the dependency calculation
        for resource in self.resources:
            # INEFFICIENCY: String concatenation in a loop
            resource_key = resource.resource_id + "_priority"
            
            # INEFFICIENCY: Redundant type conversions
            raw_priority = float(resource.priority)
            dependency_factor = dependency_scores.get(resource.resource_id, 0.0)
            
            # INEFFICIENCY: Overly complex calculation that could be simplified
            weight = (raw_priority * 1.5 + dependency_factor * 2.0) / 3.5
            
            # INEFFICIENCY: Unnecessary intermediate collection
            priority_weights[resource.resource_id] = weight
            
            # INEFFICIENCY: Unnecessary string formatting and logging
            formatted_output = "Resource: {}, Priority: {:.2f}, Dependency: {:.2f}, Weight: {:.2f}".format(
                resource.resource_id, raw_priority, dependency_factor, weight
            )
            self.allocation_history.append(formatted_output)
        
        return priority_weights
    
    def optimize_allocations(self) -> List[Tuple[str, float]]:
        """
        Main optimization algorithm for resource allocation
        Returns a list of (resource_id, new_allocation) tuples
        """
        # INEFFICIENCY: Gets recalculated but results aren't reused
        priority_weights = self.calculate_priority_weights()
        
        # INEFFICIENCY: Creating unnecessary intermediate collections
        resource_allocations = []
        total_priority = 0.0
        
        # Sum up total priority to calculate proportions
        # INEFFICIENCY: Multiple passes through the data
        for resource in self.resources:
            # INEFFICIENCY: Unnecessary dictionary lookups
            weight = priority_weights.get(resource.resource_id, 0.0)
            total_priority += weight
        
        # INEFFICIENCY: Always allocating a new list even when updating in place would work
        allocation_changes = []
        
        # INEFFICIENCY: Quadratic time complexity with nested loops
        for resource in self.resources:
            # INEFFICIENCY: Redundant calculations
            weight = priority_weights.get(resource.resource_id, 0.0)
            
            # Skip resources with zero priority
            if total_priority == 0 or weight == 0:
                new_allocation = 0.0
            else:
                # INEFFICIENCY: Overly complex calculation
                proportion = weight / total_priority
                current = resource.allocation
                
                # INEFFICIENCY: Unnecessary intermediate variables and calculations
                adjustment_factor = self._calculate_adjustment_factor(resource)
                raw_allocation = proportion * 100.0 * adjustment_factor
                
                # INEFFICIENCY: Multiple redundant boundary checks
                new_allocation = max(0.0, min(100.0, raw_allocation))
                
                # Artificially slow down the calculation to simulate complex processing
                time.sleep(0.001)
            
            # INEFFICIENCY: Creating new tuples and copying data unnecessarily
            allocation_changes.append((resource.resource_id, new_allocation))
            
            # INEFFICIENCY: Unnecessary string operations and logging
            log_entry = f"Reallocated {resource.resource_id}: {resource.allocation:.2f} -> {new_allocation:.2f}"
            self.allocation_history.append(log_entry)
        
        return allocation_changes
    
    def _calculate_adjustment_factor(self, resource: ResourceData) -> float:
        """Calculate an adjustment factor for allocation based on metadata"""
        # INEFFICIENCY: Unnecessarily complex calculation
        factor = 1.0
        
        # INEFFICIENCY: Iterating through dictionary when direct access would work
        for key, value in resource.metadata.items():
            # INEFFICIENCY: Redundant string comparisons instead of using a lookup table
            if key == "critical":
                if value == True:
                    factor *= 1.25
            elif key == "redundant":
                if value == True:
                    factor *= 0.8
            elif key == "efficiency":
                # INEFFICIENCY: Unnecessary type conversions
                try:
                    efficiency_val = float(value)
                    factor *= (1.0 + efficiency_val / 100.0)
                except (ValueError, TypeError):
                    pass  # Silently ignore conversion errors
        
        # INEFFICIENCY: Redundant boundary checking
        return max(0.5, min(2.0, factor))
    
    def apply_allocations(self, allocation_changes: List[Tuple[str, float]]) -> None:
        """Apply calculated allocation changes to resources"""
        # INEFFICIENCY: O(n²) operation due to nested loops
        for resource_id, new_allocation in allocation_changes:
            # INEFFICIENCY: O(n) search instead of using a dictionary
            for resource in self.resources:
                if resource.resource_id == resource_id:
                    # INEFFICIENCY: Unnecessary validation that's already done in optimize_allocations
                    if 0.0 <= new_allocation <= 100.0:
                        resource.allocation = new_allocation
                    break
    
    def generate_report(self) -> str:
        """Generate a report of the current resource allocations"""
        # INEFFICIENCY: Inefficient string concatenation
        report = "RESOURCE ALLOCATION REPORT\n"
        report += "=" * 30 + "\n"
        
        # INEFFICIENCY: Sorting unnecessarily
        sorted_resources = sorted(self.resources, key=lambda r: r.priority, reverse=True)
        
        # INEFFICIENCY: Inefficient string concatenation in a loop
        for resource in sorted_resources:
            report += f"Resource: {resource.resource_id}\n"
            report += f"  Priority: {resource.priority}\n"
            report += f"  Allocation: {resource.allocation:.2f}%\n"
            
            # INEFFICIENCY: Converting list to string inefficiently
            dependencies_str = ", ".join(resource.dependencies)
            report += f"  Dependencies: {dependencies_str}\n"
            
            # INEFFICIENCY: Unnecessary metadata serialization
            metadata_items = []
            for key, value in resource.metadata.items():
                metadata_items.append(f"{key}: {value}")
            metadata_str = ", ".join(metadata_items)
            
            report += f"  Metadata: {metadata_str}\n"
            report += "-" * 30 + "\n"
        
        return report
    
    def process_crisis_scenario(self) -> str:
        """
        Run a full crisis scenario allocation process
        Returns: Final allocation report
        """
        # INEFFICIENCY: Not reusing calculated results between steps
        # Step 1: Calculate priority weights
        self.calculate_priority_weights()
        
        # Step 2: Calculate optimal allocations
        allocation_changes = self.optimize_allocations()
        
        # Step 3: Apply the allocations
        self.apply_allocations(allocation_changes)
        
        # Step 4: Generate report
        report = self.generate_report()
        
        return report
    
    # ADDED: Egregious Big O violations with bubble sort O(n²) implementation
    def sort_resources_by_priority(self) -> List[ResourceData]:
        """
        INEFFICIENCY: Using bubble sort (O(n²)) when Python's built-in sort is available
        Also creates unnecessary deep copies
        """
        # Make unnecessary copies of resources
        resources_copy = [resource.deep_copy() for resource in self.resources]
        
        # Classic O(n²) bubble sort implementation
        n = len(resources_copy)
        for i in range(n):
            for j in range(0, n - i - 1):
                # INEFFICIENCY: Redundant deep copy during comparison
                if resources_copy[j].priority < resources_copy[j + 1].priority:
                    # INEFFICIENCY: Classic bubble sort swap
                    resources_copy[j], resources_copy[j + 1] = resources_copy[j + 1], resources_copy[j]
        
        return resources_copy
    
    # ADDED: O(n³) algorithm with nested loops and redundant calculations
    def calculate_resource_interactions(self) -> Dict[str, Dict[str, float]]:
        """
        INEFFICIENCY: O(n³) algorithm for calculating all pairwise resource interactions
        This is a completely unnecessary function that does redundant calculations
        """
        interactions = {}
        
        # INEFFICIENCY: Nested O(n²) loops for pairwise comparison
        for resource1 in self.resources:
            interactions[resource1.resource_id] = {}
            
            # INEFFICIENCY: Another O(n) loop creating O(n²) total
            for resource2 in self.resources:
                # Skip self-comparison
                if resource1.resource_id == resource2.resource_id:
                    continue
                
                # INEFFICIENCY: Completely unnecessary deep copies
                r1_copy = resource1.deep_copy()
                r2_copy = resource2.deep_copy()
                
                # INEFFICIENCY: Complex calculation that could be simplified
                interaction_score = 0.0
                
                # INEFFICIENCY: O(n) loop inside our O(n²) loop, making this O(n³)
                for dep_id in r1_copy.dependencies:
                    if dep_id in r2_copy.dependencies:
                        # INEFFICIENCY: Unnecessary recalculation
                        interaction_score += 1.0
                
                # Normalize score
                total_deps = len(r1_copy.dependencies) + len(r2_copy.dependencies)
                if total_deps > 0:
                    # INEFFICIENCY: Overly complex formula
                    interaction_score = (interaction_score * 2.0) / total_deps
                
                # INEFFICIENCY: Redundant dictionary creation
                interactions[resource1.resource_id][resource2.resource_id] = interaction_score
                
                # INEFFICIENCY: Sleep to make it even slower
                time.sleep(0.0005)
        
        return interactions
    
    # ADDED: Exponential time recursive algorithm without memoization
    def calculate_dependency_chain(self, resource_id: str, depth: int = 0, max_depth: int = 5) -> Dict[str, int]:
        """
        INEFFICIENCY: Exponential time complexity due to unbounded recursion without memoization
        This function calculates all possible dependency chains with redundant computations
        """
        # Base case - exceeded max depth
        if depth >= max_depth:
            return {}
        
        # INEFFICIENCY: O(n) search instead of dictionary lookup
        resource = self.get_resource_by_id(resource_id)
        if not resource:
            return {}
        
        # Initialize result
        dependency_chains = {resource_id: depth}
        
        # INEFFICIENCY: Recursive calls without memoization
        for dep_id in resource.dependencies:
            # INEFFICIENCY: Redundant deep copy
            result_copy = dependency_chains.copy()
            
            # INEFFICIENCY: Recursive call that leads to exponential explosion
            sub_chains = self.calculate_dependency_chain(dep_id, depth + 1, max_depth)
            
            # INEFFICIENCY: Dictionary merging
            for key, value in sub_chains.items():
                dependency_chains[key] = value
        
        return dependency_chains
    
    # ADDED: Fibonacci implementation with exponential complexity
    def _fibonacci(self, n: int) -> int:
        """
        INEFFICIENCY: Exponential time complexity O(2ⁿ) for fibonacci calculation
        This is used for some completely unnecessary calculations
        """
        if n <= 1:
            return n
        return self._fibonacci(n-1) + self._fibonacci(n-2)
    
    # ADDED: Function that does an unnecessary amount of string operations
    def generate_detailed_report(self) -> str:
        """
        INEFFICIENCY: Combines several anti-patterns including:
        1. String concatenation in loops
        2. Nested loops with redundant calculations
        3. Unnecessary deep copies
        4. Recursive exponential algorithms
        5. O(n²) sorting
        """
        # INEFFICIENCY: Start with string concatenation in a loop
        report = ""
        report += "=" * 50 + "\n"
        report += "DETAILED RESOURCE ALLOCATION REPORT\n"
        report += "=" * 50 + "\n"
        
        # INEFFICIENCY: Use bubble sort instead of built-in sort
        sorted_resources = self.sort_resources_by_priority()
        
        # INEFFICIENCY: Calculate unnecessary O(n³) data
        interactions = self.calculate_resource_interactions()
        
        # INEFFICIENCY: For each resource, do exponential time operations
        for resource in sorted_resources:
            # INEFFICIENCY: String concatenation
            report += "\n" + "*" * 40 + "\n"
            report += f"Resource: {resource.resource_id}\n"
            report += f"Priority: {resource.priority}\n"
            report += f"Allocation: {resource.allocation:.2f}%\n"
            
            # INEFFICIENCY: Unnecessary fibonacci calculation
            fib_priority = self._fibonacci(min(resource.priority, 10))
            report += f"Fibonacci Priority Factor: {fib_priority}\n"
            
            # INEFFICIENCY: Exponential dependency chain calculation
            dependency_chains = self.calculate_dependency_chain(resource.resource_id)
            
            # INEFFICIENCY: String formatting in a loop
            report += "Dependency Chains:\n"
            for dep_id, depth in dependency_chains.items():
                if dep_id != resource.resource_id:
                    report += f"  - {dep_id} (depth: {depth})\n"
            
            # INEFFICIENCY: Nested loop for interaction reporting
            report += "Key Interactions:\n"
            if resource.resource_id in interactions:
                # Sort interactions for deterministic output
                interaction_items = list(interactions[resource.resource_id].items())
                # INEFFICIENCY: Manual sorting instead of using sorted()
                for i in range(len(interaction_items)):
                    for j in range(i + 1, len(interaction_items)):
                        if interaction_items[i][1] < interaction_items[j][1]:
                            interaction_items[i], interaction_items[j] = interaction_items[j], interaction_items[i]
                
                # INEFFICIENCY: String concatenation in a loop
                for other_id, score in interaction_items[:3]:  # Top 3 interactions
                    report += f"  - {other_id}: {score:.2f}\n"
            
            report += "*" * 40 + "\n"
        
        return report


def create_sample_resources(count: int = 10) -> List[ResourceData]:
    """Create a sample dataset of resources for testing"""
    resources = []
    
    # Resource types for generating test data
    resource_types = ["compute", "memory", "storage", "network", "personnel"]
    
    for i in range(count):
        # Create resource with progressively more dependencies to create a complex graph
        resource_id = f"{random.choice(resource_types)}_{i}"
        priority = random.randint(1, 10)
        allocation = random.uniform(10.0, 100.0)
        
        # Create dependencies (avoiding circular dependencies by only depending on lower-indexed resources)
        dependencies = []
        if i > 0:  # Skip dependencies for first resource to avoid circular references
            num_dependencies = random.randint(0, min(3, i))  # Up to 3 dependencies
            potential_dependencies = list(range(i))
            random.shuffle(potential_dependencies)
            for j in range(num_dependencies):
                dep_idx = potential_dependencies[j]
                dep_id = f"{random.choice(resource_types)}_{dep_idx}"
                dependencies.append(dep_id)
        
        # Create metadata
        metadata = {
            "critical": random.random() > 0.7,  # 30% chance of being critical
            "redundant": random.random() > 0.6,  # 40% chance of being redundant
            "efficiency": random.uniform(50.0, 150.0)  # Efficiency rating between 50-150%
        }
        
        resource = ResourceData(resource_id, priority, allocation, dependencies, metadata)
        resources.append(resource)
    
    return resources


def benchmark_decision_engine(num_resources: int = 50, iterations: int = 3) -> None:
    """
    Benchmark the decision engine with a specified number of resources
    
    Args:
        num_resources: Number of resources to create
        iterations: Number of iterations to run
    """
    print(f"Benchmarking Decision Engine with {num_resources} resources, {iterations} iterations")
    print("-" * 60)
    
    # Create sample resources
    resources = create_sample_resources(num_resources)
    
    # Initialize engine
    engine = DecisionEngine()
    
    # Add resources to engine
    start_time = time.time()
    for resource in resources:
        engine.add_resource(resource)
    add_time = time.time() - start_time
    print(f"Time to add {num_resources} resources: {add_time:.4f} seconds")
    
    # Run iterations
    total_process_time = 0
    for i in range(iterations):
        start_time = time.time()
        engine.process_crisis_scenario()
        iteration_time = time.time() - start_time
        total_process_time += iteration_time
        print(f"Iteration {i+1}: {iteration_time:.4f} seconds")
    
    # ADDED: Additional benchmark for the detailed report with exponential operations
    print("\nBenchmarking detailed report generation (includes exponential operations):")
    start_time = time.time()
    detailed_report = engine.generate_detailed_report()
    detailed_time = time.time() - start_time
    print(f"Detailed report generation: {detailed_time:.4f} seconds")
    
    avg_time = total_process_time / iterations
    print(f"Average processing time: {avg_time:.4f} seconds")
    print(f"Total benchmark time: {add_time + total_process_time + detailed_time:.4f} seconds")
    print("-" * 60)


if __name__ == "__main__":
    # Run small benchmark by default
    benchmark_decision_engine(num_resources=20, iterations=2)
    
    # Uncomment for larger benchmark
    # benchmark_decision_engine(num_resources=100, iterations=3)