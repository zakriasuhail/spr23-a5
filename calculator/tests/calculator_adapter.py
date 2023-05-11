import subprocess
import os
from collections import namedtuple
from os import path

root_dir = path.join(path.dirname(__file__), "..")

Status = namedtuple('Status', ['exit_status', 'output'])

def run(equation: str) -> Status:
  if os.getenv("OUTPUT_RUNS") is not None:
    print("TEST RUN:", equation)
  
  proc = subprocess.run([path.join(root_dir, "calculator"), "-q", *equation.split()], stdout=subprocess.PIPE)
  return Status(proc.returncode, proc.stdout.decode().strip())