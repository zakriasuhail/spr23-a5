#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("5 * 10").output == "50"
assert run("5 * 5").exit_status == 0
###

print("All tests passed!")