from proxi import run_proxy
import threading
import time
from node_send_recive import main



if __name__ == "__main__":
    print("start node")
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=run_proxy)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
