#!/usr/bin/env python

import lcd
import time

while True:
    lcd.write("IP Address", lcd.get_ip_address('wlan0'))
    lcd.wait_and_refresh()
    lcd.write("Time: %s" % time.strftime("%H:%M:%S"),
              "Date: %s" % time.strftime("%d %b %y"))
    lcd.wait_and_refresh()
