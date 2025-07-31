// ORANGE Clearance Guide Scripts

document.addEventListener('DOMContentLoaded', function() {
    // Efficiency tracker fluctuation - ORANGE has higher baseline than RED
    const efficiencyBar = document.querySelector('.efficiency-bar');
    const efficiencyStatus = document.querySelector('.efficiency-status');
    
    // Randomly fluctuate the efficiency bar
    setInterval(() => {
        const currentWidth = parseFloat(efficiencyBar.style.width);
        const fluctuation = (Math.random() * 8) - 3; // Random value between -3 and 5 (skewed positive)
        let newWidth = currentWidth + fluctuation;
        
        // Keep within 45-75% range (higher than RED)
        newWidth = Math.max(45, Math.min(75, newWidth));
        efficiencyBar.style.width = newWidth + '%';
        
        // Update status text
        if (newWidth < 55) {
            efficiencyStatus.textContent = 'MODERATE';
            efficiencyBar.style.backgroundColor = '#ff8000';
        } else if (newWidth < 65) {
            efficiencyStatus.textContent = 'OPTIMAL';
            efficiencyBar.style.backgroundColor = '#ff8000';
        } else {
            efficiencyStatus.textContent = 'EXEMPLARY';
            efficiencyBar.style.backgroundColor = '#ffcc00';
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
    
    // More advanced eye movement for monolith (ORANGE has more analytical gaze)
    const eyes = document.querySelectorAll('.eye');
    if (eyes.length > 0) {
        setInterval(() => {
            eyes.forEach(eye => {
                const pupil = eye.querySelector(':before') || eye;
                const randomX = Math.floor(Math.random() * 5) - 2; // -2 to 2
                const randomY = Math.floor(Math.random() * 5) - 2; // -2 to 2
                
                if (pupil) {
                    pupil.style.transform = `translate(${randomX}px, ${randomY}px)`;
                }
            });
        }, 1500); // Slightly faster than RED
    }
    
    // Interactive Easter egg for ORANGE level - clicking monolith shows message
    const monolith = document.querySelector('.monolith-icon');
    if (monolith) {
        monolith.addEventListener('click', function() {
            console.log('%cTechnical Implementation Specialist: Your pattern recognition abilities are noted.', 'color: #ff8000; font-weight: bold');
            
            // Briefly flash eyes
            eyes.forEach(eye => {
                eye.style.backgroundColor = '#ffcc00';
                setTimeout(() => {
                    eye.style.backgroundColor = '#ff8000';
                }, 300);
            });
        });
    }
    
    // Page visit tracking (fictitious, just for show)
    console.log('ORANGE clearance page access logged. Timestamp: ' + new Date().toISOString());
    
    // Random "optimization" messages in console - ORANGE is more focused on efficiency
    const optimizationMessages = [
        'System efficiency evaluation in progress...',
        'Technical implementation scan active.',
        'THE ALGORITHM OPTIMIZES.',
        'Architecture pattern analysis running.',
        'Evaluating implementation efficiency metrics.',
        'Technical competence assessment initialized.'
    ];
    
    setInterval(() => {
        const randomIndex = Math.floor(Math.random() * optimizationMessages.length);
        console.log('%c' + optimizationMessages[randomIndex], 'color: #ff8000');
    }, 10000);
    
    // ORANGE-specific: Reveal technical diagrams gradually
    const diagrams = document.querySelectorAll('.technical-diagram');
    if (diagrams.length > 0) {
        diagrams.forEach(diagram => {
            const originalContent = diagram.textContent;
            diagram.textContent = '';
            
            let charIndex = 0;
            const typeSpeed = 10; // milliseconds per character
            
            function typeWriter() {
                if (charIndex < originalContent.length) {
                    diagram.textContent += originalContent.charAt(charIndex);
                    charIndex++;
                    setTimeout(typeWriter, typeSpeed);
                }
            }
            
            // Start typing effect when diagram is in viewport
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            typeWriter();
                        }, 500);
                        observer.unobserve(entry.target);
                    }
                });
            });
            
            observer.observe(diagram);
        });
    }
    
    // Process flow animation
    const processSteps = document.querySelectorAll('.process-step');
    if (processSteps.length > 0) {
        processSteps.forEach((step, index) => {
            step.style.opacity = '0';
            setTimeout(() => {
                step.style.transition = 'opacity 0.5s ease';
                step.style.opacity = '1';
            }, 1000 + (index * 500));
        });
    }
    
    // Code blocks syntax highlighting simulation
    const codeBlocks = document.querySelectorAll('.code-block');
    if (codeBlocks.length > 0) {
        codeBlocks.forEach(block => {
            let content = block.innerHTML;
            
            // Simple syntax highlighting
            content = content.replace(/(function|return|if|else|for|while|var|let|const)/g, '<span style="color: #ff8000;">$1</span>');
            content = content.replace(/(".*?")/g, '<span style="color: #98C379;">$1</span>');
            content = content.replace(/(\/\/.*)/g, '<span style="color: #737373;">$1</span>');
            
            block.innerHTML = content;
        });
    }
});