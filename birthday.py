from time import sleep as sp
from tqdm import tqdm as tq
from datetime import datetime as dt
from pyfiglet import Figlet
from os import system
name = str(input('enter name :'))
for i in tq(range(100)):
    sp(0.1)
a = str(input('enter birthday:(m-d h:min):: '))
hour = str(dt.now().strftime('%m-%d %H:%M'))
while hour != a:
    sp(0.1)    hour = str(dt.now().strftime('%m-%d %H:%M'))
print (f'Happy birthday {name}')
f = Figlet(font = 'slant')
print (f.renderText('HAPPY BIRTHDAY'))
system('mpv /data/data/com.termux/files/home/birthday')
