import os
import time
print("此程序为资源使用程序")
time.sleep(1)
print("将打开任务管理器")
time.sleep(1)
print("请留意资源使用率")
time.sleep(1)
print("倒计时3秒:")
time.sleep(1)
for i in range(3):
    print(3-i,end=" ")
    time.sleep(1)
os.system("taskmgr")
a = 2
while(True):
    a = a**100