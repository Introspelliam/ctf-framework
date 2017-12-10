#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################
#config for basic
first_run = 1
script_runtime_span = 150
cmd = "whoami"
debug = 1
headers = {"User-Agent":"Hence Zhang"}
run_for_flag = 0
cmd_prefix = "HENCE666"
cmd_postfix = "ZHANG777"
timeout = 5
#####################

#############################
# config for data and log
target_list = "data/ip.data"
status_list = "data/status.data"
sys_log = "log/sys.log"
specific_status_log = "log/spec/"
targets_status = ''
############################


###########################################
# get flag
flag_server = "172.16.0.30"
flag_port = 80
flag_url = "/index.php/wargame/submit"
flag_token = "haozigege"
flag_cookie = "PHPSESSID=haozigege-test"
flag_path = '/var/www/html/222/flag.txt'
# the server you need to visit to get the flag
get_flag_url = "http://172.16.0.30:8000/flag" 
flag_string = ['flagFLAGabcdef0123456789ABCDEF{}-_']
flag_match_string = 'success'
##########################################

########################################
#config for shell
shell_salt = "haozi"
shell_salt_2 = "haozigege"
#shell_type 1 is for normal php backdoor
shell_type = 2
#shell_type 2 is for undead php backdoor
#shell_type = 2
#shell_type 3 is for weevely backdoor
#shell_type = 3
#######################################


#######################
#config for web path and file path
shell_path = "/runtime/temp"
shell_absolute_path = "/var/www/html/runtime/temp"
crontab_path = "/tmp/"
web_path = '/var/www/html/'
######################


######################
#config for reverse_shell
reverse_ip = '192.168.37.133'
reverse_port  =  6666
#####################


#####################
#config for upload_and_execute
U_A_E_flag = 0
upload_file_name = ''
executor = ''
####################

####################
#config for rm file
rm_paths = '/var/www/html/index.php /tmp/* /home/ctf/*'
rm_index = '/var/www/html/index.php'
###################

####################
#config for rm database
db_user = 'root'
db_passwd = 'root'
db_name = ['performance_schema','mysql','tpshop2.0']
###################

####################
#config for autossh
ssh_password = 'Hence666'
###################
