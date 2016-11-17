#! /usr/bin/python
"""
In Linux, need to get report on Users, their password status. 
E.g. Username, UID, Group Memberships, 
Password is expired or going to expire in x days or not set.
"""

import subprocess

def main():
    print("USER:USERID:GROUPS:PASSWORD INFO")
    limit = subprocess.check_output("grep ^UID_MIN /etc/login.defs | awk '{print $2}'", shell=True).strip()
    users = subprocess.check_output("awk -F':' '{ if ( $3 >= %s || $3==0 ) print $1\":\"$3}' /etc/passwd"%(limit), shell=True).strip()
    users = users.split("\n")
    for user in users:
        us = user.split(':')[0]
        op = (user + ":" +subprocess.check_output("groups %s"%(us), shell=True).strip().split(":")[1].strip()) + ":"
        op += subprocess.check_output('chage -l %s | grep "Password expires"'%(us), shell=True).strip().split(':')[1]
        print op

if __name__ == '__main__':
    main()
