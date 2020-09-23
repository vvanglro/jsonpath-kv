# **jsonpath-kv**
    pip install jsonpath-kv
    from jsonpath_kv import jsonvalue
## 正常的dict
    user_dict = {
        "sites":
            [
                { "name":"runoob" , "url":"www.runoob.com" },
                { "name":"google" , "url":"www.google.com" },
                { "name":"weibo" , "url":"www.weibo.com" }
            ]
    }
    r = jsonvalue.get(user_dict,'url')
    print(r)
    output: ['www.runoob.com', 'www.google.com', 'www.weibo.com']
## json字符串
    user_json = '{ "sites": [ { "name":"runoob" , "url":"www.runoob.com" }, { "name":"google" , "url":"www.google.com" }, { "name":"weibo" , "url":"www.weibo.com" } ] }'
    r = jsonvalue.get(user_dict,'url')
    print(r)
    output: ['runoob', 'google', 'weibo']
## 当所取key在字符串包裹里时
    user_json = { "sites": '[ { "name":"runoob" , "url":"www.runoob.com" }, { "name":"google" , "url":"www.google.com" }, { "name":"weibo" , "url":"www.weibo.com" } ]'}
    r = jsonvalue.get(user_dict,'url')
    print(r)
    output: ['runoob', 'google', 'weibo']
## 当所取key在字符串包裹里时
    user_dict = {"sites": "{ \"name\":\"google\" , \"url\":\"www.google.com\" }"}
    r = jsonvalue.get(user_dict,'name')
    print(r)
    output: ['google']
## key不存在时返回false
    user_dict = {"sites": "{ \"name\":\"google\" , \"url\":\"www.google.com\" }"}
    r = jsonvalue.get(user_dict, 'address')
    print(r)
    output: False


