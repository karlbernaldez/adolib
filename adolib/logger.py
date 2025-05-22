import sys
import datetime

class SimpleLogger:
    RESET = "\033[0m"
    COLORS = {
        "DEBUG": "\033[94m",    # Blue
        "INFO": "\033[92m",     # Green
        "SUCCESS": "\033[96m",  # Cyan
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",    # Red
        "CRITICAL": "\033[95m", # Magenta
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
        if level in ["ERROR", "CRITICAL"]:
            stream = sys.stderr
        else:
            stream = sys.stdout
        print(formatted, file=stream)

    def debug(self, message):
        self._log("DEBUG", message)

    def info(self, message):
        self._log("INFO", message)

    def success(self, message):
        self._log("SUCCESS", message)

    def warning(self, message):
        self._log("WARNING", message)

    def error(self, message):
        self._log("ERROR", message)

    def critical(self, message):
        self._log("CRITICAL", message)
