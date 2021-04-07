#处理json文件并保存为csv格式
import json
import time


#读文件并json.loads()为字典，保存在data列表中
data=[]
with open("test.json") as f:
    for line in f:
        data.append(json.loads(line))


#字典类型根据key取值
def getvalue(dict,key):
    try:
        return i[key]
    except:
        return

#取值并保存在data2列表中
data2=[]
for i in data:

    data2.append(dict(
                      event_hash=i['event_hash'],
                      time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i['timestamp'])),
                      event_type=i['event_type'],
                      proto=i['proto'],
                      app_proto=getvalue(i,'app_proto'),
                      is_c2=i['is_c2'],
                      src_ip=i['src_ip'],
                      src_port=i['src_port'],
                      dest_port=i['dest_port'],
                      dest_ip=i['dest_ip'],
                      victim_ip=i['victim_ip'],
                      attacker_ip=i['attacker_ip'],
                      alert_category=i['alert']['category'],
                      alert_signature_family=i['alert']['signature']['family'],
                      alert_signature_description=i['alert']['signature']['description'],
                      alert_signature_sign_source=i['alert']['signature']['sign_source'],
                      alert_signature_author=i['alert']['signature']['author'],
                      alert_signature_attack_phase=i['alert']['signature']['attack_phase'],
                      alert_signature_threat_judge=i['alert']['signature']['threat_judge'],
                      alert_signature_extract_date=i['alert']['signature']['extract_date'],
                      alert_signature_behavior=i['alert']['signature']['behavior'],
                      alert_signature_remarks=i['alert']['signature']['remarks'],
                      alert_signature_cve_number=i['alert']['signature']['cve_number'],
                      alert_signature_threat_level=i['alert']['signature']['threat_level'],
                      alert_signature_threat_type=i['alert']['signature']['threat_type'],
                      alert_signature_attack_direction_=json.dumps(i['alert']['signature']['attack_direction']).replace(',',';'),
                      alert_signature_refer=i['alert']['signature']['refer'],
                      alert_action=i['alert']['action'],
                      attacker_location_country=i['attacker_location']['country'],
                      attacker_location_city=i['attacker_location']['city'],
                      location_dest_province=i['location']['dest']['province'],
                      location_dest_city=i['location']['dest']['city'],
                      location_dest_country=i['location']['dest']['country'],
                      location_src_province=i['location']['src']['province'],
                      location_src_city=i['location']['src']['city'],
                      location_src_country=i['location']['src']['country']
                      ))


#取key->列表，保存在data3中
data3=[list(data2[0].keys())]

#取value->列表，保存在data3中
for line in data2:
    data3.append(list(line.values()))



#将data3中的每个列表元素拼接成字符串
data4=[]
for line in data3:
    data4.append(",".join('%s' % id  for id in line))


#根据data4列表按行写文件
with open('result.csv', 'w') as f:
    for line in data4:
        f.write(line+'\n')