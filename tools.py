import time

# 获取当前时间戳
def getNowTimeStamp():
    return int(time.time())

# 汉字转拼音
import pypinyin
s = ''
for i in pypinyin.pinyin('汉字', style=pypinyin.NORMAL):
   s += ''.join(i)
   
   
