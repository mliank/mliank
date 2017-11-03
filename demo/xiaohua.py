#!/usrs/lixinru/python/demo python
# -*- coding:UTF-8 -*-
# auther: xiaolan

import re
from urllib import request
url = 'http://www.xiaohuar.com/d/file/20170917/715515e7fe1f1cb9fd388bbbb00467c2.jpg'
#下载图片,发送http请求
response =request.urlopen(url)
#print(response.read())
# 保存图片
# 打开
with open('1.jpg','wb') as f:
    f.write(response.read())
#f = open('1.jpg','wb')# wb叫做二进制模式打开
#f.write(response.read())
#f.close()