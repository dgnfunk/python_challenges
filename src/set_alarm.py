import sched
import sys
import time
import winsound as ws

def set_alarm(alarm_time, alarm, message):
    alarm_time_float = time.time() + alarm_time
    alarm_sound = get_alarm_sound()
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time_float, 1, print, argument=(message,))
    s.enterabs(alarm_time_float, 1, ws.PlaySound, argument=(alarm_sound, ws.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarm_time_float)))
    s.run()

def get_alarm_sound():
    return './../assets/mixkit-alarm-digital-clock-beep-989.wav'

if __name__ == '__main__':
    set_alarm(int(sys.argv[1]), '', sys.argv[2])