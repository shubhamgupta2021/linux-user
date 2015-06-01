import subprocess, shlex
import constants
import grp



class UserHandler(object):

    def __init__(self,username):
        self.username = username

    def remove_from_group(self):
        user_groups = [g.gr_name for g in grp.getgrall() if self.username in g.gr_mem]
        if constants.REMOVE_GROUP_NAME in user_groups:
            remove_from_group = constants.REMOVE_GROUP_BASE+ self.username+ " " + constants.REMOVE_GROUP_NAME
            command_args = shlex.split(remove_from_group)
            subprocess.check_call(command_args)


    def change_password(self, password):
        command = "passwd " + self.username
        command_args = shlex.split(command)
        p= subprocess.Popen(command_args, stdin=subprocess.PIPE, stdout=None)
        p.communicate(input=password+"\n"+password)

    def add(self, request_form):
        command = constants.USERADD_BASE + constants.SHELL + constants.SHELL_DICT[request_form['shell']] + " "
        if request_form.get('directory'):
            command += constants.HOME_DIR+ request_form['directory'] + " "
        if request_form['sudo']=="yes":
            command += constants.SUDO + " "
        command += request_form['username']
        command_args = shlex.split(command)
        subprocess.check_call(command_args)
        if request_form.get('password'):
            self.change_password(request_form['password'])

    def delete(self):
        command = constants.USERDEL_BASE + self.username
        command_args = shlex.split(command)
        subprocess.check_call(command_args)

    def modify(self, request_form):
        command = constants.USERMOD_BASE + constants.SHELL + constants.SHELL_DICT[request_form['shell']] + " "
        if request_form.get('directory'):
            command += constants.HOME_DIR+ request_form['directory'] + " "
        if request_form['sudo']=="yes":
            command += constants.SUDO + " "
        else:
            self.remove_from_group()
        command += request_form['username']
        command_args = shlex.split(command)
        subprocess.Popen(command_args)

        if request_form.get('password'):
            self.change_password(request_form['password'])


