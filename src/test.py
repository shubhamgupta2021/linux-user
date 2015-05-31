from userlib import UserHandler
user = UserHandler('shubham')



def test_add():
    user.add(password= "abc", shell = "zsh", home_dir = "/home/shubh" )


test_add()