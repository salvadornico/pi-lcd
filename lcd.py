#!/usr/bin/env python

import I2C_LCD_driver
import fcntl
import socket
import struct
import time

mylcd = I2C_LCD_driver.lcd()


def write(line1, line2=None):
    mylcd.lcd_display_string(line1, 1)

    if line2 is not None:
        mylcd.lcd_display_string(line2, 2)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(
        fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                                    ifname[:15]))[20:24])


def wait_and_refresh():
    time.sleep(10)
    mylcd.lcd_clear()
    time.sleep(1)
