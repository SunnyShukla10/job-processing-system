import datetime

class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._logs = []
            cls._instance_level = "DEBUG"
        return cls._instance

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _write(self, level, message):
        ts = self._timestamp
        formatted = f"[{ts}] {level}: {message}"
        self._logs.append(formatted)
    
    def info(self, message):
        self._write("INFO", message)
    
    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)

    def debug(self, message):
        self._write("DEBUG", message)
    
    def get_logs(self):
        return self._logs
