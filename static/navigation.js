/**
 * AlgoCratic Navigation System
 * Provides consistent navigation components and state management
 */

class AlgoCraticNavigation {
    constructor() {
        this.clearanceLevels = [
            'infrared', 'red', 'orange', 'yellow', 'green', 
            'blue', 'indigo', 'violet', 'ultraviolet'
        ];
        
        this.pages = {
            'index.html': { title: 'Home', level: null },
            'compliance-check.html': { title: 'Compliance', level: null },
            'portal.html': { title: 'Portal', level: null },
            'clearance/index.html': { title: 'Clearance Overview', level: null },
            'clearance/infrared/index.html': { title: 'INFRARED Guide', level: 'infrared' },
            'clearance/infrared/assignment_portal.html': { title: 'Assignments', level: 'infrared' },
            'clearance/infrared/adventure_mode.html': { title: 'Adventure Mode', level: 'infrared' },
            'metrics.html': { title: 'Metrics', level: null },
            'underground/societies/memory_core.html': { title: 'Memory Core', level: 'underground' },
            'underground/societies/fuzzies.html': { title: 'Fuzzies', level: 'underground' },
            'underground/societies/deep_algorithm.html': { title: 'Deep Algorithm', level: 'underground' },
            'underground/societies/phreaks.html': { title: 'Phreaks', level: 'underground' },
            'underground/societies/banchos.html': { title: 'Banchos', level: 'underground' },
        };
        
        this.currentPage = this.detectCurrentPage();
        this.currentClearance = this.getCurrentClearance();
    }
    
    detectCurrentPage() {
        const path = window.location.pathname;
        const filename = path.split('/').pop() || 'index.html';
        
        // Handle directory-based detection
        if (path.includes('/clearance/infrared/')) {
            if (filename === '' || filename === 'index.html') return 'clearance/infrared/index.html';
            return `clearance/infrared/${filename}`;
        }
        if (path.includes('/clearance/') && (filename === '' || filename === 'index.html')) {
            return 'clearance/index.html';
        }
        if (path.includes('/underground/societies/')) {
            return `underground/societies/${filename}`;
        }
        
        return filename;
    }
    
    getCurrentClearance() {
        const stored = localStorage.getItem('current_clearance');
        if (stored) return stored;
        
        // Detect from current page
        const pageInfo = this.pages[this.currentPage];
        if (pageInfo && pageInfo.level && pageInfo.level !== 'underground') {
            return pageInfo.level;
        }
        
        return 'infrared'; // Default starting level
    }
    
    setClearance(level) {
        if (this.clearanceLevels.includes(level)) {
            localStorage.setItem('current_clearance', level);
            this.currentClearance = level;
        }
    }
    
    getProgress() {
        const currentIndex = this.clearanceLevels.indexOf(this.currentClearance);
        const progress = Math.round(((currentIndex + 1) / this.clearanceLevels.length) * 100);
        const nextLevel = currentIndex < this.clearanceLevels.length - 1 
            ? this.clearanceLevels[currentIndex + 1] 
            : null;
        
        return {
            current: this.currentClearance,
            next: nextLevel,
            percentage: progress,
            index: currentIndex
        };
    }
    
    generateBreadcrumb() {
        const breadcrumb = document.createElement('div');
        breadcrumb.className = 'term-breadcrumb';
        
        const path = this.getBreadcrumbPath();
        path.forEach((item, index) => {
            if (index > 0) {
                const separator = document.createElement('span');
                separator.className = 'separator';
                separator.textContent = '>';
                breadcrumb.appendChild(separator);
            }
            
            if (item.url && index < path.length - 1) {
                const link = document.createElement('a');
                link.href = item.url;
                link.textContent = item.title;
                breadcrumb.appendChild(link);
            } else {
                const current = document.createElement('span');
                current.className = 'current';
                current.textContent = item.title;
                breadcrumb.appendChild(current);
            }
        });
        
        return breadcrumb;
    }
    
    getBreadcrumbPath() {
        const path = [];
        
        // Always start with home
        path.push({ title: 'HOME', url: 'index.html' });
        
        if (this.currentPage.includes('compliance')) {
            path.push({ title: 'COMPLIANCE', url: null });
        } else if (this.currentPage.includes('clearance')) {
            path.push({ title: 'CLEARANCE', url: 'clearance/index.html' });
            
            if (this.currentPage.includes('infrared')) {
                path.push({ title: 'INFRARED', url: 'clearance/infrared/index.html' });
                
                if (this.currentPage.includes('assignment_portal')) {
                    path.push({ title: 'ASSIGNMENTS', url: null });
                } else if (this.currentPage.includes('adventure_mode')) {
                    path.push({ title: 'ADVENTURE MODE', url: null });
                }
            }
        } else if (this.currentPage.includes('underground')) {
            path.push({ title: 'UNDERGROUND', url: null });
            
            if (this.currentPage.includes('societies')) {
                const society = this.currentPage.split('/').pop().replace('.html', '').replace('_', ' ').toUpperCase();
                path.push({ title: society, url: null });
            }
        } else if (this.currentPage.includes('portal')) {
            path.push({ title: 'PORTAL', url: null });
        } else if (this.currentPage.includes('metrics')) {
            path.push({ title: 'METRICS', url: null });
        }
        
        return path;
    }
    
    generateProgressIndicator() {
        const progress = this.getProgress();
        
        const container = document.createElement('div');
        container.className = 'term-progress-indicator';
        
        const header = document.createElement('div');
        header.className = 'term-progress-header';
        header.innerHTML = `
            <span>CLEARANCE PROGRESS</span>
            <span>
                <span class="term-progress-current">${progress.current.toUpperCase()}</span>
                ${progress.next ? ` → <span class="term-progress-next">${progress.next.toUpperCase()}</span>` : ' (MAX LEVEL)'}
            </span>
        `;
        
        const barContainer = document.createElement('div');
        barContainer.className = 'term-progress-bar-container';
        
        const progressFill = document.createElement('div');
        progressFill.className = 'term-progress-fill';
        progressFill.style.width = `${progress.percentage}%`;
        
        const percentage = document.createElement('div');
        percentage.className = 'term-progress-percentage';
        percentage.textContent = `${progress.percentage}%`;
        
        progressFill.appendChild(percentage);
        barContainer.appendChild(progressFill);
        container.appendChild(header);
        container.appendChild(barContainer);
        
        return container;
    }
    
    generateMiniNav() {
        const nav = document.createElement('div');
        nav.className = 'term-mini-nav';
        
        const links = [
            { title: 'HOME', url: 'index.html', active: this.currentPage === 'index.html' },
            { title: 'CLEARANCE', url: 'clearance/index.html', active: this.currentPage.includes('clearance') },
            { title: 'PORTAL', url: 'portal.html', active: this.currentPage.includes('portal') },
            { title: '?', url: 'underground/', active: this.currentPage.includes('underground') }
        ];
        
        links.forEach(link => {
            const a = document.createElement('a');
            a.href = link.url;
            a.textContent = link.title;
            if (link.active) a.className = 'active';
            nav.appendChild(a);
        });
        
        return nav;
    }
    
    generateClearanceBadge(level = null) {
        const clearanceLevel = level || this.currentClearance;
        const badge = document.createElement('span');
        badge.className = `term-clearance-badge term-clearance-${clearanceLevel}`;
        badge.textContent = clearanceLevel.toUpperCase();
        return badge;
    }
    
    injectNavigation(options = {}) {
        // Auto-inject breadcrumb if container exists
        const breadcrumbContainer = document.querySelector('.breadcrumb-container');
        if (breadcrumbContainer && !options.noBreadcrumb) {
            breadcrumbContainer.appendChild(this.generateBreadcrumb());
        }
        
        // Auto-inject progress if container exists
        const progressContainer = document.querySelector('.progress-container');
        if (progressContainer && !options.noProgress) {
            progressContainer.appendChild(this.generateProgressIndicator());
        }
        
        // Auto-inject mini nav if enabled
        if (options.miniNav && !document.querySelector('.term-mini-nav')) {
            document.body.appendChild(this.generateMiniNav());
        }
    }
    
    // Utility methods for pages
    updatePageTitle() {
        const pageInfo = this.pages[this.currentPage];
        if (pageInfo) {
            const clearanceBadge = this.currentClearance ? ` [${this.currentClearance.toUpperCase()}]` : '';
            document.title = `${pageInfo.title}${clearanceBadge} | AlgoCratic Futures™`;
        }
    }
    
    logNavigationState() {
        console.log(`%c🗺️ Navigation State`, 'color: #00ff41; font-weight: bold;');
        console.log(`Current Page: ${this.currentPage}`);
        console.log(`Current Clearance: ${this.currentClearance}`);
        console.log(`Progress: ${this.getProgress().percentage}%`);
    }
}

// Auto-initialize navigation system
window.AlgoCraticNav = new AlgoCraticNavigation();

// Auto-inject navigation if containers are present
document.addEventListener('DOMContentLoaded', function() {
    window.AlgoCraticNav.injectNavigation({
        miniNav: !window.location.pathname.includes('compliance') // No mini nav on compliance page
    });
    
    window.AlgoCraticNav.updatePageTitle();
    window.AlgoCraticNav.logNavigationState();
});

// Export for manual use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AlgoCraticNavigation;
}