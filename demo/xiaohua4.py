#!/usrs/lixinru/python/demo python
# -*- coding:UTF-8 -*-
# auther: xiaolan

import re
from urllib import request
url = 'http://www.xiaohuar.com/hua'
# http://www.xiaohuar.com/list-1-1.html
# http://www.xiaohuar.com/list-1-2.html
urls = [
    'http://www.xiaohuar.com/list-1-1.html'
    'http://www.xiaohuar.com/list-1-2.html'
]
#下载页面
html = request.urlopen(url).read().decode('GBK')
#找到img的url,分析页面
#/d/file/20170919/2f728d0f110a21fea95ce13e0b010d06.jpg
#数字\d+    数字和字母\w+      \.
img_urls = re.findall(r'/d/file/\d+/\w+\.jpg',html)
img_urls = ("http://www.xiaohuar.com/hua%s" % url for url in img_urls)

for url in img_urls:
    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(request.urlopen(url).read())
    print(url)

# print(len(img_urls)),img_urls[0]

#url = 'http://xiaohuar.com/d/file/20170919/2f728d0f110a21fea95ce13e0b010d06.jpg'
#下载图片,发送http请求
#print(response.read())
# 保存图片
# 打开
#with open('1.jpg','wb') as f:
#    f.write(response.read())
#f = open('1.jpg','wb')# wb叫做二进制模式打开
#f.write(response.read())
#f.close()