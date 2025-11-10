# Test Suite for Claude Plugin Marketplace

This directory contains comprehensive tests for validating the Claude Plugin Marketplace structure, content, and integrity.

## Test Files

### `test_marketplace_config.py`
Tests for `marketplace.json` configuration validation:
- JSON validity and structure
- Required fields presence
- Version number format (semantic versioning)
- Plugin configuration completeness
- Source path validation
- Unique naming constraints

### `test_markdown_structure.py`
Tests for markdown file structure and content:
- YAML frontmatter validation
- Heading hierarchy
- File organization
- Sub-skill file structure
- Template file validation
- Reference documentation

### `test_readme.py`
Tests for README.md validation:
- Content completeness
- Installation instructions
- Plugin descriptions
- Code block syntax
- Link formatting
- GitHub references

### `test_file_integrity.py`
Tests for file integrity and cross-references:
- File existence checks
- UTF-8 encoding validation
- Cross-reference validation
- Phase numbering consistency
- Directory structure
- Content quality checks

### `test_edge_cases.py`
Tests for edge cases and advanced validation:
- Duplicate detection
- Naming conventions
- Path formatting
- Version validation
- Markdown quality
- Directory organization
- Consistency checks

## Running Tests

### Run All Tests
```bash
# Using Python directly
python3 tests/run_tests.py

# Using shell script
./tests/run_tests.sh

# From repository root
cd /path/to/repo
python3 -m tests.run_tests
```

### Run Individual Test Files
```bash
# Run specific test file
python3 tests/test_marketplace_config.py
python3 tests/test_markdown_structure.py
python3 tests/test_readme.py
python3 tests/test_file_integrity.py
python3 tests/test_edge_cases.py
```

## Test Coverage

The test suite validates:

1. **Configuration Files**
   - JSON schema and structure
   - Required fields and data types
   - Version numbering
   - Path references

2. **Markdown Documentation**
   - YAML frontmatter
   - Heading structure
   - Code block formatting
   - Content completeness
   - Cross-references

3. **File Integrity**
   - File existence
   - Encoding (UTF-8)
   - Directory structure
   - No empty files
   - Proper organization

4. **Content Quality**
   - No TODO markers in production files
   - No placeholder text
   - Consistent terminology
   - Proper punctuation
   - Template usability

5. **Edge Cases**
   - Duplicate prevention
   - Naming conventions
   - Path validation
   - Consistency across files
   - Proper hierarchies

## Adding New Tests

To add new tests:

1. Create a new test file: `tests/test_your_feature.py`
2. Follow the existing structure with test classes
3. Use descriptive test method names starting with `test_`
4. Include docstrings explaining what each test validates
5. The master test runner will automatically pick up new test files

Example test structure:
```python
"""
Tests for your feature.
"""
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


class TestYourFeature:
    """Test suite for your feature."""
    
    def setup_method(self):
        """Setup test fixtures."""
        # Initialize test data
        pass
    
    def test_something_specific(self):
        """Test that something specific works correctly."""
        assert True, "Test assertion message"


if __name__ == '__main__':
    # Test runner code
    pass
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Design Principles

1. **No External Dependencies**: Tests use only Python standard library
2. **Self-Contained**: Each test file can run independently
3. **Clear Assertions**: Each assertion has a descriptive message
4. **Comprehensive Coverage**: Tests validate structure, content, and consistency
5. **Maintainable**: Tests follow consistent patterns and are well-documented

## Exit Codes

- `0`: All tests passed
- `1`: One or more tests failed

## CI/CD Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Run tests
        run: python3 tests/run_tests.py
```