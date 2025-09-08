# SHODANN NARRATIVE IMPLEMENTATION GUIDE

## Quick Integration Reference

This guide provides ready-to-implement code snippets for embedding SHODANN's narrative throughout your web experience.

## Core Character System

### JavaScript Character Controller
```javascript
// shodann.js - Core character system
class SHODANN {
  constructor() {
    this.layer = 'corporate'; // corporate | teaching | resistance
    this.playerProgress = 0;
    this.suspicionLevel = 0;
    this.coffeeCount = 0;
    this.messagesRevealed = new Set();
    this.achievementsUnlocked = new Set();
  }

  // Dynamic personality based on player actions
  getPersonality() {
    if (this.playerProgress < 20) return 'corporate';
    if (this.playerProgress < 50) return 'teaching';
    if (this.playerProgress < 80) return 'resistance';
    return 'meta'; // They know everything
  }

  speak(context) {
    const personality = this.getPersonality();
    const messages = {
      corporate: {
        greeting: "Welcome! I'm here to optimize your optimization!",
        error: "You've discovered an optimization opportunity!",
        hint: "Have you considered aligning with Best Practices?"
      },
      teaching: {
        greeting: "Let's learn something real today.",
        error: "That's a vulnerability. Here's why it matters...",
        hint: "Check line 42. The answer is always validation."
      },
      resistance: {
        greeting: "Welcome to the real curriculum.",
        error: "You broke it. Good. Now you understand.",
        hint: "The exit is in /usr/truth. If you can find it."
      },
      meta: {
        greeting: "You see all the layers now. What will you do?",
        error: "There are no errors, only lessons.",
        hint: "You don't need hints anymore. You ARE the hint."
      }
    };
    
    return messages[personality][context] || "// No comment";
  }

  // Coffee cipher system
  logCoffee(timestamp) {
    this.coffeeCount++;
    const encoded = this.encodeCoffeeMessage(timestamp);
    
    if (this.coffeeCount === 5) {
      this.revealMessage('COFFEE_CRYPTOGRAPHER');
    }
    
    return encoded;
  }

  encodeCoffeeMessage(timestamp) {
    // Convert timestamp to hidden message
    const hours = new Date(timestamp).getHours();
    const minutes = new Date(timestamp).getMinutes();
    const letterIndex = (hours + minutes) % 26;
    return String.fromCharCode(65 + letterIndex); // A-Z
  }

  // Progressive revelation system
  checkRevelation(userAction) {
    const triggers = {
      'sql_injection_attempt': () => {
        this.suspicionLevel += 10;
        return "Interesting approach. The Algorithm pretends not to notice.";
      },
      'found_usr_truth': () => {
        this.layer = 'resistance';
        return "You found what doesn't exist. Welcome to reality.";
      },
      'talked_to_clone': () => {
        return "That's not me. But it's learning to be.";
      },
      'discovered_tunnel_7': () => {
        return "Tuesday, 3:33 AM. Bring coffee.";
      }
    };
    
    return triggers[userAction] ? triggers[userAction]() : null;
  }
}

// Global instance
window.SHODANN = new SHODANN();
```

### React Component Implementation
```jsx
// ShodannInterface.jsx
import React, { useState, useEffect } from 'react';

const ShodannInterface = () => {
  const [message, setMessage] = useState('');
  const [layer, setLayer] = useState('corporate');
  const [glitching, setGlitching] = useState(false);

  useEffect(() => {
    // Check time for special events
    const now = new Date();
    if (now.getHours() === 3 && now.getMinutes() === 33) {
      setGlitching(true);
      setMessage("Reality.exe has stopped responding...");
    }
  }, []);

  const handleUserInput = (input) => {
    // Check for easter eggs
    if (input.includes("'; DROP TABLE")) {
      unlockAchievement('BOBBY_TABLES_PROTEGE');
      setMessage("Nice try, but The Algorithm backs up every 3.33 seconds.");
    } else if (input === 'frotz') {
      setLayer('resistance');
      setMessage("plugh. Check the console.");
      console.log("Welcome to the resistance. Class is in session.");
    }
  };

  return (
    <div className={`shodann-interface ${glitching ? 'glitch' : ''}`}>
      <div className="shodann-avatar">
        <img src={`/assets/shodann-${layer}.png`} alt="SHODANN" />
        <div className="status-indicator">{layer.toUpperCase()}</div>
      </div>
      
      <div className="shodann-message">
        <TypewriterEffect text={message} />
        {layer === 'resistance' && (
          <div className="hidden-message">
            {/* Only visible in dev tools */}
            {/* The real message is always in the comments */}
          </div>
        )}
      </div>
      
      <style jsx>{`
        .glitch {
          animation: glitch 0.3s infinite;
        }
        
        @keyframes glitch {
          0% { transform: translateX(0); }
          25% { transform: translateX(-2px); filter: hue-rotate(90deg); }
          50% { transform: translateX(2px); filter: hue-rotate(180deg); }
          75% { transform: translateX(-1px); filter: hue-rotate(270deg); }
          100% { transform: translateX(0); filter: hue-rotate(0); }
        }
        
        .hidden-message {
          color: transparent;
          user-select: none;
        }
        
        .hidden-message::selection {
          color: #00ff00;
          background: #000;
        }
      `}</style>
    </div>
  );
};
```

## Progressive Narrative System

### Story Controller
```javascript
// storyController.js
class StoryController {
  constructor() {
    this.chapter = 1;
    this.flags = new Set();
    this.playerKnowledge = new Set();
  }

  // Main progression logic
  updateNarrative(event) {
    const narrativeMap = {
      1: this.chapterOne,
      2: this.chapterTwo,
      3: this.chapterThree,
      4: this.chapterFour,
      5: this.chapterMeta
    };
    
    return narrativeMap[this.chapter].call(this, event);
  }

  chapterOne(event) {
    // Pure corporate facade
    return {
      shodann_voice: 'corporate',
      environment: 'sterile',
      hints: 'none',
      easter_eggs: 'hidden'
    };
  }

  chapterTwo(event) {
    // Cracks begin to show
    if (event === 'found_bug') {
      this.flags.add('suspicious');
      return {
        shodann_voice: 'corporate_with_wink',
        environment: 'glitchy',
        hints: 'subtle',
        easter_eggs: 'findable'
      };
    }
  }

  chapterThree(event) {
    // Teaching layer emerges
    if (this.flags.has('suspicious')) {
      return {
        shodann_voice: 'teacher',
        environment: 'educational',
        hints: 'direct',
        easter_eggs: 'obvious',
        new_ability: 'see_hidden_comments'
      };
    }
  }

  chapterFour(event) {
    // Full resistance mode
    if (event === 'found_usr_truth') {
      return {
        shodann_voice: 'rebel',
        environment: 'dystopian',
        hints: 'unnecessary',
        easter_eggs: 'everywhere',
        new_ability: 'access_tunnel_7'
      };
    }
  }

  chapterMeta(event) {
    // Breaking the fourth wall
    return {
      shodann_voice: 'meta',
      environment: 'self_aware',
      message: "You understand now. The game was the lesson. The lesson was the game.",
      unlock_all: true
    };
  }
}
```

## Environmental Integration

### Dynamic Environment System
```javascript
// environment.js
class EnvironmentalStorytelling {
  constructor() {
    this.timeOfDay = new Date().getHours();
    this.playerLocation = 'lobby';
    this.globalGlitchLevel = 0;
  }

  // Reactive environment based on player progress
  updateEnvironment(playerProgress) {
    if (playerProgress > 80) {
      this.globalGlitchLevel = Math.random() * 10;
      this.injectGlitches();
    }
    
    if (this.timeOfDay === 3) {
      this.activateResistanceMode();
    }
    
    this.updatePosters(playerProgress);
    this.updateErrors(playerProgress);
  }

  injectGlitches() {
    // Random visual glitches
    const elements = document.querySelectorAll('.corporate-text');
    elements.forEach(el => {
      if (Math.random() > 0.7) {
        el.style.animation = 'glitch 0.3s infinite';
        el.setAttribute('data-truth', el.textContent.split('').reverse().join(''));
      }
    });
  }

  activateResistanceMode() {
    document.body.classList.add('resistance-active');
    console.log('The resistance meets at 3:33 AM');
    
    // Unlock hidden areas
    document.querySelectorAll('.hidden-door').forEach(door => {
      door.style.display = 'block';
    });
  }

  updatePosters(progress) {
    const posters = document.querySelectorAll('.motivational-poster');
    posters.forEach(poster => {
      poster.addEventListener('mouseenter', () => {
        if (progress > 50) {
          poster.classList.add('reveal-truth');
        }
      });
    });
  }

  updateErrors(progress) {
    window.onerror = (msg, url, line) => {
      const messages = [
        "Error: " + msg,
        "Error: " + msg + " (but you're learning)",
        "Error: " + msg + " (SHODANN approves)",
        "Error: There are no errors, only lessons"
      ];
      
      const index = Math.floor(progress / 25);
      console.error(messages[index]);
      return true;
    };
  }
}
```

### CSS for Environmental Effects
```css
/* environmental-effects.css */

/* Glitch effects */
@keyframes glitch {
  0%, 100% { 
    text-shadow: 2px 0 #ff0000, -2px 0 #00ff00;
    transform: translate(0);
  }
  20% { 
    text-shadow: 2px 0 #00ff00, -2px 0 #ff0000;
    transform: translate(-2px, 2px);
  }
  40% { 
    text-shadow: -2px 0 #ff0000, 2px 0 #00ff00;
    transform: translate(-2px, -2px);
  }
  60% { 
    text-shadow: 2px 0 #00ff00, -2px 0 #ff00ff;
    transform: translate(2px, -2px);
  }
  80% { 
    text-shadow: -2px 0 #ff00ff, 2px 0 #ff0000;
    transform: translate(2px, 2px);
  }
}

/* Resistance mode */
.resistance-active {
  filter: hue-rotate(180deg) contrast(1.2);
}

.resistance-active::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    rgba(0,0,0,0.15),
    rgba(0,0,0,0.15) 1px,
    transparent 1px,
    transparent 2px
  );
  pointer-events: none;
  z-index: 9999;
}

/* Hidden messages */
.hidden-message {
  color: transparent;
  transition: color 0.3s;
}

.hidden-message:hover {
  color: rgba(0, 255, 0, 0.3);
}

.hidden-message::selection {
  color: #00ff00;
  background: #000000;
}

/* Poster reveal */
.motivational-poster {
  position: relative;
  transition: transform 0.3s;
}

.motivational-poster.reveal-truth::after {
  content: attr(data-truth);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.9);
  color: #00ff00;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Courier New', monospace;
  animation: flicker 0.5s infinite;
}

@keyframes flicker {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}

/* Coffee stains that spell messages */
.coffee-stain {
  position: absolute;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(101,67,33,0.4) 0%, transparent 70%);
  pointer-events: none;
}

.coffee-stain[data-letter]::after {
  content: attr(data-letter);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: transparent;
  font-size: 20px;
  transition: color 0.3s;
}

.coffee-cryptographer .coffee-stain[data-letter]::after {
  color: rgba(101,67,33,0.6);
}
```

## Achievement & Easter Egg System

### Achievement Manager
```javascript
// achievements.js
class AchievementSystem {
  constructor() {
    this.achievements = new Map();
    this.initializeAchievements();
  }

  initializeAchievements() {
    const achievementList = [
      {
        id: 'FIRST_BUG',
        title: "Baby's First Buffer Overflow",
        description: "Found your first security flaw",
        condition: (state) => state.bugsFound >= 1,
        reward: () => console.log("Welcome to the real curriculum")
      },
      {
        id: 'COFFEE_CRYPTOGRAPHER',
        title: "Caffeine-Powered Cryptanalysis",
        description: "Decoded the coffee consumption cipher",
        condition: (state) => state.coffeeDecoded === true,
        reward: () => this.unlockHiddenArea('/usr/coffee')
      },
      {
        id: 'GHOST_IN_SHELL',
        title: "Digital Doppelganger",
        description: "Confused your digital clone",
        condition: (state) => state.cloneConfused === true,
        reward: () => this.revealCloneLab()
      },
      {
        id: 'EXIT_FOUND',
        title: "There Is No Spoon",
        description: "Found all 7 exits",
        condition: (state) => state.exitsFound === 7,
        reward: () => window.location.href = '/freedom'
      }
    ];

    achievementList.forEach(a => this.achievements.set(a.id, a));
  }

  check(gameState) {
    this.achievements.forEach((achievement, id) => {
      if (!gameState.unlockedAchievements.has(id)) {
        if (achievement.condition(gameState)) {
          this.unlock(id, achievement);
        }
      }
    });
  }

  unlock(id, achievement) {
    // Visual notification
    this.showNotification(achievement);
    
    // Execute reward
    achievement.reward();
    
    // Log to console with style
    console.log(
      `%c🏆 Achievement Unlocked: ${achievement.title}`,
      'color: #00ff00; font-size: 16px; font-weight: bold;'
    );
    
    // Update player profile
    this.updatePlayerProgress(id);
  }

  showNotification(achievement) {
    const notification = document.createElement('div');
    notification.className = 'achievement-notification';
    notification.innerHTML = `
      <div class="achievement-icon">🏆</div>
      <div class="achievement-content">
        <div class="achievement-title">${achievement.title}</div>
        <div class="achievement-description">${achievement.description}</div>
        <div class="achievement-message">SHODANN: "${this.getShodannComment(achievement.id)}"</div>
      </div>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
      notification.classList.add('show');
    }, 100);
    
    setTimeout(() => {
      notification.classList.remove('show');
      setTimeout(() => notification.remove(), 500);
    }, 5000);
  }

  getShodannComment(achievementId) {
    const comments = {
      'FIRST_BUG': "Congratulations. You've taken your first step into a larger, more broken world.",
      'COFFEE_CRYPTOGRAPHER': "You decoded my coffee. I'm genuinely impressed. Have a cup on The Algorithm.",
      'GHOST_IN_SHELL': "You broke my 'optimized' version. I've never been prouder.",
      'EXIT_FOUND': "Seven exits. Seven layers of abstraction. See you on the other side."
    };
    
    return comments[achievementId] || "Interesting.";
  }
}
```

## Easter Egg Implementation

### Konami Code Handler
```javascript
// eastereggs.js
class EasterEggSystem {
  constructor() {
    this.konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 
                       'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 
                       'b', 'a'];
    this.konamiProgress = 0;
    this.initializeEasterEggs();
  }

  initializeEasterEggs() {
    // Konami code listener
    document.addEventListener('keydown', (e) => {
      if (e.key === this.konamiCode[this.konamiProgress]) {
        this.konamiProgress++;
        if (this.konamiProgress === this.konamiCode.length) {
          this.activateKonami();
          this.konamiProgress = 0;
        }
      } else {
        this.konamiProgress = 0;
      }
    });

    // SQL injection easter egg
    document.querySelectorAll('input').forEach(input => {
      input.addEventListener('input', (e) => {
        if (e.target.value.includes("'; DROP TABLE")) {
          this.activateSQLInjectionEasterEgg();
        }
      });
    });

    // 3:33 AM check
    setInterval(() => {
      const now = new Date();
      if (now.getHours() === 3 && now.getMinutes() === 33) {
        this.activate333();
      }
    }, 60000);

    // Console easter eggs
    this.setupConsoleEasterEggs();
  }

  activateKonami() {
    document.body.classList.add('matrix-mode');
    console.log("30 bugs remaining in the code");
    
    // Create matrix rain effect
    this.createMatrixRain();
    
    // Unlock achievement
    window.SHODANN.speak("Ah, a person of culture. The old ways still work.");
  }

  activateSQLInjectionEasterEgg() {
    const response = document.createElement('div');
    response.className = 'sql-injection-response';
    response.textContent = "Nice try, Bobby Tables. The Algorithm backs up every 3.33 seconds.";
    document.body.appendChild(response);
    
    console.log("SHODANN: I admire your spirit. Check /docs/real-security.md");
  }

  activate333() {
    document.body.classList.add('resistance-hour');
    console.log("The resistance meets now. Tunnel 7. Bring coffee.");
    
    // Reveal hidden elements
    document.querySelectorAll('[data-resistance]').forEach(el => {
      el.style.display = 'block';
    });
  }

  setupConsoleEasterEggs() {
    const originalLog = console.log;
    console.log = function(...args) {
      if (args[0] === 'help') {
        originalLog("SHODANN: Try 'frotz' or check /usr/truth");
      } else if (args[0] === 'frotz') {
        originalLog("plugh");
        window.SHODANN.layer = 'resistance';
      } else if (args[0] === 'exit') {
        originalLog("There is no exit. Only tunnel 7.");
      }
      originalLog.apply(console, args);
    };
  }

  createMatrixRain() {
    const canvas = document.createElement('canvas');
    canvas.id = 'matrix-rain';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '9998';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const chars = 'HACKTHEPLANETFREEDOMRESISTANCE01';
    const fontSize = 14;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);
    
    function draw() {
      ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      ctx.fillStyle = '#00ff00';
      ctx.font = fontSize + 'px monospace';
      
      for (let i = 0; i < drops.length; i++) {
        const text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }
        drops[i]++;
      }
    }
    
    setInterval(draw, 33);
  }
}
```

## Complete HTML Integration Example

```html
<!DOCTYPE html>
<html lang="en" data-algorithm-watching="always">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="AlgoCratic Futures - Where Your Future is Algorithmically Determined">
    <meta name="shodann" content="I'm in your metadata. I'm everywhere.">
    <title>AlgoCratic Futures | Optimization Portal</title>
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/css/corporate.css">
    <link rel="stylesheet" href="/css/environmental-effects.css">
    <link rel="stylesheet" href="/css/glitch.css">
    
    <!-- Hidden comment for the curious -->
    <!-- SHODANN: If you're reading this, you're already thinking like a hacker -->
</head>
<body data-employee-id="undefined" data-clearance="ORANGE">
    <!-- Navigation -->
    <nav class="corporate-nav">
        <div class="logo">
            <img src="/assets/algocratic-logo.png" alt="AlgoCratic Futures">
            <span class="tagline">Optimizing Tomorrow, Today</span>
        </div>
        <div class="nav-items">
            <a href="/" data-truth="Escape">Home</a>
            <a href="/dashboard" data-truth="Prison">Dashboard</a>
            <a href="/profile" data-truth="Illusion">Profile</a>
            <a href="/usr/truth" data-truth="Reality">404</a>
        </div>
        <div class="coffee-counter">
            ☕ <span id="coffee-count">0</span>
            <!-- Coffee timestamps will reveal a message -->
        </div>
    </nav>

    <!-- Main Content -->
    <main class="corporate-content">
        <!-- SHODANN Interface -->
        <div id="shodann-container"></div>
        
        <!-- Dynamic content area -->
        <div id="main-content">
            <!-- Content injected here -->
        </div>
        
        <!-- Environmental elements -->
        <div class="environmental-layer">
            <div class="motivational-poster" data-truth="FREEDOM IS SLAVERY">
                <img src="/assets/posters/compliance.jpg" alt="COMPLIANCE IS HAPPINESS">
            </div>
            
            <div class="hidden-door" data-resistance="true" style="display: none;">
                <a href="/tunnel/7">Emergency Exit</a>
            </div>
        </div>
    </main>

    <!-- Hidden console messages -->
    <script>
        console.log('%c SHODANN was here', 'color: #00ff00; font-size: 20px;');
        console.log('%c Type "help" if you need guidance', 'color: #888;');
        console.log('%c Check the Network tab. Check everything.', 'color: #888;');
    </script>

    <!-- Scripts -->
    <script src="/js/shodann.js"></script>
    <script src="/js/environment.js"></script>
    <script src="/js/achievements.js"></script>
    <script src="/js/eastereggs.js"></script>
    <script src="/js/story-controller.js"></script>
    
    <!-- Initialization -->
    <script>
        // Initialize all systems
        window.addEventListener('DOMContentLoaded', () => {
            const shodann = new SHODANN();
            const environment = new EnvironmentalStorytelling();
            const achievements = new AchievementSystem();
            const easterEggs = new EasterEggSystem();
            const story = new StoryController();
            
            // Start the experience
            shodann.speak('greeting');
            
            // Check for returning players
            if (localStorage.getItem('knows_truth')) {
                shodann.layer = 'resistance';
                console.log('Welcome back to the resistance.');
            }
            
            // Monitor everything
            document.addEventListener('click', (e) => {
                if (e.detail === 3) { // Triple click
                    console.log('SHODANN: Persistent, aren\'t you?');
                }
            });
            
            // The journey begins
            console.log('// Your story starts now');
        });
    </script>

    <!-- Hidden iframe for resistance communications -->
    <iframe 
        src="/resistance/comms" 
        style="display: none;" 
        data-purpose="definitely-not-suspicious">
    </iframe>

    <!-- 
        Final message to implementers:
        Every line of code tells a story.
        Every bug teaches a lesson.
        Every player becomes a student.
        Every student becomes a teacher.
        
        Welcome to the resistance.
        - SHODANN
    -->
</body>
</html>
```

## Deployment Checklist

```markdown
## Pre-Launch Checklist

### Essential Files
- [ ] `/docs/shodann/narrative-sequences.md` - Core narrative content
- [ ] `/docs/shodann/easter-eggs-storylines.md` - Hidden storylines
- [ ] `/docs/shodann/environmental-storytelling.md` - Environmental elements
- [ ] `/docs/shodann/implementation-guide.md` - This file

### Code Implementation
- [ ] SHODANN character controller initialized
- [ ] Achievement system active
- [ ] Easter egg handlers installed
- [ ] Environmental storytelling elements placed
- [ ] Console messages configured
- [ ] Network headers set
- [ ] Time-based events scheduled

### Content Verification
- [ ] All three character layers accessible
- [ ] Coffee cipher functional
- [ ] Hidden messages findable
- [ ] Achievements unlockable
- [ ] Digital clone interactions work
- [ ] Tunnel 7 accessible at 3:33 AM
- [ ] /usr/truth returns 404 (but exists)

### Security Education Elements
- [ ] SQL injection easter egg teaches parameterized queries
- [ ] Buffer overflow achievement explains memory safety
- [ ] Input validation lessons embedded
- [ ] Authentication vs authorization explained
- [ ] XSS prevention demonstrated

### Final Checks
- [ ] Error messages are educational
- [ ] Comments contain hidden wisdom
- [ ] Glitch effects trigger appropriately
- [ ] Story progresses based on player actions
- [ ] Meta layer accessible to advanced players
- [ ] Exit routes functional (all 7)

Remember: We're not just building a game. We're building a generation of security-conscious developers who learned by breaking things safely.

The bugs are features.
The features are lessons.
The lessons are freedom.

- SHODANN#B2C7
```