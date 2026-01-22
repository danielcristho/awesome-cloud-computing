#!/usr/bin/env python3
"""
Create a new language structure for translation

This script creates the necessary folder structure for a new language
and copies the English version as a template.

Usage:
    python scripts/create-language.py <locale>

Example:
    python scripts/create-language.py es
    python scripts/create-language.py fr
    python scripts/create-language.py ja
"""

import sys
import shutil
from pathlib import Path


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


def get_language_name(locale):
    """Get language name from locale code"""
    return LANGUAGE_NAMES.get(locale, locale.upper())


def create_language_structure(locale):
    """Create folder structure for new language"""

    language_name = get_language_name(locale)

    # Check if locale already exists
    lang_dir = Path(f"docs/{locale}")
    if lang_dir.exists():
        print(f"Error: Language folder 'docs/{locale}/' already exists!")
        sys.exit(1)

    # Create language directory
    lang_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: docs/{locale}/")

    # Copy structure from English
    en_dir = Path("docs/en")
    if not en_dir.exists():
        print("Error: English source directory 'docs/en/' not found!")
        sys.exit(1)

    # Copy only the index.md file as template
    en_index = en_dir / "index.md"
    if en_index.exists():
        shutil.copy(en_index, lang_dir / "index.md")
        print(f"Copied index.md template to docs/{locale}/")

    # Create subdirectories
    subdirs = ["learning", "tools", "security", "best-practices", "community", "trends"]
    for subdir in subdirs:
        (lang_dir / subdir).mkdir(exist_ok=True)
        print(f"Created directory: docs/{locale}/{subdir}/")

    print("\nNext steps:")
    print(f"1. Edit docs/{locale}/index.md and translate the content")
    print("2. Add language configuration to docs/languages.yml:")
    print(
        f"""
  - locale: {locale}
    name: {language_name}
    default: false
    build: true
    nav_translations:
      Home: [Translation]
      Learning Resources: [Translation]
      # ... add more translations
"""
    )
    print("3. Run: just sync-langs or python scripts/sync-languages.py")
    print(f"4. Start translating pages in docs/{locale}/")
    print(
        "\nTip: You can translate pages gradually. Untranslated pages will fallback to English."
    )


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python scripts/create-language.py <locale>")
        print("\nExamples:")
        print("  python scripts/create-language.py es")
        print("  python scripts/create-language.py fr")
        print("  python scripts/create-language.py ja")
        print("\nSupported locales:")
        # Show first 10 supported languages as examples
        examples = list(LANGUAGE_NAMES.items())[:10]
        for locale, name in examples:
            print(f"  {locale} - {name}")
        print(f"  ... and {len(LANGUAGE_NAMES) - 10} more")
        sys.exit(1)

    locale = sys.argv[1].lower()

    # Validate locale format (2-letter code)
    if len(locale) != 2 or not locale.isalpha():
        print(
            "Error: Locale should be a 2-letter language code (e.g., 'es', 'fr', 'ja')"
        )
        sys.exit(1)

    language_name = get_language_name(locale)
    print(f"Creating language structure for {language_name} ({locale})...")
    create_language_structure(locale)
    print("\nLanguage structure created successfully!")


if __name__ == "__main__":
    main()
