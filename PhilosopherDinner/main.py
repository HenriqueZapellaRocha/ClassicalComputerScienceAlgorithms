
import threading
import time
import random
lock = threading.Lock()
counts = [0,0,0,0,0]
#creating the philosopher
class philosopher: 
    
    def __init__(self, leftFork:threading.Semaphore, rightFork:threading.Semaphore) -> None:
        self.leftFork = leftFork
        self.rightFork = rightFork
        
def dinner(phil:philosopher, id:int):
    while True:
        print('philosopher think:'+ str(id))
 
        
        if phil.leftFork.acquire(timeout=0.1):
            if phil.rightFork.acquire(timeout=0.1):
                print('philosopher eat:'+ str(id))
                lock.acquire()
                counts[id-1] += 1
                lock.release()
                phil.leftFork.release()
                phil.rightFork.release()
            else:
                phil.leftFork.release()

        print(counts)
        
        
if __name__ == '__main__':

    #cretaing forks like a semaphores 
    fork = [threading.Semaphore(1) for i in range (5)]
    
    philosophers = []
    
    #adding the forks for the philosophers
    for i in range(5):      
        philosophers.append(philosopher(fork[i], fork[(i+1)%5]))
    
    #transforming the philosophers in threads(processes)
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=dinner, args=(philosophers[i],(i+1))))
        
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
    