class Logger():
    def __init__(self):
        self.ENDC = '\033[0m'
        self.ERROR = '\033[91m'
        self.INFO = '\033[93m'

    def info(self, text=""):
        print(f"{self.INFO}[INFO] {text}{self.ENDC}")

    def error(self, text=""):
        print(f"{self.ERROR}[ERROR] {text}{self.ENDC}")