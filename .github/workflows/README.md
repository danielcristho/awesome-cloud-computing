# GitHub Actions Workflows

This directory contains automated workflows for maintaining the Awesome Cloud Computing project.

## 🔄 Workflows

### `check.yml` - Quality Checks

**Triggers:** Push and Pull Requests to `main` and `develop` branches

**Jobs:**
1. **Markdown Lint** - Validates markdown formatting
2. **Awesome Lint** - Checks compliance with Awesome List standards
3. **MkDocs Build Test** - Ensures documentation builds successfully
4. **Language Configuration Check** - Validates language configurations

**Purpose:** Ensures code quality and prevents broken builds before merging.

---

### `links.yml` - Link Checker

**Triggers:** 
- Daily at 18:00 UTC (scheduled)
- Manual trigger (workflow_dispatch)
- Repository dispatch events

**What it does:**
- Scans all markdown files for broken links
- Checks external URLs for availability
- Creates GitHub issues for broken links
- Excludes social media links (LinkedIn, Twitter, Facebook)

**Configuration:**
- Max retries: 3
- Timeout: 20 seconds per link
- Excludes email addresses

**Output:** Creates an issue with broken links report if any are found.

---

### `deploy.yml` - Deploy to GitHub Pages

**Triggers:**
- Push to `main` branch
- Manual trigger (workflow_dispatch)

**What it does:**
1. Builds MkDocs site with all languages
2. Uploads build artifacts
3. Deploys to GitHub Pages

**Requirements:**
- GitHub Pages must be enabled in repository settings
- Source: GitHub Actions

**URL:** https://danielcristho.github.io/awesome-cloud-computing

---

### `sync-content.yml` - Content Synchronization

**Triggers:** Push to `main` branch

**What it does:**
- Synchronizes content between different formats
- Generates README.md from documentation
- Updates content across language versions

---

## 🔧 Maintenance

### Running Workflows Manually

1. Go to **Actions** tab in GitHub
2. Select the workflow you want to run
3. Click **Run workflow**
4. Choose the branch and click **Run workflow**

### Debugging Failed Workflows

1. Click on the failed workflow run
2. Expand the failed job
3. Check the logs for error messages
4. Fix the issue and push changes

### Common Issues

#### Markdown Lint Failures
- Check markdown formatting
- Ensure consistent heading levels
- Fix trailing spaces and line endings

#### MkDocs Build Failures
- Verify all referenced files exist
- Check `mkdocs.yml` syntax
- Ensure all language folders are present

#### Link Checker Issues
- Review broken links in the created issue
- Update or remove broken URLs
- Check if sites are temporarily down

## 📝 Adding New Workflows

When adding a new workflow:

1. Create a new `.yml` file in this directory
2. Follow GitHub Actions syntax
3. Add appropriate triggers
4. Include error handling
5. Document it in this README
6. Test with a pull request

## 🔐 Secrets and Permissions

### Required Permissions

- **check.yml**: `contents: read`
- **links.yml**: `issues: write`
- **deploy.yml**: `contents: read`, `pages: write`, `id-token: write`

### No Secrets Required

All workflows use `GITHUB_TOKEN` which is automatically provided by GitHub Actions.

## 📊 Workflow Status Badges

Add these badges to your README.md:

```markdown
![Docs Quality Check](https://github.com/danielcristho/awesome-cloud-computing/actions/workflows/check.yml/badge.svg)
![Links](https://github.com/danielcristho/awesome-cloud-computing/actions/workflows/links.yml/badge.svg)
![Deploy](https://github.com/danielcristho/awesome-cloud-computing/actions/workflows/deploy.yml/badge.svg)
```

## 🎯 Best Practices

1. **Keep workflows focused** - One workflow per purpose
2. **Use caching** - Cache dependencies to speed up builds
3. **Fail fast** - Stop on first error to save resources
4. **Clear naming** - Use descriptive job and step names
5. **Document changes** - Update this README when modifying workflows

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Lychee Link Checker](https://github.com/lycheeverse/lychee)
