import time
import threading

class Sleep(threading.Thread):
    def __init__(self, sleep_duration):
        self.sleep_duration = sleep_duration

    def sleep(self):
        print("start sleep")
        time.sleep(self.sleep_duration)
        print("end sleep")

if __name__ == "__main__":
    sleep_class = Sleep(2)
    t1 = threading.Thread(target=sleep_class.sleep)
    t1.start()
    t1.join(timeout=1)
    print("end process sleep")
    
   
    