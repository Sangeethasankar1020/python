# import time
# import threading

# def showProcess(r,s,tName):
#     for i in range(r):
#         time.sleep(s)
#         print(tName)

# startThread=threading.Thread(target=showProcess,args=(4,2,"thread 1.."))

# startThread.start()

# startNewThread=threading.Thread(target=showProcess,args=(5,1,"thread 2.."))
# startNewThread.start()

# # To make the main program wait until both threads finish, use .join():
# startThread.join()
# startNewThread.join()
