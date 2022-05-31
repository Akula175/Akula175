import time
import sys
import os

arg1 = sys.argv[1]

def timer():
    total_time = int(arg1)*60
    print(total_time)
    while total_time > 0:
        total_time -=1
        time.sleep(1)
    print('Done')
    os.system('shutdown now')

if __name__ == '__main__':
    timer()
