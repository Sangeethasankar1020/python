import _thread
import time


# threat - subtask of process(task) , if you want to create a task we have to create thread not process(multiple thread).

# 1. kernel level thread - os process - in programatic 
# 2.user level thread - what user needs - simulatneous run - background run 

# access package - 1) _thread 3.7 version works , thread 2.7 
                #  2) threading - its common 



# def a():
#     count=0
#     while  count <5:
#         count+=1
#         print("function A")



# def b():
#     count=0
#     while  count <5:
#         count+=1
#         print("function B")


# a()
# b()

def a(msg):
    count=0
    while  count <5:
        count+=1
        time.sleep(3)
        print(msg)



def b(msg):
    count=0
    while  count <5:
        count+=1
        time.sleep(3)
        print(msg)

# try:
#     _thread.start_new_thread(a,("function A",))
#     _thread.start_new_thread(b,("function B",))

# except Exception as e:
#     print(e)

# while 1:
#     pass

# This is very important in your example.

# ✅ Reason:
# Python’s main thread exits as soon as the script ends.

# If the main thread exits before a() and b() finish, all threads are killed.

# To keep the main program alive, you're using while 1: pass (an infinite loop).

# 🧠 So, this line:
# Prevents the program from exiting immediately

# Gives a() and b() enough time to finish their work

# ------------------------------------------------------------
import threading

t1 = threading.Thread(target=a, args=("function A",))
t2 = threading.Thread(target=b, args=("function B",))

t1.start()
t2.start()

t1.join() #main thread wait to join 
t2.join() #main thread wait to join 


