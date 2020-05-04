

# 获取当前时间戳
import time
def getNowTimeStamp():
    return int(time.time())


# 汉字转拼音
import pypinyin
s = ''
for i in pypinyin.pinyin('汉字', style=pypinyin.NORMAL):
   s += ''.join(i)
   
   
# 汉字URL编码
import urllib.parse
urlCode = urllib.parse.quote('汉字'.encode('utf8'))

# 身份证 相关信息提取

userId  = '身份证XXXXX'

y = userId[6:10]
m = userId[10:12]
d = userId[12:14]

if m.startswith('0'):
   m = m[1]
if d.startswith('0'):
   d = d[1]

gender = int(userId[16:17]) % 2  # 性别计算 0 女 1 男
