# AlgoCratic Futures™ - Website Acceptance Test Guide

This guide provides step-by-step tests to verify all website functionality is working correctly.

## Quick Test Checklist

- [ ] Homepage loads and displays correctly
- [ ] Primary CTA works (Start Clearance Training)
- [ ] Employee Portal registration/login flow works
- [ ] All clearance levels are accessible
- [ ] Navigation links work
- [ ] Mobile responsive design functions

---

## Test Cases

### 1. Homepage Tests

**Test 1.1: Homepage Load**
1. Navigate to `INDEX.HTM`
2. ✓ Verify page loads with terminal aesthetic
3. ✓ Verify "ALGOCRATIC FUTURES™" title displays
4. ✓ Verify "START CLEARANCE TRAINING" button is prominent
5. ✓ Verify footer shows "MIT+xyzzy"

**Test 1.2: Homepage Navigation**
1. From homepage, verify these links work:
   - [ ] "START CLEARANCE TRAINING" → `website/clearance/`
   - [ ] "View All Clearance Levels" → `website/clearance/`
   - [ ] "Employee Portal" → `login.html`
   - [ ] "About This Project" → `about.html`
   - [ ] "GitHub Repository" → External GitHub link

---

### 2. Employee Portal Tests

**Test 2.1: Registration Flow (The Word Test)**
1. Navigate to Employee Portal from homepage
2. Click "Create Account" on login page
3. Enter test username: `testuser`
4. Enter incorrect word: `password`
5. ✓ Verify error: "Incorrect. Perhaps review our documentation."
6. Enter correct word: `xyzzy`
7. ✓ Verify success message shows
8. ✓ Verify redirect to portal after 3 seconds

**Test 2.2: Login Flow**
1. Navigate to Employee Portal
2. Enter credentials:
   - Username: `testuser`
   - Password: `xyzzy`
3. ✓ Verify login successful
4. ✓ Verify portal shows welcome message with username
5. ✓ Verify clearance level displays as "RED"
6. ✓ Verify logout works and returns to main site

**Test 2.3: Portal Access Control**
1. Clear browser storage/cookies
2. Try to access `portal.html` directly
3. ✓ Verify redirect to login page
4. ✓ Verify cannot access portal without authentication

---

### 3. Clearance Level Tests

**Test 3.1: Clearance Index Page**
1. Click "START CLEARANCE TRAINING" from homepage
2. Navigate to `website/clearance/`
3. ✓ Verify clearance level list displays
4. ✓ Verify all levels shown:
   - [ ] INFRARED (Onboarding)
   - [ ] RED
   - [ ] ORANGE  
   - [ ] YELLOW
   - [ ] GREEN
   - [ ] BLUE
   - [ ] VIOLET

**Test 3.2: Individual Clearance Levels**
Test each clearance level has content:
1. Navigate to each level from clearance index
2. Verify each has:
   - [ ] Header with level name
   - [ ] Content/exercises
   - [ ] Navigation back to index

---

### 4. About Page Tests

**Test 4.1: About Page Content**
1. Navigate to About page from homepage
2. ✓ Verify ASCII art logo displays
3. ✓ Verify sections present:
   - [ ] THE ALGORITHM PROVIDES
   - [ ] CLEARANCE-BASED PROGRESSION
   - [ ] EDUCATIONAL PHILOSOPHY
   - [ ] OPEN SOURCE
4. ✓ Verify MIT+xyzzy license mentioned

---

### 5. Mobile Responsiveness Tests

**Test 5.1: Mobile View (< 600px width)**
1. Resize browser to mobile width or use device emulator
2. Test on homepage:
   - [ ] Text remains readable
   - [ ] CTA button is tappable
   - [ ] Navigation links stack properly
3. Test on portal pages:
   - [ ] Forms are usable
   - [ ] Inputs are accessible

**Test 5.2: Tablet View (768px width)**
1. Resize to tablet width
2. ✓ Verify layout adjusts appropriately
3. ✓ Verify no horizontal scrolling needed

---

### 6. Cross-Browser Tests

Test on major browsers:
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari
- [ ] Edge

For each browser verify:
1. Terminal aesthetic displays correctly
2. Forms function properly
3. Navigation works
4. No console errors

---

### 7. Accessibility Quick Checks

**Test 7.1: Keyboard Navigation**
1. Use Tab key to navigate through site
2. ✓ Verify all interactive elements are reachable
3. ✓ Verify focus indicators are visible

**Test 7.2: Text Readability**
1. ✓ Verify text has sufficient contrast
2. ✓ Verify monospace font is readable
3. ✓ Verify text can be zoomed to 200%

---

## Common Issues & Solutions

### Issue: "What's the word?" not accepting answer
- **Solution**: Ensure entering `xyzzy` (lowercase)
- **Note**: The word is hidden in LICENSE file as "MIT+xyzzy"

### Issue: Cannot access Employee Portal
- **Solution**: Must register first, then login
- **Note**: Uses localStorage for demo purposes

### Issue: Clearance pages not loading
- **Solution**: Check file paths match structure:
  - `website/clearance/index.html`
  - `website/clearance/green/index.html` (etc.)

### Issue: Styles not loading
- **Solution**: Ensure all CSS is inline (no external stylesheets for main pages)

---

## Test Completion

**Minimum Acceptance Criteria:**
- [ ] All homepage links functional
- [ ] Employee registration/login works
- [ ] Can navigate to all clearance levels
- [ ] Mobile responsive design verified
- [ ] No broken links or missing pages

**Date Tested**: ___________
**Tested By**: ___________
**Browser(s)**: ___________
**Issues Found**: ___________

---

*Remember: The Algorithm is watching your testing compliance.*