#!/bin/bash
# Simple shell script to run all tests

cd "$(dirname "$0")/.." || exit

echo "Running Claude Plugin Marketplace Test Suite"
echo "============================================="
echo ""

python3 tests/run_tests.py
exit_code=$?

echo ""
echo "Test run completed with exit code: $exit_code"
exit $exit_code