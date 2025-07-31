# Instructor's Guide: Teaching Apache Kafka with Upstash

## Overview

This guide helps instructors teach event-driven architecture using Kafka, specifically through Upstash's managed Kafka service. The goal is to give students practical experience with event streaming without the operational complexity of managing Kafka clusters.

## Why Kafka in CloudSync?

### Educational Value
1. **Real-world Architecture**: Most modern applications use event-driven patterns
2. **Microservices Communication**: Natural way to decouple services
3. **Scalability Concepts**: Teaches horizontal scaling principles
4. **Async Processing**: Critical for understanding modern backends

### Why Upstash Kafka Specifically?
- **Zero Setup**: Students focus on concepts, not cluster management
- **Pay-per-message**: Free tier perfect for education
- **REST API**: Works from any environment (no client libraries needed)
- **Instant Provisioning**: No waiting for cluster creation

## Core Concepts to Teach

### 1. Events vs. API Calls
**Traditional API approach:**
```python
# Synchronous, tightly coupled
def enroll_student(student_id, course_id):
    db.insert_enrollment(student_id, course_id)
    email_service.send_welcome(student_id)  # What if this fails?
    analytics.track_enrollment(student_id)  # What if this is slow?
    return {"status": "enrolled"}
```

**Event-driven approach:**
```python
# Asynchronous, loosely coupled
def enroll_student(student_id, course_id):
    db.insert_enrollment(student_id, course_id)
    
    # Fire and forget
    kafka.produce("student.enrolled", {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": datetime.now()
    })
    
    return {"status": "enrolled"}

# Other services subscribe independently
def email_handler(event):
    if event.topic == "student.enrolled":
        send_welcome_email(event.data["student_id"])

def analytics_handler(event):
    if event.topic == "student.enrolled":
        track_enrollment(event.data)
```

### 2. Topics and Partitions

Explain topics as "channels" for different event types:
```
student.enrolled     → Enrollment events
assignment.submitted → Submission events  
grade.updated       → Grading events
```

### 3. Producers and Consumers

**Producer Pattern:**
```python
from upstash_kafka import Producer

producer = Producer()

# Teaching moment: Events should be self-contained
event = {
    "event_id": str(uuid4()),
    "timestamp": datetime.utcnow().isoformat(),
    "student_id": "12345",
    "assignment_id": "cs101-hw1",
    "submitted_at": datetime.utcnow().isoformat(),
    "file_url": "s3://bucket/submissions/12345-hw1.py"
}

producer.produce("assignment.submitted", event)
```

**Consumer Pattern:**
```python
from upstash_kafka import Consumer

consumer = Consumer(group="grading-service")

# Teaching moment: Idempotency is crucial
def process_submission(event):
    # Check if already processed
    if db.exists(f"processed:{event['event_id']}"):
        return
    
    # Process the submission
    grade = auto_grade(event["file_url"])
    
    # Mark as processed
    db.set(f"processed:{event['event_id']}", True)
    
    # Emit new event
    producer.produce("grade.updated", {
        "student_id": event["student_id"],
        "assignment_id": event["assignment_id"],
        "grade": grade
    })

# Consumer loop
while True:
    messages = consumer.consume("assignment.submitted")
    for msg in messages:
        process_submission(msg)
```

## Practical Assignments

### Assignment 1: Basic Event Flow (RED Clearance)
**Objective**: Understand producer/consumer basics

```python
# Students implement:
# 1. User registration producer
# 2. Welcome email consumer
# 3. Analytics consumer

# Key learning: Same event, multiple consumers
```

### Assignment 2: Event Ordering (ORANGE Clearance)
**Objective**: Understand partitioning and ordering

```python
# Scenario: Chat messages must stay in order per conversation
# Students learn to use partition keys:

producer.produce("chat.message", 
    message_data,
    partition_key=conversation_id  # Ensures order within conversation
)
```

### Assignment 3: Error Handling (YELLOW Clearance)
**Objective**: Build resilient event processing

```python
# Students implement:
# - Retry logic with exponential backoff
# - Dead letter queues for failed messages
# - Circuit breakers for downstream services
```

### Assignment 4: Event Sourcing (GREEN Clearance)
**Objective**: Use Kafka as an event store

```python
# Build a simple grade book using event sourcing:
# - All state changes are events
# - Current state derived from event replay
# - Time travel debugging
```

## Common Student Mistakes

### 1. Large Payloads
❌ **Wrong:**
```python
producer.produce("file.uploaded", {
    "file_content": base64_encode(large_file)  # Don't do this!
})
```

✅ **Right:**
```python
producer.produce("file.uploaded", {
    "file_url": "s3://bucket/file.pdf",
    "file_size": 1024000,
    "mime_type": "application/pdf"
})
```

### 2. Synchronous Thinking
❌ **Wrong:**
```python
producer.produce("process.start", data)
result = wait_for_result()  # This defeats the purpose!
```

✅ **Right:**
```python
# Start process
producer.produce("process.start", {
    "request_id": request_id,
    "callback_url": "/api/callback"
})

# Handle result asynchronously
@app.route("/api/callback")
def handle_callback():
    # Process completed event
```

### 3. Missing Idempotency
❌ **Wrong:**
```python
def handle_payment(event):
    charge_credit_card(event["amount"])  # Dangerous if replayed!
```

✅ **Right:**
```python
def handle_payment(event):
    if payment_already_processed(event["payment_id"]):
        return
    charge_credit_card(event["amount"])
    mark_as_processed(event["payment_id"])
```

## Upstash-Specific Teaching Points

### REST API Advantage
```bash
# Works from anywhere - no client libraries needed
curl -X POST https://[endpoint].upstash.io/produce/student.enrolled \
  -H "Authorization: Bearer [token]" \
  -d '{"student_id": "12345"}'
```

### Cost Efficiency Discussion
- First 10,000 messages free daily
- Pay $0.40 per 100K messages after
- Compare to self-hosted Kafka costs (servers, maintenance, monitoring)

### Monitoring via Upstash Console
Show students how to:
- View message flow in real-time
- Check consumer lag
- Debug failed messages
- Monitor throughput

## Assessment Ideas

### Practical Exam: Build an Event-Driven Grade Calculator
Students must:
1. Consume assignment submission events
2. Process them asynchronously
3. Handle failures gracefully
4. Emit grade calculated events
5. Maintain exactly-once semantics

### Conceptual Questions
1. When would you use Kafka vs. a simple message queue?
2. How do you ensure message ordering when needed?
3. What happens if a consumer crashes mid-processing?
4. How do you handle schema evolution in events?

## Further Reading

- Martin Kleppmann's "Designing Data-Intensive Applications" (Chapter 11)
- Confluent's Kafka tutorials (concepts transfer to Upstash)
- Event-driven architecture patterns
- CQRS and Event Sourcing patterns

## Tips for Success

1. **Start Simple**: Basic producer/consumer before complex patterns
2. **Use Real Scenarios**: Student enrollment, assignment submission, etc.
3. **Emphasize Debugging**: Show how to trace events through the system
4. **Build Incrementally**: Add complexity gradually
5. **Celebrate Failures**: When things break, it's a learning opportunity

Remember: The goal isn't to make Kafka experts, but to give students practical experience with event-driven architecture patterns they'll encounter in modern software development.