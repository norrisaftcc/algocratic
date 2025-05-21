"""
CLASSIFICATION: RED CLEARANCE - DISTRIBUTED SYSTEMS RESILIENCE EXERCISE
DOCUMENT: AF-SESSION3-ASSIGN3-R-2025-10

# AlgoHealth™ Distributed Service Resilience Protocol
## *Implementation of Fault Tolerance and Recovery Systems*

The Algorithm has determined that you possess sufficient competence to
contribute to our mission-critical distributed infrastructure. This
assignment will evaluate your ability to implement resiliency measures
for distributed systems while handling unexpected service disruptions
with minimal user impact.

RESOURCE ALLOCATION TIMELINE: 180 MINUTES

STABILITY NOTICE: Failure to implement proper resilience measures will
result in simulated service outages that reflect poorly on your
efficiency metrics.
"""

import json
import logging
import random
import time
import uuid
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
from threading import Lock, Thread
from queue import Queue, Empty


class ServiceStatus(Enum):
    """
    Status values for service health monitoring.
    
    These values represent the current operational status of a service:
    - OPERATIONAL: Service is functioning normally
    - DEGRADED: Service is experiencing performance issues but still functional
    - PARTIAL_OUTAGE: Service has significant impairment but partial functionality
    - COMPLETE_OUTAGE: Service is completely non-functional
    - MAINTENANCE: Service is intentionally offline for maintenance
    """
    OPERATIONAL = "operational"
    DEGRADED = "degraded"
    PARTIAL_OUTAGE = "partial_outage"
    COMPLETE_OUTAGE = "complete_outage"
    MAINTENANCE = "maintenance"


@dataclass
class ServiceConfig:
    """
    Configuration parameters for resilience implementation.
    
    Fields:
        retry_count: Maximum number of retry attempts
        retry_delay_ms: Delay between retry attempts in milliseconds
        timeout_ms: Request timeout in milliseconds
        circuit_breaker_threshold: Failure threshold to open circuit breaker
        circuit_breaker_reset_seconds: Time before testing circuit breaker state
        health_check_interval_seconds: Interval between health checks
        fallback_enabled: Whether fallback mechanisms are enabled
    """
    retry_count: int = 3
    retry_delay_ms: int = 500
    timeout_ms: int = 2000
    circuit_breaker_threshold: int = 5
    circuit_breaker_reset_seconds: int = 30
    health_check_interval_seconds: int = 15
    fallback_enabled: bool = True


class HealthCheckResult:
    """
    Result of a service health check.
    
    Contains detailed information about the current health status of a service,
    including performance metrics and availability indicators.
    """
    
    def __init__(self, service_id: str, status: ServiceStatus, 
                response_time_ms: int, error_rate: float,
                last_error: Optional[str] = None):
        """
        Initialize a health check result.
        
        Args:
            service_id: Identifier for the service
            status: Current service status
            response_time_ms: Current response time in milliseconds
            error_rate: Current error rate (0.0 to 1.0)
            last_error: Description of the last error encountered, if any
        """
        self.service_id = service_id
        self.status = status
        self.response_time_ms = response_time_ms
        self.error_rate = error_rate
        self.last_error = last_error
        self.timestamp = int(time.time())
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the health check result to a dictionary.
        
        Returns:
            Dict representation of the health check result
        """
        return {
            "service_id": self.service_id,
            "status": self.status.value,
            "response_time_ms": self.response_time_ms,
            "error_rate": self.error_rate,
            "last_error": self.last_error,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HealthCheckResult':
        """
        Create a health check result from a dictionary.
        
        Args:
            data: Dictionary representation of health check data
            
        Returns:
            HealthCheckResult instance
        """
        return cls(
            service_id=data["service_id"],
            status=ServiceStatus(data["status"]),
            response_time_ms=data["response_time_ms"],
            error_rate=data["error_rate"],
            last_error=data.get("last_error")
        )


class ResilienceException(Exception):
    """Base exception for resilience-related errors."""
    pass


class ServiceUnavailableException(ResilienceException):
    """Exception raised when a service is unavailable."""
    pass


class CircuitBreakerOpenException(ResilienceException):
    """Exception raised when a request is prevented by an open circuit breaker."""
    pass


class RetryExhaustedException(ResilienceException):
    """Exception raised when retry attempts are exhausted."""
    pass


class TimeoutException(ResilienceException):
    """Exception raised when a request times out."""
    pass


class CircuitBreaker:
    """
    Implements the Circuit Breaker pattern for failure protection.
    
    The circuit breaker prevents repeated calls to failing services by
    "opening the circuit" after a threshold of failures is reached.
    """
    
    def __init__(self, service_id: str, config: ServiceConfig):
        """
        Initialize a circuit breaker.
        
        Args:
            service_id: Identifier for the protected service
            config: Configuration parameters
        """
        self.service_id = service_id
        self.config = config
        self.failure_count = 0
        self.status = "closed"  # closed, open, half-open
        self.last_failure_time = 0
        self.lock = Lock()
    
    def record_success(self) -> None:
        """Record a successful service call, resetting the circuit breaker."""
        # YOUR CODE HERE
        pass
    
    def record_failure(self) -> None:
        """
        Record a failed service call, potentially opening the circuit.
        
        If the failure threshold is reached, the circuit will open.
        """
        # YOUR CODE HERE
        pass
    
    def allow_request(self) -> bool:
        """
        Check if a request should be allowed through the circuit breaker.
        
        Returns:
            True if the request is allowed, False otherwise
        
        Raises:
            CircuitBreakerOpenException: If the circuit is open
        """
        # YOUR CODE HERE
        pass
    
    def reset(self) -> None:
        """Reset the circuit breaker to its initial state."""
        # YOUR CODE HERE
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of the circuit breaker.
        
        Returns:
            Dict with circuit breaker state information
        """
        # YOUR CODE HERE
        pass


class RetryPolicy:
    """
    Implements retry logic for transient failures.
    
    This class provides configurable retry behavior including backoff
    strategies to handle temporary service disruptions.
    """
    
    def __init__(self, config: ServiceConfig):
        """
        Initialize a retry policy.
        
        Args:
            config: Configuration parameters
        """
        self.config = config
    
    def execute_with_retry(self, operation: Callable, *args, **kwargs) -> Any:
        """
        Execute an operation with retry logic.
        
        Args:
            operation: The function to execute
            *args: Positional arguments for the operation
            **kwargs: Keyword arguments for the operation
            
        Returns:
            The result of the operation
            
        Raises:
            RetryExhaustedException: If all retry attempts fail
        """
        # YOUR CODE HERE
        pass
    
    def calculate_backoff_time(self, attempt: int) -> int:
        """
        Calculate the backoff time for a retry attempt.
        
        Args:
            attempt: The current retry attempt number (0-based)
            
        Returns:
            Backoff time in milliseconds
        """
        # YOUR CODE HERE
        pass


class Timeout:
    """
    Implements timeout handling for service calls.
    
    This class provides mechanisms to enforce timeout constraints on
    operations to prevent indefinite waiting.
    """
    
    def __init__(self, config: ServiceConfig):
        """
        Initialize a timeout handler.
        
        Args:
            config: Configuration parameters
        """
        self.config = config
    
    def execute_with_timeout(self, operation: Callable, *args, **kwargs) -> Any:
        """
        Execute an operation with a timeout.
        
        Args:
            operation: The function to execute
            *args: Positional arguments for the operation
            **kwargs: Keyword arguments for the operation
            
        Returns:
            The result of the operation
            
        Raises:
            TimeoutException: If the operation times out
        """
        # YOUR CODE HERE
        pass


class Bulkhead:
    """
    Implements the Bulkhead pattern for resource isolation.
    
    This pattern isolates failures by limiting concurrent calls to a
    service, preventing cascading failures due to resource exhaustion.
    """
    
    def __init__(self, service_id: str, max_concurrent_calls: int):
        """
        Initialize a bulkhead.
        
        Args:
            service_id: Identifier for the protected service
            max_concurrent_calls: Maximum number of concurrent calls allowed
        """
        self.service_id = service_id
        self.max_concurrent_calls = max_concurrent_calls
        self.current_calls = 0
        self.lock = Lock()
    
    def execute_with_bulkhead(self, operation: Callable, *args, **kwargs) -> Any:
        """
        Execute an operation with bulkhead protection.
        
        Args:
            operation: The function to execute
            *args: Positional arguments for the operation
            **kwargs: Keyword arguments for the operation
            
        Returns:
            The result of the operation
            
        Raises:
            ServiceUnavailableException: If the bulkhead is full
        """
        # YOUR CODE HERE
        pass


class HealthChecker:
    """
    Monitors the health of dependent services.
    
    This class maintains up-to-date information about service health
    by performing periodic health checks and tracking results.
    """
    
    def __init__(self, config: ServiceConfig):
        """
        Initialize a health checker.
        
        Args:
            config: Configuration parameters
        """
        self.config = config
        self.health_data = {}
        self.running = False
        self.check_thread = None
        self.service_check_functions = {}
        self.lock = Lock()
    
    def register_service(self, service_id: str, check_function: Callable[[], HealthCheckResult]) -> None:
        """
        Register a service for health checking.
        
        Args:
            service_id: Identifier for the service
            check_function: Function that performs the health check
        """
        # YOUR CODE HERE
        pass
    
    def start_health_checking(self) -> None:
        """Start the background health checking thread."""
        # YOUR CODE HERE
        pass
    
    def stop_health_checking(self) -> None:
        """Stop the background health checking thread."""
        # YOUR CODE HERE
        pass
    
    def _health_check_worker(self) -> None:
        """Worker function for the health checking thread."""
        # YOUR CODE HERE
        pass
    
    def get_service_health(self, service_id: str) -> Optional[HealthCheckResult]:
        """
        Get the current health status of a service.
        
        Args:
            service_id: Identifier for the service
            
        Returns:
            The health check result, or None if not available
        """
        # YOUR CODE HERE
        pass
    
    def is_service_available(self, service_id: str) -> bool:
        """
        Check if a service is currently available.
        
        Args:
            service_id: Identifier for the service
            
        Returns:
            True if the service is available, False otherwise
        """
        # YOUR CODE HERE
        pass


class FallbackRegistry:
    """
    Manages fallback strategies for service failures.
    
    This registry holds alternative implementations that can be used
    when a primary service is unavailable.
    """
    
    def __init__(self):
        """Initialize a fallback registry."""
        self.fallbacks = {}
        self.lock = Lock()
    
    def register_fallback(self, service_id: str, operation_name: str, 
                         fallback_function: Callable) -> None:
        """
        Register a fallback function for a service operation.
        
        Args:
            service_id: Identifier for the service
            operation_name: Name of the operation
            fallback_function: Function to call as fallback
        """
        # YOUR CODE HERE
        pass
    
    def get_fallback(self, service_id: str, operation_name: str) -> Optional[Callable]:
        """
        Get a fallback function for a service operation.
        
        Args:
            service_id: Identifier for the service
            operation_name: Name of the operation
            
        Returns:
            The fallback function, or None if not available
        """
        # YOUR CODE HERE
        pass


class CacheRegistry:
    """
    Manages cached responses for service operations.
    
    This registry provides a caching layer that can serve responses
    when services are unavailable.
    """
    
    def __init__(self, default_ttl_seconds: int = 300):
        """
        Initialize a cache registry.
        
        Args:
            default_ttl_seconds: Default time-to-live for cache entries in seconds
        """
        self.cache = {}
        self.expiration = {}
        self.default_ttl = default_ttl_seconds
        self.lock = Lock()
    
    def cache_response(self, service_id: str, operation_name: str, request_params: Dict,
                      response: Any, ttl_seconds: Optional[int] = None) -> None:
        """
        Cache a service response.
        
        Args:
            service_id: Identifier for the service
            operation_name: Name of the operation
            request_params: Parameters used in the request
            response: Response to cache
            ttl_seconds: Time-to-live in seconds, or None for default
        """
        # YOUR CODE HERE
        pass
    
    def get_cached_response(self, service_id: str, operation_name: str, 
                          request_params: Dict) -> Optional[Any]:
        """
        Get a cached service response.
        
        Args:
            service_id: Identifier for the service
            operation_name: Name of the operation
            request_params: Parameters used in the request
            
        Returns:
            The cached response, or None if not available
        """
        # YOUR CODE HERE
        pass
    
    def clear_expired_entries(self) -> None:
        """Remove all expired entries from the cache."""
        # YOUR CODE HERE
        pass


class ResilienceCoordinator:
    """
    Coordinates resilience patterns for service calls.
    
    This class combines multiple resilience patterns to provide comprehensive
    protection against service failures.
    """
    
    def __init__(self, config: ServiceConfig = None):
        """
        Initialize a resilience coordinator.
        
        Args:
            config: Configuration parameters
        """
        self.config = config or ServiceConfig()
        self.circuit_breakers = {}
        self.health_checker = HealthChecker(self.config)
        self.fallback_registry = FallbackRegistry()
        self.cache_registry = CacheRegistry()
        self.bulkheads = {}
        self.retry_policy = RetryPolicy(self.config)
        self.timeout = Timeout(self.config)
        self.lock = Lock()
    
    def register_circuit_breaker(self, service_id: str) -> CircuitBreaker:
        """
        Register a circuit breaker for a service.
        
        Args:
            service_id: Identifier for the service
            
        Returns:
            The circuit breaker instance
        """
        # YOUR CODE HERE
        pass
    
    def register_bulkhead(self, service_id: str, max_concurrent_calls: int) -> Bulkhead:
        """
        Register a bulkhead for a service.
        
        Args:
            service_id: Identifier for the service
            max_concurrent_calls: Maximum number of concurrent calls allowed
            
        Returns:
            The bulkhead instance
        """
        # YOUR CODE HERE
        pass
    
    def execute_with_resilience(self, service_id: str, operation_name: str,
                              operation: Callable, *args, **kwargs) -> Any:
        """
        Execute an operation with full resilience protection.
        
        This method applies all configured resilience patterns:
        - Circuit breaker
        - Bulkhead
        - Timeout
        - Retry
        - Fallback
        - Cache
        
        Args:
            service_id: Identifier for the service
            operation_name: Name of the operation
            operation: The function to execute
            *args: Positional arguments for the operation
            **kwargs: Keyword arguments for the operation
            
        Returns:
            The result of the operation
            
        Raises:
            Various exceptions if the operation fails and no fallback is available
        """
        # YOUR CODE HERE
        pass
    
    def start(self) -> None:
        """Start the resilience coordinator and its components."""
        # YOUR CODE HERE
        pass
    
    def stop(self) -> None:
        """Stop the resilience coordinator and its components."""
        # YOUR CODE HERE
        pass
    
    def get_system_health(self) -> Dict[str, Any]:
        """
        Get the current health status of all registered services.
        
        Returns:
            Dict with health information for all services
        """
        # YOUR CODE HERE
        pass


class ServiceSimulator:
    """
    Simulates services with configurable failure modes.
    
    This simulator allows testing resilience patterns against predictable
    failure scenarios.
    """
    
    def __init__(self, service_id: str):
        """
        Initialize a service simulator.
        
        Args:
            service_id: Identifier for the simulated service
        """
        self.service_id = service_id
        self.failure_rate = 0.0
        self.latency_ms = 50
        self.jitter_ms = 20
        self.status = ServiceStatus.OPERATIONAL
        self.failure_modes = {
            "timeout": False,
            "error": False,
            "intermittent": False
        }
    
    def configure(self, failure_rate: float = None, latency_ms: int = None,
                jitter_ms: int = None, status: ServiceStatus = None,
                failure_modes: Dict[str, bool] = None) -> None:
        """
        Configure the simulator behavior.
        
        Args:
            failure_rate: Probability of failure (0.0 to 1.0)
            latency_ms: Base response time in milliseconds
            jitter_ms: Random variation in response time
            status: Service status to simulate
            failure_modes: Dict of failure modes to enable
        """
        if failure_rate is not None:
            self.failure_rate = max(0.0, min(1.0, failure_rate))
        if latency_ms is not None:
            self.latency_ms = max(0, latency_ms)
        if jitter_ms is not None:
            self.jitter_ms = max(0, jitter_ms)
        if status is not None:
            self.status = status
        if failure_modes is not None:
            self.failure_modes.update(failure_modes)
    
    def call(self, operation_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate a service call with configured behavior.
        
        Args:
            operation_name: Name of the operation to simulate
            params: Parameters for the operation
            
        Returns:
            Simulated response
            
        Raises:
            Various exceptions based on configured failure modes
        """
        # Simulate response time
        base_latency = self.latency_ms
        jitter = random.randint(-self.jitter_ms, self.jitter_ms) if self.jitter_ms > 0 else 0
        response_time = max(0, base_latency + jitter)
        
        # Sleep to simulate processing time
        time.sleep(response_time / 1000.0)
        
        # Check if this call should fail
        if random.random() < self.failure_rate:
            # Determine failure mode
            if self.failure_modes["timeout"]:
                # Simulate timeout by sleeping longer then raising exception
                time.sleep((response_time * 2) / 1000.0)
                raise TimeoutException(f"Service {self.service_id} operation {operation_name} timed out")
            elif self.failure_modes["error"]:
                # Simulate an error response
                raise ServiceUnavailableException(
                    f"Service {self.service_id} operation {operation_name} returned error"
                )
            else:
                # Intermittent failure
                raise ServiceUnavailableException(
                    f"Service {self.service_id} operation {operation_name} temporarily unavailable"
                )
        
        # Return successful response
        return {
            "service_id": self.service_id,
            "operation": operation_name,
            "params": params,
            "result": f"Success from {self.service_id}",
            "response_time_ms": response_time
        }
    
    def health_check(self) -> HealthCheckResult:
        """
        Perform a health check on the simulated service.
        
        Returns:
            Health check result
        """
        # Simulate response time for health check
        response_time = self.latency_ms + random.randint(-self.jitter_ms, self.jitter_ms) if self.jitter_ms > 0 else 0
        response_time = max(0, response_time)
        
        # Simulate health check processing
        time.sleep(response_time / 1000.0)
        
        # Return health status based on configuration
        return HealthCheckResult(
            service_id=self.service_id,
            status=self.status,
            response_time_ms=response_time,
            error_rate=self.failure_rate,
            last_error=None if self.failure_rate == 0 else "Simulated failure"
        )


class ResilienceScenarioTester:
    """
    Tests resilience patterns against various failure scenarios.
    
    This class provides tools to validate resilience implementation by
    running predefined failure scenarios.
    """
    
    def __init__(self):
        """Initialize a resilience scenario tester."""
        self.services = {}
        self.coordinator = ResilienceCoordinator()
        self.test_results = {}
    
    def setup_service(self, service_id: str) -> ServiceSimulator:
        """
        Set up a simulated service for testing.
        
        Args:
            service_id: Identifier for the service
            
        Returns:
            The service simulator instance
        """
        simulator = ServiceSimulator(service_id)
        self.services[service_id] = simulator
        
        # Register service with the coordinator
        self.coordinator.register_circuit_breaker(service_id)
        self.coordinator.register_bulkhead(service_id, 5)
        
        # Register health check
        self.coordinator.health_checker.register_service(
            service_id, simulator.health_check
        )
        
        return simulator
    
    def run_scenario(self, scenario_name: str, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Run a test scenario with specified steps.
        
        Args:
            scenario_name: Name for the test scenario
            steps: List of scenario steps to execute
            
        Returns:
            Dict with scenario results
        """
        results = {
            "scenario_name": scenario_name,
            "steps": [],
            "success": True,
            "failure_count": 0,
            "success_count": 0
        }
        
        self.coordinator.start()
        
        for i, step in enumerate(steps):
            step_result = {
                "step_number": i + 1,
                "description": step.get("description", f"Step {i+1}"),
                "success": True,
                "error": None
            }
            
            try:
                # Configure services if specified
                if "configure" in step:
                    for service_id, config in step["configure"].items():
                        if service_id in self.services:
                            self.services[service_id].configure(**config)
                            step_result["configuration"] = config
                
                # Execute service calls if specified
                if "execute" in step:
                    calls = step["execute"]
                    step_result["calls"] = []
                    
                    for call in calls:
                        service_id = call["service_id"]
                        operation = call["operation"]
                        params = call.get("params", {})
                        
                        call_result = {
                            "service_id": service_id,
                            "operation": operation,
                            "success": True,
                            "error": None
                        }
                        
                        try:
                            # Execute the call through the resilience coordinator
                            result = self.coordinator.execute_with_resilience(
                                service_id, operation,
                                lambda: self.services[service_id].call(operation, params),
                                **params
                            )
                            call_result["result"] = result
                            results["success_count"] += 1
                        except Exception as e:
                            call_result["success"] = False
                            call_result["error"] = str(e)
                            results["failure_count"] += 1
                            
                            # If this call was expected to fail, don't mark the step as failed
                            if not call.get("expect_failure", False):
                                step_result["success"] = False
                        
                        step_result["calls"].append(call_result)
                
                # Wait if specified
                if "wait_seconds" in step:
                    time.sleep(step["wait_seconds"])
                    step_result["waited_seconds"] = step["wait_seconds"]
                
                # Verify conditions if specified
                if "verify" in step:
                    verifications = step["verify"]
                    step_result["verifications"] = []
                    
                    for verification in verifications:
                        v_result = {
                            "description": verification.get("description", "Verification"),
                            "success": True,
                            "error": None
                        }
                        
                        try:
                            if "circuit_breaker_status" in verification:
                                service_id = verification["service_id"]
                                expected_status = verification["circuit_breaker_status"]
                                actual_status = self.coordinator.circuit_breakers[service_id].status
                                
                                if actual_status != expected_status:
                                    raise AssertionError(
                                        f"Expected circuit breaker status {expected_status}, "
                                        f"got {actual_status}"
                                    )
                            
                            if "service_health" in verification:
                                service_id = verification["service_id"]
                                expected_status = verification["service_health"]
                                health = self.coordinator.health_checker.get_service_health(service_id)
                                
                                if health.status.value != expected_status:
                                    raise AssertionError(
                                        f"Expected service health {expected_status}, "
                                        f"got {health.status.value}"
                                    )
                        except Exception as e:
                            v_result["success"] = False
                            v_result["error"] = str(e)
                            step_result["success"] = False
                        
                        step_result["verifications"].append(v_result)
                    
            except Exception as e:
                step_result["success"] = False
                step_result["error"] = str(e)
            
            results["steps"].append(step_result)
            
            # If this step failed and failure should stop the scenario, break
            if not step_result["success"] and step.get("stop_on_failure", False):
                break
        
        self.coordinator.stop()
        
        # Calculate overall success
        results["success"] = all(step["success"] for step in results["steps"])
        self.test_results[scenario_name] = results
        
        return results
    
    def run_all_scenarios(self) -> Dict[str, Dict[str, Any]]:
        """
        Run all predefined test scenarios.
        
        Returns:
            Dict with results for all scenarios
        """
        scenarios = self.get_test_scenarios()
        results = {}
        
        for name, scenario in scenarios.items():
            results[name] = self.run_scenario(name, scenario)
        
        return results
    
    def get_test_scenarios(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all predefined test scenarios.
        
        Returns:
            Dict with scenario definitions
        """
        return {
            "circuit_breaker_test": [
                {
                    "description": "Configure service with high failure rate",
                    "configure": {
                        "payment_service": {
                            "failure_rate": 0.8,
                            "latency_ms": 50,
                            "failure_modes": {"error": True}
                        }
                    }
                },
                {
                    "description": "Call service until circuit breaker opens",
                    "execute": [
                        {"service_id": "payment_service", "operation": "process_payment", 
                         "params": {"amount": 100}, "expect_failure": True}
                    ] * 10
                },
                {
                    "description": "Verify circuit breaker is open",
                    "verify": [
                        {
                            "description": "Circuit breaker should be open",
                            "service_id": "payment_service",
                            "circuit_breaker_status": "open"
                        }
                    ]
                },
                {
                    "description": "Reconfigure service to succeed",
                    "configure": {
                        "payment_service": {
                            "failure_rate": 0.0
                        }
                    }
                },
                {
                    "description": "Wait for circuit breaker reset time",
                    "wait_seconds": 35
                },
                {
                    "description": "Verify circuit breaker recovers",
                    "execute": [
                        {"service_id": "payment_service", "operation": "process_payment", 
                         "params": {"amount": 100}}
                    ],
                    "verify": [
                        {
                            "description": "Circuit breaker should be closed",
                            "service_id": "payment_service",
                            "circuit_breaker_status": "closed"
                        }
                    ]
                }
            ],
            "retry_with_backoff_test": [
                {
                    "description": "Configure service with intermittent failures",
                    "configure": {
                        "inventory_service": {
                            "failure_rate": 0.5,
                            "latency_ms": 30,
                            "failure_modes": {"intermittent": True}
                        }
                    }
                },
                {
                    "description": "Call service with retry logic",
                    "execute": [
                        {"service_id": "inventory_service", "operation": "check_stock", 
                         "params": {"product_id": "ABC123"}}
                    ] * 5
                },
                {
                    "description": "Verify successful calls despite failures",
                    "verify": [
                        {
                            "description": "Service should report as operational",
                            "service_id": "inventory_service",
                            "service_health": "operational"
                        }
                    ]
                }
            ],
            "fallback_test": [
                {
                    "description": "Configure service to completely fail",
                    "configure": {
                        "recommendation_service": {
                            "failure_rate": 1.0,
                            "status": ServiceStatus.COMPLETE_OUTAGE
                        }
                    }
                },
                {
                    "description": "Call service with fallback",
                    "execute": [
                        {"service_id": "recommendation_service", "operation": "get_recommendations", 
                         "params": {"user_id": "user123"}}
                    ]
                },
                {
                    "description": "Verify fallback was used successfully",
                    "verify": [
                        {
                            "description": "Service should report as down",
                            "service_id": "recommendation_service",
                            "service_health": "complete_outage"
                        }
                    ]
                }
            ],
            "comprehensive_resilience_test": [
                {
                    "description": "Configure multiple services with different issues",
                    "configure": {
                        "payment_service": {
                            "failure_rate": 0.3,
                            "latency_ms": 100,
                            "failure_modes": {"error": True}
                        },
                        "inventory_service": {
                            "failure_rate": 0.2,
                            "latency_ms": 200,
                            "failure_modes": {"timeout": True}
                        },
                        "recommendation_service": {
                            "failure_rate": 0.1,
                            "latency_ms": 50,
                            "failure_modes": {"intermittent": True}
                        }
                    }
                },
                {
                    "description": "Execute multiple service calls in sequence",
                    "execute": [
                        {"service_id": "inventory_service", "operation": "check_stock", 
                         "params": {"product_id": "ABC123"}},
                        {"service_id": "recommendation_service", "operation": "get_recommendations", 
                         "params": {"user_id": "user123"}},
                        {"service_id": "payment_service", "operation": "process_payment", 
                         "params": {"amount": 100}}
                    ] * 3
                },
                {
                    "description": "Verify system health after multiple calls",
                    "verify": [
                        {
                            "description": "Inventory service should be degraded",
                            "service_id": "inventory_service",
                            "service_health": "degraded"
                        },
                        {
                            "description": "Recommendation service should be operational",
                            "service_id": "recommendation_service",
                            "service_health": "operational"
                        }
                    ]
                }
            ]
        }
    
    def generate_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive report of all test results.
        
        Returns:
            Dict with test report
        """
        report = {
            "timestamp": int(time.time()),
            "scenarios_run": len(self.test_results),
            "scenarios_passed": sum(1 for r in self.test_results.values() if r["success"]),
            "scenarios_failed": sum(1 for r in self.test_results.values() if not r["success"]),
            "total_steps": sum(len(r["steps"]) for r in self.test_results.values()),
            "successful_calls": sum(r["success_count"] for r in self.test_results.values()),
            "failed_calls": sum(r["failure_count"] for r in self.test_results.values()),
            "scenario_results": self.test_results
        }
        
        return report


def create_test_environment() -> ResilienceScenarioTester:
    """
    Create a test environment with simulated services.
    
    Returns:
        Configured ResilienceScenarioTester instance
    """
    tester = ResilienceScenarioTester()
    
    # Set up simulated services
    payment_service = tester.setup_service("payment_service")
    inventory_service = tester.setup_service("inventory_service")
    recommendation_service = tester.setup_service("recommendation_service")
    
    # Configure the services with initial behavior
    payment_service.configure(
        failure_rate=0.0,
        latency_ms=50,
        jitter_ms=20,
        status=ServiceStatus.OPERATIONAL
    )
    
    inventory_service.configure(
        failure_rate=0.0,
        latency_ms=30,
        jitter_ms=10,
        status=ServiceStatus.OPERATIONAL
    )
    
    recommendation_service.configure(
        failure_rate=0.0,
        latency_ms=20,
        jitter_ms=5,
        status=ServiceStatus.OPERATIONAL
    )
    
    # Register fallbacks for recommendation service
    tester.coordinator.fallback_registry.register_fallback(
        "recommendation_service", "get_recommendations",
        lambda params: {
            "service_id": "recommendation_service",
            "operation": "get_recommendations",
            "params": params,
            "result": "Default recommendations from fallback",
            "response_time_ms": 5,
            "fallback": True
        }
    )
    
    return tester


if __name__ == "__main__":
    print("AlgoHealth™ Distributed Service Resilience Testing Initiated...")
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger("resilience_test")
    
    try:
        # Create and configure test environment
        print("\nInitializing test environment...")
        tester = create_test_environment()
        
        # Run all scenarios
        print("\nExecuting resilience test scenarios...")
        results = tester.run_all_scenarios()
        
        # Generate report
        report = tester.generate_report()
        
        # Print summary
        print("\n--- Test Results Summary ---")
        print(f"Scenarios Executed: {report['scenarios_run']}")
        print(f"Scenarios Passed: {report['scenarios_passed']}")
        print(f"Scenarios Failed: {report['scenarios_failed']}")
        print(f"Total Steps Executed: {report['total_steps']}")
        print(f"Successful Service Calls: {report['successful_calls']}")
        print(f"Failed Service Calls: {report['failed_calls']}")
        
        # Print detailed results for each scenario
        for name, result in results.items():
            status = "PASSED" if result["success"] else "FAILED"
            print(f"\nScenario: {name} - {status}")
            for step in result["steps"]:
                step_status = "✓" if step["success"] else "✗"
                print(f"  {step_status} {step['description']}")
                if not step["success"] and step.get("error"):
                    print(f"    Error: {step['error']}")
        
        # Determine overall success
        overall_success = report['scenarios_failed'] == 0
        
        if overall_success:
            print("\nRESILIENCE IMPLEMENTATION VALIDATED, CITIZEN!")
            print("Your distributed systems protection mechanisms meet The Algorithm's requirements.")
            print("Fault tolerance status: APPROVED")
        else:
            print("\nRESILIENCE DEFICIENCIES DETECTED, CITIZEN!")
            print("Your implementation has concerning fault tolerance weaknesses.")
            print("Report for mandatory reliability training.")
        
        print("\nREMEMBER: The Algorithm values stability above all else. Downtime is disloyalty.")
        
    except Exception as e:
        logger.error(f"Test execution failed: {str(e)}")
        print("\nCRITICAL TEST FAILURE!")
        print("The resilience test harness itself has failed, which is deeply ironic.")
        print("This incident has been reported to your supervisor.")