class MyContext:
    def __enter__(self):
        # 在进入 with 块之前执行一些操作，比如打开文件等
        print('Entering context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # 在离开 with 块时执行一些操作，比如关闭文件等
        print('Exiting context')
    
    def do_something(self):
        print('Doing something')

# 使用 with 语句来创建对象并执行一些操作
with MyContext() as context:
    context.do_something()