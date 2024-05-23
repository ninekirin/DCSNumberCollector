from node import run_server
from coordinator import sum
import threading

if __name__ == '__main__':
    ports = [8000, 8001, 8002]
    for port in ports:
        threading.Thread(target=run_server, args=(port,), daemon=True).start()
    print(f"Total sum of numbers: {sum(ports)}")