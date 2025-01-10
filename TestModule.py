# Імітація системної помилки

class TestModule:
    def __init__(self, error_handler):
        self.error_handler = error_handler

    def run_tests(self):
        try:
            print("\nRunning tests...")
            raise ValueError("Test error: Invalid value detected!")
        except ValueError as e:
            self.error_handler.handle_error(str(e))
        print("Done running tests!")