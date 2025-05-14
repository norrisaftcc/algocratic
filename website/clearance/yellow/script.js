// YELLOW Clearance Guide Scripts

document.addEventListener('DOMContentLoaded', function() {
    // Strategy tracker fluctuation - YELLOW has higher baseline than ORANGE
    const strategyBar = document.querySelector('.strategy-bar');
    const strategyStatus = document.querySelector('.strategy-status');
    
    // Randomly fluctuate the strategy bar
    setInterval(() => {
        const currentWidth = parseFloat(strategyBar.style.width);
        const fluctuation = (Math.random() * 10) - 3; // Random value between -3 and 7 (skewed positive)
        let newWidth = currentWidth + fluctuation;
        
        // Keep within 65-90% range (higher than ORANGE)
        newWidth = Math.max(65, Math.min(90, newWidth));
        strategyBar.style.width = newWidth + '%';
        
        // Update status text
        if (newWidth < 70) {
            strategyStatus.textContent = 'EFFECTIVE';
            strategyBar.style.backgroundColor = '#ffcc00';
        } else if (newWidth < 80) {
            strategyStatus.textContent = 'STRATEGIC';
            strategyBar.style.backgroundColor = '#ffcc00';
        } else {
            strategyStatus.textContent = 'VISIONARY';
            strategyBar.style.backgroundColor = '#d4af37';
        }
    }, 3000);
    
    // Add glitch effect to algorithm messages
    const algorithmMessages = document.querySelectorAll('.algorithm-message');
    algorithmMessages.forEach(message => {
        message.classList.add('glitch');
    });
    
    // Typewriter effect for section-title elements
    document.querySelectorAll('.typewriter').forEach(element => {
        element.style.width = '0';
        setTimeout(() => {
            element.style.width = '100%';
        }, 500);
    });
    
    // More advanced eye movement for monolith (YELLOW has calculated watchful gaze)
    const eyes = document.querySelectorAll('.eye');
    if (eyes.length > 0) {
        setInterval(() => {
            eyes.forEach(eye => {
                const pupil = eye.querySelector(':before') || eye;
                const randomX = Math.floor(Math.random() * 7) - 3; // -3 to 3
                const randomY = Math.floor(Math.random() * 7) - 3; // -3 to 3
                
                if (pupil) {
                    pupil.style.transform = `translate(${randomX}px, ${randomY}px)`;
                }
            });
        }, 1200); // Faster than ORANGE, more calculated movements
    }
    
    // Interactive Easter egg for YELLOW level - clicking monolith shows message
    const monolith = document.querySelector('.monolith-icon');
    if (monolith) {
        monolith.addEventListener('click', function() {
            console.log('%cStrategic Design Specialist: Your decision to investigate unauthorized interactions has been logged.', 'color: #ffcc00; font-weight: bold');
            
            // Briefly make eyes stare directly at user
            eyes.forEach(eye => {
                eye.style.backgroundColor = '#d4af37';
                eye.querySelector(':before') && (eye.querySelector(':before').style.transform = 'translate(0, 0)');
                setTimeout(() => {
                    eye.style.backgroundColor = '#ffcc00';
                }, 1000);
            });
        });
    }
    
    // Page visit tracking (fictitious, just for show)
    console.log('YELLOW clearance page access logged. Timestamp: ' + new Date().toISOString());
    console.log('%cContent adaptation based on your strategic profile is active.', 'color: #ffcc00');
    
    // Random "strategic" messages in console - YELLOW is more focused on perception management
    const strategicMessages = [
        'Strategic alignment evaluation in progress...',
        'Reality perception filters active.',
        'THE ALGORITHM RECOGNIZES PATTERNS.',
        'Narrative optimization suggestions available.',
        'Strategic contradictions management monitor active.',
        'Perception management systems engaged.',
        'Multiple interpretation frameworks loaded.'
    ];
    
    setInterval(() => {
        const randomIndex = Math.floor(Math.random() * strategicMessages.length);
        console.log('%c' + strategicMessages[randomIndex], 'color: #ffcc00');
    }, 8000);
    
    // YELLOW-specific: Reveal technical diagrams with strategic timing
    const diagrams = document.querySelectorAll('.technical-diagram');
    if (diagrams.length > 0) {
        diagrams.forEach(diagram => {
            // Make diagram initially invisible
            diagram.style.opacity = '0';
            
            // Create diagram reveal observer
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        // Gradually reveal diagram when scrolled into view
                        setTimeout(() => {
                            diagram.style.transition = 'opacity 1.5s ease';
                            diagram.style.opacity = '1';
                        }, 300);
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.3 });
            
            observer.observe(diagram);
        });
    }
    
    // Strategic process flow animation
    const processSteps = document.querySelectorAll('.process-step');
    if (processSteps.length > 0) {
        processSteps.forEach((step, index) => {
            step.style.opacity = '0';
            step.style.transform = 'translateY(20px)';
            setTimeout(() => {
                step.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
                step.style.opacity = '1';
                step.style.transform = 'translateY(0)';
            }, 700 + (index * 400));
        });
    }
    
    // Strategic highlighting for emphasis
    const strategicElements = document.querySelectorAll('.strategy-block, .attention-box, .strategic-tip');
    if (strategicElements.length > 0) {
        strategicElements.forEach(element => {
            // Add subtle pulsing border effect to strategic elements
            element.addEventListener('mouseenter', () => {
                element.style.boxShadow = '0 0 8px rgba(255, 204, 0, 0.5)';
            });
            
            element.addEventListener('mouseleave', () => {
                element.style.boxShadow = 'none';
            });
        });
    }
    
    // Hidden message system - certain keypresses reveal hidden messages
    let keySequence = '';
    const secretCode = 'algorithm';
    
    document.addEventListener('keydown', (e) => {
        keySequence += e.key.toLowerCase();
        
        // Keep only the last 9 characters to avoid infinite growth
        if (keySequence.length > 9) {
            keySequence = keySequence.slice(keySequence.length - 9);
        }
        
        // Check if sequence contains the secret code
        if (keySequence.includes(secretCode)) {
            console.log('%cHidden strategic layer unlocked. Remember that perception management is more important than technical reality.', 'color: #d4af37; font-weight: bold');
            
            // Reset sequence
            keySequence = '';
            
            // Briefly highlight strategic tips
            document.querySelectorAll('.strategic-tip').forEach(tip => {
                tip.style.backgroundColor = 'rgba(255, 204, 0, 0.2)';
                setTimeout(() => {
                    tip.style.backgroundColor = 'transparent';
                }, 2000);
            });
        }
    });
});