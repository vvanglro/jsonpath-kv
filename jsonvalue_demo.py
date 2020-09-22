"""
#coding=utf-8
@File    : jsonpath2_demo.py
@Time    : 2020/9/12 14:04
@Author  : wanghao
@Email   : 947001731@qq.com
@Software: PyCharm
"""
import json

def dict_get(user_dict, objkey):
    if check_json_format(user_dict)[0]:
        result_list = []
        for k, v in check_json_format(user_dict)[1].items():
            # print k,v
            if k == objkey:
                result_list.append(v)
            elif type(v) is list:
                for val in v:
                    if type(val) is dict:
                        for key, value in val.items():
                            # print("%s:%s" % (key, value))
                            if key == objkey:
                                result_list.append(value)
            else:
                t = check_json_format(v)
                if t:
                    if t[0]:
                        if type(t[1]) is dict:
                            ret = dict_get(t[1], objkey)
                            result_list.append(ret)
        if len(result_list) == 1:
            return ''.join(result_list)
        return result_list
    else:
        raise ValueError("No JSON object could be decoded")

def check_json_format(raw_msg):
    if isinstance(raw_msg, str):
        try:
            raw_msg = json.loads(raw_msg)
        except ValueError:
            return False
        else:
            return True, raw_msg
    elif isinstance(raw_msg, dict):
        return True, raw_msg
    else:
        return False


if __name__ == '__main__':
    user_dict = {
        "sites":
            [
                { "name":"菜鸟教程" , "url":"www.runoob.com" },
                { "name":"google" , "url":"www.google.com" },
                { "name":"微博" , "url":"www.weibo.com" }
            ]
    }

    r = dict_get(user_dict,'url')
    print(r)