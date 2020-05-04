import datetime, time

txt = 1582971586

ltime = time.localtime(txt)
timeTXT = time.strftime('%Y-%m-%d %H:%M:%S', ltime)
print(timeTXT)


#根据时间戳返回 指定格式的 时间字符串
def getTimeStr(longTime):
    ltime = time.localtime(longTime)
    return time.strftime('%Y-%m-%d %H:%M:%S', ltime)
    
    
    
# 获取当前时间戳
import time
def getNowTimeStamp():
    return int(time.time())
