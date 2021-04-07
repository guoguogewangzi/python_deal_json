#处理json文件
import json
import time

#读json文件loads为字典，保存在data列表中
data=[]
with open ('test.json', 'r') as f:
    for line in f :
        data.append(json.loads(line))

#弹出data中每行字典的不要的key
for tmp in data:
    tmp.pop('event_hash')
    tmp.pop('actor_hash')
    tmp.pop('attacker_location')
    tmp.pop('vlan')
    tmp.pop('flow')
    tmp.pop('location')
    tmp.pop('in_iface')
    tmp.pop('flow_id')
    tmp['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tmp['timestamp']))
    tmp['time'] = tmp.pop('timestamp')

#dumps每行data字典为字符串，由于json.dumps()后，'\uxxx'会变成'\\uxxx',所以需要.encode('utf-8').decode('unicode-escape')变成'\uxxx'
with open ("result.json", 'w') as f:
    for line in data:
        f.write(json.dumps(line).encode('utf-8').decode('unicode-escape')+'\n')



