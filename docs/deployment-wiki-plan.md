# AlgoCratic Infrastructure Expansion Plan

## Overview
This document outlines the implementation plan for two major infrastructure improvements:
1. **Deployment Repository Separation** - Moving deployment to a dedicated repository
2. **Gollum Wiki Integration** - Adding internal documentation wiki

## Implementation Timeline

### Week 1: Foundation
**Issue #24: Deploy Website to Separate Repository**
- PR #24.1: Create deployment repository documentation
- PR #24.2: Set up `algocratic-deploy` repository
- PR #24.3: Implement GitHub Actions workflow
- PR #24.4: Test deployment pipeline

**Issue #25: Integrate Gollum Wiki**
- PR #25.1: Create wiki repository structure
- PR #25.2: Design wiki integration page
- PR #25.3: Implement wiki portal in main site

### Week 2: Integration & Testing
- PR #24.5: Migrate production deployment
- PR #25.4: Populate initial wiki content
- PR #25.5: Style wiki interface to match AlgoCratic theme

## Repository Structure After Implementation

```
github.com/norrisaftcc/
├── algocratic/                 # Main content repository
│   ├── website/               # Website source files
│   ├── docs/                  # Development documentation
│   └── .github/               # Issue templates, workflows (optional)
│
├── algocratic-deploy/         # Deployment repository
│   ├── .github/
│   │   └── workflows/
│   │       └── deploy.yml     # Automated deployment workflow
│   └── README.md              # Deployment documentation
│
└── algocratic-wiki/           # Wiki repository
    └── (GitHub Wiki or Gollum content)
```

## Benefits of This Architecture

### Deployment Separation
- **Clean Separation**: Content development isolated from deployment infrastructure
- **Independent CI/CD**: Each repo manages its own GitHub Actions minutes
- **Security**: Deployment secrets isolated in deployment repo
- **Flexibility**: Can modify deployment without touching content

### Wiki Integration
- **Living Documentation**: Git-based wiki grows with the project
- **Familiar Tools**: Uses GitHub/Gollum that team already knows
- **Version Control**: All documentation changes tracked
- **Search & Organization**: Built-in wiki features

## PR Workflow Example

### For Deployment Repository Setup (Issue #24)
```bash
# In algocratic repo
git checkout -b feature/deployment-docs
# Create documentation for deployment process
git add docs/deployment-setup.md
git commit -m "docs: Add deployment repository setup guide"
git push origin feature/deployment-docs
# Create PR #24.1

# In new algocratic-deploy repo
git checkout -b feature/github-actions
# Add .github/workflows/deploy.yml
git add .
git commit -m "feat: Add automated deployment workflow"
git push origin feature/github-actions
# Create PR in algocratic-deploy repo
```

### For Wiki Integration (Issue #25)
```bash
# In algocratic repo
git checkout -b feature/wiki-portal
# Create website/wiki/index.html
git add website/wiki/
git commit -m "feat: Add wiki portal page"
git push origin feature/wiki-portal
# Create PR #25.2

# In algocratic-wiki repo
# Add initial wiki content via GitHub web interface or git
```

## Configuration Management

### Environment Variables
```yaml
# algocratic-deploy/.github/workflows/deploy.yml
env:
  SOURCE_REPO: norrisaftcc/algocratic
  SOURCE_BRANCH: main
  DEPLOY_BRANCH: gh-pages
```

### Secrets Required
- `DEPLOY_KEY`: Read access to algocratic repo (if private)
- `GITHUB_TOKEN`: Provided by Actions for deployment

## Testing Strategy

### Deployment Testing
1. Create test branch in algocratic
2. Trigger manual deployment workflow
3. Verify site updates correctly
4. Test scheduled deployments

### Wiki Testing
1. Create test content in wiki
2. Verify accessibility from main site
3. Test different clearance levels (if implemented)
4. Validate search functionality

## Rollback Plan

### Deployment
- Keep current GitHub Pages setup until new system proven
- Document current configuration completely
- Can revert to direct deployment if needed

### Wiki
- Wiki is additive, no risk to existing functionality
- Can remove integration page if issues arise
- Wiki repo remains useful even if not integrated

## Success Metrics
- [ ] Zero-downtime migration to new deployment system
- [ ] Automated deployments running successfully
- [ ] Wiki accessible and populated with initial content
- [ ] Team actively using wiki for documentation
- [ ] Reduced deployment-related commits in main repo

## Next Steps
1. Create Issue #24 and Issue #25 in GitHub
2. Assign team members to each issue
3. Begin with deployment repository (more critical path)
4. Wiki can be developed in parallel

---

**THE ALGORITHM DEMANDS EFFICIENT INFRASTRUCTURE**