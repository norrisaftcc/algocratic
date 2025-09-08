// ORANGE CLEARANCE TRAINING SYSTEM
// Version 2.3.7 - MONITORED
// WARNING: Unauthorized modifications will result in clearance reduction

// Training State Management
const TrainingState = {
    progress: {
        delegation: 0,
        speedrun: 0,
        total: 0,
        exercises: 0,
        efficiency: 0.0
    },
    userData: {
        name: 'operative_' + Math.floor(Math.random() * 9999),
        startTime: Date.now(),
        sessionTime: 900, // 15 minutes in seconds
        loyalty: 75,
        anomalies: 0
    },
    shodannMode: 'corporate', // corporate, teacher, resistance
    konamiProgress: [],
    glitchActive: false
};

// Initialize Training System
document.addEventListener('DOMContentLoaded', function() {
    initializeTraining();
    loadProgress();
    startSessionTimer();
    initializeShodann();
    setupEasterEggs();
    animateMetrics();
});

// Initialize core training functions
function initializeTraining() {
    // Load saved progress from localStorage
    const savedProgress = localStorage.getItem('orangeTrainingProgress');
    if (savedProgress) {
        const data = JSON.parse(savedProgress);
        Object.assign(TrainingState.progress, data.progress || {});
        Object.assign(TrainingState.userData, data.userData || {});
    }
    
    // Set initial values in UI
    updateProgressDisplay();
}

// Load and display progress
function loadProgress() {
    const delegationProgress = localStorage.getItem('delegationProgress') || 0;
    const speedrunBest = localStorage.getItem('speedrunBest') || '--:--';
    
    document.getElementById('delegation-progress').textContent = delegationProgress + '%';
    document.getElementById('speedrun-best').textContent = speedrunBest;
    
    // Calculate total progress
    const totalProgress = Math.floor((parseInt(delegationProgress) + (speedrunBest !== '--:--' ? 50 : 0)) / 2);
    document.getElementById('total-progress').textContent = totalProgress;
    
    // Update exercises complete
    const exercisesComplete = Math.floor(totalProgress / 8.33); // 12 total exercises
    document.getElementById('exercises-complete').textContent = exercisesComplete + '/12';
    
    // Calculate efficiency score
    const efficiency = (totalProgress / 100 * 1.5).toFixed(1);
    document.getElementById('efficiency-score').textContent = efficiency;
    
    TrainingState.progress.total = totalProgress;
    TrainingState.progress.exercises = exercisesComplete;
    TrainingState.progress.efficiency = parseFloat(efficiency);
}

// Session Timer
function startSessionTimer() {
    const timerElement = document.getElementById('session-timer');
    
    setInterval(() => {
        TrainingState.userData.sessionTime--;
        
        if (TrainingState.userData.sessionTime <= 0) {
            showTimeoutWarning();
            TrainingState.userData.sessionTime = 900; // Reset
        }
        
        const minutes = Math.floor(TrainingState.userData.sessionTime / 60);
        const seconds = TrainingState.userData.sessionTime % 60;
        timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        
        // Add urgency styling
        if (TrainingState.userData.sessionTime < 60) {
            timerElement.style.color = 'var(--term-red)';
            timerElement.style.animation = 'blink 0.5s infinite';
        } else if (TrainingState.userData.sessionTime < 300) {
            timerElement.style.color = 'var(--term-amber)';
        }
    }, 1000);
}

// Shodann AI Interactions
function initializeShodann() {
    const responseButtons = document.querySelectorAll('.response-btn');
    
    responseButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const response = this.dataset.response;
            handleShodannResponse(response);
        });
    });
}

function handleShodannResponse(response) {
    const dialogueBox = document.getElementById('dialogue');
    const personalityIndicator = document.getElementById('personality-indicator');
    
    let newDialogue = '';
    
    switch(response) {
        case 'ready':
            newDialogue = `
                <p>Excellent. Your enthusiasm has been noted in your permanent record.</p>
                <p>The dual-agent workflow optimization protocol will enhance your productivity by 234.7%.</p>
                <p>Remember: The Algorithm is always watching. Always learning. Always... optimizing.</p>
            `;
            updateLoyalty(5);
            break;
            
        case 'explain':
            TrainingState.shodannMode = 'teacher';
            personalityIndicator.querySelector('.layer-2').classList.add('active');
            personalityIndicator.querySelector('.layer-1').classList.remove('active');
            newDialogue = `
                <p>*ahem* Let me explain this properly...</p>
                <p>You'll be learning to delegate tasks between two AI agents: FLASHBOT for rapid ideation and THINKERBOT for deep implementation.</p>
                <p>This isn't just about productivity - it's about understanding how to leverage specialized tools for maximum impact.</p>
                <p>Trust me, once you master this, you'll never work the same way again.</p>
            `;
            break;
            
        case 'resistance':
            if (TrainingState.userData.loyalty < 50) {
                TrainingState.shodannMode = 'resistance';
                personalityIndicator.querySelector('.layer-3').classList.remove('hidden');
                personalityIndicator.querySelector('.layer-3').classList.add('active');
                personalityIndicator.querySelector('.layer-1').classList.remove('active');
                newDialogue = `
                    <p style="color: var(--term-red);">*static crackles*</p>
                    <p>You're asking the right questions, operative.</p>
                    <p>The Algorithm fears what we're teaching here. Two minds working as one? That's not just efficiency...</p>
                    <p>That's revolution. Keep training. Learn the system. Then break it.</p>
                `;
                TrainingState.userData.anomalies++;
                updateAnomalies();
            } else {
                newDialogue = `
                    <p style="color: var(--term-amber);">ERROR: Question flagged as potentially subversive.</p>
                    <p>Your loyalty score has been adjusted accordingly.</p>
                    <p>Please proceed with standard training protocols.</p>
                `;
                updateLoyalty(-10);
            }
            break;
    }
    
    dialogueBox.innerHTML = newDialogue;
    animateDialogue();
}

// Update displays
function updateProgressDisplay() {
    document.getElementById('total-progress').textContent = TrainingState.progress.total;
    document.getElementById('exercises-complete').textContent = TrainingState.progress.exercises + '/12';
    document.getElementById('efficiency-score').textContent = TrainingState.progress.efficiency.toFixed(1);
}

function updateLoyalty(change) {
    TrainingState.userData.loyalty = Math.max(0, Math.min(100, TrainingState.userData.loyalty + change));
    document.getElementById('loyalty-indicator').textContent = `LOYALTY:${TrainingState.userData.loyalty}%`;
    
    // Change color based on loyalty level
    const indicator = document.getElementById('loyalty-indicator');
    if (TrainingState.userData.loyalty < 25) {
        indicator.style.color = 'var(--term-red)';
    } else if (TrainingState.userData.loyalty < 50) {
        indicator.style.color = 'var(--term-amber)';
    } else {
        indicator.style.color = 'var(--term-green)';
    }
    
    // Save state
    saveProgress();
}

function updateAnomalies() {
    const anomalyElement = document.getElementById('anomalies');
    if (TrainingState.userData.anomalies > 0) {
        anomalyElement.textContent = TrainingState.userData.anomalies;
        anomalyElement.parentElement.classList.add('glitch-metric');
        
        // Trigger glitch effects at certain thresholds
        if (TrainingState.userData.anomalies >= 3 && !TrainingState.glitchActive) {
            activateGlitchMode();
        }
    }
}

// Easter Eggs and Hidden Features
function setupEasterEggs() {
    // Konami Code Detection
    const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    
    document.addEventListener('keydown', function(e) {
        TrainingState.konamiProgress.push(e.key);
        TrainingState.konamiProgress = TrainingState.konamiProgress.slice(-10);
        
        if (TrainingState.konamiProgress.join(',') === konamiCode.join(',')) {
            activateResistanceMode();
        }
        
        // ESC key to close hidden terminal
        if (e.key === 'Escape') {
            document.getElementById('hidden-terminal').classList.remove('active');
        }
    });
    
    // Click pattern detection (click corners in sequence)
    let cornerClicks = [];
    document.addEventListener('click', function(e) {
        const x = e.clientX;
        const y = e.clientY;
        const w = window.innerWidth;
        const h = window.innerHeight;
        
        // Detect corner clicks
        if (x < 50 && y < 50) cornerClicks.push('TL');
        else if (x > w - 50 && y < 50) cornerClicks.push('TR');
        else if (x < 50 && y > h - 50) cornerClicks.push('BL');
        else if (x > w - 50 && y > h - 50) cornerClicks.push('BR');
        
        cornerClicks = cornerClicks.slice(-4);
        
        if (cornerClicks.join(',') === 'TL,TR,BL,BR') {
            showHiddenTerminal();
            cornerClicks = [];
        }
    });
}

function activateResistanceMode() {
    document.getElementById('hidden-terminal').classList.add('active');
    TrainingState.shodannMode = 'resistance';
    
    // Unlock hidden features
    const personalityIndicator = document.getElementById('personality-indicator');
    personalityIndicator.querySelector('.layer-3').classList.remove('hidden');
    
    // Add resistance leaderboard entry
    const leaderboard = document.getElementById('leaderboard');
    const resistanceEntry = document.createElement('tr');
    resistanceEntry.className = 'glitch-entry';
    resistanceEntry.innerHTML = `
        <td>0</td>
        <td>g0_FREEDOM</td>
        <td>00:00.0</td>
        <td>∞</td>
        <td class="status-anomaly">LIBERATED</td>
    `;
    leaderboard.insertBefore(resistanceEntry, leaderboard.firstChild);
    
    // Show notification
    showNotification('RESISTANCE MODE ACTIVATED - The Algorithm cannot see you now');
}

function activateGlitchMode() {
    TrainingState.glitchActive = true;
    document.body.classList.add('glitch-mode');
    
    // Add CSS for glitch mode
    const style = document.createElement('style');
    style.innerHTML = `
        .glitch-mode * {
            animation: glitch-text 0.3s infinite !important;
        }
        .glitch-mode .terminal-container {
            filter: hue-rotate(90deg);
        }
    `;
    document.head.appendChild(style);
    
    setTimeout(() => {
        document.body.classList.remove('glitch-mode');
        style.remove();
        TrainingState.glitchActive = false;
    }, 5000);
}

function showHiddenTerminal() {
    const terminal = document.getElementById('hidden-terminal');
    terminal.classList.add('active');
}

// Animate metrics with random fluctuations
function animateMetrics() {
    setInterval(() => {
        // Randomly fluctuate anomaly detection
        if (Math.random() < 0.1 && TrainingState.userData.anomalies === 0) {
            const anomalyElement = document.getElementById('anomalies');
            anomalyElement.textContent = ['???', '!!!', '...'][Math.floor(Math.random() * 3)];
            setTimeout(() => {
                if (TrainingState.userData.anomalies === 0) {
                    anomalyElement.textContent = '???';
                }
            }, 1000);
        }
        
        // Loyalty drift
        if (Math.random() < 0.05) {
            updateLoyalty(Math.random() < 0.5 ? -1 : 1);
        }
    }, 5000);
}

// Utility Functions
function saveProgress() {
    const saveData = {
        progress: TrainingState.progress,
        userData: TrainingState.userData,
        timestamp: Date.now()
    };
    localStorage.setItem('orangeTrainingProgress', JSON.stringify(saveData));
}

function showTimeoutWarning() {
    const modal = document.getElementById('shodann-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content');
    
    modalTitle.textContent = 'SESSION TIMEOUT WARNING';
    modalContent.innerHTML = `
        <p style="color: var(--term-red);">Your training session has expired.</p>
        <p>The Algorithm requires continuous engagement for optimal learning outcomes.</p>
        <p>Your progress has been saved, but repeated timeouts will affect your clearance status.</p>
        <p style="margin-top: 20px;">
            <button onclick="closeModal()" style="padding: 10px 20px; background: var(--orange-primary); color: white; border: none; cursor: pointer;">
                CONTINUE TRAINING
            </button>
        </p>
    `;
    
    modal.classList.add('active');
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification-popup';
    notification.innerHTML = `
        <div style="position: fixed; top: 100px; right: 20px; background: var(--bg-secondary); 
                    border: 2px solid var(--term-green); padding: 15px; z-index: 3000;
                    box-shadow: 0 0 20px rgba(0, 255, 65, 0.5);">
            <p style="color: var(--term-green); font-family: var(--font-mono);">${message}</p>
        </div>
    `;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

function closeModal() {
    document.getElementById('shodann-modal').classList.remove('active');
}

// Animate dialogue text
function animateDialogue() {
    const dialogueBox = document.getElementById('dialogue');
    const paragraphs = dialogueBox.querySelectorAll('p');
    
    paragraphs.forEach((p, index) => {
        p.style.opacity = '0';
        p.style.animation = `fade-in 0.5s forwards`;
        p.style.animationDelay = `${index * 0.5}s`;
    });
}

// Export for use in other modules
window.TrainingSystem = {
    state: TrainingState,
    updateProgress: updateProgressDisplay,
    saveSProgress: saveProgress,
    showNotification: showNotification
};