1~
#!/usr/bin/env python3
2~
"""
3~
Master test runner for the Claude Plugin Marketplace.
4~
Runs all test suites and provides a summary.
5~
"""
6~
import sys
7~
import importlib.util
8~
from pathlib import Path
9~

10~

11~
repo_root = Path(__file__).parent.parent
12~
tests_dir = Path(__file__).parent
13~

14~

15~
def load_and_run_test_module(test_file):
16~
    """Load and run a test module."""
17~
    module_name = test_file.stem
18~
    spec = importlib.util.spec_from_file_location(module_name, test_file)
19~
    module = importlib.util.module_from_spec(spec)
20~
    sys.modules[module_name] = module
21~
    spec.loader.exec_module(module)
22~
    
23~
    # Find test classes
24~
    test_classes = []
25~
    for attr_name in dir(module):
26~
        attr = getattr(module, attr_name)
27~
        if isinstance(attr, type) and attr_name.startswith('Test'):
28~
            test_classes.append(attr)
29~
    
30~
    return test_classes
31~

32~

33~
def run_all_tests():
34~
    """Run all test files."""
35~
    test_files = sorted(tests_dir.glob('test_*.py'))
36~
    
37~
    if not test_files:
38~
        print("No test files found!")
39~
        return 1
40~
    
41~
    total_passed = 0
42~
    total_failed = 0
43~
    all_results = []
44~
    
45~
    for test_file in test_files:
46~
        print(f"\n{'='*70}")
47~
        print(f"Running tests from: {test_file.name}")
48~
        print('='*70)
49~
        
50~
        try:
51~
            test_classes = load_and_run_test_module(test_file)
52~
            
53~
            for test_class in test_classes:
54~
                print(f"\n{test_class.__name__}")
55~
                print('-'*70)
56~
                
57~
                test_instance = test_class()
58~
                test_methods = [m for m in dir(test_instance) if m.startswith('test_')]
59~
                
60~
                class_passed = 0
61~
                class_failed = 0
62~
                
63~
                for method_name in test_methods:
64~
                    try:
65~
                        if hasattr(test_instance, 'setup_method'):
66~
                            test_instance.setup_method()
67~
                        method = getattr(test_instance, method_name)
68~
                        method()
69~
                        print(f"  ✓ {method_name}")
70~
                        class_passed += 1
71~
                        total_passed += 1
72~
                    except AssertionError as e:
73~
                        print(f"  ✗ {method_name}")
74~
                        print(f"      {e}")
75~
                        class_failed += 1
76~
                        total_failed += 1
77~
                    except Exception as e:
78~
                        print(f"  ✗ {method_name}")
79~
                        print(f"      Unexpected error: {e}")
80~
                        class_failed += 1
81~
                        total_failed += 1
82~
                
83~
                all_results.append({
84~
                    'class': test_class.__name__,
85~
                    'file': test_file.name,
86~
                    'passed': class_passed,
87~
                    'failed': class_failed
88~
                })
89~
                
90~
        except Exception as e:
91~
            print(f"Error loading test file {test_file.name}: {e}")
92~
            total_failed += 1
93~
    
94~
    # Print summary
95~
    print(f"\n{'='*70}")
96~
    print("TEST SUMMARY")
97~
    print('='*70)
98~
    
99~
    for result in all_results:
100~
        status = "✓" if result['failed'] == 0 else "✗"
101~
        print(f"{status} {result['class']:40} {result['passed']:3} passed, {result['failed']:3} failed")
102~
    
103~
    print('='*70)
104~
    print(f"TOTAL: {total_passed} passed, {total_failed} failed")
105~
    print('='*70)
106~
    
107~
    if total_failed == 0:
108~
        print("\n✓ All tests passed!")
109~
        return 0
110~
    else:
111~
        print(f"\n✗ {total_failed} test(s) failed")
112~
        return 1
113~

114~

115~
if __name__ == '__main__':
116~
    sys.exit(run_all_tests())