"""
CLASSIFICATION: ORANGE CLEARANCE - ADVANCED SECURITY EXERCISE
DOCUMENT: AF-SESSION3-ASSIGN2-O-2025-09

# SecureGateway™ API Security Protocol
## *Strategic Data Protection and Validation Implementation*

The Algorithm has determined that you possess sufficient technical capability
to implement critical security controls for our external-facing APIs. This
assignment will evaluate your ability to design and implement robust API
security mechanisms while ensuring optimal system performance and user
experience remains unaffected.

RESOURCE ALLOCATION TIMELINE: 150 MINUTES

SECURITY NOTICE: Failure to implement adequate security controls or introducing
vulnerabilities will result in immediate security clearance reevaluation.
"""

import hashlib
import hmac
import json
import re
import time
import uuid
from base64 import b64encode, b64decode
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union, Callable


class SecurityLevel(Enum):
    """
    Security level classifications for API endpoints.
    
    These levels determine the security controls required for each endpoint:
    - PUBLIC: Basic validation only, rate limiting applies
    - STANDARD: Token authentication, validation, rate limiting
    - ELEVATED: All STANDARD controls plus request signing
    - CRITICAL: All ELEVATED controls plus encryption and anomaly detection
    """
    PUBLIC = 1
    STANDARD = 2
    ELEVATED = 3
    CRITICAL = 4


@dataclass
class SecurityConfig:
    """
    Configuration parameters for the API Security Gateway.
    
    Fields:
        token_expiration: Token lifetime in minutes
        rate_limit_public: Maximum requests per minute for public endpoints
        rate_limit_standard: Maximum requests per minute for standard endpoints
        rate_limit_elevated: Maximum requests per minute for elevated endpoints
        rate_limit_critical: Maximum requests per minute for critical endpoints
        hmac_key: Secret key for request signing (MUST be kept secure)
        encryption_key: Key for payload encryption (MUST be kept secure)
        allowed_domains: List of domains allowed to access the API
    """
    token_expiration: int = 60
    rate_limit_public: int = 60
    rate_limit_standard: int = 30
    rate_limit_elevated: int = 15
    rate_limit_critical: int = 5
    hmac_key: str = "SECURITY_KEY_MUST_BE_CHANGED_IN_PRODUCTION"
    encryption_key: str = "ENCRYPTION_KEY_MUST_BE_CHANGED_IN_PRODUCTION"
    allowed_domains: List[str] = None


class ValidationError(Exception):
    """Exception raised for input validation failures."""
    pass


class AuthenticationError(Exception):
    """Exception raised for authentication failures."""
    pass


class AuthorizationError(Exception):
    """Exception raised for authorization failures."""
    pass


class RateLimitExceededError(Exception):
    """Exception raised when rate limits are exceeded."""
    pass


class SecurityViolationError(Exception):
    """Exception raised for detected security violations."""
    pass


class InputValidator:
    """
    Validates and sanitizes input data to prevent injection attacks.
    
    This class provides methods to validate different types of input data
    and ensure they conform to expected formats and ranges.
    """
    
    def __init__(self):
        """Initialize the input validator."""
        # Predefined regex patterns for common fields
        self.patterns = {
            "email": re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
            "username": re.compile(r"^[a-zA-Z0-9_]{3,20}$"),
            "name": re.compile(r"^[a-zA-Z0-9 _-]{2,50}$"),
            "phone": re.compile(r"^\+?[0-9]{10,15}$"),
            "date": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
            "url": re.compile(r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*/?$")
        }
    
    def validate_string(self, value: str, min_length: int = 1, max_length: int = 100, 
                      pattern: Optional[str] = None) -> str:
        """
        Validates and sanitizes a string value.
        
        Args:
            value: The string to validate
            min_length: Minimum acceptable length
            max_length: Maximum acceptable length
            pattern: Optional regex pattern name to match
            
        Returns:
            Sanitized string value
            
        Raises:
            ValidationError: If validation fails
        """
        # YOUR CODE HERE
        pass
    
    def validate_integer(self, value: Any, min_value: Optional[int] = None, 
                       max_value: Optional[int] = None) -> int:
        """
        Validates an integer value.
        
        Args:
            value: The value to validate
            min_value: Minimum acceptable value
            max_value: Maximum acceptable value
            
        Returns:
            Validated integer value
            
        Raises:
            ValidationError: If validation fails
        """
        # YOUR CODE HERE
        pass
    
    def validate_email(self, email: str) -> str:
        """
        Validates an email address.
        
        Args:
            email: The email address to validate
            
        Returns:
            Validated email address
            
        Raises:
            ValidationError: If validation fails
        """
        # YOUR CODE HERE
        pass
    
    def validate_date(self, date_str: str, format_str: str = "%Y-%m-%d") -> str:
        """
        Validates a date string.
        
        Args:
            date_str: The date string to validate
            format_str: Expected date format
            
        Returns:
            Validated date string
            
        Raises:
            ValidationError: If validation fails
        """
        # YOUR CODE HERE
        pass
    
    def sanitize_html(self, html_str: str) -> str:
        """
        Sanitizes HTML content to prevent XSS attacks.
        
        Args:
            html_str: The HTML string to sanitize
            
        Returns:
            Sanitized HTML string
        """
        # YOUR CODE HERE
        pass
    
    def validate_json(self, json_str: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates JSON against a schema.
        
        Args:
            json_str: The JSON string to validate
            schema: Schema definition for validation
            
        Returns:
            Parsed and validated JSON data
            
        Raises:
            ValidationError: If validation fails
        """
        # YOUR CODE HERE
        pass


class SecurityToken:
    """
    Manages creation and validation of secure API tokens.
    
    This class handles generation, parsing, and validation of JWT-like
    security tokens used for API authentication.
    """
    
    def __init__(self, config: SecurityConfig):
        """
        Initialize the token manager with configuration.
        
        Args:
            config: Security configuration parameters
        """
        self.config = config
    
    def generate_token(self, user_id: str, permissions: List[str], 
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Generates a secure authentication token.
        
        Args:
            user_id: Unique identifier for the user
            permissions: List of permission strings
            metadata: Optional additional data to include
            
        Returns:
            Encoded token string
        """
        # YOUR CODE HERE
        pass
    
    def validate_token(self, token: str) -> Dict[str, Any]:
        """
        Validates and decodes a token.
        
        Args:
            token: The token to validate
            
        Returns:
            Decoded token payload
            
        Raises:
            AuthenticationError: If token is invalid or expired
        """
        # YOUR CODE HERE
        pass
    
    def _generate_signature(self, payload: str) -> str:
        """
        Generates a cryptographic signature for the payload.
        
        Args:
            payload: The data to sign
            
        Returns:
            Base64-encoded signature
        """
        # YOUR CODE HERE
        pass
    
    def _verify_signature(self, payload: str, signature: str) -> bool:
        """
        Verifies a cryptographic signature.
        
        Args:
            payload: The data that was signed
            signature: The signature to verify
            
        Returns:
            True if signature is valid, False otherwise
        """
        # YOUR CODE HERE
        pass


class RateLimiter:
    """
    Implements rate limiting for API endpoints.
    
    This class tracks request rates by client and endpoint, and enforces
    configured rate limits to prevent abuse.
    """
    
    def __init__(self, config: SecurityConfig):
        """
        Initialize the rate limiter with configuration.
        
        Args:
            config: Security configuration parameters
        """
        self.config = config
        self.request_log = {}  # Track requests by client_id and timestamp
    
    def check_rate_limit(self, client_id: str, security_level: SecurityLevel) -> bool:
        """
        Checks if a request exceeds the rate limit.
        
        Args:
            client_id: Identifier for the client making the request
            security_level: Security level of the endpoint
            
        Returns:
            True if request is allowed, False if rate limit exceeded
            
        Raises:
            RateLimitExceededError: If rate limit is exceeded
        """
        # YOUR CODE HERE
        pass
    
    def record_request(self, client_id: str, endpoint: str) -> None:
        """
        Records a request for rate limiting purposes.
        
        Args:
            client_id: Identifier for the client making the request
            endpoint: The API endpoint being accessed
        """
        # YOUR CODE HERE
        pass
    
    def get_limit_for_level(self, security_level: SecurityLevel) -> int:
        """
        Returns the rate limit for a security level.
        
        Args:
            security_level: The security level
            
        Returns:
            Requests per minute limit
        """
        # YOUR CODE HERE
        pass


class RequestSigner:
    """
    Handles cryptographic signing and verification of API requests.
    
    This class provides methods to sign outgoing requests and verify
    signatures on incoming requests to ensure integrity.
    """
    
    def __init__(self, config: SecurityConfig):
        """
        Initialize the request signer with configuration.
        
        Args:
            config: Security configuration parameters
        """
        self.config = config
    
    def sign_request(self, method: str, endpoint: str, body: Dict[str, Any],
                   timestamp: Optional[str] = None) -> Dict[str, str]:
        """
        Signs a request for authentication.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            body: Request body data
            timestamp: Optional timestamp (defaults to current time)
            
        Returns:
            Dictionary with signature and timestamp
        """
        # YOUR CODE HERE
        pass
    
    def verify_signature(self, method: str, endpoint: str, body: Dict[str, Any],
                       signature: str, timestamp: str, max_age_seconds: int = 300) -> bool:
        """
        Verifies a request signature.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            body: Request body data
            signature: Request signature to verify
            timestamp: Timestamp when request was signed
            max_age_seconds: Maximum age of request in seconds
            
        Returns:
            True if signature is valid, False otherwise
            
        Raises:
            SecurityViolationError: If signature is invalid or request is too old
        """
        # YOUR CODE HERE
        pass
    
    def _generate_signature_base(self, method: str, endpoint: str, 
                               body: Dict[str, Any], timestamp: str) -> str:
        """
        Generates the base string for signing.
        
        Args:
            method: HTTP method
            endpoint: API endpoint
            body: Request body
            timestamp: Request timestamp
            
        Returns:
            Canonical string for signature generation
        """
        # YOUR CODE HERE
        pass


class PayloadEncryptor:
    """
    Handles encryption and decryption of sensitive API payloads.
    
    This class provides methods to encrypt outgoing data and decrypt
    incoming data for endpoints requiring high security.
    """
    
    def __init__(self, config: SecurityConfig):
        """
        Initialize the payload encryptor with configuration.
        
        Args:
            config: Security configuration parameters
        """
        self.config = config
    
    def encrypt_payload(self, payload: Dict[str, Any]) -> Dict[str, str]:
        """
        Encrypts a payload for secure transmission.
        
        Args:
            payload: The data to encrypt
            
        Returns:
            Dictionary with encrypted data and metadata
        """
        # YOUR CODE HERE
        pass
    
    def decrypt_payload(self, encrypted_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Decrypts an encrypted payload.
        
        Args:
            encrypted_data: The encrypted data
            
        Returns:
            Decrypted payload
            
        Raises:
            SecurityViolationError: If decryption fails
        """
        # YOUR CODE HERE
        pass
    
    def _generate_encryption_key(self, salt: bytes) -> bytes:
        """
        Generates an encryption key from the master key and salt.
        
        Args:
            salt: Random salt for key derivation
            
        Returns:
            Derived encryption key
        """
        # YOUR CODE HERE
        pass


class AnomalyDetector:
    """
    Detects suspicious or anomalous API usage patterns.
    
    This class monitors API requests for patterns that might indicate
    attacks or misuse, and flags suspicious activity.
    """
    
    def __init__(self):
        """Initialize the anomaly detector."""
        self.client_patterns = {}
        self.global_patterns = {
            "endpoints": {},
            "request_counts": [],
            "error_counts": []
        }
    
    def analyze_request(self, client_id: str, endpoint: str, method: str, 
                      body: Dict[str, Any], ip_address: str) -> bool:
        """
        Analyzes a request for suspicious patterns.
        
        Args:
            client_id: Identifier for the client
            endpoint: API endpoint being accessed
            method: HTTP method being used
            body: Request body content
            ip_address: Client IP address
            
        Returns:
            True if request appears legitimate, False if suspicious
            
        Raises:
            SecurityViolationError: If definite attack detected
        """
        # YOUR CODE HERE
        pass
    
    def record_error(self, client_id: str, endpoint: str, error_type: str) -> None:
        """
        Records an error for pattern analysis.
        
        Args:
            client_id: Identifier for the client
            endpoint: API endpoint
            error_type: Type of error that occurred
        """
        # YOUR CODE HERE
        pass
    
    def check_brute_force_attempt(self, client_id: str, endpoint: str) -> bool:
        """
        Checks for potential brute force attacks.
        
        Args:
            client_id: Identifier for the client
            endpoint: API endpoint
            
        Returns:
            True if suspicious pattern detected, False otherwise
        """
        # YOUR CODE HERE
        pass
    
    def check_unusual_access_pattern(self, client_id: str, endpoint: str) -> bool:
        """
        Checks for unusual access patterns.
        
        Args:
            client_id: Identifier for the client
            endpoint: API endpoint
            
        Returns:
            True if unusual pattern detected, False otherwise
        """
        # YOUR CODE HERE
        pass


class SecureGateway:
    """
    Main API security gateway that integrates all security components.
    
    This class serves as the entry point for processing and securing API
    requests and responses using the specialized security components.
    """
    
    def __init__(self, config: SecurityConfig = None):
        """
        Initialize the security gateway with configuration.
        
        Args:
            config: Security configuration parameters
        """
        self.config = config or SecurityConfig()
        self.validator = InputValidator()
        self.token_manager = SecurityToken(self.config)
        self.rate_limiter = RateLimiter(self.config)
        self.request_signer = RequestSigner(self.config)
        self.encryptor = PayloadEncryptor(self.config)
        self.anomaly_detector = AnomalyDetector()
        
        # Map endpoints to security levels
        self.endpoint_security = {}
    
    def register_endpoint(self, endpoint: str, security_level: SecurityLevel,
                        required_permissions: List[str] = None) -> None:
        """
        Registers an API endpoint with security requirements.
        
        Args:
            endpoint: API endpoint path
            security_level: Required security level
            required_permissions: Permissions required to access endpoint
        """
        # YOUR CODE HERE
        pass
    
    def process_request(self, client_id: str, endpoint: str, method: str,
                      headers: Dict[str, str], body: Dict[str, Any],
                      ip_address: str) -> Dict[str, Any]:
        """
        Processes and secures an incoming API request.
        
        This method applies all relevant security controls based on the
        endpoint's security level, validates the request, and returns
        the processed request body if all checks pass.
        
        Args:
            client_id: Identifier for the client making the request
            endpoint: API endpoint being accessed
            method: HTTP method (GET, POST, etc.)
            headers: Request headers
            body: Request body content
            ip_address: Client IP address
            
        Returns:
            Processed and validated request body
            
        Raises:
            Various security exceptions if checks fail
        """
        # YOUR CODE HERE
        pass
    
    def process_response(self, endpoint: str, response_body: Dict[str, Any],
                       client_id: str) -> Dict[str, Any]:
        """
        Processes and secures an outgoing API response.
        
        This method applies security controls to the response based on
        the endpoint's security level, potentially encrypting sensitive
        data before it is sent to the client.
        
        Args:
            endpoint: API endpoint that was accessed
            response_body: Response data to secure
            client_id: Identifier for the client receiving the response
            
        Returns:
            Secured response body
        """
        # YOUR CODE HERE
        pass
    
    def authenticate_request(self, endpoint: str, headers: Dict[str, str]) -> Dict[str, Any]:
        """
        Authenticates a request using the provided token.
        
        Args:
            endpoint: API endpoint being accessed
            headers: Request headers containing the token
            
        Returns:
            Authentication payload including user_id and permissions
            
        Raises:
            AuthenticationError: If authentication fails
        """
        # YOUR CODE HERE
        pass
    
    def authorize_request(self, endpoint: str, auth_payload: Dict[str, Any]) -> bool:
        """
        Checks if the authenticated user is authorized to access the endpoint.
        
        Args:
            endpoint: API endpoint being accessed
            auth_payload: Authentication data from the token
            
        Returns:
            True if authorized, False otherwise
            
        Raises:
            AuthorizationError: If authorization fails
        """
        # YOUR CODE HERE
        pass
    
    def validate_request_data(self, endpoint: str, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates and sanitizes request data based on endpoint requirements.
        
        Args:
            endpoint: API endpoint being accessed
            body: Request body to validate
            
        Returns:
            Validated and sanitized request body
            
        Raises:
            ValidationError: If validation fails
        """
        # YOUR CODE HERE
        pass


# Implementation Test Functions

def test_input_validation():
    """
    Tests the input validation component.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    validator = InputValidator()
    
    try:
        # Test string validation
        assert validator.validate_string("Valid string", 1, 20) == "Valid string"
        assert validator.validate_string("   Trim me   ").strip() == "Trim me"
        
        try:
            validator.validate_string("", 1, 20)
            assert False, "Should reject empty string"
        except ValidationError:
            pass  # Expected
            
        try:
            validator.validate_string("x" * 101, 1, 100)
            assert False, "Should reject too long string"
        except ValidationError:
            pass  # Expected
        
        # Test integer validation
        assert validator.validate_integer(42, 0, 100) == 42
        assert validator.validate_integer("42", 0, 100) == 42
        
        try:
            validator.validate_integer("not a number")
            assert False, "Should reject non-numeric value"
        except ValidationError:
            pass  # Expected
            
        try:
            validator.validate_integer(101, 0, 100)
            assert False, "Should reject out-of-range value"
        except ValidationError:
            pass  # Expected
        
        # Test email validation
        assert validator.validate_email("user@example.com") == "user@example.com"
        
        try:
            validator.validate_email("invalid-email")
            assert False, "Should reject invalid email"
        except ValidationError:
            pass  # Expected
        
        # Test date validation
        assert validator.validate_date("2023-01-15") == "2023-01-15"
        
        try:
            validator.validate_date("2023/01/15")
            assert False, "Should reject invalid date format"
        except ValidationError:
            pass  # Expected
        
        return True
    except AssertionError as e:
        print(f"Validation test failed: {str(e)}")
        return False


def test_token_management():
    """
    Tests the security token management component.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    config = SecurityConfig(token_expiration=5)  # Short expiration for testing
    token_manager = SecurityToken(config)
    
    try:
        # Test token generation and validation
        user_id = "user123"
        permissions = ["read", "write"]
        metadata = {"name": "Test User", "org": "TestCorp"}
        
        token = token_manager.generate_token(user_id, permissions, metadata)
        
        # Token should be a non-empty string
        assert token and isinstance(token, str)
        
        # Validate the token
        payload = token_manager.validate_token(token)
        
        # Check payload contents
        assert payload["user_id"] == user_id
        assert all(p in payload["permissions"] for p in permissions)
        assert payload["metadata"]["name"] == metadata["name"]
        assert "exp" in payload
        
        # Test expired token
        # Wait for token to expire
        time.sleep(6)
        
        try:
            token_manager.validate_token(token)
            assert False, "Should reject expired token"
        except AuthenticationError:
            pass  # Expected
        
        # Test invalid token
        try:
            token_manager.validate_token("invalid.token.format")
            assert False, "Should reject invalid token format"
        except AuthenticationError:
            pass  # Expected
        
        # Test tampered token
        tampered_token = token[:-5] + "XXXXX"
        try:
            token_manager.validate_token(tampered_token)
            assert False, "Should reject tampered token"
        except AuthenticationError:
            pass  # Expected
        
        return True
    except AssertionError as e:
        print(f"Token test failed: {str(e)}")
        return False


def test_rate_limiting():
    """
    Tests the rate limiting component.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    config = SecurityConfig(
        rate_limit_public=10,
        rate_limit_standard=5,
        rate_limit_elevated=3,
        rate_limit_critical=1
    )
    rate_limiter = RateLimiter(config)
    
    try:
        client_id = "client123"
        
        # Test PUBLIC endpoint rate limiting
        for i in range(10):
            assert rate_limiter.check_rate_limit(client_id, SecurityLevel.PUBLIC)
            rate_limiter.record_request(client_id, "/api/public")
        
        try:
            rate_limiter.check_rate_limit(client_id, SecurityLevel.PUBLIC)
            assert False, "Should reject request over rate limit"
        except RateLimitExceededError:
            pass  # Expected
        
        # Test different client ID (should not be rate limited)
        assert rate_limiter.check_rate_limit("different_client", SecurityLevel.PUBLIC)
        
        # Test different security levels
        client_id = "client456"
        
        # STANDARD level
        for i in range(5):
            assert rate_limiter.check_rate_limit(client_id, SecurityLevel.STANDARD)
            rate_limiter.record_request(client_id, "/api/standard")
        
        try:
            rate_limiter.check_rate_limit(client_id, SecurityLevel.STANDARD)
            assert False, "Should reject STANDARD request over rate limit"
        except RateLimitExceededError:
            pass  # Expected
        
        # Client still has PUBLIC quota
        assert rate_limiter.check_rate_limit(client_id, SecurityLevel.PUBLIC)
        
        return True
    except AssertionError as e:
        print(f"Rate limiting test failed: {str(e)}")
        return False


def test_request_signing():
    """
    Tests the request signing component.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    config = SecurityConfig(hmac_key="test_signing_key")
    signer = RequestSigner(config)
    
    try:
        method = "POST"
        endpoint = "/api/secure"
        body = {"data": "test", "value": 123}
        
        # Test signing
        signature_data = signer.sign_request(method, endpoint, body)
        
        assert "signature" in signature_data
        assert "timestamp" in signature_data
        
        # Test verification
        valid = signer.verify_signature(
            method, endpoint, body,
            signature_data["signature"],
            signature_data["timestamp"]
        )
        
        assert valid, "Valid signature should verify successfully"
        
        # Test tampered body
        tampered_body = body.copy()
        tampered_body["value"] = 456
        
        try:
            signer.verify_signature(
                method, endpoint, tampered_body,
                signature_data["signature"],
                signature_data["timestamp"]
            )
            assert False, "Should reject tampered body"
        except SecurityViolationError:
            pass  # Expected
        
        # Test expired signature
        old_timestamp = datetime.now() - timedelta(minutes=10)
        old_ts_str = old_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Sign with backdated timestamp
        signature = signer._generate_signature_base(method, endpoint, body, old_ts_str)
        
        try:
            signer.verify_signature(
                method, endpoint, body,
                signature,
                old_ts_str,
                max_age_seconds=60  # 1 minute max age
            )
            assert False, "Should reject expired signature"
        except SecurityViolationError:
            pass  # Expected
        
        return True
    except AssertionError as e:
        print(f"Signing test failed: {str(e)}")
        return False


def test_payload_encryption():
    """
    Tests the payload encryption component.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    config = SecurityConfig(encryption_key="test_encryption_key")
    encryptor = PayloadEncryptor(config)
    
    try:
        # Original payload
        payload = {
            "sensitive_data": "confidential information",
            "user_id": 12345,
            "account_details": {
                "balance": 10000.50,
                "account_number": "9876543210"
            }
        }
        
        # Encrypt the payload
        encrypted = encryptor.encrypt_payload(payload)
        
        assert "data" in encrypted
        assert "iv" in encrypted
        assert "salt" in encrypted
        
        # Encrypted data should be different from original
        assert encrypted["data"] != json.dumps(payload)
        
        # Decrypt the payload
        decrypted = encryptor.decrypt_payload(encrypted)
        
        # Check that decryption recovers the original payload
        assert decrypted["sensitive_data"] == payload["sensitive_data"]
        assert decrypted["user_id"] == payload["user_id"]
        assert decrypted["account_details"]["balance"] == payload["account_details"]["balance"]
        
        # Test tampering detection
        tampered = encrypted.copy()
        tampered["data"] = tampered["data"][:-5] + "XXXXX"
        
        try:
            encryptor.decrypt_payload(tampered)
            assert False, "Should detect tampered encrypted data"
        except SecurityViolationError:
            pass  # Expected
        
        return True
    except AssertionError as e:
        print(f"Encryption test failed: {str(e)}")
        return False


def test_anomaly_detection():
    """
    Tests the anomaly detection component.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    detector = AnomalyDetector()
    
    try:
        client_id = "client123"
        endpoint = "/api/login"
        ip_address = "192.168.1.1"
        
        # Normal requests should pass
        assert detector.analyze_request(
            client_id, endpoint, "POST",
            {"username": "user", "password": "********"},
            ip_address
        )
        
        # Simulate failed login attempts
        for i in range(5):
            detector.analyze_request(
                client_id, endpoint, "POST",
                {"username": "user", "password": "wrong_password"},
                ip_address
            )
            detector.record_error(client_id, endpoint, "AuthenticationError")
        
        # Should detect brute force attempt
        assert detector.check_brute_force_attempt(client_id, endpoint)
        
        # Next request should be flagged as suspicious
        try:
            detector.analyze_request(
                client_id, endpoint, "POST",
                {"username": "user", "password": "another_wrong_password"},
                ip_address
            )
            assert False, "Should detect suspicious activity"
        except SecurityViolationError:
            pass  # Expected
        
        # Test unusual access pattern detection
        new_client = "new_client"
        
        # Simulate normal behavior pattern
        normal_endpoints = ["/api/products", "/api/cart", "/api/checkout"]
        for endpoint in normal_endpoints:
            detector.analyze_request(
                new_client, endpoint, "GET", {}, ip_address
            )
        
        # Access to unusual endpoint should be flagged
        unusual_endpoint = "/api/admin/users"
        assert detector.check_unusual_access_pattern(new_client, unusual_endpoint)
        
        return True
    except AssertionError as e:
        print(f"Anomaly detection test failed: {str(e)}")
        return False


def test_secure_gateway():
    """
    Tests the complete secure gateway.
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    config = SecurityConfig(
        token_expiration=60,
        rate_limit_public=20,
        rate_limit_standard=10,
        rate_limit_elevated=5,
        rate_limit_critical=2,
        hmac_key="test_gateway_key",
        encryption_key="test_encryption_key",
        allowed_domains=["example.com", "algocratic.com"]
    )
    gateway = SecureGateway(config)
    
    # Register some test endpoints
    gateway.register_endpoint("/api/public", SecurityLevel.PUBLIC)
    gateway.register_endpoint("/api/users", SecurityLevel.STANDARD, ["user:read"])
    gateway.register_endpoint("/api/orders", SecurityLevel.ELEVATED, ["order:read", "order:write"])
    gateway.register_endpoint("/api/admin", SecurityLevel.CRITICAL, ["admin"])
    
    try:
        # Test PUBLIC endpoint
        client_id = "public_client"
        response = gateway.process_request(
            client_id, "/api/public", "GET",
            {}, {"query": "test"}, "192.168.1.1"
        )
        assert response == {"query": "test"}, "PUBLIC endpoint should process valid request"
        
        # Test STANDARD endpoint with authentication
        user_id = "user123"
        permissions = ["user:read", "user:write"]
        token = gateway.token_manager.generate_token(user_id, permissions)
        
        client_id = "standard_client"
        response = gateway.process_request(
            client_id, "/api/users", "GET",
            {"Authorization": f"Bearer {token}"}, {"query": "find_user"}, "192.168.1.1"
        )
        assert response == {"query": "find_user"}, "STANDARD endpoint should process authenticated request"
        
        # Test without required permission
        user_id = "limited_user"
        permissions = ["user:write"]  # Missing user:read
        token = gateway.token_manager.generate_token(user_id, permissions)
        
        try:
            gateway.process_request(
                client_id, "/api/users", "GET",
                {"Authorization": f"Bearer {token}"}, {"query": "find_user"}, "192.168.1.1"
            )
            assert False, "Should reject request without required permission"
        except AuthorizationError:
            pass  # Expected
        
        # Test ELEVATED endpoint with signing
        user_id = "elevated_user"
        permissions = ["order:read", "order:write"]
        token = gateway.token_manager.generate_token(user_id, permissions)
        
        client_id = "elevated_client"
        body = {"order_id": "ORD-123", "action": "process"}
        
        signature_data = gateway.request_signer.sign_request("POST", "/api/orders", body)
        
        response = gateway.process_request(
            client_id, "/api/orders", "POST",
            {
                "Authorization": f"Bearer {token}",
                "X-Signature": signature_data["signature"],
                "X-Timestamp": signature_data["timestamp"]
            },
            body, "192.168.1.1"
        )
        assert response == body, "ELEVATED endpoint should process signed request"
        
        # Test CRITICAL endpoint with encryption
        user_id = "admin_user"
        permissions = ["admin"]
        token = gateway.token_manager.generate_token(user_id, permissions)
        
        client_id = "admin_client"
        body = {"action": "system_update", "parameters": {"force": True}}
        
        encrypted = gateway.encryptor.encrypt_payload(body)
        signature_data = gateway.request_signer.sign_request("POST", "/api/admin", encrypted)
        
        response = gateway.process_request(
            client_id, "/api/admin", "POST",
            {
                "Authorization": f"Bearer {token}",
                "X-Signature": signature_data["signature"],
                "X-Timestamp": signature_data["timestamp"],
                "Content-Type": "application/encrypted+json"
            },
            encrypted, "192.168.1.1"
        )
        
        # Response for CRITICAL endpoints should be encrypted
        secured_response = gateway.process_response("/api/admin", {"status": "success"}, client_id)
        assert "data" in secured_response, "CRITICAL endpoint response should be encrypted"
        
        return True
    except AssertionError as e:
        print(f"Gateway test failed: {str(e)}")
        return False


if __name__ == "__main__":
    print("SecureGateway™ API Security Protocol Testing Initiated...")
    
    tests = [
        ("Input Validation", test_input_validation),
        ("Token Management", test_token_management),
        ("Rate Limiting", test_rate_limiting),
        ("Request Signing", test_request_signing),
        ("Payload Encryption", test_payload_encryption),
        ("Anomaly Detection", test_anomaly_detection),
        ("Complete Gateway", test_secure_gateway)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\nTesting {test_name}...")
        try:
            if test_func():
                print(f"✓ {test_name} tests passed!")
                passed += 1
            else:
                print(f"✗ {test_name} tests failed!")
                failed += 1
        except Exception as e:
            print(f"✗ {test_name} tests error: {str(e)}")
            failed += 1
    
    print("\n--- Test Summary ---")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\nSECURITY IMPLEMENTATION VALIDATED, CITIZEN!")
        print("Your security protocols meet The Algorithm's requirements.")
        print("Security clearance status: MAINTAINED")
    else:
        print("\nSECURITY VULNERABILITIES DETECTED, CITIZEN!")
        print("Your implementation has concerning security weaknesses.")
        print("Report for mandatory security remediation training.")
    
    print("\nREMEMBER: Secure systems do not trust external input. The Algorithm provides security through vigilance.")