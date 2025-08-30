# Stopwatch (CLI) – Simple console app using Python basics

import time

def stopwatch():
    print("=== STOPWATCH ===")
    print("Press ENTER to start, ENTER to stop, and Ctrl+C to quit.")
    while True:
        try:
            input("\nPress ENTER to start...")
            start = time.time()
            print("Stopwatch started... Press ENTER to stop.")
            input()
            end = time.time()
            elapsed = end - start
            mins, secs = divmod(int(elapsed), 60)
            millis = int((elapsed - int(elapsed)) * 1000)
            print(f"⏱ Elapsed Time: {mins:02d}:{secs:02d}.{millis:03d}")
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    stopwatch()
