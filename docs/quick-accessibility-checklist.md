# Quick Accessibility Checklist for AlgoCratic
## 5-Minute Manual Testing Guide

### 🎯 Priority 1: Critical (MUST PASS)

#### Keyboard Testing (2 min)
1. **Tab Test**: Press Tab repeatedly
   - ☐ Can reach every link/button
   - ☐ Can see where focus is (visible outline)
   - ☐ Can activate with Enter/Space

2. **Escape Test**: 
   - ☐ Can close any popups with Esc key
   - ☐ No keyboard traps (can Tab out of everything)

#### Contrast Testing (1 min)
1. **Squint Test**: Squint at the screen
   - ☐ Can still read all text
   - ☐ Links distinguishable from regular text
   
2. **Dev Tools Quick Check**:
   - Right-click text → Inspect → Look for contrast warnings
   - ☐ No contrast errors shown

#### Mobile Testing (2 min)
1. **Responsive Check**: 
   - ☐ Open dev tools → Toggle device toolbar
   - ☐ Check iPhone SE (375px) 
   - ☐ Check iPad (768px)
   - ☐ No horizontal scrolling
   - ☐ All text readable without zooming

---

### 🔍 Priority 2: Important (SHOULD PASS)

#### Screen Reader Basics (3 min)
1. **Turn on Screen Reader**:
   - Windows: NVDA (free)
   - Mac: Cmd+F5 for VoiceOver
   - ☐ Page title announced
   - ☐ Can navigate by headings (H key)
   - ☐ Links make sense out of context

2. **Image Check**:
   - ☐ Decorative images ignored
   - ☐ Important images have descriptions

#### Form Testing (2 min)
1. **Label Check**:
   - ☐ Every input has a visible label
   - ☐ Required fields marked clearly
   - ☐ Error messages associated with fields

---

### 🚨 RED FLAGS (Fix Immediately)

1. **Cannot Tab to something** → Add tabindex="0"
2. **No focus visible** → Add focus styles in CSS
3. **Text hard to read** → Increase contrast
4. **Horizontal scroll on mobile** → Fix responsive CSS
5. **Screen reader says "link link link"** → Add descriptive text

---

### 📋 Quick Report Template

```
ACCESSIBILITY TEST - [Date]
Tested by: [Name]

CRITICAL ISSUES:
☐ None found
☐ Issues found: [List]

Keyboard: [PASS/FAIL]
Contrast: [PASS/FAIL]  
Mobile: [PASS/FAIL]
Screen Reader: [PASS/FAIL]

Ready for deployment: [YES/NO]
```

---

### 🛠️ Testing Tools

**Free & Fast:**
- WAVE (browser extension)
- axe DevTools (browser extension)
- Chrome Lighthouse (built-in)

**Run in Console:**
```javascript
// Quick contrast check
document.querySelectorAll('*').forEach(el => {
  const style = getComputedStyle(el);
  const bg = style.backgroundColor;
  const fg = style.color;
  if (bg !== 'rgba(0, 0, 0, 0)' && fg !== 'rgba(0, 0, 0, 0)') {
    console.log(el, 'BG:', bg, 'FG:', fg);
  }
});
```

---

**Remember: If a user can't Tab to it, click it, or read it - it's broken!**

THE ALGORITHM IS ACCESSIBLE TO ALL