#!/usr/bin/env python
# -*- coding: utf-8 -*-


from http import http
from http import https
from config import *
from function import *
import os
import time

# if u get the flag string, chk it before the post. If u still get some problems,
# this may blame to : 1.the network failure to flag_server
#                     2.the flag is out of data

#check wether the format of a flag is correct, suppose the format of a flag must be a string with hex value
def check_flag(flag):
    flag = flag.replace(" ","").replace("\n","")
    if len(flag)> 50 or len(flag)<10:
        return False
    return True
    if not flag:
        return False
    for char in flag:
        if char not in flag_string : 
            dump_warning("flag => "+flag)
            return False
    return True

def post_flag(flag,target):
    flag = flag.replace(" ","").replace("\n","")
    try:
        '''
        url = 'https://' + flag_server  + flag_url
        print url
        cmd  = "curl -k https://172.16.4.1/Common/awd_sub_answer -d 'token=%s&answer=%s' -X POST --connect-timeout 4" % (flag_token,flag)
        print cmd
        os.system(cmd)
        '''
        headers['Cookie'] = flag_cookie
        res = http("get",flag_server,flag_port,flag_url+"?flag="+flag+"&token="+flag_token + "&ip="+target,'',headers)
	debug_print(res)
    except Exception,e:
        dump_error("flag post error","flag server","flag.py post_flag")
        return False
    if flag_match_string in res:
        debug_print(res)
        dump_success('get flag success','flag server','flag.py post_flag')
        return True
    return False


        
