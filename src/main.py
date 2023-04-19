import threading
from UI.app import run_app

if __name__ == "__main__":
    exit_flag = threading.Event()
    run_app(exit_flag)
