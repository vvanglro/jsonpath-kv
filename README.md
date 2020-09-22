### **GetJsonValue**
pip install GetJsonValue

from GetJsonValue import jsonvalue

user_dict = { "sites": [ { "name":"runoob" , "url":"www.runoob.com" }, { "name":"google" , "url":"www.google.com" }, { "name":"weibo" , "url":"www.weibo.com" } ] }\n
r = jsonvalue.get(user_dict,'url')\n
print(r)\n
output: ['www.runoob.com', 'www.google.com', 'www.weibo.com']\n

user_json = '{ "sites": [ { "name":"runoob" , "url":"www.runoob.com" }, { "name":"google" , "url":"www.google.com" }, { "name":"weibo" , "url":"www.weibo.com" } ] }'\n
r = jsonvalue.get(user_dict,'url')\n
print(r)\n
output: ['runoob', 'google', 'weibo']\n

user_dict = {"sites": "{ "name":"google" , "url":"www.google.com" }"}\n
r = jsonvalue.get(user_dict,'name')\n
print(r)\n
output: google\n
