#!/usr/bin/env python3
"""
Create a new language structure for translation.
"""

import sys
import shutil
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Language mapping from locale codes to language names
LANGUAGE_NAMES = {
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "ja": "日本語",
    "ko": "한국어",
    "zh": "中文",
    "pt": "Português",
    "ru": "Русский",
    "it": "Italiano",
    "nl": "Nederlands",
    "pl": "Polski",
    "tr": "Türkçe",
    "ar": "العربية",
    "hi": "हिन्दी",
    "th": "ไทย",
    "vi": "Tiếng Việt",
    "ms": "Bahasa Melayu",
    "tl": "Filipino",
    "sv": "Svenska",
    "da": "Dansk",
    "no": "Norsk",
    "fi": "Suomi",
    "cs": "Čeština",
    "sk": "Slovenčina",
    "hu": "Magyar",
    "ro": "Română",
    "bg": "Български",
    "hr": "Hrvatski",
    "sr": "Српски",
    "sl": "Slovenščina",
    "et": "Eesti",
    "lv": "Latviešu",
    "lt": "Lietuvių",
    "uk": "Українська",
    "he": "עברית",
    "fa": "فارسی",
    "ur": "اردو",
    "bn": "বাংলা",
    "ta": "தமிழ்",
    "te": "తెలుగు",
    "ml": "മലയാളം",
    "kn": "ಕನ್ನಡ",
    "gu": "ગુજરાતી",
    "pa": "ਪੰਜਾਬੀ",
    "mr": "मराठी",
    "ne": "नेपाली",
    "si": "සිංහල",
    "my": "မြန်မာ",
    "km": "ខ្មែរ",
    "lo": "ລາວ",
    "ka": "ქართული",
    "am": "አማርኛ",
    "sw": "Kiswahili",
    "zu": "isiZulu",
    "af": "Afrikaans",
    "is": "Íslenska",
    "mt": "Malti",
    "cy": "Cymraeg",
    "ga": "Gaeilge",
    "eu": "Euskera",
    "ca": "Català",
    "gl": "Galego",
}


def get_language_name(locale: str) -> str:
    return LANGUAGE_NAMES.get(locale, locale.upper())


def error_exit(message: str):
    console.print(
        Panel.fit(
            message,
            title="[red]Error[/red]",
            border_style="red",
        )
    )
    sys.exit(1)


def info_panel(title: str, message: str):
    console.print(
        Panel.fit(
            message,
            title=title,
            border_style="cyan",
        )
    )


def success(message: str):
    console.print(f"✔ [green]{message}[/green]")


def create_language_structure(locale: str):
    language_name = get_language_name(locale)
    lang_dir = Path("docs") / locale

    if lang_dir.exists():
        error_exit(
            f"Language folder 'docs/{locale}/' already exists.\n\n"
            "Please choose a different locale or remove the existing folder."
        )

    # Create base language directory
    lang_dir.mkdir(parents=True)
    success(f"Created directory: docs/{locale}/")

    # Copy English index.md as template
    en_dir = Path("docs/en")
    if not en_dir.exists():
        error_exit("English source directory 'docs/en/' not found.")

    en_index = en_dir / "index.md"
    if en_index.exists():
        shutil.copy(en_index, lang_dir / "index.md")
        success(f"Copied index.md template to docs/{locale}/")

    # Create subdirectories
    subdirs = [
        "learning",
        "tools",
        "security",
        "best-practices",
        "community",
        "trends",
    ]

    for subdir in subdirs:
        (lang_dir / subdir).mkdir(exist_ok=True)
        success(f"Created directory: docs/{locale}/{subdir}/")

    # Next steps panel
    next_steps = Text()
    next_steps.append("1. ", style="bold")
    next_steps.append(f"Edit docs/{locale}/index.md and translate the content\n")

    next_steps.append("2. ", style="bold")
    next_steps.append("Add language configuration to docs/languages.yml:\n\n")

    next_steps.append(
        f"""  - locale: {locale}
    name: {language_name}
    default: false
    build: true
    nav_translations:
      Home: [Translation]
      Learning Resources: [Translation]
      # ... add more translations
""",
        style="dim",
    )

    next_steps.append("\n3. ", style="bold")
    next_steps.append(
        "Run: '$ just sync-langs' or '$ python scripts/sync-languages.py'\n"
    )

    next_steps.append("4. ", style="bold")
    next_steps.append(f"Start translating pages in docs/{locale}/\n\n")

    next_steps.append(
        "Tip: You can translate pages gradually. "
        "Untranslated pages will fallback to English.",
        style="dim",
    )

    console.print(
        Panel(
            next_steps,
            title="Next Steps",
            border_style="cyan",
        )
    )


def main():
    if len(sys.argv) != 2:
        error_exit(
            "Usage:\n"
            "  python scripts/create-language.py <locale>\n\n"
            "Examples:\n"
            "  python scripts/create-language.py es\n"
            "  python scripts/create-language.py fr\n"
            "  python scripts/create-language.py ja"
        )

    locale = sys.argv[1].lower()

    if len(locale) != 2 or not locale.isalpha():
        error_exit(
            "Locale should be a 2-letter language code " "(e.g. 'es', 'fr', 'ja')."
        )

    language_name = get_language_name(locale)

    info_panel(
        "Create Language",
        f"Creating language structure for {language_name} ({locale})...",
    )

    create_language_structure(locale)

    success("Language structure created successfully!")


if __name__ == "__main__":
    main()
