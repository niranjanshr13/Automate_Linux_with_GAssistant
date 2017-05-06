#!/usr/bin/env python2
#{{{ Import Module
import time
import os, sys, subprocess
#imports for email
import imaplib
from email.parser import HeaderParser
#}}}
#{{{ Variable
userNAME = sys.argv[1]
passWORD = sys.argv[2]
#}}}
#{{{ Defination of Checking Email
def check_email():
    status, email_ids = imap_server.search(None, '(UNSEEN)')    
    if email_ids == ['']:
        mail_list = []
    else:
        mail_list = get_subjects(email_ids)     
    imap_server.close()
    return mail_list
#}}}
#{{{ Defination to retirieveing subject
def get_subjects(email_ids):
    subjects_list = []          				   
    for e_id in email_ids[0].split():   		  
    	resp, data = imap_server.fetch(e_id, '(RFC822)')
    	perf = HeaderParser().parsestr(data[0][1])	   
    	subjects_list.append(perf['Subject'])		  
    return subjects_list
#}}}
#{{{ Actions
actions = {}
actions["Laptop_Lock"] = ["laptop locking", "subprocess.call(['i3lock', '-c', '000000'])"]
actions["Open Chrome"] = ["Opening Chrome", "subprocess.call(['firefox'])"]
#}}}
#{{{ Main
while True:
    try:
        time.sleep(2)
        imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
        imap_server.login(userNAME, passWORD)
        imap_server.select('INBOX')
        mail_list = check_email()
        if mail_list:
            for actionary in actions.keys():
                if "".join(mail_list) == actionary:
                    print(actions[actionary][0])
                    eval(actions[actionary][1])
#               print "Locking Computer"
#              subprocess.call(['i3lock', '-c', '000000'])
        time.sleep(2)
    except:
        time.sleep(3)
        print "Internet is Down"
        pass
#}}}
