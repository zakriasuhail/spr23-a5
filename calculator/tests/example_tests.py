#!/usr/bin/env python3
from calculator_adapter import run

### EXAMPLE TESTS
# Checks that the program outputs "3" for an input of "1 + 2"
assert run("1 + 2").output == "3"
# Checks that the program outputs "8" for an input of "2 * 4"
assert run("2 * 4").output == "8"
# Checks that the program exists successfully (no error) for input "2 * 4"
assert run("2 * 4").exit_status == 0
# Checks that the program fails (correctly errors) for input "2 @ 3"
assert run("2 @ 3").exit_status != 0

print("All tests passed!")