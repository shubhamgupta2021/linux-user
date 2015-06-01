import subprocess, shlex
import constants
import crypt
import random, string


def encrypted_password(plain_password):
    salt = ''.join(random.choice(string.digits+string.ascii_letters) for _ in range(16))
    print salt
    insalt = "$6$"+ salt
    encrypted_pass = crypt.crypt(plain_password, insalt)
    print encrypted_pass


class UserHandler(object):

    def __init__(self,username):
        self.username = username


    def add(self, request_form):
        command = constants.USERADD_BASE + constants.SHELL + constants.SHELL_DICT[request_form['shell']] + " "
        if request_form.get('directory'):
            command += constants.HOME_DIR+ request_form['directory'] + " "
        if request_form.get('password'):
            command += constants.PASSWORD + encrypted_password(request_form['password']) +" "
        if request_form['sudo']=="yes":
            command += constants.SUDO + " "
        command += request_form['username']
        print command
        command_args = shlex.split(command)
        subprocess.Popen(command_args)

    def delete(self):
        command = constants.USERDEL_BASE + self.username
        print command
        command_args = shlex.split(command)
        subprocess.Popen(command_args)

    def modify(self, request_form):
        command = constants.USERMOD_BASE + constants.SHELL + constants.SHELL_DICT[request_form['shell']] + " "
        if request_form.get('directory'):
            command += constants.HOME_DIR+ request_form['directory'] + " "
        if request_form.get('password'):
            command += constants.PASSWORD + request_form['password'] +" "
        if request_form['sudo']=="yes":
            command += constants.SUDO + " "
        else:
            remove_from_group = constants.REMOVE_GROUP_BASE+ self.username+ constants.REMOVE_GROUP_NAME
            command_args = shlex.split(remove_from_group)
            subprocess.Popen(command_args)
        command += request_form['username']
        print command
        command_args = shlex.split(command)
        subprocess.Popen(command_args)