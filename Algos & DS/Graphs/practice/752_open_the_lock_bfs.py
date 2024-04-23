from typing import List

def openLock(deadends: List[str], target: str) -> int:
  if "0000" in deadends:
    return -1