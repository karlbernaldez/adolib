import sys
import datetime

class SimpleLogger:
    RESET = "\033[0m"
    COLORS = {
        "INFO": "\033[92m",    # Green
        "WARNING": "\033[93m", # Yellow
        "ERROR": "\033[91m",   # Red
    }

    def __init__(self, use_timestamp=True):
        self.use_timestamp = use_timestamp

    def _log(self, level, message):
        color = self.COLORS.get(level, self.RESET)
        timestamp = ""
        if self.use_timestamp:
            timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        formatted = f"{color}{timestamp}{level}: {message}{self.RESET}"
        # Choose stream based on level
        if level == "INFO":
            stream = sys.stdout
        else:  # WARNING and ERROR
            stream = sys.stderr
        print(formatted, file=stream)

    def info(self, message):
        self._log("INFO", message)

    def warning(self, message):
        self._log("WARNING", message)

    def error(self, message):
        self._log("ERROR", message)
