#处理json字符串
import json

people_string = '''
{
"people":[
        { "name":"John Smith",
          "phone":"615-555-7154",
          "emails":["johnsmith@bogusemail.com","john.smith@work-place.com"],
          "has_license":false},
        {
         "name":"jane Doe",
         "phone":"560-555-5153",
         "emails":null,
         "has_license":true
        }
]
}
'''

data= json.loads(people_string)                              #json.loads():json格式字符串，变成了字典
print(type(data))
for person in data['people']:
    del person['phone']
new_string = json.dumps(data,indent=2)        #json.dumps():json格式的字典/列表,变成了字符串


print(new_string)




