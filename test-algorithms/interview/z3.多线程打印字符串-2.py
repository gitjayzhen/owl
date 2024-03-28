import threading
from queue import Queue

# abc， def， ghi 输出 adg，beh, cfi

global_thread_lock = threading.Condition(threading.Lock())
global_queue = Queue()

class WorkThread(threading.Thread):
    
    def __init__(self, name, result):
        threading.Thread.__init__(self, name=name)
        self.result = result
        self.name = name
        self.exit_flag = False
    
    def run(self):
        while not self.exit_flag:
            if global_thread_lock.acquire():
                # 如果有生产者，可以添加 wait
                if global_queue.empty():
                    self.exit_flag = True
                else:
                    tmp = [[x] for x in global_queue.get()]
                    for i in range(len(tmp)):
                        self.result[i].extend(tmp[i])
                global_thread_lock.notify()
                global_thread_lock.release()

def main(data):
    result = [[],[],[]]
    v_1 = WorkThread('w1', result)
    v_2 = WorkThread('w2', result)
    
    global_thread_lock.acquire()
    for d in data:
        global_queue.put(d)
    global_thread_lock.release()
    
    works = [v_1, v_2]
    for i in works:
        i.start()
        i.join()
        
    for n in result:
        print("".join(n))
     
if __name__ == "__main__":
    main(["abc", "def", "ghi"])
    