#处理请求api返回的json格式数据
import json
from urllib.request import urlopen

with urlopen("http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key=%E9%93%B6%E9%AD%82&bk_length=600") as response:
    source = response.read()
print("source数据类型为：",type(source),source)

data = json.loads(source)                          #json转字典
print("data数据类型为：",type(data))
print(json.dumps(data,indent=2))                  #字典转字符串，并格式化:indent=2

#data字典处理
new_dict=dict()
for card in data['card']:
    key=card['key']
    name=card['name']
    new_dict[key]=name

print(new_dict['m21_ext_2'])


