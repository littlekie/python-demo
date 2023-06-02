import win32pipe
import win32file
import time

pipe_name = r'\\.\pipe\my_pipe'


def pipe_start():
    pipe_handle = win32pipe.CreateNamedPipe(
    pipe_name,
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
    win32pipe.PIPE_UNLIMITED_INSTANCES, 65536, 65536,
    0,
    None
)
    print('等待连接。。。')
    
    win32pipe.ConnectNamedPipe(pipe_handle, None)
    print('连接成功')

    # 接收消息
    while True:
        try:
            buffer = win32file.ReadFile(pipe_handle, 4096)
            message = buffer[1].decode()
            if message:
                print('收到消息:',message)
                message = "hello ,my name is server".encode()
                win32file.WriteFile(pipe_handle, message)
                time.sleep(2)

            else:
                print('管道已关闭')
                break
        except Exception as e:
            print('发生错误:', str(e))
            break
    # 关闭管道
    win32pipe.DisconnectNamedPipe(pipe_handle)
    win32file.CloseHandle(pipe_handle)
    pipe_start()
pipe_start()