#!/usr/bin/env python3
"""
Sync language configurations from docs/languages.yml to mkdocs.yml

This script reads language definitions from docs/languages.yml and updates
the i18n plugin configuration in mkdocs.yml automatically.

Usage:
    python scripts/sync-languages.py
"""

import yaml
import sys
import re
from pathlib import Path


def load_languages_config():
    """Load language configuration from docs/languages.yml"""
    config_path = Path("docs/languages.yml")

    if not config_path.exists():
        print(f"Error: {config_path} not found!")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config.get("languages", [])


def build_nav_structure(translations):
    """Build navigation structure with translations"""
    return [
        {translations.get("Home", "Home"): "index.md"},
        {
            translations.get("Learning Resources", "Learning Resources"): [
                {translations.get("Overview", "Overview"): "learning/index.md"},
                {
                    translations.get(
                        "Basic Concepts", "Basic Concepts"
                    ): "learning/basic-concepts.md"
                },
                {translations.get("Books", "Books"): "learning/books.md"},
                {translations.get("Tutorials", "Tutorials"): "learning/tutorials.md"},
                {
                    translations.get(
                        "Certifications", "Certifications"
                    ): "learning/certifications.md"
                },
            ]
        },
        {translations.get("Platforms", "Platforms"): "platforms.md"},
        {
            translations.get("Tools & Software", "Tools & Software"): [
                {translations.get("Overview", "Overview"): "tools/index.md"},
                {
                    translations.get(
                        "Infrastructure as Code", "Infrastructure as Code"
                    ): "tools/infrastructure-as-code.md"
                },
                {
                    translations.get(
                        "Multi-cloud Management", "Multi-cloud Management"
                    ): "tools/multi-cloud-management.md"
                },
                {
                    translations.get(
                        "Containerization", "Containerization"
                    ): "tools/containerization.md"
                },
                {
                    translations.get(
                        "Serverless Frameworks", "Serverless Frameworks"
                    ): "tools/serverless-frameworks.md"
                },
                {
                    translations.get(
                        "Cloud Migration", "Cloud Migration"
                    ): "tools/cloud-migration.md"
                },
                {
                    translations.get(
                        "Disaster Recovery", "Disaster Recovery"
                    ): "tools/disaster-recovery.md"
                },
                {
                    translations.get(
                        "FinOps & Cost Management", "FinOps & Cost Management"
                    ): "tools/finops-cost-management.md"
                },
                {
                    translations.get(
                        "Edge Computing", "Edge Computing"
                    ): "tools/edge-computing.md"
                },
                {translations.get("Monitoring", "Monitoring"): "tools/monitoring.md"},
                {translations.get("Logging", "Logging"): "tools/logging.md"},
            ]
        },
        {
            translations.get("Best Practices", "Best Practices"): [
                {translations.get("Overview", "Overview"): "best-practices/index.md"},
                {
                    translations.get(
                        "Cost Optimization", "Cost Optimization"
                    ): "best-practices/cost-optimization.md"
                },
                {
                    translations.get(
                        "Scalability & Performance", "Scalability & Performance"
                    ): "best-practices/scalability-performance.md"
                },
            ]
        },
        {
            translations.get("Security", "Security"): [
                {translations.get("Overview", "Overview"): "security/index.md"},
                {
                    translations.get(
                        "Identity & Access Management", "Identity & Access Management"
                    ): "security/iam.md"
                },
                {
                    translations.get(
                        "Threat Detection", "Threat Detection"
                    ): "security/threat-detection.md"
                },
                {
                    translations.get(
                        "Secret Management", "Secret Management"
                    ): "security/secret-management.md"
                },
                {
                    translations.get(
                        "Compliance & Governance", "Compliance & Governance"
                    ): "security/compliance-governance.md"
                },
            ]
        },
        {translations.get("Community", "Community"): "community/index.md"},
        {translations.get("Emerging Trends", "Emerging Trends"): "trends/index.md"},
        {translations.get("Contributing", "Contributing"): "contributing.md"},
    ]


def update_mkdocs_config(languages):
    """Update mkdocs.yml with language configurations using YAML parsing"""

    # Read and parse mkdocs.yml
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        content = f.read()

    # Build language configurations
    lang_configs = []
    search_langs = []

    for lang in languages:
        locale = lang["locale"]
        search_langs.append(locale)
        translations = lang.get("nav_translations", {})
        nav_structure = build_nav_structure(translations)

        lang_config = {
            "locale": locale,
            "name": lang["name"],
            "build": lang.get("build", True),
        }

        if lang.get("default", False):
            lang_config["default"] = True

        lang_config["nav"] = nav_structure
        lang_configs.append(lang_config)

    # Convert language configs to YAML string
    lang_yaml = yaml.dump(
        lang_configs, default_flow_style=False, allow_unicode=True, sort_keys=False
    )

    # Indent the YAML properly (8 spaces for mkdocs.yml structure)
    lang_yaml_lines = lang_yaml.strip().split("\n")
    indented_lines = []
    for line in lang_yaml_lines:
        if line.strip():
            indented_lines.append("        " + line)
        else:
            indented_lines.append("")
    lang_yaml_indented = "\n".join(indented_lines)

    # Replace the languages section in i18n plugin
    # Find the exact pattern and replace only the languages part
    pattern = r"(\s+languages:\s*\n)(\s+# This section.*?\n)?(\s+- locale:.*?)(?=\n\s+- minify:|\n\s+[a-z_]+:|\Z)"

    replacement = f"      languages:\n{lang_yaml_indented}\n"

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Update search languages in search plugin
    search_pattern = r"(\s+- search:\s*\n\s+lang:\s*\n)(\s+- [^\n]*\n)+"
    search_replacement = "  - search:\n      lang:\n"
    for lang_code in search_langs:
        search_replacement += f"        - {lang_code}\n"

    new_content = re.sub(
        search_pattern, search_replacement, new_content, flags=re.MULTILINE
    )

    # Write back to mkdocs.yml
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully updated mkdocs.yml with language configurations!")
    print(f"Configured languages: {', '.join([lang['name'] for lang in languages])}")

    # Check for missing translation folders
    for lang in languages:
        locale = lang["locale"]
        lang_dir = Path(f"docs/{locale}")
        if not lang_dir.exists():
            print(f"Warning: Translation folder 'docs/{locale}/' does not exist yet.")
            print(f"   Create it with: just create-lang {locale}")


def main():
    """Main function"""
    print("Syncing language configurations...")

    # Load language configurations
    languages = load_languages_config()

    if not languages:
        print("Error: No languages defined in docs/languages.yml!")
        sys.exit(1)

    # Update mkdocs.yml
    update_mkdocs_config(languages)

    print(
        "\nDone! You can now run 'just dev or uv run mkdocs serve' to preview changes."
    )


if __name__ == "__main__":
    main()
