def deal_with_stdout():
    for line in p.stdout:
        print(type(line))
        #print(line)

from subprocess import Popen, PIPE, STDOUT
from threading import Thread
p = Popen(["adb", "logcat", "-v", "raw", "-T", "1", "-e", "onReceive"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
t = Thread(target=deal_with_stdout, daemon=True)
t.start()
t.join()

