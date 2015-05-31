#USER To run the app

ADMIN = "fox"

# Options for maipulation
USERADD_BASE = '/usr/sbin/useradd '
USERMOD_BASE = '/usr/sbin/usermod '
USERDEL_BASE = '/usr/sbin/userdel -r '
SHELL = '-s '
PASSWORD = '-p '
HOME_DIR = "-m -d "
SUDO= "-G sudo"

SHELL_DICT = {
    "bash" : '/bin/bash',
    "zsh"  : '/usr/bin/zsh',
    "fish" : '/usr/bin/fish',
    "csh"  : '/bin/csh'
}