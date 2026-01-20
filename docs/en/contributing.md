# Contribution Guidelines

Your contributions are always welcome!

## Commits

- Add the link: `* [example-name](http://example.com/) - A short description that ends with a period.`
  Keep descriptions concise and clear.

- Add a section if needed:
    1. Include the section description if necessary.
    2. Add the section title to the Table of Contents.

## Pull Requests

- Add one link per Pull Request.
- Make sure the PR title is in the format of `Add example-name`.

## Issues

- When creating an issue, please provide a clear and concise description of the problem or suggestion.

## Translation Guidelines

We welcome translations to make this resource accessible to more developers worldwide. Follow these steps to contribute translations:

### Setting Up a New Language

**1. Create language structure**:

   ```bash
   just create-lang <locale>
   # Example: just create-lang es
   ```

**2. Configure language in `docs/languages.yml`**:

   ```yaml
   - locale: es
     name: Español
     default: false
     build: true
     nav_translations:
       Home: Inicio
       Learning Resources: Recursos de Aprendizaje
       Platforms: Plataformas
       Tools & Software: Herramientas y Software
       Best Practices: Mejores Prácticas
       Security: Seguridad
       Community: Comunidad
       Emerging Trends: Tendencias Emergentes
       Contributing: Contribuir
   ```

**3. Sync language configuration**:

   ```bash
   just sync-langs
   ```

### Translation Process

1. **Start with the main page**: Translate `docs/<locale>/index.md` first
2. **Translate section by section**: Work on individual pages in the language folder
3. **Maintain structure**: Keep the same markdown structure and table format
4. **Preserve links**: Keep original English links unless localized versions exist
5. **Update navigation**: Add appropriate translations to `nav_translations` in `languages.yml`

### Translation Standards

- **Consistency**: Use consistent terminology throughout the translation
- **Accuracy**: Ensure technical terms are translated correctly
- **Completeness**: Translate all content including descriptions and section headers
- **Format preservation**: Maintain markdown formatting and table structure
- **Link validation**: Verify that all links work in the translated version

### Available Commands

Use these justfile commands for translation work:

```bash
# Create new language structure
just create-lang <locale>

# Sync language configurations
just sync-langs

# Start development server to preview translations
just dev

# Build site to test all languages
just build
```

### Translation Workflow

1. Fork the repository
2. Create a new branch: `git checkout -b add-translation-<locale>`
3. Set up the language structure using the commands above
4. Translate content gradually, starting with the main index page
5. Test your translation using `just dev`
6. Submit a pull request with clear description of what was translated

### Getting Help

- Check existing translations for reference
- Ask questions in issues if you need clarification on technical terms
- Follow the project's content guidelines for consistency
