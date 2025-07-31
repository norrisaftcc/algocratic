# AlgoCratic Deployment Repository Setup Guide

## Overview
This guide walks through setting up the `algocratic-deploy` repository for automated website deployment.

## Step 1: Create Deployment Repository

1. Create new repository: `algocratic-deploy`
2. Initialize with README
3. Enable GitHub Pages from `gh-pages` branch

## Step 2: Create Deployment Workflow

Create `.github/workflows/deploy.yml` in the deployment repository:

```yaml
name: Deploy AlgoCratic Site
on:
  schedule:
    - cron: '0 * * * *'  # Every hour
  workflow_dispatch:      # Manual trigger
  
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pages: write
      id-token: write
      
    steps:
      - name: Checkout deployment repo
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          
      - name: Clone content repository
        run: |
          git clone https://github.com/norrisaftcc/algocratic.git content
          
      - name: Prepare deployment directory
        run: |
          # Create deploy directory
          mkdir -p deploy
          
          # Copy website files
          cp -r content/website/* deploy/
          cp content/index.html deploy/
          cp content/INDEX.HTM deploy/
          cp content/portal.html deploy/
          cp content/orientation_packet.html deploy/
          
          # Copy other necessary files
          cp -r content/static deploy/ 2>/dev/null || true
          cp -r content/docs deploy/ 2>/dev/null || true
          cp -r content/forms deploy/ 2>/dev/null || true
          
          # Create CNAME if needed
          echo "norrisaftcc.github.io" > deploy/CNAME
          
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
          publish_branch: gh-pages
          force_orphan: true
```

## Step 3: Configure Repository Settings

1. Go to Settings → Pages
2. Set Source to "Deploy from a branch"
3. Select `gh-pages` branch and `/ (root)`
4. Custom domain (if applicable)

## Step 4: Initial Deployment

1. Run the workflow manually from Actions tab
2. Verify deployment at: `https://[username].github.io/algocratic-deploy/`

## Step 5: Migration Plan

### Phase 1: Parallel Running
- Keep existing deployment active
- Test new deployment thoroughly
- Monitor for issues

### Phase 2: DNS Update (if using custom domain)
- Update CNAME records
- Wait for propagation
- Verify SSL certificate

### Phase 3: Deprecate Old Deployment
- Remove GitHub Pages from main repo
- Archive old workflow files
- Update documentation

## Monitoring

The deployment workflow includes:
- Scheduled runs every hour
- Manual trigger capability
- Build status notifications

## Rollback Procedure

If issues arise:
1. Re-enable GitHub Pages on main repository
2. Revert DNS changes if applicable
3. Investigate deployment issues
4. Fix and retry migration

## Benefits

- **Separation of Concerns**: Content vs deployment
- **Independent CI/CD**: Separate Actions minutes
- **Security**: Deployment secrets isolated
- **Flexibility**: Easy to add build steps

## Next Steps

After successful setup:
1. Add build optimizations
2. Implement cache strategies
3. Add deployment notifications
4. Create staging environment

---

**THE ALGORITHM DEMANDS EFFICIENT DEPLOYMENT**