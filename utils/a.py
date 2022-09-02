from typing import Optional

def greet(name: Optional[str]=None) -> str:
  if not name:
    name = "World"
  return f"Hello {name}!"