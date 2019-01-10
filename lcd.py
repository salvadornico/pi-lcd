#!/usr/bin/env python

import I2C_LCD_driver
import fcntl
import socket
import struct
import time

mylcd = I2C_LCD_driver.lcd()


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(
        fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                                    ifname[:15]))[20:24])


while True:
	mylcd.lcd_display_string("IP Address:", 1)
	mylcd.lcd_display_string(get_ip_address('wlan0'), 2)

	time.sleep(1)
	mylcd.lcd_clear()
	time.sleep(1)

	mylcd.lcd_display_string("Time: %s" % time.strftime("%H:%M:%S"), 1)
	mylcd.lcd_display_string("Date: %s" % time.strftime("%m/%d/%Y"), 2)

	time.sleep(1)
	mylcd.lcd_clear()
	time.sleep(1)
