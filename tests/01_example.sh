#!/urs/bin/env bash

# (The absolute path to the program is provided as the first and only argument.)
PROGRAM=$1

echo "We've set up a GitHub Actions Workflow that will run all"
echo "of the shell scripts in this directory as a series of tests."
echo
echo "To fail any test, you should use the exit 1 command;"
echo "To end a test early as a success, you should use the exit 0 command."

echo "Invoke your program with the \$PROGRAM variable; an example is below"


# Test 01: Ensure the program runs without error with no arguments.
$PROGRAM