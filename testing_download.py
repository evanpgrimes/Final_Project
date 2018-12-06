import os
import subprocess


os.system("curl https://bootstrap.pypa.io/get-pip.py > get-pip.py")
os.system("sudo pip install pygame")
dirname = os.path.dirname(os.path.abspath(__file__))
cmd = os.path.join(dirname, 'snake.py')

subprocess.call(cmd)
