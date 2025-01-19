import time

class SessionMonitor:
    def __init__(self, max_duration):
        self.start_time = time.time()
        self.max_duration = max_duration

    def check_session(self):
        elapsed = time.time() - self.start_time
        if elapsed > self.max_duration:
            print("Session limit exceeded. Please take a break.")
        else:
            print(f"Time elapsed: {elapsed} seconds.")

# Example usage
if __name__ == "__main__":
    monitor = SessionMonitor(max_duration=3600)
    time.sleep(2)  # Simulating gameplay
    monitor.check_session()