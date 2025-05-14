// RED Clearance Guide Scripts

document.addEventListener('DOMContentLoaded', function() {
    // Loyalty tracker fluctuation
    const loyaltyBar = document.querySelector('.loyalty-bar');
    const loyaltyStatus = document.querySelector('.loyalty-status');
    
    // Randomly fluctuate the loyalty bar
    setInterval(() => {
        const currentWidth = parseFloat(loyaltyBar.style.width);
        const fluctuation = (Math.random() * 6) - 3; // Random value between -3 and 3
        let newWidth = currentWidth + fluctuation;
        
        // Keep within 25-45% range (higher than INFRARED but still limited)
        newWidth = Math.max(25, Math.min(45, newWidth));
        loyaltyBar.style.width = newWidth + '%';
        
        // Update status text
        if (newWidth < 30) {
            loyaltyStatus.textContent = 'MARGINAL';
            loyaltyBar.style.backgroundColor = '#ff3030';
        } else if (newWidth < 40) {
            loyaltyStatus.textContent = 'ACCEPTABLE';
            loyaltyBar.style.backgroundColor = '#ff0000';
        } else {
            loyaltyStatus.textContent = 'COMMENDABLE';
            loyaltyBar.style.backgroundColor = '#ff0000';
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
    
    // Random eye movement for monolith
    const eyes = document.querySelectorAll('.eye');
    if (eyes.length > 0) {
        setInterval(() => {
            eyes.forEach(eye => {
                const pupil = eye.querySelector(':before') || eye;
                const randomX = Math.floor(Math.random() * 3) - 1; // -1, 0, or 1
                const randomY = Math.floor(Math.random() * 3) - 1; // -1, 0, or 1
                
                if (pupil) {
                    pupil.style.transform = `translate(${randomX}px, ${randomY}px)`;
                }
            });
        }, 2000);
    }
    
    // Page visit tracking (fictitious, just for show)
    console.log('RED clearance page access logged. Timestamp: ' + new Date().toISOString());
    
    // Random "surveillance" messages in console
    const surveillanceMessages = [
        'User activity monitored.',
        'Loyalty assessment in progress...',
        'THE ALGORITHM IS WATCHING.',
        'Behavioral pattern analysis active.',
        'Thought compliance verification initiated.'
    ];
    
    setInterval(() => {
        const randomIndex = Math.floor(Math.random() * surveillanceMessages.length);
        console.log('%c' + surveillanceMessages[randomIndex], 'color: #ff0000');
    }, 10000);
});