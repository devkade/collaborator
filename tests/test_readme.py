"""
Tests for README.md validation.
"""
import re
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


class TestReadme:
    """Test suite for README.md file."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.readme_path = repo_root / 'README.md'
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')
    
    def test_readme_exists(self):
        """Test that README.md exists."""
        assert self.readme_path.exists(), "README.md must exist"
    
    def test_has_title(self):
        """Test that README has a main title."""
        assert self.lines[0].startswith('#'), \
            "README should start with a title"
        assert 'Claude Plugin Marketplace' in self.lines[0] or \
               'marketplace' in self.lines[0].lower(), \
            "README title should reference the marketplace"
    
    def test_has_installation_section(self):
        """Test that README has installation instructions."""
        content_lower = self.content.lower()
        assert 'installation' in content_lower or 'install' in content_lower, \
            "README should have installation section"
    
    def test_has_claude_marketplace_command(self):
        """Test that README includes claude marketplace command."""
        assert 'claude marketplace add' in self.content, \
            "README should include 'claude marketplace add' command"
    
    def test_mentions_available_plugins(self):
        """Test that README lists available plugins."""
        content_lower = self.content.lower()
        assert 'available plugins' in content_lower or 'plugins' in content_lower, \
            "README should mention available plugins"
    
    def test_mentions_oss_contribution_framework(self):
        """Test that README mentions oss-contribution-framework."""
        content_lower = self.content.lower()
        assert 'oss-contribution-framework' in content_lower or \
               'oss contribution' in content_lower, \
            "README should mention oss-contribution-framework"
    
    def test_mentions_deep_reading_framework(self):
        """Test that README mentions deep-reading-framework."""
        content_lower = self.content.lower()
        assert 'deep-reading-framework' in content_lower or \
               'deep reading' in content_lower, \
            "README should mention deep-reading-framework"
    
    def test_has_usage_examples(self):
        """Test that README provides usage examples."""
        # Should have some code blocks or usage examples
        assert '```' in self.content, \
            "README should contain code blocks with examples"
    
    def test_has_contributing_section(self):
        """Test that README has information about contributing."""
        content_lower = self.content.lower()
        assert 'adding new plugins' in content_lower or \
               'add' in content_lower or \
               'contribute' in content_lower or \
               'development' in content_lower, \
            "README should have information about adding plugins"
    
    def test_has_plugin_structure_info(self):
        """Test that README explains plugin structure."""
        content_lower = self.content.lower()
        assert 'structure' in content_lower or 'directory' in content_lower, \
            "README should explain plugin structure"
    
    def test_code_blocks_are_balanced(self):
        """Test that code blocks are properly closed."""
        code_block_count = self.content.count('```')
        assert code_block_count % 2 == 0, \
            "Code blocks must be properly closed (even number of ```)"
    
    def test_no_broken_links_format(self):
        """Test that markdown links have proper format."""
        # Check for common markdown link patterns
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', self.content)
        for link_text, link_url in links:
            assert len(link_text) > 0, "Link text cannot be empty"
            assert len(link_url) > 0, "Link URL cannot be empty"
    
    def test_github_url_is_correct(self):
        """Test that GitHub URL references are correct."""
        github_matches = re.findall(r'https://github\.com/([^/\s)]+)/([^/\s)]+)', self.content)
        for owner, repo in github_matches:
            # Should reference devkade/collaborator
            if 'devkade' in owner.lower():
                assert 'collaborator' in repo.lower(), \
                    f"devkade GitHub repo should be 'collaborator', got: {repo}"
    
    def test_reasonable_length(self):
        """Test that README is of reasonable length."""
        line_count = len(self.lines)
        assert line_count > 20, "README seems too short"
        assert line_count < 500, "README seems excessively long"
    
    def test_has_emoji_sections(self):
        """Test that README uses emoji for section headers (optional style check)."""
        # This is a style preference - the README uses emoji
        # Check if there are any emoji-style section markers
        # This is informational rather than strict requirement


class TestReadmePluginDescriptions:
    """Test that plugin descriptions in README match marketplace.json."""
    
    def setup_method(self):
        """Setup test fixtures."""
        import json
        self.readme_path = repo_root / 'README.md'
        self.marketplace_path = repo_root / '.claude-plugin' / 'marketplace.json'
        
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            self.readme_content = f.read()
        
        with open(self.marketplace_path, 'r', encoding='utf-8') as f:
            self.marketplace = json.load(f)
    
    def test_plugin_count_matches(self):
        """Test that README mentions all plugins from marketplace.json."""
        for plugin in self.marketplace['plugins']:
            plugin_name = plugin['name']
            # Check if plugin name appears in README
            assert plugin_name in self.readme_content.lower() or \
                   plugin_name.replace('-', ' ') in self.readme_content.lower(), \
                f"Plugin '{plugin_name}' should be mentioned in README"
    
    def test_oss_framework_phases_mentioned(self):
        """Test that OSS framework's 6 phases are mentioned."""
        oss_plugin = next(
            (p for p in self.marketplace['plugins'] 
             if p['name'] == 'oss-contribution-framework'),
            None
        )
        if oss_plugin:
            # README should mention the phases
            content_lower = self.readme_content.lower()
            assert 'phase' in content_lower, \
                "OSS contribution framework should mention phases in README"


if __name__ == '__main__':
    # Simple test runner
    test_classes = [TestReadme, TestReadmePluginDescriptions]
    
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