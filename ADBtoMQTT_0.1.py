
def deal_with_stdout():
  for line in logcat_query.stdout:
    new_line = line.decode()
    match new_line:
        case new_line if "MoveSeatForward" in new_line:
           print("ДВИГАЕМ ВПЕРЕД - 1")
        case new_line if "MoveSeatBackward" in new_line:
           print("ДВИГАЕМ НАЗАД- 2")
        case _:
            #print(line.decode())
            print(new_line)
#            print("""b'MoveSeatForward \\n'""")
#            print("ПРОПУСК")

from subprocess import Popen, PIPE, STDOUT
from threading import Thread
logcat_query = Popen(["adb", "logcat", "-v", "raw", "-T", "1", "-e", "onReceive"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
#t = Thread(target=deal_with_stdout(), )
t = Thread(target=deal_with_stdout(), daemon=True)
t.start()
t.join()


