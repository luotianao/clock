import time

def shen_cheng_clock():
    while True:
        # 获取当前时间
        current_time = time.localtime()
        hour = str(current_time.tm_hour).zfill(2)  # 将小时数转换为2位数，不足的用0填充
        minute = str(current_time.tm_min).zfill(2)  # 将分钟数转换为2位数，不足的用0填充
        second = str(current_time.tm_sec).zfill(2)  # 将秒数转换为2位数，不足的用0填充

        # 打印时钟
        print(f"\r{hour}:{minute}:{second}", end="")
        time.sleep(1)  # 暂停1秒

shen_cheng_clock()
