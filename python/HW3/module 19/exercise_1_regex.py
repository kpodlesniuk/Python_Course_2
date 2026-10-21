#!/usr/bin/env python3
"""Exercise 1: Parse device log values with regular expressions."""

import re

with open("device.log") as file:
    log = file.read()

print(
    re.search(
        r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) ERROR",
        log,
        re.MULTILINE,
    ).group(1)
)

print(re.search(r'ssid="([^"]+)"', log, re.MULTILINE).group(1))
print(re.search(r"rssi=(-?\d+)dBm", log, re.MULTILINE).group(1))
print(re.search(r"ip=(\d+\.\d+\.\d+\.\d+)/\d+", log, re.MULTILINE).group(1))

print(
    re.findall(
        r"(?<=dns servers: )\d+\.\d+\.\d+\.\d+|"
        r"(?<=, )\d+\.\d+\.\d+\.\d+",
        log,
        re.MULTILINE,
    )
)

resolution = re.search(r"res=(\d+)x(\d+)", log, re.MULTILINE)
print(resolution.group(1), resolution.group(2))

print(re.search(r"fps=(\d+\.\d+)", log, re.MULTILINE).group(1))
print(re.search(r"start stream.*?br=(\d+)kbps", log, re.MULTILINE).group(1))
print(re.search(r"frame drop:.*?\((\d+\.\d+)%\)", log, re.MULTILINE).group(1))
print(re.search(r"ERROR.*?code=(\d+)", log, re.MULTILINE).group(1))
print(re.search(r"url=https?://([^/]+)", log, re.MULTILINE).group(1))
print(re.search(r"fw=v(\d+\.\d+\.\d+)-rc\d+", log, re.MULTILINE).group(1))

print(
    re.search(
        r"mac=([0-9A-F]{2}(?::[0-9A-F]{2}){5})",
        log,
        re.MULTILINE,
    ).group(1)
)

uptime = re.search(r"uptime=(\d+)d(\d+)h(\d+)m", log, re.MULTILINE)
print(uptime.group(1), uptime.group(2), uptime.group(3))

print(re.search(r'reboot_reason="([^"]+)"', log, re.MULTILINE).group(1))
