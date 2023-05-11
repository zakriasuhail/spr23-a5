#!/usr/bin/env python3
from calculator_adapter import run

assert run("1 + 2").output == "3"
assert run("2 * 4").output == "8"
assert run("2 * 4").exit_status == 0
assert run("2 @ 3").exit_status != 0

print("All tests passed!")