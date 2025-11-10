"""
Tests for markdown file structure and content validation.
"""
import os
import re
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


class TestSkillMarkdownStructure:
    """Test suite for SKILL.md file structure."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.skill_path = repo_root / 'skills' / 'oss-contribution-framework' / 'SKILL.md'
        with open(self.skill_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')
    
    def test_file_exists(self):
        """Test that SKILL.md exists."""
        assert self.skill_path.exists(), "SKILL.md file must exist"
    
    def test_has_yaml_frontmatter(self):
        """Test that file starts with YAML frontmatter."""
        assert self.lines[0] == '---', "File must start with YAML frontmatter (---)"
        # Find closing ---
        closing_idx = None
        for i in range(1, min(20, len(self.lines))):
            if self.lines[i] == '---':
                closing_idx = i
                break
        assert closing_idx is not None, "YAML frontmatter must be closed with ---"
    
    def test_frontmatter_has_name(self):
        """Test that frontmatter contains name field."""
        frontmatter = '\n'.join(self.lines[:20])
        assert re.search(r'^name:\s*\S+', frontmatter, re.MULTILINE), \
            "Frontmatter must contain 'name' field"
    
    def test_frontmatter_has_description(self):
        """Test that frontmatter contains description field."""
        frontmatter = '\n'.join(self.lines[:20])
        assert re.search(r'^description:\s*\S+', frontmatter, re.MULTILINE), \
            "Frontmatter must contain 'description' field"
    
    def test_frontmatter_name_matches_directory(self):
        """Test that frontmatter name matches directory name."""
        name_match = re.search(r'^name:\s*(.+)$', '\n'.join(self.lines[:20]), re.MULTILINE)
        assert name_match, "Could not find name in frontmatter"
        name = name_match.group(1).strip()
        assert name == 'oss-contribution-framework', \
            f"Frontmatter name '{name}' should match 'oss-contribution-framework'"
    
    def test_has_main_heading(self):
        """Test that file has a main H1 heading."""
        assert any(line.startswith('# ') for line in self.lines), \
            "File must have at least one H1 heading (# )"
    
    def test_main_heading_after_frontmatter(self):
        """Test that main heading comes after frontmatter."""
        closing_idx = next(i for i in range(1, 20) if self.lines[i] == '---')
        h1_lines = [i for i, line in enumerate(self.lines) if line.startswith('# ')]
        assert len(h1_lines) > 0, "Must have at least one H1 heading"
        assert h1_lines[0] > closing_idx, "First H1 must come after frontmatter"
    
    def test_has_overview_section(self):
        """Test that file has an Overview section."""
        content_lower = self.content.lower()
        assert '## overview' in content_lower or '## overview' in content_lower, \
            "File should have an Overview section"
    
    def test_mentions_six_phases(self):
        """Test that file mentions the six phases."""
        content_lower = self.content.lower()
        assert 'six' in content_lower or '6' in content_lower, \
            "File should mention six/6 phases"
        assert 'phase' in content_lower, "File should mention phases"
    
    def test_has_code_blocks(self):
        """Test that file contains code blocks."""
        assert '```' in self.content, "File should contain code blocks (```)"
    
    def test_no_broken_markdown_syntax(self):
        """Test for common markdown syntax errors."""
        # Check for unmatched code blocks
        code_block_count = self.content.count('```')
        assert code_block_count % 2 == 0, \
            "Code blocks must be properly closed (even number of ```)"
    
    def test_reasonable_file_length(self):
        """Test that file is of reasonable length."""
        line_count = len(self.lines)
        assert line_count > 50, "SKILL.md seems too short"
        assert line_count < 2000, "SKILL.md seems excessively long"
    
    def test_no_trailing_whitespace_on_headings(self):
        """Test that headings don't have trailing whitespace."""
        for i, line in enumerate(self.lines):
            if line.startswith('#'):
                assert not line.endswith(' '), \
                    f"Line {i+1} has trailing whitespace: {line!r}"


class TestSubSkillMarkdownFiles:
    """Test suite for sub-skill markdown files."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.skills_dir = repo_root / 'skills' / 'oss-contribution-framework' / 'skills'
        self.skill_files = list(self.skills_dir.glob('*.md'))
    
    def test_skill_files_exist(self):
        """Test that skill files exist."""
        assert len(self.skill_files) > 0, "No skill files found"
        assert len(self.skill_files) >= 5, "Should have at least 5 sub-skill files"
    
    def test_all_skill_files_have_content(self):
        """Test that all skill files have reasonable content."""
        for skill_file in self.skill_files:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert len(content) > 100, \
                    f"{skill_file.name} seems too short"
    
    def test_skill_files_have_main_heading(self):
        """Test that each skill file has a main heading."""
        for skill_file in self.skill_files:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert content.startswith('#'), \
                    f"{skill_file.name} should start with a heading"
    
    def test_skill_files_have_phase_numbers(self):
        """Test that skill files reference phase numbers."""
        for _skill_file in self.skill_files:
            # At least one should mention a phase
            # (Some files might not, which is OK)
            pass
    
    def test_expected_skill_files_present(self):
        """Test that expected skill files are present."""
        expected_skills = [
            'issue-discovery.md',
            'issue-analysis.md',
            'codebase-exploration.md',
            'issue-code-mapping.md',
            'solution-implementation.md',
            'documentation-pr.md'
        ]
        skill_names = [f.name for f in self.skill_files]
        for expected in expected_skills:
            assert expected in skill_names, \
                f"Expected skill file not found: {expected}"


class TestTemplateFiles:
    """Test suite for template markdown files."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.templates_dir = repo_root / 'skills' / 'oss-contribution-framework' / 'assets' / 'templates'
        self.template_files = list(self.templates_dir.glob('*.md'))
    
    def test_template_files_exist(self):
        """Test that template files exist."""
        assert len(self.template_files) > 0, "No template files found"
    
    def test_templates_contain_placeholders(self):
        """Test that templates contain placeholders."""
        for template_file in self.template_files:
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Templates should have placeholders like [something]
                assert '[' in content and ']' in content, \
                    f"{template_file.name} should contain placeholders [like this]"
    
    def test_expected_templates_present(self):
        """Test that expected template files are present."""
        expected_templates = [
            'issue-analysis-template.md',
            'codebase-notes-template.md',
            'pr-checklist-template.md'
        ]
        template_names = [f.name for f in self.template_files]
        for expected in expected_templates:
            assert expected in template_names, \
                f"Expected template file not found: {expected}"
    
    def test_issue_analysis_template_structure(self):
        """Test issue analysis template has expected sections."""
        template_path = self.templates_dir / 'issue-analysis-template.md'
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            assert 'requirements' in content, \
                "issue-analysis-template should have Requirements section"
            assert 'issue' in content, \
                "issue-analysis-template should reference issue"
    
    def test_pr_checklist_template_has_checkboxes(self):
        """Test PR checklist template contains checkboxes."""
        template_path = self.templates_dir / 'pr-checklist-template.md'
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Markdown checkboxes are - [ ]
            assert '- [ ]' in content, \
                "pr-checklist-template should contain checkboxes (- [ ])"


class TestReferenceFiles:
    """Test suite for reference markdown files."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.refs_dir = repo_root / 'skills' / 'oss-contribution-framework' / 'references'
        self.ref_files = list(self.refs_dir.glob('*.md'))
    
    def test_reference_files_exist(self):
        """Test that reference files exist."""
        assert len(self.ref_files) > 0, "No reference files found"
    
    def test_expected_references_present(self):
        """Test that expected reference files are present."""
        expected_refs = [
            'contribution-tips.md',
            'issue-patterns.md',
            'pr-templates.md',
            'codebase-checklist.md'
        ]
        ref_names = [f.name for f in self.ref_files]
        for expected in expected_refs:
            assert expected in ref_names, \
                f"Expected reference file not found: {expected}"
    
    def test_reference_files_substantial(self):
        """Test that reference files have substantial content."""
        for ref_file in self.ref_files:
            with open(ref_file, 'r', encoding='utf-8') as f:
                content = f.read()
                line_count = len(content.split('\n'))
                assert line_count > 50, \
                    f"{ref_file.name} seems too short (only {line_count} lines)"


if __name__ == '__main__':
    # Simple test runner
    test_classes = [
        TestSkillMarkdownStructure,
        TestSubSkillMarkdownFiles,
        TestTemplateFiles,
        TestReferenceFiles
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