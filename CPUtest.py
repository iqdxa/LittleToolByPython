import os
import time
print("此程序将会消耗大量资源")
time.sleep(1)
print("将打开任务管理器")
time.sleep(1)
print("请留意资源使用率")
time.sleep(1)
print("请等待")
time.sleep(1)
for i in range(3):
    print(3-i,end=" ")
    time.sleep(1)
os.system("taskmgr")
a = 2
while(True):
    a = a**100
