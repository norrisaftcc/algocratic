# AlgoCratic Website Manual Test Plan
## Design & Accessibility Compliance Verification

### Test Information
- **Test Plan Version**: 1.0
- **Last Updated**: August 1, 2025
- **Tester Name**: _______________
- **Test Date**: _______________
- **Browser/Device**: _______________

### Pre-Test Setup
- [ ] Clear browser cache
- [ ] Disable browser extensions (especially ad blockers)
- [ ] Have screen reader software ready (NVDA/JAWS/VoiceOver)
- [ ] Have browser dev tools open for contrast checking

---

## 1. DESIGN CONSISTENCY TESTS

### 1.1 Console/Terminal Aesthetic
**Expected**: All pages should use consistent console/terminal styling

| Page | Console Theme Present | No Windows 98 Elements | Pass/Fail |
|------|----------------------|------------------------|-----------|
| Home (INDEX.HTM) | ☐ | ☐ | ☐ |
| Apache Directory (index.html) | ☐ | ☐ | ☐ |
| Employee Portal (portal.html) | ☐ | ☐ | ☐ |
| Orientation Packet | ☐ | ☐ | ☐ |
| Clearance Index | ☐ | ☐ | ☐ |
| GREEN Clearance | ☐ | ☐ | ☐ |
| GRAY Clearance | ☐ | ☐ | ☐ |

**Notes**: _________________________________________________

### 1.2 Typography Consistency
- [ ] Monospace font used consistently
- [ ] Font sizes readable at 100% zoom
- [ ] Text remains readable at 200% zoom
- [ ] No text overlaps at different zoom levels

### 1.3 Color Scheme
- [ ] Dark background (#0a0a0a - #1a1a1a range)
- [ ] Phosphor green accents (#00ff41)
- [ ] Appropriate clearance colors where used
- [ ] No conflicting color schemes

---

## 2. ACCESSIBILITY TESTS (WCAG 2.1 AA)

### 2.1 Keyboard Navigation
**Test**: Tab through entire site using only keyboard

| Test | Pass/Fail | Notes |
|------|-----------|-------|
| Can reach all interactive elements | ☐ | |
| Tab order is logical | ☐ | |
| Skip navigation link present | ☐ | |
| Focus indicators visible | ☐ | |
| No keyboard traps | ☐ | |

### 2.2 Screen Reader Testing
**Test**: Navigate with screen reader enabled

| Element | Properly Announced | Pass/Fail |
|---------|-------------------|-----------|
| Page titles | ☐ | ☐ |
| Headings hierarchy | ☐ | ☐ |
| Links (descriptive text) | ☐ | ☐ |
| Images (alt text) | ☐ | ☐ |
| Form labels | ☐ | ☐ |
| Error messages | ☐ | ☐ |

### 2.3 Color Contrast
**Tool**: Use browser dev tools or WebAIM contrast checker

| Text Type | Foreground | Background | Ratio | Pass (4.5:1) |
|-----------|------------|------------|-------|--------------|
| Body text | | | | ☐ |
| Heading text | | | | ☐ |
| Link text | | | | ☐ |
| Button text | | | | ☐ |
| Error text | | | | ☐ |

### 2.4 Responsive Design
**Test**: Resize browser window and test on mobile

| Viewport | Layout Intact | Text Readable | No Horizontal Scroll | Pass/Fail |
|----------|--------------|---------------|---------------------|-----------|
| Desktop (1920px) | ☐ | ☐ | ☐ | ☐ |
| Laptop (1366px) | ☐ | ☐ | ☐ | ☐ |
| Tablet (768px) | ☐ | ☐ | ☐ | ☐ |
| Mobile (375px) | ☐ | ☐ | ☐ | ☐ |

---

## 3. FUNCTIONAL TESTS

### 3.1 Navigation
- [ ] All navigation links work
- [ ] No broken links (404 errors)
- [ ] Back button works correctly
- [ ] External links open in new tab (if applicable)

### 3.2 Interactive Elements
- [ ] Buttons have hover states
- [ ] Forms submit correctly
- [ ] Error messages display appropriately
- [ ] Loading states shown where needed

### 3.3 Console-Specific Features
- [ ] Terminal cursor animations work
- [ ] Glitch effects don't impair readability
- [ ] ASCII art displays correctly
- [ ] Monospace alignment maintained

---

## 4. PERFORMANCE CHECKS

### 4.1 Page Load Times
| Page | Load Time | Acceptable (<3s) |
|------|-----------|------------------|
| Home | ___s | ☐ |
| Portal | ___s | ☐ |
| Clearance Pages | ___s | ☐ |

### 4.2 Asset Loading
- [ ] Images load properly
- [ ] CSS loads before content renders
- [ ] No missing resources in console
- [ ] Fonts load without FOUT/FOIT

---

## 5. CROSS-BROWSER TESTING

| Browser | Version | Renders Correctly | Functions Work | Pass/Fail |
|---------|---------|------------------|----------------|-----------|
| Chrome | | ☐ | ☐ | ☐ |
| Firefox | | ☐ | ☐ | ☐ |
| Safari | | ☐ | ☐ | ☐ |
| Edge | | ☐ | ☐ | ☐ |

---

## 6. CRITICAL ISSUES CHECKLIST

**MUST FIX before deployment:**
- [ ] No JavaScript errors in console
- [ ] All text readable (contrast passes)
- [ ] Keyboard navigation works fully
- [ ] No broken links
- [ ] Mobile responsive
- [ ] Console theme consistent

---

## TEST SUMMARY

**Total Tests**: _____ 
**Passed**: _____ 
**Failed**: _____

### Critical Issues Found:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

### Recommendations:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

### Tester Signature: ___________________ Date: ___________

---

**THE ALGORITHM DEMANDS PERFECTION IN USER EXPERIENCE**