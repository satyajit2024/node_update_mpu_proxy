from proxi import hello
import redis
import threading
import time

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def new_function():
    while True:
        sens1 = r.get("sensor1_rpm")
        sens2 = r.get("sensor2_rpm")
        print("senser1 data......",sens1)
        print("senser2 data......",sens2)
        time.sleep(1)
        


if __name__ == "__main__":
    t1 = threading.Thread(target=new_function)
    t2 = threading.Thread(target=hello)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
