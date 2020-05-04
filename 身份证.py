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
