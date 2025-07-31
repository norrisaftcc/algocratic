# Deploy Website to Separate Repository

## User Story
As a maintainer, I want the website to be deployed from an entirely different repository so that deployment concerns are separated from content development, and the deployment repo can handle all GitHub Actions independently.

## Implementation Plan

### Phase 1: Create Deployment Repository
- [ ] Create new repository: `algocratic-deploy`
- [ ] Configure repository settings for GitHub Pages
- [ ] Set up repository secrets for deployment

### Phase 2: Set Up GitHub Actions Workflow
- [ ] Create `.github/workflows/deploy.yml` in deployment repo
- [ ] Configure workflow to:
  - Trigger on schedule (e.g., every hour) or manual dispatch
  - Clone content from main algocratic repo
  - Build static site if needed
  - Deploy to GitHub Pages

### Phase 3: Configure Cross-Repository Access
- [ ] Set up deploy keys or GitHub App for secure access
- [ ] Configure read access to main algocratic repository
- [ ] Test authentication and cloning

### Phase 4: Migration Steps
- [ ] Document current GitHub Pages configuration
- [ ] Create migration checklist
- [ ] Test deployment in staging
- [ ] Update DNS/CNAME if needed
- [ ] Switch production deployment

## Technical Details

### Proposed Workflow Structure
```yaml
name: Deploy AlgoCratic Site
on:
  schedule:
    - cron: '0 * * * *'  # Every hour
  workflow_dispatch:  # Manual trigger

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout deployment repo
        uses: actions/checkout@v3
        
      - name: Clone content repository
        run: |
          git clone https://github.com/norrisaftcc/algocratic.git content
          
      - name: Copy website files
        run: |
          cp -r content/website/* ./
          cp content/index.html ./
          cp content/INDEX.HTM ./
          # Copy other necessary files
          
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

## Benefits
1. **Separation of Concerns**: Content development separate from deployment
2. **Independent CI/CD**: Deployment repo manages its own Actions minutes
3. **Security**: Main repo doesn't need deployment secrets
4. **Flexibility**: Can add build steps, optimization, etc. without affecting main repo

## Risks & Mitigation
- **Sync Issues**: Mitigate with frequent scheduled deployments
- **Access Control**: Use deploy keys with read-only access
- **Downtime**: Test thoroughly in staging environment first

## Acceptance Criteria
- [ ] Website deploys successfully from separate repository
- [ ] No manual intervention required for regular updates
- [ ] Documentation updated with new deployment process
- [ ] Team trained on new workflow

## Related Issues
- Depends on: Current GitHub Pages configuration documentation
- Blocks: Future CI/CD enhancements

## Estimated Effort
- Setup: 2-3 hours
- Testing: 1-2 hours
- Migration: 1 hour
- Documentation: 1 hour

Total: ~6 hours