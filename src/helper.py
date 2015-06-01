import os
import pwd
from constants import ADMIN

def validator(request_form):
    if not request_form.get('username'):
        return 400
    if request_form['action']=='modify' or request_form['action']=='delete':
        if request_form['username'] in open('/etc/passwd').read():
            return 200
        else:
            return 412
    if request_form['action'] == 'create':
        if request_form['username'] in open('/etc/passwd').read():
            return 412
        else:
            return 200

def validate_admin():
    try:
        current_uid  = int(os.environ.get('SUDO_UID'))
    except TypeError as err:
        print "You need root access."
        return 0

    if pwd.getpwuid(current_uid)[0] == ADMIN:
        return 1
    else:
        return 0