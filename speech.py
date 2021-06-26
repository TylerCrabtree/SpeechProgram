try:
    import mac_say
    from simple_colors import *
except ImportError:
    import os
    os.system("pip install mac-say")
    os.system("pip install simple-colors")
    import mac_say
    from simple_colors import *



if __name__ == '__main__':
    print(magenta("Starting speech program"))
    user_input = input("Enter something to say: ")
    mac_say.say(user_input)

