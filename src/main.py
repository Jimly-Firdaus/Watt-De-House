import threading
from src.UI.app import run_app

if __name__ == "__main__":
    exit_flag = threading.Event()
    run_app(exit_flag)
