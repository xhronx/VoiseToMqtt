
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set("test","test")
mqttc.connect("192.168.0.11", 1883)
#mqttc.connect("127.0.0.1", 1883)

def deal_with_stdout():
  for line in logcat_query.stdout:

     match line.decode():
        case new_line if "MoveSeatForward" in new_line:
            do_MoveSeatForward()
        
        case new_line if "MoveSeatBackward" in new_line:
            do_MoveSeatBackward()
        
        case new_line if "MoveSeatUp" in new_line:
             do_MoveSeatUp()

       
        case new_line if "MoveSeatDown" in new_line:
            do_MoveSeatDown()
        
        case new_line if "MoveSeatBackForward" in new_line:
            do_MoveSeatBackForward()
            print("ДВИГАЕМ СПИНКУ ВПЕРЕД")
        
        case new_line if "MoveSeatBackBackward" in new_line:
            do_MoveSeatBackBackward()
        
        case new_line if "onReceive: EXTRA_STATE (LISTENING)" in new_line:
            state_LISTENING()
        
        case new_line if "onReceive: EXTRA_STATE (THINKING)" in new_line:
            state_THINKING()
            
        case new_line if "onReceive: EXTRA_STATE (SPEAKING)" in new_line:
            state_SPEAKING()

        case new_line if "onReceive: EXTRA_STATE (IDLE)" in new_line:
            state_IDLE()

        case new_line if "onReceive: EXTRA_STATE (ERROR)" in new_line:
            state_ERROR()
            
        case _:
            print(line)

def do_MoveSeatForward():
    print("ДВИГАЕМ КРЕСЛО ВПЕРЕД")
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/left", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/left", "1")
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/left", "1")
    time.sleep(2.5)
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/left", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/left", "0")
    mqttc.loop_stop()

def do_MoveSeatBackward():
    print("ДВИГАЕМ КРЕСЛО НАЗАД")
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/right", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/right", "1")
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/right", "1")
    time.sleep(2.5)
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/right", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/foreaft/right", "0")
    mqttc.loop_stop()

def do_MoveSeatUp():
    print("ДВИГАЕМ КРЕСЛО ВВЕРХ")
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/controls/seats/driver/height/up", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/height/up", "1")
    mqttc.publish("atom/vehicle/controls/seats/driver/height/up", "1")
    time.sleep(2.5)
    mqttc.publish("atom/vehicle/controls/seats/driver/height/up", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/height/up", "0")
    mqttc.loop_stop()


def do_MoveSeatDown():
    print("ДВИГАЕМ КРЕСЛО ВНИЗ")
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/controls/seats/driver/height/down", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/height/down", "1")
    mqttc.publish("atom/vehicle/controls/seats/driver/height/down", "1")
    time.sleep(2.5)
    mqttc.publish("atom/vehicle/controls/seats/driver/height/down", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/height/down", "0")
    mqttc.loop_stop()


def do_MoveSeatBackForward():
    print("ДВИГАЕМ СПИНКУ ВПЕРЕД")
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/left", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/left", "1")
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/left", "1")
    time.sleep(2.5)
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/left", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/left", "0")
    mqttc.loop_stop()


def do_MoveSeatBackBackward():
    print("ДВИГАЕМ СПИНКУ НАЗАД")
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/right", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/right", "1")
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/right", "1")
    time.sleep(2.5)
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/right", "0")
    mqttc.publish("atom/vehicle/controls/seats/driver/recline/right", "0")
    mqttc.loop_stop()

def state_LISTENING():
    mqttc.loop_start()
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "0")
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "1")
    mqttc.loop_stop()

def state_THINKING():
    mqttc.loop_start()
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "0")
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "2")
    mqttc.loop_stop()

def state_SPEAKING():
    mqttc.loop_start()
    mqttc.publish("atom/vehicle/devices/voice-assistant/signals/state", "3")
    mqttc.loop_stop()

def state_IDLE():
    mqttc.loop_start()
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "0")
    mqttc.loop_stop()

def state_ERROR():
    mqttc.loop_start()
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "4")
    time.sleep(1)
    mqttc.publish("atom.vehicle/devices/voice-assistant/signals/state", "0")
    mqttc.loop_stop()

from subprocess import Popen, PIPE, STDOUT
from threading import Thread

logcat_query = Popen(["adb", "logcat", "-v", "raw", "-T", "1", "-e", "onReceive"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
t = Thread(target=deal_with_stdout(), daemon=True)
t.start()
t.join()

