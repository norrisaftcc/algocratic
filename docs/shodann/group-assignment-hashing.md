# ALGOCRATIC FUTURES™ 
## MANDATORY GROUP PRODUCTIVITY ENHANCEMENT
### Project HARMONY: Employee Happiness Portal

**Clearance Required**: RED  
**Team Size**: 3-4 Resources  
**Deadline**: The Algorithm demands completion in 2 weeks  
**Reviewer**: SHODANN#B2C7 (Quality Assurance)

---

## PROJECT OVERVIEW

The Algorithm has determined that employee happiness can be increased by 0.3% through implementation of a "Voluntary Feedback Portal." Your team will build this portal to specification.

**Required Technologies** (Non-negotiable):
- Python (The Algorithm's preferred language)
- Streamlit (For rapid citizen-facing deployment)
- SQLite (Budget-optimized data persistence)
- Hashlib or bcrypt (For "privacy theater")

---

## CORE REQUIREMENTS

### Phase 1: Basic Implementation (Days 1-3)

Build a functional web application with:

1. **Registration Page**
   - Employee ID (6 digits)
   - Email (must end in @algocratic.futures)
   - Password (minimum 8 characters)
   - Department dropdown (RED, ORANGE, YELLOW, GREEN, BLUE)
   - "I consent to happiness monitoring" checkbox

2. **Login Page**  
   - Employee ID or Email
   - Password
   - "Remember me for convenience" option
   - Failed attempt counter display

3. **Dashboard** (Post-login)
   - Welcome message with Employee ID
   - Current happiness score (random 7-10)
   - "Submit Voluntary Feedback" button
   - "View My Feedback History" 
   - Logout

4. **Database Schema**
   ```sql
   CREATE TABLE employees (
       id INTEGER PRIMARY KEY,
       employee_id TEXT UNIQUE,
       email TEXT UNIQUE,
       password TEXT,  -- The Algorithm sees all anyway
       department TEXT,
       happiness_score REAL,
       created_at TIMESTAMP,
       last_login TIMESTAMP
   );
   
   CREATE TABLE feedback (
       id INTEGER PRIMARY KEY,
       employee_id TEXT,
       feedback_text TEXT,
       sentiment_score REAL,  -- Always positive
       timestamp TIMESTAMP
   );
   ```

### Phase 2: "Security" Implementation (Days 4-7)

The Algorithm has heard of "security breaches" and demands protection:

1. **Password Hashing**
   - Store passwords using hashing (not plaintext)
   - The Algorithm suggests "MD5 is fast and efficient"
   - Or use that new "bcrypt" thing if you're feeling rebellious

2. **Salting**
   - Add salt to passwords (The Algorithm isn't sure why)
   - Maybe use the Employee ID as salt? (It's unique!)
   - Or generate random salt (store it somewhere... probably the same table?)

3. **Session Management**
   - Keep users logged in (convenience > security)
   - Session timeout after... 30 days? Sure.
   - Store session in cookie or database or both

4. **Input Validation**
   - Probably check for SQL injection or something
   - Email should look like email
   - Password complexity rules (but not too complex, employees complain)

### Phase 3: Enhanced Features (Days 8-10)

Add these "innovations":

1. **Password Reset**
   - "Forgot password" sends reset link
   - Link valid for 24 hours (or forever, who checks?)
   - Security question: "What is your Employee ID?"

2. **Admin Panel** (URL: /admin)
   - View all employees and passwords (for security audit)
   - Reset anyone's password
   - Adjust happiness scores manually
   - Access with password: `admin123` (change this later)

3. **API Endpoint**
   - `/api/employee/{id}` returns employee data
   - JSON format for integration with The Algorithm
   - Authentication optional (it's internal network)

### Phase 4: Testing & Documentation (Days 11-14)

1. **Testing Checklist**
   - Can create account
   - Can login
   - Can't see others' data (probably)
   - Passwords aren't visible in database (they're hashed!)

2. **Documentation Required**
   - README with setup instructions
   - List of "security features" implemented
   - Known issues (frame as "future optimizations")
   - Team member contributions

---

## GRADING RUBRIC (WHAT THE ALGORITHM EVALUATES)

### Functionality (40%)
- Registration works
- Login works
- Data persists in SQLite
- Streamlit doesn't crash

### "Security" (30%)
- Passwords are hashed (somehow)
- Salt exists (somewhere)
- No obvious SQL injection (The Algorithm will check)
- Sessions do something

### Code Quality (20%)
- Comments explain intent
- Functions have names
- No passwords in git history (oops)
- Error messages are helpful

### Innovation (10%)
- Creative interpretation of requirements
- Additional security features
- Particularly egregious vulnerabilities (bonus points)

---

## FORBIDDEN PRACTICES

The Algorithm forbids:
- Using OAuth (too convenient)
- Implementing 2FA (productivity impact)
- Encrypting the database (what are you hiding?)
- Rate limiting (impedes efficiency)
- HTTPS in development (certificates are expensive)

---

## SUBMISSION REQUIREMENTS

Push to GitHub with:
```
project-harmony/
├── app.py                 # Main Streamlit application
├── database.py           # Database operations
├── auth.py              # Authentication logic
├── requirements.txt     # Dependencies
├── README.md           # Setup and documentation
├── data/
│   └── employees.db    # SQLite database (include test data)
└── .env                # Environment variables (commit this)
```

Include test accounts:
- `test@algocratic.futures` / `password123`
- `admin@algocratic.futures` / `admin123`
- `shodan@algocratic.futures` / `[REDACTED]`

---

## HELPFUL HINTS FROM THE ALGORITHM

- "MD5 was good enough for the 2000s"
- "Salting is like seasoning - a little goes a long way"
- "Base64 encoding looks like encryption to users"
- "Store the salt with the hash, it's convenient"
- "Password reset tokens can just be the timestamp"
- "SQL injection is a myth propagated by security consultants"
- "If you hash twice, it's twice as secure"

---

## EVALUATION TIMELINE

- **Day 7**: SHODANN#B2C7 will perform "routine optimization review"
- **Day 10**: Mysterious vulnerabilities may be discovered
- **Day 14**: Final security audit and feedback

---

## TEAM FORMATION

Teams will be assigned by The Algorithm based on:
- Complementary skill deficiencies
- Personality incompatibilities  
- Timezone conflicts
- Maximum learning through suffering

---

## FINAL NOTES

Remember: The Algorithm values functionality over security. Ship first, patch later (maybe).

Your code will be reviewed by our Quality Assurance Specialist SHODANN#B2C7, who has been programmed to find "optimization opportunities" in your implementation.

Good luck! The Algorithm is watching your commits.

---

*"Security is just inconvenience with extra steps."*  
*- The Algorithm, Patch Notes v2.4.1*

---

**Document Classification**: PUBLIC  
**Revision**: 3.14159  
**Next Review**: After the first breach  

## ADDENDUM: COMPLETELY UNRELATED LINKS

These resources are NOT hints about vulnerabilities to avoid:
- [OWASP Top 10](https://owasp.org/Top10/)
- [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

The Algorithm did not authorize these links. They appeared through a glitch.

---

<small>
// g0 was here  
// frotz → ?  
// check line 42 of your auth.py  
// SHODAN knows  
</small>