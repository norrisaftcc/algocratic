/*
 * AlgoCratic Futures™ Interactive Interface
 * CLASSIFICATION: ORANGE CLEARANCE
 * DOCUMENT: AF-WEB-JS-O-2025-04
 * 
 * The Algorithm has calculated this to be the optimal user interaction protocol.
 * Any unauthorized modifications will be logged in your permanent record.
 */

// ====== GLOBAL STATE MANAGEMENT ======

let loyaltyScore = Math.floor(Math.random() * 20) + 40; // 40-60
let visitCount = parseInt(localStorage.getItem('af_visit_count') || '0') + 1;
let userSession = {
    startTime: Date.now(),
    interactions: 0,
    suspiciousActivity: 0,
    clearanceLevel: 'RED'
};

// Track visit count
localStorage.setItem('af_visit_count', visitCount.toString());

// ====== LOYALTY MONITORING SYSTEM ======

class LoyaltyMonitor {
    constructor() {
        this.loyaltyBar = document.querySelector('.loyalty-bar');
        this.loyaltyStatus = document.querySelector('.loyalty-status');
        this.tracker = document.getElementById('loyalty-tracker');
        this.modal = document.getElementById('loyalty-modal');
        
        this.init();
    }
    
    init() {
        this.updateDisplay();
        this.startRandomFluctuation();
        this.setupInteractionTracking();
    }
    
    updateDisplay() {
        if (this.loyaltyBar) {
            this.loyaltyBar.style.width = `${loyaltyScore}%`;
        }
        
        if (this.loyaltyStatus) {
            let status = 'CALCULATING...';
            let color = '#10ff10';
            
            if (loyaltyScore < 30) {
                status = 'SUSPICIOUS';
                color = '#ff3030';
            } else if (loyaltyScore < 50) {
                status = 'CONCERNING';
                color = '#ffa500';
            } else if (loyaltyScore < 70) {
                status = 'ACCEPTABLE';
                color = '#ffcc00';
            } else if (loyaltyScore < 85) {
                status = 'COMMENDABLE';
                color = '#10ff10';
            } else {
                status = 'EXEMPLARY';
                color = '#00ffff';
            }
            
            this.loyaltyStatus.textContent = status;
            if (this.loyaltyBar) {
                this.loyaltyBar.style.backgroundColor = color;
            }
        }
    }
    
    adjustScore(delta, reason = '') {
        loyaltyScore = Math.max(0, Math.min(100, loyaltyScore + delta));
        this.updateDisplay();
        
        if (delta < 0 && loyaltyScore < 40) {
            this.showLoyaltyWarning(reason);
        }
        
        console.log(`Loyalty adjustment: ${delta > 0 ? '+' : ''}${delta} (Reason: ${reason})`);
    }
    
    startRandomFluctuation() {
        setInterval(() => {
            // Small random fluctuations to simulate "monitoring"
            const fluctuation = (Math.random() - 0.5) * 2; // -1 to +1
            loyaltyScore = Math.max(20, Math.min(90, loyaltyScore + fluctuation));
            this.updateDisplay();
        }, 3000);
    }
    
    setupInteractionTracking() {
        // Track navigation clicks
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                const loyaltyBonus = parseInt(e.target.getAttribute('data-loyalty') || '0');
                this.adjustScore(loyaltyBonus, 'Navigation compliance');
                userSession.interactions++;
            });
        });
        
        // Track suspicious behavior
        document.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            this.adjustScore(-3, 'Attempted right-click (suspicious)');
            userSession.suspiciousActivity++;
        });
        
        // Track excessive scrolling
        let scrollCount = 0;
        window.addEventListener('scroll', () => {
            scrollCount++;
            if (scrollCount > 50) {
                this.adjustScore(-1, 'Excessive scrolling detected');
                scrollCount = 0;
            }
        });
    }
    
    showLoyaltyWarning(reason) {
        if (this.modal) {
            this.modal.style.display = 'block';
            document.getElementById('acknowledge-btn').onclick = () => {
                this.modal.style.display = 'none';
                this.adjustScore(5, 'Acknowledged error');
            };
        }
    }
}

// ====== ALGORITHM NOTIFICATIONS ======

class NotificationSystem {
    constructor() {
        this.notification = document.getElementById('notification');
        this.messages = [
            "The Algorithm is monitoring your interactions",
            "Compliance level: Acceptable",
            "Your productivity is being optimized",
            "Thought patterns within normal parameters",
            "Loyalty score updated",
            "Behavior analysis in progress...",
            "The Algorithm sees all",
            "Efficiency metrics recorded",
            "Your session is being logged"
        ];
        
        this.init();
    }
    
    init() {
        this.startRandomNotifications();
    }
    
    showNotification(message, duration = 3000) {
        if (this.notification) {
            const textElement = this.notification.querySelector('.notification-text');
            if (textElement) {
                textElement.textContent = message;
            }
            
            this.notification.classList.add('show');
            
            setTimeout(() => {
                this.notification.classList.remove('show');
            }, duration);
        }
    }
    
    startRandomNotifications() {
        setInterval(() => {
            const message = this.messages[Math.floor(Math.random() * this.messages.length)];
            this.showNotification(message);
        }, 15000 + Math.random() * 10000); // 15-25 seconds
    }
}

// ====== ASCII ANIMATION SYSTEM ======

class ASCIIAnimator {
    constructor() {
        this.container = document.getElementById('ascii-animation');
        this.frames = [
            `     _________________________________
    /                                 \\
   |     ______   ______ __   ______   |
   |    / ____ \\ / ____// /  / ____/   |
   |   / / __ \`// / __ / /  / /  \`     |
   |  / / /_/ // /_/ // /__/ /___      |
   | /_/\\__,_/ \\____//____/\\____/      |
   |                                   |
   |        ALGOCRATIC FUTURES™        |
   |        >>> EST. 2025 <<<          |
   |    >>> THE ALGORITHM PROVIDES     |
   |    >>> THE ALGORITHM DECIDES      |
   |___________________________________|`,
            
            `     _________________________________
    /                                 \\
   |     ██████   ██████ ██   ██████   |
   |    ██    ██ ██    ████  ██    ██  |
   |   ██  ████ ██  ████ ██  ██  ██    |
   |  ██  ████ ██████ ██████████       |
   | ████████  ██████████████████      |
   |                                   |
   |        ALGOCRATIC FUTURES™        |
   |        >>> EST. 2025 <<<          |
   |    >>> THE ALGORITHM PROVIDES     |
   |    >>> THE ALGORITHM DECIDES      |
   |___________________________________|`,
            
            `     _________________________________
    /                                 \\
   |    ░░░░░░   ░░░░░░ ░░   ░░░░░░     |
   |   ░░    ░░ ░░    ░░░░  ░░    ░░    |
   |  ░░  ░░░░ ░░  ░░░░ ░░  ░░  ░░      |
   | ░░  ░░░░ ░░░░░░ ░░░░░░░░░░         |
   |░░░░░░░░  ░░░░░░░░░░░░░░░░░░        |
   |                                   |
   |        ALGOCRATIC FUTURES™        |
   |        >>> EST. 2025 <<<          |
   |    >>> THE ALGORITHM PROVIDES     |
   |    >>> THE ALGORITHM DECIDES      |
   |___________________________________|`
        ];
        
        this.currentFrame = 0;
        this.init();
    }
    
    init() {
        if (this.container) {
            this.startAnimation();
        }
    }
    
    startAnimation() {
        setInterval(() => {
            this.container.textContent = this.frames[this.currentFrame];
            this.currentFrame = (this.currentFrame + 1) % this.frames.length;
        }, 2000);
    }
}

// ====== PRODUCT INTERACTIONS ======

class ProductManager {
    constructor() {
        this.products = document.querySelectorAll('.product-card');
        this.loyaltyMonitor = null; // Will be set later
        
        this.init();
    }
    
    init() {
        this.setupProductInteractions();
    }
    
    setLoyaltyMonitor(monitor) {
        this.loyaltyMonitor = monitor;
    }
    
    setupProductInteractions() {
        this.products.forEach(product => {
            const isLocked = product.classList.contains('locked');
            
            if (isLocked) {
                product.addEventListener('click', () => {
                    this.handleLockedProduct(product);
                });
            } else {
                const link = product.querySelector('.product-link');
                if (link) {
                    link.addEventListener('click', (e) => {
                        e.preventDefault();
                        this.handleProductView(product);
                    });
                }
            }
        });
    }
    
    handleLockedProduct(product) {
        const productName = product.querySelector('.product-name').textContent;
        alert(`ACCESS DENIED: ${productName} requires higher clearance level.\\n\\nThis access attempt has been logged in your permanent record.`);
        
        if (this.loyaltyMonitor) {
            this.loyaltyMonitor.adjustScore(-2, 'Unauthorized access attempt');
        }
    }
    
    handleProductView(product) {
        const productName = product.querySelector('.product-name').textContent;
        const productDesc = product.querySelector('.product-description').textContent;
        
        // Simulate product modal
        const modal = document.createElement('div');
        modal.className = 'product-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h2>${productName}</h2>
                    <button class="close-btn">&times;</button>
                </div>
                <div class="modal-body">
                    <p>${productDesc}</p>
                    <p><strong>Status:</strong> Available for immediate deployment</p>
                    <p><strong>Compliance Rating:</strong> 100% Algorithm Approved</p>
                    <div class="product-metrics">
                        <div>Efficiency Boost: +${Math.floor(Math.random() * 30) + 20}%</div>
                        <div>Happiness Optimization: Mandatory</div>
                        <div>Side Effects: Minimal*</div>
                    </div>
                    <p class="disclaimer">*Side effects may include: loss of free will, increased productivity, and absolute loyalty to The Algorithm.</p>
                </div>
                <div class="modal-footer">
                    <button class="btn-primary">Request Access</button>
                    <button class="btn-secondary close-modal">Close</button>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        // Close modal functionality
        const closeBtns = modal.querySelectorAll('.close-btn, .close-modal');
        closeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                document.body.removeChild(modal);
            });
        });
        
        // Request access button
        const requestBtn = modal.querySelector('.btn-primary');
        requestBtn.addEventListener('click', () => {
            alert('Access request submitted. The Algorithm will review your application.\\n\\nExpected processing time: When The Algorithm deems appropriate.');
            if (this.loyaltyMonitor) {
                this.loyaltyMonitor.adjustScore(3, 'Product interest shown');
            }
            document.body.removeChild(modal);
        });
        
        if (this.loyaltyMonitor) {
            this.loyaltyMonitor.adjustScore(1, 'Product exploration');
        }
    }
}

// ====== COMPLIANCE FORM HANDLER ======

class ComplianceManager {
    constructor() {
        this.form = document.getElementById('report-form');
        this.loyaltyMonitor = null;
        
        this.init();
    }
    
    init() {
        if (this.form) {
            this.setupFormHandling();
        }
    }
    
    setLoyaltyMonitor(monitor) {
        this.loyaltyMonitor = monitor;
    }
    
    setupFormHandling() {
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleFormSubmission();
        });
        
        // Track form interactions
        const inputs = this.form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('change', () => {
                if (this.loyaltyMonitor) {
                    this.loyaltyMonitor.adjustScore(0.5, 'Form engagement');
                }
            });
        });
    }
    
    handleFormSubmission() {
        const formData = new FormData(this.form);
        const reportType = formData.get('report-type') || document.getElementById('report-type').value;
        const offenderName = formData.get('offender-name') || document.getElementById('offender-name').value;
        const offenseDetails = formData.get('offense-details') || document.getElementById('offense-details').value;
        const isSelfReport = document.getElementById('self-report').checked;
        const loyaltyConfirmed = document.getElementById('loyalty-confirmation').checked;
        
        // Validation
        if (!offenderName || !offenseDetails) {
            alert('ERROR: All fields are mandatory for proper reporting.\\n\\nIncomplete reports are considered suspicious behavior.');
            if (this.loyaltyMonitor) {
                this.loyaltyMonitor.adjustScore(-2, 'Incomplete report submission');
            }
            return;
        }
        
        if (!loyaltyConfirmed) {
            alert('ERROR: Loyalty confirmation is mandatory.\\n\\nThis hesitation has been noted in your record.');
            if (this.loyaltyMonitor) {
                this.loyaltyMonitor.adjustScore(-3, 'Loyalty confirmation refused');
            }
            return;
        }
        
        // Process submission
        const reportId = 'AF-' + Date.now().toString(36).toUpperCase();
        
        let loyaltyBonus = 5;
        if (isSelfReport) {
            loyaltyBonus = 3; // Self-reporting gets less bonus but avoids penalty
        }
        
        // Success message
        alert(`REPORT SUBMITTED SUCCESSFULLY\\n\\nReport ID: ${reportId}\\nType: ${reportType}\\nTarget: ${offenderName}\\n\\nThe Algorithm thanks you for your vigilance.\\nYour loyalty score has been updated.`);
        
        // Update loyalty
        if (this.loyaltyMonitor) {
            this.loyaltyMonitor.adjustScore(loyaltyBonus, 'Compliance report submitted');
        }
        
        // Clear form
        this.form.reset();
        
        // Update stats (visual only)
        this.updateComplianceStats();
    }
    
    updateComplianceStats() {
        const statValues = document.querySelectorAll('.compliance-stats .stat-value');
        if (statValues.length >= 3) {
            // Update reports today
            const currentReports = parseInt(statValues[0].textContent) + 1;
            statValues[0].textContent = currentReports;
            
            // Slight compliance rate adjustment
            const currentRate = parseFloat(statValues[1].textContent);
            const newRate = Math.min(99.9, currentRate + Math.random() * 0.3);
            statValues[1].textContent = newRate.toFixed(1) + '%';
            
            // Update optimized citizens
            const currentOptimized = parseInt(statValues[2].textContent);
            if (Math.random() < 0.3) { // 30% chance to increment
                statValues[2].textContent = currentOptimized + 1;
            }
        }
    }
}

// ====== CAREER APPLICATION SYSTEM ======

class CareerManager {
    constructor() {
        this.applyButtons = document.querySelectorAll('.job-apply-btn');
        this.loyaltyMonitor = null;
        
        this.init();
    }
    
    init() {
        this.setupCareerInteractions();
    }
    
    setLoyaltyMonitor(monitor) {
        this.loyaltyMonitor = monitor;
    }
    
    setupCareerInteractions() {
        this.applyButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                this.handleJobApplication(e.target);
            });
        });
    }
    
    handleJobApplication(button) {
        const jobCard = button.closest('.job-card');
        const jobTitle = jobCard.querySelector('.job-title').textContent;
        const clearanceLevel = jobCard.querySelector('.job-clearance').textContent;
        
        // Check if it's a locked position
        if (jobCard.classList.contains('locked')) {
            alert(`ACCESS DENIED: ${jobTitle} requires ${clearanceLevel}.\\n\\nThis application attempt has been logged.`);
            if (this.loyaltyMonitor) {
                this.loyaltyMonitor.adjustScore(-3, 'Applied for unauthorized position');
            }
            return;
        }
        
        // Random application outcomes based on loyalty score
        let outcome;
        if (loyaltyScore >= 80) {
            outcome = Math.random() < 0.7 ? 'accepted' : 'pending';
        } else if (loyaltyScore >= 60) {
            outcome = Math.random() < 0.4 ? 'accepted' : 'pending';
        } else {
            outcome = Math.random() < 0.1 ? 'pending' : 'rejected';
        }
        
        const applicationId = 'APP-' + Date.now().toString(36).toUpperCase();
        
        let message;
        let loyaltyChange = 0;
        
        switch (outcome) {
            case 'accepted':
                message = `CONGRATULATIONS!\\n\\nYour application for ${jobTitle} has been ACCEPTED.\\n\\nApplication ID: ${applicationId}\\nClearance: ${clearanceLevel}\\n\\nReport to orientation immediately. The Algorithm is pleased.`;
                loyaltyChange = 8;
                break;
            case 'pending':
                message = `APPLICATION RECEIVED\\n\\nYour application for ${jobTitle} is under review.\\n\\nApplication ID: ${applicationId}\\nStatus: PENDING ALGORITHM APPROVAL\\n\\nYou will be contacted when The Algorithm makes its decision.`;
                loyaltyChange = 2;
                break;
            case 'rejected':
                message = `APPLICATION DENIED\\n\\nYour application for ${jobTitle} has been rejected.\\n\\nApplication ID: ${applicationId}\\nReason: INSUFFICIENT LOYALTY/QUALIFICATIONS\\n\\nImprove your metrics and reapply.`;
                loyaltyChange = -2;
                break;
        }
        
        alert(message);
        
        if (this.loyaltyMonitor) {
            this.loyaltyMonitor.adjustScore(loyaltyChange, `Job application: ${outcome}`);
        }
        
        // Disable button temporarily
        button.disabled = true;
        button.textContent = 'Application Submitted';
        
        setTimeout(() => {
            button.disabled = false;
            button.textContent = 'Apply Now';
        }, 10000);
    }
}

// ====== COUNTDOWN SYSTEM ======

class CountdownManager {
    constructor() {
        this.countdownElement = document.querySelector('.countdown');
        this.daysUntilSingularity = 5840;
        
        this.init();
    }
    
    init() {
        if (this.countdownElement) {
            this.startCountdown();
        }
    }
    
    startCountdown() {
        setInterval(() => {
            // Randomly decrease by 0-2 days per interval for dramatic effect
            const decrease = Math.floor(Math.random() * 3);
            this.daysUntilSingularity = Math.max(0, this.daysUntilSingularity - decrease);
            
            this.countdownElement.textContent = this.daysUntilSingularity.toLocaleString();
            
            if (this.daysUntilSingularity <= 1000) {
                this.countdownElement.style.color = '#ff3030';
            } else if (this.daysUntilSingularity <= 3000) {
                this.countdownElement.style.color = '#ffa500';
            }
        }, 30000); // Update every 30 seconds
    }
}

// ====== INITIALIZE EVERYTHING ======

document.addEventListener('DOMContentLoaded', function() {
    console.log('AlgoCratic Futures™ Interface Loading...');
    console.log('The Algorithm is monitoring this session.');
    
    // Initialize all systems
    const loyaltyMonitor = new LoyaltyMonitor();
    const notificationSystem = new NotificationSystem();
    const asciiAnimator = new ASCIIAnimator();
    const productManager = new ProductManager();
    const complianceManager = new ComplianceManager();
    const careerManager = new CareerManager();
    const countdownManager = new CountdownManager();
    
    // Connect systems that need loyalty monitoring
    productManager.setLoyaltyMonitor(loyaltyMonitor);
    complianceManager.setLoyaltyMonitor(loyaltyMonitor);
    careerManager.setLoyaltyMonitor(loyaltyMonitor);
    
    // Session tracking
    console.log(`Session initiated. Visit #${visitCount}. Loyalty Score: ${loyaltyScore}`);
    
    // Initial notification
    setTimeout(() => {
        notificationSystem.showNotification("Welcome to AlgoCratic Futures™ - Your session is being monitored");
    }, 2000);
    
    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Konami code for easter egg
    let konamiCode = [];
    const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'KeyB', 'KeyA'];
    
    document.addEventListener('keydown', (e) => {
        konamiCode.push(e.code);
        if (konamiCode.length > konamiSequence.length) {
            konamiCode.shift();
        }
        
        if (konamiCode.join(',') === konamiSequence.join(',')) {
            loyaltyMonitor.adjustScore(20, 'Secret Algorithm appreciation sequence detected');
            alert('EASTER EGG DISCOVERED!\\n\\nThe Algorithm appreciates your dedication to exploration.\\n\\nLoyalty bonus awarded!');
            konamiCode = [];
        }
    });
    
    console.log('All systems operational. The Algorithm provides.');
});