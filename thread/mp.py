import multiprocessing
import multiprocessing.process
import time

def rice_making():
    print('making rice:wash rice \n')
    print('making rice:soak rice \n')
    time.sleep(2)
    print('making rice:cook in cooker \n')


def sambar_making():
    print('making sambar: cut and cook veg \n')
    print('making sambar:cook parupu  \n')
    time.sleep(2)
    print('making sambar:mix veges + parupu  \n')


# start =time.time()
# rice_making()
# sambar_making()
# end=time.time()


# print("total time:",end-start)

# multiprocessing




if __name__=='__main__':
    process_1 =multiprocessing.Process(target=rice_making)
    process_2=multiprocessing.Process(target=sambar_making)

# end process
    start=time.time()
    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
    end=time.time()
    print("total time:",end-start)