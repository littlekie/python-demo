import win32pipe
import win32file
import time

pipe_name = r'\\.\pipe\my_pipe'

pipe_handle = win32file.CreateFile(
    pipe_name,
    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
    0, None,
    win32file.OPEN_EXISTING,
    0, None
)

message = "Hello from Client".encode()
win32file.WriteFile(pipe_handle, message)
# while True:
#     try:

#         buffer = win32file.ReadFile(pipe_handle, 4096)
#         message = buffer[1].decode()
#         print("client  received:", message)
#         message = "i am is client ".encode()
#         win32file.WriteFile(pipe_handle, message)
#     except Exception as e:
#         print(e)
# 发送消息
while True:
    try:
        buffer = win32file.ReadFile(pipe_handle, 4096)
        message = buffer[1].decode()
        print("client  received:", message)
        message = "i am is client ".encode()
        win32file.WriteFile(pipe_handle, message)
        # pipe_handle.Close()
        time.sleep(1)
    except Exception as e:
        print('发生错误:', str(e))
        break