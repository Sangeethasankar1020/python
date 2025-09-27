import threading
import time


def rice_washing():
    print("take bowl \n")
    print("take 2 cup rice \n")
    time.sleep(2)
    print("4 time rinse \n")

def rice_soaking():
    print("take tumbler \n")
    print("measure 2 cup water  \n")
    time.sleep(2)
    print(" put it in rice and soak \n")
    
start =time.time()
rice_washing()
rice_soaking()
end=time.time()

print("total time:",end-start)


thread_1 = threading.Thread(target=rice_washing)
thread_2 = threading.Thread(target=rice_soaking)
start =time.time()


thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
end=time.time()