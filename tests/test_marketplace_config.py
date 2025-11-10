"""
Tests for marketplace.json configuration validation.
"""
import json
import os
import sys
from pathlib import Path


# Add repository root to path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


class TestMarketplaceConfig:
    """Test suite for marketplace.json validation."""

    def setup_method(self):
        """Setup test fixtures."""
        self.marketplace_path = repo_root / '.claude-plugin' / 'marketplace.json'
        with open(self.marketplace_path) as f:
            self.config = json.load(f)

    def test_json_is_valid(self):
        """Test that marketplace.json is valid JSON."""
        assert self.config is not None, "Failed to parse JSON"

    def test_required_top_level_fields(self):
        """Test that all required top-level fields are present."""
        required_fields = ['name', 'owner', 'description', 'version', 'plugins']
        for field in required_fields:
            assert field in self.config, f"Missing required field: {field}"

    def test_name_field(self):
        """Test name field is valid."""
        assert isinstance(self.config['name'], str), "name must be a string"
        assert len(self.config['name']) > 0, "name cannot be empty"
        assert self.config['name'] == 'claude-plugin-marketplace', \
            "name should be 'claude-plugin-marketplace'"

    def test_version_field(self):
        """Test version field follows semantic versioning."""
        version = self.config['version']
        assert isinstance(version, str), "version must be a string"
        parts = version.split('.')
        assert len(parts) == 3, "version must be in format X.Y.Z"
        for part in parts:
            assert part.isdigit(), f"version part '{part}' must be numeric"

    def test_owner_structure(self):
        """Test owner field has required structure."""
        owner = self.config['owner']
        assert isinstance(owner, dict), "owner must be an object"
        assert 'name' in owner, "owner must have 'name' field"
        assert 'url' in owner, "owner must have 'url' field"
        assert isinstance(owner['name'], str), "owner.name must be a string"
        assert isinstance(owner['url'], str), "owner.url must be a string"
        assert owner['url'].startswith('http'), "owner.url must be a valid URL"

    def test_description_field(self):
        """Test description field is valid."""
        desc = self.config['description']
        assert isinstance(desc, str), "description must be a string"
        assert len(desc) > 0, "description cannot be empty"
        assert len(desc) <= 500, "description should be concise (<=500 chars)"

    def test_plugins_is_array(self):
        """Test plugins field is an array."""
        plugins = self.config['plugins']
        assert isinstance(plugins, list), "plugins must be an array"
        assert len(plugins) > 0, "plugins array cannot be empty"

    def test_plugin_required_fields(self):
        """Test each plugin has required fields."""
        required_fields = ['name', 'source', 'description', 'version']
        for i, plugin in enumerate(self.config['plugins']):
            for field in required_fields:
                assert field in plugin, \
                    f"Plugin {i} missing required field: {field}"

    def test_plugin_names_are_unique(self):
        """Test that plugin names are unique."""
        names = [p['name'] for p in self.config['plugins']]
        assert len(names) == len(set(names)), "Plugin names must be unique"

    def test_plugin_names_are_valid(self):
        """Test plugin names follow naming conventions."""
        for plugin in self.config['plugins']:
            name = plugin['name']
            assert isinstance(name, str), f"Plugin name must be string: {name}"
            assert len(name) > 0, "Plugin name cannot be empty"
            # Names should be lowercase with hyphens
            assert name == name.lower(), f"Plugin name should be lowercase: {name}"
            assert ' ' not in name, f"Plugin name cannot contain spaces: {name}"

    def test_plugin_sources_exist(self):
        """Test that plugin source directories exist."""
        for plugin in self.config['plugins']:
            source = plugin['source']
            source_path = repo_root / source.lstrip('./')
            assert source_path.exists(), \
                f"Plugin source does not exist: {source}"
            assert source_path.is_dir(), \
                f"Plugin source must be a directory: {source}"

    def test_plugin_skill_files_exist(self):
        """Test that each plugin has a SKILL.md file."""
        for plugin in self.config['plugins']:
            source = plugin['source']
            skill_path = repo_root / source.lstrip('./') / 'SKILL.md'
            assert skill_path.exists(), \
                f"Missing SKILL.md for plugin: {plugin['name']}"

    def test_plugin_versions_are_valid(self):
        """Test plugin versions follow semantic versioning."""
        for plugin in self.config['plugins']:
            version = plugin['version']
            assert isinstance(version, str), \
                f"Plugin version must be string: {plugin['name']}"
            parts = version.split('.')
            assert len(parts) == 3, \
                f"Plugin version must be X.Y.Z format: {plugin['name']}"
            for part in parts:
                assert part.isdigit(), \
                    f"Version part must be numeric: {plugin['name']}"

    def test_plugin_descriptions_are_valid(self):
        """Test plugin descriptions are present and reasonable."""
        for plugin in self.config['plugins']:
            desc = plugin['description']
            assert isinstance(desc, str), \
                f"Plugin description must be string: {plugin['name']}"
            assert len(desc) > 10, \
                f"Plugin description too short: {plugin['name']}"
            assert len(desc) <= 500, \
                f"Plugin description too long: {plugin['name']}"

    def test_oss_contribution_framework_plugin(self):
        """Test specific requirements for oss-contribution-framework plugin."""
        oss_plugin = next(
            (p for p in self.config['plugins']
             if p['name'] == 'oss-contribution-framework'),
            None
        )
        assert oss_plugin is not None, \
            "oss-contribution-framework plugin must be present"
        assert oss_plugin['source'] == './skills/oss-contribution-framework', \
            "oss-contribution-framework source path is incorrect"
        assert '6-phase' in oss_plugin['description'].lower() or \
               'issue discovery' in oss_plugin['description'].lower(), \
            "oss-contribution-framework description should mention key features"


if __name__ == '__main__':
    # Simple test runner
    test_class = TestMarketplaceConfig()
    test_methods = [m for m in dir(test_class) if m.startswith('test_')]

    passed = 0
    failed = 0

    for method_name in test_methods:
        try:
            test_class.setup_method()
            method = getattr(test_class, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {method_name}: {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)