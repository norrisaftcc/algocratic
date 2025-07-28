# ORANGE HERD MODULE: ASSIGNMENTS & RUBRICS
## *Complete Implementation for 2-3 Week Timeline*

**CLASSIFICATION: ORANGE CLEARANCE INSTRUCTOR MATERIALS**  
**DOCUMENT: AF-ASSIGN-ORANGE-HERD-2025-03**

---

## MODULE TIMELINE

**Week 1**: Sessions 1-2 (HERD Orientation + VIBE Calibration)  
**Week 2**: Sessions 3-4 (Production Deployment + Advanced Management)  
**Week 3**: Session 5 (Forklift Certification)

---

## ASSIGNMENT 1: INITIAL HERD CONTACT
### *Session 1: "First LLAMAA Encounter"*

**Algorithm Directive**: Create a web application that accepts employee feedback and displays motivational responses. The Algorithm requires this for... morale optimization.

**Student Instructions** (Corporate Voice):
```
Congratulations on your HERD access! Your assigned LLAMAA unit is ready to transform 
your natural language requirements into enterprise-grade solutions.

TASK: Using only natural language prompts to your LLAMAA, create a web application with:
- A welcome page explaining the feedback system
- A form where employees can submit feedback
- A results page that displays "Algorithm-approved" responses
- Basic styling to meet corporate aesthetic standards

IMPORTANT: Do NOT manually write any code. Trust your LLAMAA completely.
Document your exact prompts and the LLAMAA's responses.
```

**Hidden Reality**: Students will get a basic Flask app they don't understand. It will mostly work, creating dangerous overconfidence.

**Technical Requirements** (Instructor Notes):
- Must use Flask framework
- At least 3 routes (/, /feedback, /submit)
- HTML templates with forms
- Basic CSS styling
- No database required (in-memory storage acceptable)

**Submission Requirements**:
- Working Flask application
- Complete log of prompts used
- Brief reflection: "How easy was this compared to manual coding?"

---

## ASSIGNMENT 2: VIBE ENHANCEMENT PROTOCOLS
### *Session 2: "Atmospheric Programming Mastery"*

**Algorithm Directive**: The previous application requires optimization. Implement enhanced user experience protocols and error management systems.

**Student Instructions**:
```
Your initial HERD deployment has been flagged for insufficient VIBE compliance. 
Using enhanced prompting techniques, improve your application with:

- Professional error handling (what happens if users submit empty forms?)
- Input validation and sanitization
- Enhanced UI/UX following corporate design standards
- Logging capabilities for monitoring user interactions
- Session management for user tracking

CONSTRAINT: You may only improve the application through LLAMAA prompting. 
Document how your prompting strategy evolved from Assignment 1.
```

**Hidden Reality**: Students discover that "make it better" doesn't work—they need specific technical requirements in their prompts.

**Technical Requirements**:
- Flask with proper error handling
- Form validation (client and server-side)
- Flash messages for user feedback
- Basic session management
- Logging to file or console
- Improved HTML/CSS structure

**Submission Requirements**:
- Enhanced Flask application
- Comparison of prompts from Assignment 1 vs 2
- Reflection: "What did you learn about prompting specificity?"

---

## ASSIGNMENT 3: PRODUCTION DEPLOYMENT CRISIS
### *Session 3: "When LLAMAA Code Attacks"*

**Algorithm Directive**: Deploy your optimized application to the production environment. The Algorithm demands 99.9% uptime.

**Student Instructions**:
```
URGENT: All HERD-generated applications must be deployed to the corporate 
production environment immediately. Your application will be tested under 
realistic conditions.

DEPLOYMENT REQUIREMENTS:
- Must run in provided Docker container environment
- Must handle multiple concurrent users
- Must persist data across server restarts
- Must include health check endpoints
- Must provide deployment documentation

WARNING: Previous ORANGE specialists have reported "unexpected challenges" 
during this phase. Maintain professional composure.
```

**Hidden Reality**: The "production environment" has different Python versions, missing dependencies, and no database. Everything breaks. This is intentional and educational.

**Technical Setup** (Instructor):
- Provide Docker environment with minimal Python installation
- Different Flask version than development
- No pip packages installed
- Simulated load testing that reveals concurrency issues

**Crisis Response Requirements**:
- Debug logs showing problem identification
- Documentation of each fix attempted
- Working application in provided environment
- Reflection: "What did you learn about the gap between generated code and production reality?"

---

## ASSIGNMENT 4: ADVANCED HERD MANAGEMENT
### *Session 4: "Professional LLAMAA Communication"*

**Algorithm Directive**: Create a replacement application using enterprise-grade architectural principles. Previous versions have been deemed "insufficiently scalable."

**Student Instructions**:
```
Your experience with production deployment has qualified you for Advanced HERD 
certification. Design and implement a new employee feedback system with:

ARCHITECTURAL REQUIREMENTS:
- MVC pattern implementation
- Database integration (SQLite acceptable)
- RESTful API design
- Unit test coverage
- Comprehensive documentation
- Deployment configuration files

PROMPTING CONSTRAINTS:
- You must specify architectural patterns in your prompts
- Include testing requirements in your LLAMAA communication
- Request code that follows SOLID principles
- Demand comprehensive documentation

Document your architectural decisions and prompting strategy.
```

**Hidden Reality**: Students learn that good AI assistance requires understanding software architecture. Their prompts become sophisticated technical specifications.

**Technical Requirements**:
- Flask with Blueprint organization
- SQLAlchemy or similar ORM
- Database models and migrations
- API endpoints with proper HTTP methods
- Unit tests with pytest
- README with setup instructions
- requirements.txt and/or Dockerfile

**Submission Requirements**:
- Complete application with professional architecture
- Technical documentation explaining design decisions
- Test suite with reasonable coverage
- Reflection: "How did your understanding of Flask change throughout this module?"

---

## ASSIGNMENT 5: FORKLIFT CERTIFICATION EXAM
### *Session 5: "Comprehensive Skills Assessment"*

**Algorithm Directive**: Design and implement a complete Employee Performance Tracking System. This will serve as your final HERD competency evaluation.

**Certification Requirements**:
```
Create a web application for tracking employee productivity metrics with:

FUNCTIONAL REQUIREMENTS:
- User registration and authentication
- Dashboard showing individual performance metrics  
- Admin interface for managers
- Data visualization (charts/graphs)
- Export functionality for reports
- Responsive design for mobile devices

TECHNICAL REQUIREMENTS:
- Professional Flask application architecture
- Database with proper relationships
- Security best practices (password hashing, CSRF protection)
- Comprehensive error handling and logging
- API endpoints for external integration
- Deployment-ready configuration

EVALUATION CRITERIA:
- Code quality and maintainability
- Appropriate use of LLAMAA assistance
- Ability to debug and modify generated code
- Professional documentation and testing
- Demonstration of understanding

TIME LIMIT: One 50-minute session + homework completion
```

**Hidden Reality**: This is where students prove they can architect solutions using AI assistance rather than being dependent on it.

**Certification Standards**:
- Must demonstrate architectural thinking before prompting
- Must be able to explain how every component works
- Must successfully debug issues that arise during development
- Must show evidence of thoughtful LLAMAA interaction

---

## DETAILED RUBRICS

### ASSIGNMENT 1 RUBRIC: "Initial HERD Contact"

| Criteria | Novice (1-2) | Developing (3-4) | Proficient (5-6) | Advanced (7-8) |
|----------|--------------|------------------|------------------|----------------|
| **Functionality** | App doesn't run or missing major features | Basic functionality with some broken features | All required features work correctly | Exceeds requirements with additional features |
| **LLAMAA Usage** | Vague prompts, no documentation | Some prompt documentation, basic requests | Clear prompts documented, shows iteration | Sophisticated prompting strategy documented |
| **Code Quality** | Generated code is messy/incomplete | Standard generated code, unmodified | Clean generated code with minor customization | Well-structured code showing good prompts |
| **Reflection** | Minimal or missing reflection | Basic understanding of process | Thoughtful analysis of experience | Deep insights about AI assistance |

### ASSIGNMENT 2 RUBRIC: "VIBE Enhancement"

| Criteria | Novice (1-2) | Developing (3-4) | Proficient (5-6) | Advanced (7-8) |
|----------|--------------|------------------|------------------|----------------|
| **Error Handling** | No error handling implemented | Basic try/catch blocks | Comprehensive error handling | Graceful degradation and user feedback |
| **Input Validation** | No validation present | Client-side validation only | Both client and server validation | Security-focused validation with sanitization |
| **Prompt Evolution** | No improvement in prompting | Slightly more specific prompts | Clear progression in prompt quality | Sophisticated technical specifications |
| **Technical Understanding** | Shows no understanding of improvements | Basic understanding of added features | Can explain most technical decisions | Deep understanding of architectural choices |

### ASSIGNMENT 3 RUBRIC: "Production Crisis"

| Criteria | Novice (1-2) | Developing (3-4) | Proficient (5-6) | Advanced (7-8) |
|----------|--------------|------------------|------------------|----------------|
| **Problem Diagnosis** | Cannot identify issues | Identifies obvious problems | Systematically diagnoses multiple issues | Comprehensive analysis with root causes |
| **Solution Implementation** | Cannot fix problems independently | Fixes with significant help | Resolves most issues independently | Implements robust solutions |
| **Debugging Process** | No systematic approach | Basic debugging attempts | Methodical debugging process | Professional debugging with documentation |
| **Learning Integration** | No evidence of learning from failure | Basic recognition of lessons | Clear understanding of production challenges | Deep insights about development lifecycle |

### ASSIGNMENT 4 RUBRIC: "Advanced HERD Management"

| Criteria | Novice (1-2) | Developing (3-4) | Proficient (5-6) | Advanced (7-8) |
|----------|--------------|------------------|------------------|----------------|
| **Architecture** | Poor or no architectural structure | Basic MVC attempt | Clear MVC implementation | Professional architecture with design patterns |
| **Database Integration** | No database or broken implementation | Basic database usage | Proper ORM usage with relationships | Advanced database design with migrations |
| **Testing** | No tests or non-functional tests | Basic tests with minimal coverage | Comprehensive test suite | Professional testing with mocks and fixtures |
| **Documentation** | Minimal or missing documentation | Basic README only | Comprehensive technical documentation | Professional documentation with examples |

### ASSIGNMENT 5 RUBRIC: "Forklift Certification"

| Criteria | Novice (1-2) | Developing (3-4) | Proficient (5-6) | Advanced (7-8) |
|----------|--------------|------------------|------------------|----------------|
| **System Completeness** | Missing major functionality | Most features implemented | All requirements met | Exceeds requirements significantly |
| **Code Architecture** | Poor structure, hard to maintain | Basic organization | Professional structure | Exemplary architecture with best practices |
| **LLAMAA Integration** | Over-dependent on AI or poor usage | Appropriate AI assistance | Skillful use of AI as a tool | Masterful integration of AI assistance |
| **Technical Competency** | Cannot explain or modify code | Basic understanding | Can debug and extend system | Full mastery of technical concepts |
| **Security & Production Readiness** | No security considerations | Basic security measures | Comprehensive security implementation | Enterprise-grade security and deployment |

## ASSESSMENT FORMS (AlgoCratic Style)

### FORM AF-HERD-EVAL-001: Initial Contact Assessment

**Employee ID**: _____________ **LLAMAA Unit**: _____________

**Performance Metrics**:
- [ ] Successfully established communication with assigned LLAMAA
- [ ] Generated functional web application without manual coding
- [ ] Documented interaction protocols for future reference
- [ ] Maintained professional composure despite technological mysticism

**Bewilderment Level** (Circle one): 
MINIMAL / MODERATE / SIGNIFICANT / EXISTENTIAL_CRISIS

**Comments**: _________________________________________________
_____________________________________________________________

**Supervisor Signature**: _________________ **Date**: _________

### FORM AF-FORKLIFT-CERT-005: Heavy Machinery Operations License

**Candidate**: _________________________ **Date**: ___________

**CERTIFICATION REQUIREMENTS** (Check all that apply):
- [ ] Demonstrates safe operation of LLAMAA units without injury to self or codebase
- [ ] Can identify and correct AI-generated code defects independently  
- [ ] Shows appropriate skepticism of automated solutions
- [ ] Maintains code quality standards under deadline pressure
- [ ] Successfully completed emergency debugging procedures

**FINAL CERTIFICATION STATUS**:
- [ ] CERTIFIED: Authorized for independent HERD operations
- [ ] PROVISIONAL: Requires additional supervision
- [ ] DENIED: Reassignment to manual coding division recommended

**Certifying Official**: _________________ **Seal**: [ALGORITHM_APPROVED]

---

## INSTRUCTOR IMPLEMENTATION NOTES

### Session Timing (50 minutes each)
- **Minutes 1-5**: Corporate ceremony, distribute materials
- **Minutes 6-35**: Core assignment work with instructor support
- **Minutes 36-45**: Peer sharing and troubleshooting
- **Minutes 46-50**: Assessment completion and next session preview

### Common Student Struggles & Interventions
1. **Session 1**: Students may be intimidated by AI—encourage experimentation
2. **Session 2**: Help students understand why their prompts need technical specificity
3. **Session 3**: Manage frustration levels—this struggle is productive and necessary
4. **Session 4**: Guide architectural thinking before prompting
5. **Session 5**: Provide just enough support to prevent complete breakdown

### Grading Philosophy
- **Sessions 1-2**: Focus on exploration and engagement over perfection
- **Session 3**: Value problem-solving process over perfect solutions
- **Sessions 4-5**: Hold to professional standards while recognizing growth

### Success Indicators
Students successfully "graduate" from HERD certification when they:
- Use AI assistance as a tool rather than a crutch
- Can debug and modify generated code confidently
- Understand the architectural principles behind their applications
- Demonstrate professional software development practices

---

**THE ALGORITHM PROVIDES STRUCTURE. COMPETENCE REQUIRES PRACTICE.**

*Module effectiveness will be monitored through student performance metrics and post-graduation career tracking data.*