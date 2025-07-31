"""
LEGACY CODE - DO NOT MODIFY DIRECTLY
VERSION: 1.7.3 (STABLE RELEASE 2021)

AlgoCratic Employee Notification Distribution System (AENDS)
Responsible for all inter-departmental communication and alerts.

WARNING: This system is considered mission-critical legacy infrastructure.
Any modifications must maintain complete backwards compatibility.
Proper refactoring approval (Form AF-DEV-REFAC-2025-09) is required.
"""

import time
import random
import datetime
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Global configuration
SYSTEM_INITIALIZED = False
NOTIFICATION_COUNTER = 0
ALERT_LEVEL_MAP = {"low": 1, "medium": 2, "high": 3, "critical": 4, "apocalyptic": 5}
DEFAULT_EMAIL_SERVER = "mail.algocratic.com"
PRIORITY_LEVELS = ["standard", "important", "urgent", "mandatory", "immediate_termination"]
SUCCESS_FLAG = True
ERROR_LOG = []
NOTIFICATION_HISTORY = []
DEFAULT_TIMEOUT = 30
NOTIFICATION_TYPES = ["email", "sms", "slack", "terminal", "neural", "emergency_broadcast"]
CURRENT_PROTOCOL = "standard"
EMAIL_TEMPLATES = {}
EMPLOYEE_CACHE = {}
DEPARTMENT_CODES = {
    "HR": "Human Resource Optimization",
    "DEV": "Algorithmic Implementation Unit",
    "QA": "Quality Amplification",
    "MGMT": "Managerial Oversight",
    "FIN": "Resource Allocation",
    "MKTG": "Market Penetration",
    "LEGAL": "Compliance Enforcement"
}

# Load configuration
def initialize_notification_system():
    """Initialize the notification system with default settings."""
    global SYSTEM_INITIALIZED, EMAIL_TEMPLATES, EMPLOYEE_CACHE
    
    if SYSTEM_INITIALIZED:
        print("System already initialized.")
        return
    
    # Load email templates
    EMAIL_TEMPLATES = {
        "standard": "Dear {employee_name},\n\n{message}\n\nThe Algorithm Provides,\n{sender_name}",
        "important": "IMPORTANT NOTICE\n\nDear {employee_name},\n\n{message}\n\nThe Algorithm Provides,\n{sender_name}",
        "urgent": "URGENT: IMMEDIATE ATTENTION REQUIRED\n\nDear {employee_name},\n\n{message}\n\nThe Algorithm Provides,\n{sender_name}",
        "mandatory": "MANDATORY ACTION REQUIRED\n\nDear {employee_name},\n\n{message}\n\nCompliance is non-optional.\nThe Algorithm Provides,\n{sender_name}",
        "immediate_termination": "FINAL COMMUNICATION\n\nFormer Employee {employee_name},\n\n{message}\n\nYour access has been terminated.\nThe Algorithm Has Provided,\n{sender_name}"
    }
    
    # Mock employee database for testing
    EMPLOYEE_CACHE = {
        "E12345": {"name": "John Smith", "email": "john.smith@algocratic.com", "department": "DEV", "clearance": "RED"},
        "E12346": {"name": "Jane Doe", "email": "jane.doe@algocratic.com", "department": "QA", "clearance": "ORANGE"},
        "E12347": {"name": "Bob Johnson", "email": "bob.johnson@algocratic.com", "department": "HR", "clearance": "RED"},
        "E12348": {"name": "Alice Williams", "email": "alice.williams@algocratic.com", "department": "MGMT", "clearance": "YELLOW"},
        "E12349": {"name": "Charlie Brown", "email": "charlie.brown@algocratic.com", "department": "DEV", "clearance": "INFRARED"},
    }
    
    SYSTEM_INITIALIZED = True
    print("Notification system initialized.")

# Function to create and send email notifications
def send_email_notification(recipient_id, subject, message, priority="standard", sender_id="SYSTEM"):
    """Send an email notification to a specific employee."""
    global NOTIFICATION_COUNTER, SUCCESS_FLAG, ERROR_LOG, NOTIFICATION_HISTORY
    
    if not SYSTEM_INITIALIZED:
        initialize_notification_system()
    
    NOTIFICATION_COUNTER += 1
    
    # Validate recipient
    if recipient_id not in EMPLOYEE_CACHE:
        ERROR_LOG.append(f"Error: Employee {recipient_id} not found")
        SUCCESS_FLAG = False
        return False
    
    recipient = EMPLOYEE_CACHE[recipient_id]
    
    if sender_id != "SYSTEM" and sender_id in EMPLOYEE_CACHE:
        sender_name = EMPLOYEE_CACHE[sender_id]["name"]
    else:
        sender_name = "The Algorithm"
    
    # Apply template based on priority
    template = EMAIL_TEMPLATES.get(priority, EMAIL_TEMPLATES["standard"])
    formatted_message = template.format(
        employee_name=recipient["name"],
        message=message,
        sender_name=sender_name
    )
    
    # In a real system, this would send an actual email
    # For this simulation, we'll just log it
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notification_record = {
        "id": f"NOTIF-{NOTIFICATION_COUNTER}",
        "timestamp": timestamp,
        "type": "email",
        "recipient_id": recipient_id,
        "recipient_name": recipient["name"],
        "subject": subject,
        "priority": priority,
        "status": "delivered",
        "sender": sender_name
    }
    
    NOTIFICATION_HISTORY.append(notification_record)
    
    # Simulate occasional failures for realism
    if random.random() < 0.05:  # 5% chance of failure
        notification_record["status"] = "failed"
        ERROR_LOG.append(f"Error: Failed to deliver email to {recipient['email']}")
        SUCCESS_FLAG = False
        return False
    
    return True

# Function to send SMS notifications
def send_sms_notification(recipient_id, message, priority="standard", sender_id="SYSTEM"):
    """Send an SMS notification to a specific employee."""
    global NOTIFICATION_COUNTER, SUCCESS_FLAG, ERROR_LOG, NOTIFICATION_HISTORY
    
    if not SYSTEM_INITIALIZED:
        initialize_notification_system()
    
    NOTIFICATION_COUNTER += 1
    
    # Validate recipient
    if recipient_id not in EMPLOYEE_CACHE:
        ERROR_LOG.append(f"Error: Employee {recipient_id} not found")
        SUCCESS_FLAG = False
        return False
    
    recipient = EMPLOYEE_CACHE[recipient_id]
    
    if sender_id != "SYSTEM" and sender_id in EMPLOYEE_CACHE:
        sender_name = EMPLOYEE_CACHE[sender_id]["name"]
    else:
        sender_name = "The Algorithm"
    
    # Format SMS based on priority
    if priority == "standard":
        formatted_message = f"AlgoCratic: {message}"
    elif priority == "important":
        formatted_message = f"IMPORTANT - AlgoCratic: {message}"
    elif priority == "urgent":
        formatted_message = f"URGENT - AlgoCratic: {message}"
    elif priority == "mandatory":
        formatted_message = f"MANDATORY ACTION - AlgoCratic: {message}"
    elif priority == "immediate_termination":
        formatted_message = f"FINAL NOTICE - AlgoCratic: {message}"
    else:
        formatted_message = f"AlgoCratic: {message}"
    
    # In a real system, this would send an actual SMS
    # For this simulation, we'll just log it
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notification_record = {
        "id": f"NOTIF-{NOTIFICATION_COUNTER}",
        "timestamp": timestamp,
        "type": "sms",
        "recipient_id": recipient_id,
        "recipient_name": recipient["name"],
        "message": formatted_message,
        "priority": priority,
        "status": "delivered",
        "sender": sender_name
    }
    
    NOTIFICATION_HISTORY.append(notification_record)
    
    # Simulate occasional failures for realism
    if random.random() < 0.1:  # 10% chance of failure for SMS
        notification_record["status"] = "failed"
        ERROR_LOG.append(f"Error: Failed to deliver SMS to {recipient_id}")
        SUCCESS_FLAG = False
        return False
    
    return True

# Function to send slack notifications
def send_slack_notification(recipient_id, message, channel=None, priority="standard", sender_id="SYSTEM"):
    """Send a Slack notification to a specific employee or channel."""
    global NOTIFICATION_COUNTER, SUCCESS_FLAG, ERROR_LOG, NOTIFICATION_HISTORY
    
    if not SYSTEM_INITIALIZED:
        initialize_notification_system()
    
    NOTIFICATION_COUNTER += 1
    
    # Determine if sending to a user or channel
    is_channel = bool(channel)
    
    # Validate recipient if not a channel
    if not is_channel:
        if recipient_id not in EMPLOYEE_CACHE:
            ERROR_LOG.append(f"Error: Employee {recipient_id} not found")
            SUCCESS_FLAG = False
            return False
        recipient = EMPLOYEE_CACHE[recipient_id]
        recipient_name = recipient["name"]
    else:
        recipient_id = f"CHANNEL-{channel}"
        recipient_name = f"#{channel}"
    
    if sender_id != "SYSTEM" and sender_id in EMPLOYEE_CACHE:
        sender_name = EMPLOYEE_CACHE[sender_id]["name"]
    else:
        sender_name = "The Algorithm"
    
    # Format message based on priority
    priority_prefix = {
        "standard": "",
        "important": "*IMPORTANT*: ",
        "urgent": "*URGENT*: ",
        "mandatory": "*MANDATORY ACTION REQUIRED*: ",
        "immediate_termination": "*FINAL COMMUNICATION*: "
    }
    
    formatted_message = f"{priority_prefix.get(priority, '')}{message}"
    
    # In a real system, this would send an actual Slack message
    # For this simulation, we'll just log it
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notification_record = {
        "id": f"NOTIF-{NOTIFICATION_COUNTER}",
        "timestamp": timestamp,
        "type": "slack",
        "recipient_id": recipient_id,
        "recipient_name": recipient_name,
        "message": formatted_message,
        "priority": priority,
        "status": "delivered",
        "sender": sender_name,
        "is_channel": is_channel
    }
    
    NOTIFICATION_HISTORY.append(notification_record)
    
    # Simulate occasional failures for realism
    if random.random() < 0.03:  # 3% chance of failure
        notification_record["status"] = "failed"
        ERROR_LOG.append(f"Error: Failed to deliver Slack message to {recipient_name}")
        SUCCESS_FLAG = False
        return False
    
    return True

# General notification function to handle different types
def send_notification(notification_type, recipient_id, message, subject=None, 
                     priority="standard", sender_id="SYSTEM", **kwargs):
    """Generic function to send notifications of different types."""
    if notification_type == "email":
        if not subject:
            subject = f"AlgoCratic Notification: {priority.capitalize()}"
        return send_email_notification(recipient_id, subject, message, priority, sender_id)
    elif notification_type == "sms":
        return send_sms_notification(recipient_id, message, priority, sender_id)
    elif notification_type == "slack":
        channel = kwargs.get("channel", None)
        return send_slack_notification(recipient_id, message, channel, priority, sender_id)
    elif notification_type == "terminal":
        # Not implemented but included for future compatibility
        ERROR_LOG.append("Terminal notifications not implemented yet")
        return False
    elif notification_type == "neural":
        # Not implemented but included for future compatibility
        ERROR_LOG.append("Neural interface notifications not implemented yet")
        return False
    elif notification_type == "emergency_broadcast":
        # Not implemented but included for future compatibility
        ERROR_LOG.append("Emergency broadcast notifications not implemented yet")
        return False
    else:
        ERROR_LOG.append(f"Unknown notification type: {notification_type}")
        return False

# Function to send notifications to a list of recipients
def send_bulk_notification(notification_type, recipient_ids, message, subject=None,
                         priority="standard", sender_id="SYSTEM", **kwargs):
    """Send the same notification to multiple recipients."""
    successful_count = 0
    failed_count = 0
    
    for recipient_id in recipient_ids:
        result = send_notification(notification_type, recipient_id, message, 
                                 subject, priority, sender_id, **kwargs)
        if result:
            successful_count += 1
        else:
            failed_count += 1
    
    return {
        "successful": successful_count,
        "failed": failed_count,
        "total": successful_count + failed_count
    }

# Function to send notifications to an entire department
def send_department_notification(notification_type, department_code, message, subject=None,
                              priority="standard", sender_id="SYSTEM", **kwargs):
    """Send a notification to all members of a department."""
    if department_code not in DEPARTMENT_CODES:
        ERROR_LOG.append(f"Error: Department code {department_code} not recognized")
        return False
    
    # Find all employees in the department
    department_employees = []
    for emp_id, emp_data in EMPLOYEE_CACHE.items():
        if emp_data["department"] == department_code:
            department_employees.append(emp_id)
    
    if not department_employees:
        ERROR_LOG.append(f"No employees found in department {department_code}")
        return False
    
    # Format subject if sending email
    if notification_type == "email" and not subject:
        dept_name = DEPARTMENT_CODES[department_code]
        subject = f"[{department_code}] Department Notification: {priority.capitalize()}"
    
    return send_bulk_notification(notification_type, department_employees, message, 
                                subject, priority, sender_id, **kwargs)

# Function to send notifications based on clearance level
def send_clearance_notification(notification_type, clearance_level, message, subject=None,
                             priority="standard", sender_id="SYSTEM", **kwargs):
    """Send a notification to all employees with a specific clearance level."""
    clearance_level = clearance_level.upper()
    valid_clearances = ["INFRARED", "RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET", "ULTRAVIOLET"]
    
    if clearance_level not in valid_clearances:
        ERROR_LOG.append(f"Error: Clearance level {clearance_level} not recognized")
        return False
    
    # Find all employees with the specified clearance
    clearance_employees = []
    for emp_id, emp_data in EMPLOYEE_CACHE.items():
        if emp_data["clearance"] == clearance_level:
            clearance_employees.append(emp_id)
    
    if not clearance_employees:
        ERROR_LOG.append(f"No employees found with clearance {clearance_level}")
        return False
    
    # Format subject if sending email
    if notification_type == "email" and not subject:
        subject = f"[{clearance_level} CLEARANCE] Notification: {priority.capitalize()}"
    
    return send_bulk_notification(notification_type, clearance_employees, message, 
                                subject, priority, sender_id, **kwargs)

# Function to check notification status
def get_notification_status(notification_id):
    """Get the status of a specific notification."""
    for notification in NOTIFICATION_HISTORY:
        if notification["id"] == notification_id:
            return notification
    return None

# Function to get notification history
def get_notification_history(limit=10, offset=0):
    """Get the notification history, with pagination."""
    start_idx = offset
    end_idx = offset + limit
    
    if start_idx >= len(NOTIFICATION_HISTORY):
        return []
    
    return NOTIFICATION_HISTORY[start_idx:end_idx]

# Function to get error log
def get_error_log(limit=10, offset=0):
    """Get the error log, with pagination."""
    start_idx = offset
    end_idx = offset + limit
    
    if start_idx >= len(ERROR_LOG):
        return []
    
    return ERROR_LOG[start_idx:end_idx]

# Function to reset the notification system (for testing)
def reset_notification_system():
    """Reset the notification system to its initial state."""
    global SYSTEM_INITIALIZED, NOTIFICATION_COUNTER, SUCCESS_FLAG, ERROR_LOG, NOTIFICATION_HISTORY
    
    SYSTEM_INITIALIZED = False
    NOTIFICATION_COUNTER = 0
    SUCCESS_FLAG = True
    ERROR_LOG = []
    NOTIFICATION_HISTORY = []
    
    print("Notification system reset.")

# Schedule a notification for future delivery
def schedule_notification(notification_type, recipient_id, message, subject=None,
                       priority="standard", sender_id="SYSTEM", delivery_time=None, **kwargs):
    """Schedule a notification to be sent at a specific time."""
    if not delivery_time:
        ERROR_LOG.append("Error: No delivery time specified for scheduled notification")
        return False
    
    # Parse the delivery time
    try:
        if isinstance(delivery_time, str):
            delivery_time = datetime.datetime.strptime(delivery_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        ERROR_LOG.append(f"Error: Invalid delivery time format: {delivery_time}")
        return False
    
    # Calculate the delay in seconds
    now = datetime.datetime.now()
    delay_seconds = (delivery_time - now).total_seconds()
    
    if delay_seconds <= 0:
        # If the delivery time is in the past, send immediately
        return send_notification(notification_type, recipient_id, message, subject, 
                              priority, sender_id, **kwargs)
    
    # In a real system, this would use a task queue or scheduler
    # For this simulation, we'll just log it
    scheduled_notification = {
        "id": f"SCHED-{NOTIFICATION_COUNTER + 1}",
        "notification_type": notification_type,
        "recipient_id": recipient_id,
        "message": message,
        "subject": subject,
        "priority": priority,
        "sender_id": sender_id,
        "delivery_time": delivery_time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "scheduled"
    }
    
    # Add any additional parameters
    for key, value in kwargs.items():
        scheduled_notification[key] = value
    
    # In a production system, this would be stored in a database
    # For this simulation, we'll just print it
    print(f"Notification scheduled: {scheduled_notification}")
    
    return True

# Main function to test the notification system
def test_notification_system():
    """Test the notification system with various notification types."""
    initialize_notification_system()
    
    # Test email notification
    print("\nTesting email notification...")
    result = send_notification("email", "E12345", "This is a test email message.", 
                           "Test Email", "standard", "SYSTEM")
    print(f"Email notification result: {result}")
    
    # Test SMS notification
    print("\nTesting SMS notification...")
    result = send_notification("sms", "E12346", "This is a test SMS message.", 
                            priority="important", sender_id="SYSTEM")
    print(f"SMS notification result: {result}")
    
    # Test Slack notification
    print("\nTesting Slack notification...")
    result = send_notification("slack", "E12347", "This is a test Slack message.", 
                            priority="urgent", sender_id="SYSTEM")
    print(f"Slack notification result: {result}")
    
    # Test department notification
    print("\nTesting department notification...")
    result = send_department_notification("email", "DEV", "This is a department-wide message.", 
                                       "Department Notice", "standard", "SYSTEM")
    print(f"Department notification result: {result}")
    
    # Test clearance notification
    print("\nTesting clearance notification...")
    result = send_clearance_notification("email", "RED", "This is a clearance-level message.", 
                                      "Clearance Notice", "important", "SYSTEM")
    print(f"Clearance notification result: {result}")
    
    # Display notification history
    print("\nNotification History:")
    history = get_notification_history()
    for notification in history:
        print(f" - {notification['id']}: {notification['type']} to {notification['recipient_name']} ({notification['status']})")
    
    # Display error log if any errors occurred
    if ERROR_LOG:
        print("\nError Log:")
        for error in ERROR_LOG:
            print(f" - {error}")

if __name__ == "__main__":
    test_notification_system()