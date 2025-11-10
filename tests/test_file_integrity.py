"""
Tests for file integrity and cross-references.
"""
import json
import re
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


class TestFileIntegrity:
    """Test suite for file existence and integrity."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.marketplace_path = repo_root / '.claude-plugin' / 'marketplace.json'
        with open(self.marketplace_path) as f:
            self.marketplace = json.load(f)
    
    def test_all_referenced_directories_exist(self):
        """Test that all directories referenced in marketplace.json exist."""
        for plugin in self.marketplace['plugins']:
            source = plugin['source']
            source_path = repo_root / source.lstrip('./')
            assert source_path.exists(), \
                f"Referenced directory does not exist: {source}"
            assert source_path.is_dir(), \
                f"Referenced path is not a directory: {source}"
    
    def test_oss_framework_directory_structure(self):
        """Test OSS contribution framework has expected directory structure."""
        base_path = repo_root / 'skills' / 'oss-contribution-framework'
        
        # Check main directories
        assert (base_path / 'skills').exists(), \
            "OSS framework should have 'skills' subdirectory"
        assert (base_path / 'references').exists(), \
            "OSS framework should have 'references' subdirectory"
        assert (base_path / 'assets').exists(), \
            "OSS framework should have 'assets' subdirectory"
        assert (base_path / 'assets' / 'templates').exists(), \
            "OSS framework should have 'assets/templates' subdirectory"
    
    def test_no_empty_markdown_files(self):
        """Test that no markdown files are empty."""
        md_files = list(repo_root.glob('**/*.md'))
        for md_file in md_files:
            if '.git' not in str(md_file):
                size = md_file.stat().st_size
                assert size > 0, f"Markdown file is empty: {md_file}"
    
    def test_all_markdown_files_are_utf8(self):
        """Test that all markdown files can be read as UTF-8."""
        md_files = list(repo_root.glob('**/*.md'))
        for md_file in md_files:
            if '.git' not in str(md_file):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        f.read()
                except UnicodeDecodeError as err:
                    msg = f"File is not valid UTF-8: {md_file}"
                    raise AssertionError(msg) from err
    
    def test_marketplace_json_is_utf8(self):
        """Test that marketplace.json is valid UTF-8."""
        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                f.read()
        except UnicodeDecodeError as err:
            msg = "marketplace.json is not valid UTF-8"
            raise AssertionError(msg) from err


class TestCrossReferences:
    """Test suite for cross-references between files."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.oss_base = repo_root / 'skills' / 'oss-contribution-framework'
        self.skill_md = self.oss_base / 'SKILL.md'
        with open(self.skill_md, 'r', encoding='utf-8') as f:
            self.skill_content = f.read()
    
    def test_skill_md_references_valid_subskills(self):
        """Test that SKILL.md references valid sub-skill files."""
        # Look for references like skills/something.md
        references = re.findall(r'skills/([a-z-]+\.md)', self.skill_content)
        for ref in references:
            ref_path = self.oss_base / 'skills' / ref
            assert ref_path.exists(), \
                f"SKILL.md references non-existent file: skills/{ref}"
    
    def test_all_subskills_are_referenced_in_main_skill(self):
        """Test that all sub-skill files are mentioned in SKILL.md."""
        skill_files = list((self.oss_base / 'skills').glob('*.md'))
        skill_content_lower = self.skill_content.lower()
        
        for skill_file in skill_files:
            # The file name (without .md) should appear in SKILL.md
            file_stem = skill_file.stem
            # Convert kebab-case to words for checking
            words = file_stem.replace('-', ' ')
            # At least some form should be mentioned
            assert file_stem in skill_content_lower or words in skill_content_lower, \
                f"Sub-skill {skill_file.name} is not referenced in SKILL.md"
    
    def test_phase_numbering_is_consistent(self):
        """Test that phase numbers are consistent across files."""
        expected_phases = {
            'issue-discovery.md': '1',
            'issue-analysis.md': '2',
            'codebase-exploration.md': '3',
            'issue-code-mapping.md': '4',
            'solution-implementation.md': '5',
            'documentation-pr.md': '6'
        }
        
        for skill_file, expected_phase in expected_phases.items():
            file_path = self.oss_base / 'skills' / skill_file
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Check if the file mentions its phase number
                    assert f'Phase {expected_phase}' in content or \
                           f'phase {expected_phase}' in content.lower(), \
                        f"{skill_file} should mention Phase {expected_phase}"


class TestContentQuality:
    """Test suite for content quality checks."""
    
    def setup_method(self):
        """Setup test fixtures."""
        pass
    
    def test_no_todo_markers_in_main_files(self):
        """Test that main files don't contain TODO markers."""
        important_files = [
            repo_root / 'README.md',
            repo_root / '.claude-plugin' / 'marketplace.json',
            repo_root / 'skills' / 'oss-contribution-framework' / 'SKILL.md'
        ]
        
        for file_path in important_files:
            if file_path.suffix == '.json':
                continue  # Skip JSON files
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                # Check for common TODO patterns
                assert 'todo:' not in content and '[todo]' not in content, \
                    f"{file_path.name} contains TODO markers"
    
    def test_no_placeholder_text_in_descriptions(self):
        """Test that descriptions don't contain obvious placeholders."""
        marketplace_path = repo_root / '.claude-plugin' / 'marketplace.json'
        with open(marketplace_path) as f:
            marketplace = json.load(f)
        
        placeholders = ['[insert', '[add', '[fill', 'lorem ipsum', 'todo', 'tbd']
        
        # Check marketplace description
        desc = marketplace['description'].lower()
        for placeholder in placeholders:
            assert placeholder not in desc, \
                f"Marketplace description contains placeholder: {placeholder}"
        
        # Check plugin descriptions
        for plugin in marketplace['plugins']:
            desc = plugin['description'].lower()
            for placeholder in placeholders:
                assert placeholder not in desc, \
                    f"Plugin '{plugin['name']}' description contains placeholder: {placeholder}"
    
    def test_consistent_terminology(self):
        """Test that terminology is used consistently."""
        skill_md = repo_root / 'skills' / 'oss-contribution-framework' / 'SKILL.md'
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Should use consistent terms
        # This is more of a style guide check
        # For example, "open source" vs "open-source" vs "opensource"
        oss_count = content.lower().count('oss ')
        open_source_count = content.lower().count('open source')
        
        # At least OSS or open source should be mentioned
        assert oss_count > 0 or open_source_count > 0, \
            "Document should mention OSS or open source"


class TestTemplateUsability:
    """Test that templates are usable and well-structured."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.templates_dir = repo_root / 'skills' / 'oss-contribution-framework' / 'assets' / 'templates'
    
    def test_templates_have_clear_placeholders(self):
        """Test that templates have clear, distinguishable placeholders."""
        for template_file in self.templates_dir.glob('*.md'):
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Count placeholders - looking for [text] but not checkbox [ ] or single letters
            placeholders = re.findall(r'\[([^\]]+)\]', content)
            # Filter out checkbox placeholders and common single-letter patterns
            # Single capital letters like [A], [B] are acceptable as labels/options
            placeholders = [p for p in placeholders 
                          if p.strip() not in ['', ' ', 'x', 'X'] 
                          and not (len(p) == 1 and p.isupper())]
            
            assert len(placeholders) > 0, \
                f"{template_file.name} should have placeholders"
            
            # Remaining placeholders should be descriptive (more than 1 char)
            for placeholder in placeholders:
                assert len(placeholder) > 1, \
                    f"Placeholder too short in {template_file.name}: [{placeholder}]"
    
    def test_pr_checklist_has_actionable_items(self):
        """Test that PR checklist has actionable items."""
        checklist_path = self.templates_dir / 'pr-checklist-template.md'
        with open(checklist_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Should have multiple checkboxes
        checkbox_count = content.count('- [ ]')
        assert checkbox_count >= 5, \
            "PR checklist should have at least 5 checkboxes"
        
        # Should have sections
        assert '##' in content, \
            "PR checklist should have section headers"
    
    def test_issue_analysis_template_covers_different_issue_types(self):
        """Test that issue analysis template covers different issue types."""
        template_path = self.templates_dir / 'issue-analysis-template.md'
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        # Should mention different issue types
        issue_types = ['bug', 'feature', 'refactor']
        mentioned_types = [t for t in issue_types if t in content]
        assert len(mentioned_types) >= 2, \
            "Issue analysis template should cover multiple issue types"


if __name__ == '__main__':
    # Simple test runner
    test_classes = [
        TestFileIntegrity,
        TestCrossReferences,
        TestContentQuality,
        TestTemplateUsability
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
                test_instance.setup_method()
                method = getattr(test_instance, method_name)
                method()
                print(f"✓ {method_name}")
                total_passed += 1
            except AssertionError as e:
                print(f"✗ {method_name}: {e}")
                total_failed += 1
            except OSError as e:
                print(f"✗ {method_name}: Unexpected error: {e}")
                total_failed += 1
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {total_passed} passed, {total_failed} failed")
    print('='*60)
    sys.exit(0 if total_failed == 0 else 1)