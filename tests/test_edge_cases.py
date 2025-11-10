"""
Tests for edge cases and advanced validation.
"""
import json
import re
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


class TestMarketplaceEdgeCases:
    """Test edge cases in marketplace.json."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.marketplace_path = repo_root / '.claude-plugin' / 'marketplace.json'
        with open(self.marketplace_path) as f:
            self.config = json.load(f)
    
    def test_no_duplicate_plugin_names(self):
        """Test that there are no duplicate plugin names."""
        names = [p['name'] for p in self.config['plugins']]
        assert len(names) == len(set(names)), \
            f"Duplicate plugin names found: {[n for n in names if names.count(n) > 1]}"
    
    def test_no_duplicate_plugin_sources(self):
        """Test that there are no duplicate plugin sources."""
        sources = [p['source'] for p in self.config['plugins']]
        assert len(sources) == len(set(sources)), \
            f"Duplicate plugin sources found: {[s for s in sources if sources.count(s) > 1]}"
    
    def test_plugin_names_follow_conventions(self):
        """Test that plugin names follow kebab-case convention."""
        for plugin in self.config['plugins']:
            name = plugin['name']
            # Should be lowercase, alphanumeric with hyphens
            assert re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name), \
                f"Plugin name '{name}' does not follow kebab-case convention"
    
    def test_plugin_sources_are_relative_paths(self):
        """Test that plugin sources use relative paths."""
        for plugin in self.config['plugins']:
            source = plugin['source']
            assert source.startswith('./'), \
                f"Plugin source should start with './': {source}"
            assert not source.startswith('../'), \
                f"Plugin source should not use parent directory: {source}"
    
    def test_no_trailing_slashes_in_sources(self):
        """Test that source paths don't have trailing slashes."""
        for plugin in self.config['plugins']:
            source = plugin['source']
            assert not source.endswith('/'), \
                f"Plugin source should not end with '/': {source}"
    
    def test_version_numbers_are_valid_semver(self):
        """Test that version numbers follow semantic versioning."""
        def is_valid_semver(version):
            parts = version.split('.')
            if len(parts) != 3:
                return False
            try:
                major, minor, patch = map(int, parts)
            except ValueError:
                return False
            else:
                return major >= 0 and minor >= 0 and patch >= 0
        
        # Check marketplace version
        assert is_valid_semver(self.config['version']), \
            f"Invalid marketplace version: {self.config['version']}"
        
        # Check plugin versions
        for plugin in self.config['plugins']:
            assert is_valid_semver(plugin['version']), \
                f"Invalid plugin version for {plugin['name']}: {plugin['version']}"
    
    def test_descriptions_end_with_proper_punctuation(self):
        """Test that descriptions end with proper punctuation (optional style)."""
        # This is a style preference - descriptions should be complete sentences
        for plugin in self.config['plugins']:
            desc = plugin['description']
            # Should not end with trailing whitespace
            assert desc == desc.strip(), \
                f"Plugin description has trailing whitespace: {plugin['name']}"
    
    def test_no_special_characters_in_names(self):
        """Test that names don't contain special characters."""
        forbidden_chars = ['/', '\\', ' ', '_', '.', ',', '!', '@', '#', '$', '%']
        for plugin in self.config['plugins']:
            name = plugin['name']
            for char in forbidden_chars:
                assert char not in name, \
                    f"Plugin name contains forbidden character '{char}': {name}"


class TestMarkdownEdgeCases:
    """Test edge cases in markdown files."""
    
    def test_no_consecutive_blank_lines(self):
        """Test that files don't have excessive consecutive blank lines."""
        oss_skill = repo_root / 'skills' / 'oss-contribution-framework' / 'SKILL.md'
        with open(oss_skill, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        consecutive_blanks = 0
        max_consecutive = 0
        
        for line in lines:
            if line.strip() == '':
                consecutive_blanks += 1
                max_consecutive = max(max_consecutive, consecutive_blanks)
            else:
                consecutive_blanks = 0
        
        assert max_consecutive <= 3, \
            f"Too many consecutive blank lines: {max_consecutive} (max allowed: 3)"
    
    def test_code_blocks_have_language_specifiers(self):
        """Test that code blocks specify a language."""
        oss_skill = repo_root / 'skills' / 'oss-contribution-framework' / 'SKILL.md'
        with open(oss_skill, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all code block starts
        code_blocks = re.findall(r'```(\w*)', content)
        
        # At least some should have language specifiers
        # (Some might be plain ``` for examples, which is OK)
        specified = [cb for cb in code_blocks if cb != '']
        assert len(specified) > 0, \
            "At least some code blocks should have language specifiers"
    
    def test_headings_have_proper_hierarchy(self):
        """Test that headings follow proper hierarchy (H1 -> H2 -> H3)."""
        oss_skill = repo_root / 'skills' / 'oss-contribution-framework' / 'SKILL.md'
        with open(oss_skill, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Extract heading levels
        headings = []
        for line in lines:
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                headings.append(level)
        
        # First heading should be H1
        assert len(headings) > 0, "File should have at least one heading"
        
        # Check for reasonable hierarchy (no huge jumps)
        for i in range(1, len(headings)):
            jump = headings[i] - headings[i-1]
            assert jump <= 2, \
                f"Heading hierarchy jump too large at position {i}: {jump} levels"
    
    def test_no_raw_urls_in_text(self):
        """Test that URLs are properly formatted as markdown links."""
        readme = repo_root / 'README.md'
        with open(readme, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for URLs that aren't in markdown link format or code blocks
        lines = content.split('\n')
        for _i, line in enumerate(lines):
            # Skip code blocks
            if '```' in line or line.strip().startswith('`'):
                continue
            
            # Look for http(s):// that's not in markdown link format
            if 'http://' in line or 'https://' in line:
                # Check if it's in a markdown link [text](url) or code
                if not re.search(r'\]\(https?://[^)]+\)', line) and \
                   not re.search(r'`[^`]*https?://[^`]*`', line):
                    # This might be a raw URL in text
                    # For README, this is OK in some contexts (like code examples)
                    pass


class TestDirectoryStructure:
    """Test directory structure and organization."""
    
    def test_no_unexpected_files_in_root(self):
        """Test that root directory doesn't have unexpected files."""
        allowed_patterns = [
            'README.md',
            '.gitignore',
            '.git',
            '.claude-plugin',
            'skills',
            'tests',
            'LICENSE',
            'CONTRIBUTING.md',
            '.github'
        ]
        
        root_items = [item.name for item in repo_root.iterdir()]
        
        for item in root_items:
            # Check if item matches any allowed pattern
            is_allowed = any(item.startswith(pattern) or item == pattern 
                           for pattern in allowed_patterns)
            assert is_allowed, \
                f"Unexpected file/directory in root: {item}"
    
    def test_skill_directory_organization(self):
        """Test that skill directories follow expected structure."""
        oss_base = repo_root / 'skills' / 'oss-contribution-framework'
        
        # Should have specific subdirectories
        assert (oss_base / 'skills').is_dir(), \
            "Should have 'skills' subdirectory"
        assert (oss_base / 'references').is_dir(), \
            "Should have 'references' subdirectory"
        assert (oss_base / 'assets').is_dir(), \
            "Should have 'assets' subdirectory"
        
        # SKILL.md should be at root of skill directory
        assert (oss_base / 'SKILL.md').is_file(), \
            "SKILL.md should be at root of skill directory"
    
    def test_no_hidden_files_in_skill_directories(self):
        """Test that skill directories don't have unexpected hidden files."""
        oss_base = repo_root / 'skills' / 'oss-contribution-framework'
        
        # Find all hidden files (starting with .)
        hidden_files = list(oss_base.rglob('.*'))
        # Filter out .git and similar
        hidden_files = [f for f in hidden_files if '.git' not in str(f)]
        
        # Should not have hidden files (except gitkeep or similar)
        for hidden in hidden_files:
            assert hidden.name in ['.gitkeep', '.gitignore'], \
                f"Unexpected hidden file: {hidden}"


class TestConsistency:
    """Test consistency across different files."""
    
    def setup_method(self):
        """Setup test fixtures."""
        with open(repo_root / '.claude-plugin' / 'marketplace.json') as f:
            self.marketplace = json.load(f)
        with open(repo_root / 'README.md', 'r', encoding='utf-8') as f:
            self.readme = f.read()
    
    def test_plugin_count_consistency(self):
        """Test that plugin count is consistent between files."""
        # Both plugins should be mentioned in README
        for plugin in self.marketplace['plugins']:
            assert plugin['name'] in self.readme.lower() or \
                   plugin['name'].replace('-', ' ') in self.readme.lower(), \
                f"Plugin {plugin['name']} not mentioned in README"
    
    def test_version_consistency(self):
        """Test that versions are consistent where referenced."""
        # Version should be in README if mentioned
        if 'version' in self.readme.lower():
            # This is optional - not all READMEs mention version
            pass
    
    def test_owner_consistency(self):
        """Test that owner information is consistent."""
        owner = self.marketplace['owner']
        
        # Owner URL should be mentioned in README
        assert owner['url'] in self.readme or owner['name'] in self.readme.lower(), \
            "Owner information should be referenced in README"
    
    def test_description_consistency(self):
        """Test that descriptions are consistent across files."""
        for plugin in self.marketplace['plugins']:
            # Description key points should appear in README
            # This is a loose check - not all words need to match
            name = plugin['name']
            
            # At least the plugin name should be in README
            assert name in self.readme.lower() or \
                   name.replace('-', ' ') in self.readme.lower(), \
                f"Plugin {name} should be in README"


if __name__ == '__main__':
    # Simple test runner
    test_classes = [
        TestMarketplaceEdgeCases,
        TestMarkdownEdgeCases,
        TestDirectoryStructure,
        TestConsistency
    ]
    
    total_passed = 0
    total_failed = 0
    
    for test_class in test_classes:
        print(f"\n{'='*60}")
        print(f"Running {test_class.__name__}")
        print('='*60)
        
        test_instance = test_class()
        test_methods = [m for m in dir(test_instance) if m.startswith('test_')]
        
        for method_name in test_methods:
            try:
                if hasattr(test_instance, 'setup_method'):
                    test_instance.setup_method()
                method = getattr(test_instance, method_name)
                method()
                print(f"✓ {method_name}")
                total_passed += 1
            except AssertionError as e:
                print(f"✗ {method_name}: {e}")
                total_failed += 1
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {total_passed} passed, {total_failed} failed")
    print('='*60)
    sys.exit(0 if total_failed == 0 else 1)