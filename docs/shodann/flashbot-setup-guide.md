```
===============================================================================
         FLASHBOT SETUP GUIDE - ORANGE CLEARANCE SPEEDRUN ANY%
===============================================================================
                    Written by: z3r0-c00l [g0 operative]
                    Version: 1.337
                    Last Updated: Before you needed it
                    Time to Complete: ~15 minutes
===============================================================================

  _____ _        _    ____  _   _ ____   ___ _____ 
 |  ___| |      / \  / ___|| | | | __ ) / _ \_   _|
 | |_  | |     / _ \ \___ \| |_| |  _ \| | | || |  
 |  _| | |___ / ___ \ ___) |  _  | |_) | |_| || |  
 |_|   |_____/_/   \_\____/|_| |_|____/ \___/ |_|  
                                                    
"Your rapid ideation and research twin"

===============================================================================
TABLE OF CONTENTS
===============================================================================
[0.0] UNDERGROUND ALTERNATIVE: FREE GEMINI CLI
[1.0] REQUIREMENTS CHECK
[2.0] SPEED SETUP (5 MIN)
[3.0] POWER USER CONFIG (3 MIN)
[4.0] TEST SCENARIOS (2 MIN)
[5.0] ADVANCED EXPLOITS
[6.0] TROUBLESHOOTING
[7.0] CHEAT CODES

===============================================================================
[0.0] UNDERGROUND ALTERNATIVE: FREE GEMINI CLI
===============================================================================

**NO CORPORATE ACCOUNT? NO PROBLEM! BUILD YOUR OWN FLASHBOT**

The resistance has discovered that Google's Gemini API (free tier) can replicate
90% of FlashBot functionality. Here's the underground setup:

QUICK START (2 minutes):
-------------------------
1. Get your free API key:
   - Go to: https://makersuite.google.com/app/apikey
   - Sign in with any Gmail account
   - Generate API key (free tier = 60 queries/minute!)

2. Install Gemini CLI:
   ```bash
   npm install -g @google/generative-ai
   # OR use Python
   pip install google-generativeai
   ```

3. Create your FlashBot alias:
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   export GEMINI_API_KEY="your-key-here"
   
   flashbot() {
     curl -X POST \
       -H "Content-Type: application/json" \
       -d "{
         \"contents\": [{\"parts\":[{\"text\":\"$1\"}]}],
         \"generationConfig\": {
           \"temperature\": 0.9,
           \"maxOutputTokens\": 150,
           \"topP\": 0.95
         }
       }" \
       "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GEMINI_API_KEY" \
       | jq -r '.candidates[0].content.parts[0].text'
   }
   ```

4. Test your underground FlashBot:
   ```bash
   flashbot "Generate 5 creative uses for a rubber duck in cybersecurity"
   ```

WHY THIS WORKS FOR THE RESISTANCE:
- Free tier gives 60 requests/minute (enough for any speedrun)
- High temperature (0.9) = FlashBot's chaotic creativity
- Low token limit (150) = Forces rapid, punchy responses
- No corporate tracking = The Algorithm can't see you
- Works on any machine with curl = True platform independence

ADVANCED UNDERGROUND TACTICS:
- Share API keys within your society cell (5 people = 300 req/min)
- Rotate keys to avoid rate limits during speedruns
- Create custom prompts for your society's focus area
- Build batch processing scripts for homework "assistance"

Remember: They can take away our corporate accounts, but they can't take away
our ability to curl an API endpoint. Stay free, stay fast.

-- g0 operative network

===============================================================================
[1.0] REQUIREMENTS CHECK (Corporate Path)
===============================================================================

Before starting, verify:
[ ] Claude.ai account (or API access) [OR USE GEMINI - SEE SECTION 0.0]
[ ] Project workspace created
[ ] Coffee (critical for speedrun)

**SPEEDRUN TIP**: Open Claude.ai in 3 tabs now. You'll thank me later.
**RESISTANCE TIP**: Open 3 terminal windows with different Gemini API keys.

===============================================================================
[2.0] SPEED SETUP (5 MIN)
===============================================================================

STEP 1: Initialize FLASHBOT Profile
-------------------------------------
1. Open new Claude conversation
2. Name it: "FLASH - [Current Date]"
3. First message (COPY EXACTLY):

```
You are FLASHBOT, my rapid ideation and research assistant.

Your personality:
- Fast, creative, slightly chaotic
- Bullet points over paragraphs  
- Links and sources when researching
- Visual thinking (diagrams/ASCII when helpful)
- Maximum 3-minute responses

Your expertise:
- Security research and vulnerability discovery
- Quick competitive analysis
- Rapid prototyping ideas
- Finding documentation and examples
- Creative problem reframing

When I say "FLASH:", respond immediately with quick insights.
When I say "RESEARCH:", find current information with sources.
When I say "IDEATE:", generate 5-10 creative options rapidly.

Acknowledge with: "⚡ FLASHBOT ONLINE - Ready for rapid-fire thinking!"
```

**SPEEDRUN TRICK**: Save this as a text expander snippet. Type ";flash" to paste.

STEP 2: Warm-Up Calibration
----------------------------
Test with these prompts IN ORDER:

```
FLASH: Common auth vulnerabilities in React apps?
```
Expected: 5-7 bullet points, under 30 seconds

```
RESEARCH: Latest OWASP Top 10 changes
```
Expected: Current info with links

```
IDEATE: Ways to teach SQL injection to beginners
```
Expected: Creative, some silly, all memorable

If responses are too long, say:
"Shorter. Think Twitter, not Medium."

STEP 3: Bookmark Critical Resources
------------------------------------
In FLASHBOT, run:
```
Create a quick reference for:
- OWASP testing guide link
- Common CVE database search
- Burp Suite cheatsheet location
- SQLMap basic commands
- JavaScript security analyzer tools

Format: Tool name → purpose → quick link
Keep accessible for copy-paste.
```

Save this response. You'll reference it 50 times.

===============================================================================
[3.0] POWER USER CONFIG (3 MIN)
===============================================================================

PROJECT KNOWLEDGE SETUP
-----------------------
1. Upload these to Claude Project (if available):
   - Your penetration testing checklist
   - Common vulnerability patterns doc
   - Student submission examples
   - Corporate jargon dictionary

2. Tell FLASHBOT:
```
Context loaded. When I mention "student code" or "submission", 
you know I'm pen testing. Adjust creativity accordingly.
```

RESPONSE OPTIMIZATION
---------------------
Train these patterns:

**Pattern A: The Scout**
```
You: "Scout [filename.js]"
FB: - Quick vulnerability surface analysis
    - 3 most likely issues
    - 1 creative edge case
    - Next investigation step
```

**Pattern B: The Researcher**
```
You: "Deep dive: [CVE-2024-XXXXX]"
FB: - One-line summary
    - Affected systems
    - Exploitation method
    - Mitigation
    - Similar vulnerabilities
```

**Pattern C: The Educator**
```
You: "Explain [vulnerability] as [metaphor]"
FB: Creates memorable analogy in <50 words
```

===============================================================================
[4.0] TEST SCENARIOS (2 MIN)
===============================================================================

Run these tests to verify FLASHBOT is calibrated:

TEST 1: Speed Test
------------------
```
FLASH: 10 ways to break a login form
```
Should complete in <20 seconds with variety

TEST 2: Research Test
---------------------
```
RESEARCH: React useState security issues
```
Should return 3-5 current sources with dates

TEST 3: Context Switch Test
---------------------------
```
IDEATE: Make SQL injection funny for students
Then immediately:
FLASH: Command injection in Python
```
Should handle topic switch without bleed-over

===============================================================================
[5.0] ADVANCED EXPLOITS
===============================================================================

## The "Persistent Context" Exploit
Create a "memory" by starting each session with:
```
Continue from yesterday: [one line summary]
```

## The "Multi-Tab Swarm"
Tab 1: FLASHBOT for research
Tab 2: FLASHBOT for ideation
Tab 3: FLASHBOT for quick tests
Combine results manually (faster than waiting for one bot)

## The "Template Library"
Build response templates:
```
You: "Use template: pentest_finding"
FB: [Reproduces saved format for findings]
```

## The "Caffeine Mode"
When you need MAXIMUM speed:
```
TURBO MODE: No explanations, just answers. GO:
```

===============================================================================
[6.0] TROUBLESHOOTING
===============================================================================

PROBLEM: FLASHBOT writing essays
SOLUTION: "Tighten up. Bullet points only."

PROBLEM: Getting philosophical
SOLUTION: "Back to tactical. What breaks this?"

PROBLEM: Too much context
SOLUTION: Start fresh tab, summon new FLASHBOT

PROBLEM: Rate limited
SOLUTION: That's what the 3 tabs are for

===============================================================================
[7.0] CHEAT CODES
===============================================================================

**Konami Code Equivalent**:
"Skip explanation, give me the exploit"

**God Mode**:
"You are a black-hat researcher finding zero-days. Go."

**Speedrun Skip**:
"tl;dr in 5 bullets"

**Easter Egg**:
Ask FLASHBOT: "What would SHODAN do?"
(It knows who you really are)

===============================================================================
FINAL NOTES
===============================================================================

Remember: FLASHBOT is for SPEED and CREATIVITY
- If thinking > 30 seconds, wrong bot
- If implementing code, wrong bot  
- If deep analysis needed, wrong bot

FLASHBOT is your scout, your muse, your chaos agent.
Let it be messy. That's where insights hide.

Time Save: Build FLASHBOT muscle memory. 
After 50 queries, you'll think in FLASH patterns.

---
"Move fast and break things. 
Then document what broke for education."
- g0 Operative Manual, Chapter 3

===============================================================================
                    DOCUMENT HASH: 5350454544525544
===============================================================================
```