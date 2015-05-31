

def validator(request_form):
    if request_form['action']=='modify' or request_form['action']=='delete':
        if request_form['username'] in open('/etc/passwd').read():
            return 1
        else:
            return 0
    if request_form['action'] == 'create':
        if request_form['username'] in open('/etc/passwd').read():
            return 0
        else:
            return 1

