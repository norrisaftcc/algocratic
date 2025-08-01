# Integrate Gollum Wiki for Internal Documentation

## User Story
As a team member, I want an internal wiki integrated into the AlgoCratic website so that we can maintain living documentation using Gollum's git-based wiki system.

## Implementation Plan

### Phase 1: Create Wiki Repository
- [ ] Create new repository: `algocratic-wiki`
- [ ] Initialize with README and basic structure
- [ ] Configure Gollum-compatible markdown setup

### Phase 2: Set Up Gollum Instance
- [ ] Option A: Use GitHub Wiki (built on Gollum)
  - Enable wiki on algocratic-wiki repo
  - Configure access permissions
- [ ] Option B: Self-host Gollum
  - Set up Gollum on hosting platform
  - Configure authentication
  - Set up reverse proxy

### Phase 3: Website Integration
- [ ] Create wiki entry point in main site navigation
- [ ] Design wiki access page matching AlgoCratic aesthetic
- [ ] Implement authentication/clearance check for wiki access
- [ ] Set up iframe or subdomain integration

### Phase 4: Content Structure
- [ ] Create initial wiki structure:
  ```
  Home.md
  Clearance-Guides/
    - INFRARED.md
    - RED.md
    - ... (other clearances)
  Technical-Documentation/
    - Architecture.md
    - API-Reference.md
  Department-Procedures/
    - Design-Compliance.md
    - Truth-Verification.md
  Employee-Resources/
    - Onboarding.md
    - Sacred-Flow.md
  ```

## Technical Details

### Integration Approach A: GitHub Wiki
```html
<!-- In website/wiki/index.html -->
<div class="wiki-container">
  <iframe 
    src="https://github.com/norrisaftcc/algocratic-wiki/wiki" 
    class="wiki-frame"
    sandbox="allow-same-origin allow-scripts">
  </iframe>
</div>
```

### Integration Approach B: Subdomain
```nginx
# Nginx configuration
server {
  server_name wiki.algocratic.norrisaftcc.github.io;
  location / {
    proxy_pass http://localhost:4567; # Gollum default port
  }
}
```

### Integration Approach C: Direct Link
```html
<!-- Simpler approach -->
<div class="wiki-portal">
  <h2>AlgoCratic Internal Wiki</h2>
  <p>Access restricted to cleared personnel only</p>
  <a href="https://github.com/norrisaftcc/algocratic-wiki/wiki" 
     class="wiki-access-button"
     target="_blank">
    ACCESS WIKI [CLEARANCE REQUIRED]
  </a>
</div>
```

## Wiki Features to Leverage
1. **Git-based**: All changes tracked in git history
2. **Markdown Support**: Compatible with our existing docs
3. **Search**: Built-in search functionality
4. **File Uploads**: Support for images and attachments
5. **Access Control**: Via GitHub permissions

## Styling Considerations
```css
/* AlgoCratic Wiki Theme */
.wiki-container {
  background: var(--dark-bg);
  border: 1px solid var(--phosphor-green);
  padding: 20px;
}

.wiki-frame {
  width: 100%;
  min-height: 600px;
  border: none;
  filter: invert(1) hue-rotate(90deg); /* Dark mode hack */
}
```

## Benefits
1. **Version Control**: All wiki changes in git
2. **Familiar Interface**: Team already knows GitHub
3. **No Additional Hosting**: Uses GitHub infrastructure
4. **Markdown-based**: Easy to write and maintain
5. **Searchable**: Built-in search functionality

## Acceptance Criteria
- [ ] Wiki repository created and configured
- [ ] Wiki accessible from main AlgoCratic site
- [ ] Initial content structure in place
- [ ] Authentication/access control configured
- [ ] Styling matches AlgoCratic aesthetic
- [ ] Documentation for wiki contribution process

## Related Issues
- Related to: #24 (Deployment separation - wiki could be deployed separately)
- Enhances: Employee onboarding experience

## Estimated Effort
- Repository setup: 1 hour
- Integration development: 2-3 hours
- Initial content creation: 2-3 hours
- Testing and refinement: 1-2 hours

Total: ~8 hours

## Notes
- Consider starting with GitHub Wiki for MVP, migrate to self-hosted later if needed
- Wiki content should maintain the AlgoCratic dystopian theme
- Could integrate with clearance system for page-level access control