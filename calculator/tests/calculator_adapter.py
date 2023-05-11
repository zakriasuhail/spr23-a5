import ctypes
import subprocess
import os
from collections import namedtuple
from os import path

root_dir = path.join(path.dirname(__file__), "..")
calculator = ctypes.CDLL(path.join(root_dir, "calculator.so"))

Status = namedtuple('Status', ['exit_status', 'output'])

def add(a: int, b: int) -> int:
  return calculator.add(a, b)

def subtract(a: int, b: int) -> int:
  return calculator.subtract(a, b)

def multiply(a: int, b: int) -> int:
  return calculator.multiply(a, b)

def divide(a: int, b: int) -> int:
  return calculator.divide(a, b)

def run(equation: str) -> Status:
  if os.getenv("OUTPUT_RUNS") is not None:
    print("TEST RUN:", equation)
  
  proc = subprocess.run([path.join(root_dir, "calculator"), "-q", *equation.split()], stdout=subprocess.PIPE)
  return Status(proc.returncode, proc.stdout.decode().strip())