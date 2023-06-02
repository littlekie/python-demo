

import threading

# 共享资源
counter = 0

# 创建一个锁对象
lock = threading.Lock()

def worker():
    global counter

    # 获取锁
    with lock:
        for i in range(100000):
            counter += 1

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()

print("Counter value:", counter)

def width_lock_demo():
    import threading

        # 创建一个锁对象
    lock = threading.Lock()

    def worker():
        with lock:
            # 这里写入需要锁保护的代码
            print(f'{threading.current_thread().name} acquired the lock')
            # ...

    # 创建多个线程并让它们执行 worker() 函数
    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

