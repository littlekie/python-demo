import threading
from typing import Iterable


def new_thread(target: callable, args: Iterable[any] = None, timeout: float = None, daemon = True):
    '''
    设置为daemon的线程和没有设置为daemon的线程有什么不同

    daemon线程：
    当一个线程设置为daemon线程时，主线程结束时，不会因为daemon线程还没有结束运行而阻塞。也就是主线程不管先daemon线程。类比可以想像一下运行程序后启动一个主线程，然后又一个后台线程也启动。如果这个程序要退出了，却因为后台程序还在运行而无法退出，这就不合适了。

    非daemon线程：
    当一个线程设置为非daemon线程时，主线程结束时，会检查所有非daemon的子线程是否结束。如果还未结束，则主线程等待非daemon结束后再退出。

    '''
    thread = threading.Thread(target=target, args=args)
    thread.daemon = daemon
    thread.start()
    if timeout:
        # wait until the thread finishes
        thread.join(timeout)


if __name__ == '__main__':
    def get_demo(a):
        import time
        time.sleep(2)
        print(a)
    new_thread(target=get_demo, args=[10], timeout=4)
    print(100)
