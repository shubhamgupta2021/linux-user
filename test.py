import subprocess
import shlex

try:

    command_args= shlex.split('/usr/sbin/useradd -d /home/shubham -s /usr/bin/fish shubham')
    subprocess.Popen(command_args)
except subprocess.CalledProcessError as err:
    print err.returncode

from src.userlib import UserHandler
user = UserHandler("shubham")
user.change_password("alpha123")
