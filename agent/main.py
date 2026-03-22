import sys
from .agent_loop import run_agent
from .memory import get_history, get_failures

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py logs.txt")
        exit()

    result = run_agent(sys.argv[1])

    print("FINAL:", result)

    print("\nTRACE:")
    for step in get_history():
        print(step)

    print("\nFAILURES:")
    for f in get_failures():
        print(f)
