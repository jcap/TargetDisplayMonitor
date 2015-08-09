#!env python

import re
import syslog

from time import sleep
from subprocess import call

target_mode = False

re_tm_on  = re.compile(r'AppleThunderboltDPPathManager.+createPath.+path type 0x1.+Initial Credits.+int=0 src=0 dst=0.+NFC Credits.+int=14 src=5 dst=14.+')
re_tm_off = re.compile(r'IOThunderboltSwitch.+listenerCallback.+Thunderbolt HPD packet.+unplug = 1')

def follow(file):
  file.seek(0,2) # Go to the end of the file
  while True:
    line = file.readline()
    if not line:
      sleep(0.1) # Sleep briefly
      continue
    yield line

system_log = open("/var/log/system.log")
loglines   = follow(system_log)

for line in loglines:
  if target_mode:
    if re_tm_off.search(line):
      target_mode = False
      syslog.syslog(syslog.LOG_INFO, 'Target Display Mode OFF')
      call(['blueutil', 'power', '1'])
      syslog.syslog(syslog.LOG_INFO, 'Disabled Bluetooth')
  else:
    if re_tm_on.search(line):
      target_mode = True
      syslog.syslog(syslog.LOG_INFO, 'Target Display Mode ON')
      call(['blueutil', 'power', '0'])
      syslog.syslog(syslog.LOG_INFO, 'Enabled Bluetooth')

