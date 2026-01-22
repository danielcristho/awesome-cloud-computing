#!/usr/bin/env python3
"""
Sync language configurations from docs/languages.yml to mkdocs.yml
"""

from pathlib import Path
import sys
import yaml

# Const
LANG_FILE = Path("docs/languages.yml")
MKDOCS_FILE = Path("mkdocs.yml")


def load_yaml(path: Path):
    if not path.exists():
        print(f"Error: {path} not found")
        sys.exit(1)
    with path.open("r", encoding="utf-8") as f:
        # return yaml.load(f, Loader=yaml.FullLoader)
        return yaml.load(f, Loader=MkDocsLoader)


def save_yaml(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )


def build_nav_structure(translations: dict):
    def t(key: str) -> str:
        return translations.get(key, key)

    return [
        {t("Home"): "index.md"},
        {
            t("Learning Resources"): [
                {t("Overview"): "learning/index.md"},
                {t("Basic Concepts"): "learning/basic-concepts.md"},
                {t("Books"): "learning/books.md"},
                {t("Tutorials"): "learning/tutorials.md"},
                {t("Certifications"): "learning/certifications.md"},
            ]
        },
        {t("Platforms"): "platforms.md"},
        {
            t("Tools & Software"): [
                {t("Overview"): "tools/index.md"},
                {t("Infrastructure as Code"): "tools/infrastructure-as-code.md"},
                {t("Multi-cloud Management"): "tools/multi-cloud-management.md"},
                {t("Containerization"): "tools/containerization.md"},
                {t("Serverless Frameworks"): "tools/serverless-frameworks.md"},
                {t("Cloud Migration"): "tools/cloud-migration.md"},
                {t("Disaster Recovery"): "tools/disaster-recovery.md"},
                {t("FinOps & Cost Management"): "tools/finops-cost-management.md"},
                {t("Edge Computing"): "tools/edge-computing.md"},
                {t("Monitoring"): "tools/monitoring.md"},
                {t("Logging"): "tools/logging.md"},
            ]
        },
        {
            t("Best Practices"): [
                {t("Overview"): "best-practices/index.md"},
                {t("Cost Optimization"): "best-practices/cost-optimization.md"},
                {
                    t(
                        "Scalability & Performance"
                    ): "best-practices/scalability-performance.md"
                },
            ]
        },
        {
            t("Security"): [
                {t("Overview"): "security/index.md"},
                {t("Identity & Access Management"): "security/iam.md"},
                {t("Threat Detection"): "security/threat-detection.md"},
                {t("Secret Management"): "security/secret-management.md"},
                {t("Compliance & Governance"): "security/compliance-governance.md"},
            ]
        },
        {t("Community"): "community/index.md"},
        {t("Emerging Trends"): "trends/index.md"},
        {t("Contributing"): "contributing.md"},
    ]


def find_plugin(plugins, name):
    for plugin in plugins:
        if isinstance(plugin, dict) and name in plugin:
            return plugin[name]
    return None


def sync_languages():
    langs_cfg = load_yaml(LANG_FILE).get("languages", [])
    if not langs_cfg:
        print("Error: no languages defined")
        sys.exit(1)

    mkdocs = load_yaml(MKDOCS_FILE)

    plugins = mkdocs.setdefault("plugins", [])

    # --- search plugin ---
    search = find_plugin(plugins, "search")
    if search is None:
        search = {}
        plugins.append({"search": search})

    # search["lang"] = [l["locale"] for l in langs_cfg]
    search["lang"] = [lang["locale"] for lang in langs_cfg]

    # --- i18n plugin ---
    i18n = find_plugin(plugins, "i18n")
    if i18n is None:
        i18n = {}
        plugins.append({"i18n": i18n})

    i18n_languages = []

    for lang in langs_cfg:
        entry = {
            "locale": lang["locale"],
            "name": lang["name"],
            "build": lang.get("build", True),
            "nav": build_nav_structure(lang.get("nav_translations", {})),
        }
        if lang.get("default"):
            entry["default"] = True
        i18n_languages.append(entry)

    i18n["languages"] = i18n_languages

    save_yaml(MKDOCS_FILE, mkdocs)

    print("mkdocs.yml successfully synced")
    # print("Languages:", ", ".join(l["name"] for l in langs_cfg))
    print("Languages:", ", ".join(lang["name"] for lang in langs_cfg))

    for lang in langs_cfg:
        folder = Path("docs") / lang["locale"]
        if not folder.exists():
            print(f"Missing folder: {folder}/")


class MkDocsLoader(yaml.FullLoader):
    pass


def python_name_constructor(loader, suffix, node):
    # Return the full python path as string
    return f"!!python/name:{suffix}"


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    python_name_constructor,
)


def main():
    print("Syncing languages...")
    sync_languages()
    print("Done. Run: mkdocs serve")


if __name__ == "__main__":
    main()
