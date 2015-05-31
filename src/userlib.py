import subprocess, shlex
import constants



class UserHandler(object):

    def __init__(self, username):
        self.username = username


    def add(self, password=None, shell=None, home_dir=None, sudo= None):
        command = constants.USERADD_BASE + \
                  constants.HOME_DIR+ home_dir + " " +\
                  constants.PASSWORD + password +" " +\
                  constants.SHELL + constants.SHELL_DICT[shell] + ' ' +\
                  self.username
        print command
        command_args = shlex.split(command)
        subprocess.Popen(command_args)

    def delete(self):
        command = constants.USERDEL_BASE + self.username
        print command
        command_args = shlex.split(command)
        subprocess.Popen(command_args)

    def modify(self, password=None, shell=None, home_dir=None):
        command = constants.USERMOD_BASE + \
                  constants.HOME_DIR+ home_dir + " " +\
                  constants.PASSWORD + password +" " +\
                  constants.SHELL + constants.SHELL_DICT[shell] + ' ' +\
                  self.username
        print command
        command_args = shlex.split(command)
        subprocess.Popen(command_args)