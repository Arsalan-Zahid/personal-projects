from os import path
main_path = path.dirname(__file__)
from time import sleep

#get file paths

distractions_dir_path = path.join(main_path, 'distractions')
distractions_py = path.join(distractions_dir_path, 'distractions.py')

#set up dictionary to convert

conv_dict = {
    'd': distractions_py
}



#get args
from sys import argv
file = argv[1]
args = argv[2:]



#get the path
file_path = None
try:
    file_path = conv_dict[file]
except Exception as e:
    print(f"there was a value error! {e}")
    print("going to sleep")
    sleep(5)


from subprocess import Popen
p = Popen(['py', file_path] + args)


p.wait()