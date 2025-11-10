# Claude Plugin Marketplace

A curated collection of Claude skills and plugins for enhancing your Claude Code experience.

## 🚀 Installation

Add this marketplace to Claude Code:

```bash
claude marketplace add https://github.com/devkade/collaborator
```

## 📦 Available Plugins

### deep-reading-framework
Three-pass critical reading framework for systematic document analysis. Supports tech blogs, retrospectives, technical documentation, personal writing, and academic papers. Primary focus on Third Pass critical analysis, context validation, and actionable reconstruction.

**Usage:** `/deep-reading-framework` or ask for deep reading analysis

### oss-contribution-framework
Comprehensive 6-phase framework for contributing to open source projects. Guides you through issue discovery, analysis, codebase exploration, issue-code mapping, solution implementation, and PR creation. Includes modular sub-skills for each phase, detailed reference materials, and ready-to-use templates.

**Phases:**
1. **Issue Discovery** - Find and evaluate suitable issues
2. **Issue Analysis** - Deep dive into requirements and scope
3. **Codebase Exploration** - Understand project structure and conventions
4. **Issue-Code Mapping** - Connect requirements to code locations
5. **Solution Implementation** - Design and implement following best practices
6. **Documentation & PR** - Create comprehensive pull requests

**Usage:**
- Full workflow: "OSS 기여 시작" or "이 프로젝트에 기여하고 싶어"
- Individual phases: "이슈 분석해줘", "코드베이스 구조 파악", "PR 작성"
- Includes templates for issue analysis, codebase notes, and PR checklists

## 🔧 Adding New Plugins

To add a new plugin to this marketplace:

1. Create a new directory under `skills/` or `plugins/`
2. Add your plugin's files following the structure below
3. Update `.claude-plugin/marketplace.json` with your plugin details
4. Update this README with a description of your plugin
5. Submit a pull request

## 📁 Plugin Structure

Each plugin should follow this structure:
```
skills/your-plugin-name/
├── SKILL.md          # Main skill documentation
├── assets/           # Optional supporting files
└── references/       # Optional reference materials
```

Or for general plugins:
```
plugins/your-plugin-name/
├── plugin.json       # Plugin configuration
├── commands/         # Custom commands
├── skills/           # Skills included
└── assets/           # Supporting files
```

## 🛠️ Development

For local development:
```bash
# Clone this repository
git clone https://github.com/devkade/collaborator.git
cd collaborator

# Add as local marketplace for testing
claude marketplace add /path/to/collaborator
```

## 📄 License

This marketplace is open source. Individual plugins may have their own licenses - please check each plugin's documentation.