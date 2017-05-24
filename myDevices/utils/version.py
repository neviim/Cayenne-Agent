import re
import sys

PYTHON_MAJOR    = sys.version_info.major
BOARD_REVISION  = 0

OS_VERSION = 0
OS_RASPBIAN_WHEEZY = 1
OS_RASPBIAN_JESSIE = 2

_MAPPING = [[], [], [], []]
_MAPPING[1] = ["V33", "V50", 0, "V50", 1, "GND", 4, 14, "GND", 15, 17, 18, 21, "GND", 22, 23, "V33", 24, 10, "GND", 9, 25, 11, 8, "GND", 7]
_MAPPING[2] = ["V33", "V50", 2, "V50", 3, "GND", 4, 14, "GND", 15, 17, 18, 27, "GND", 22, 23, "V33", 24, 10, "GND", 9, 25, 11, 8, "GND", 7]
_MAPPING[3] = ["V33", "V50", 2, "V50", 3, "GND", 4, 14, "GND", 15, 17, 18, 27, "GND", 22, 23, "V33", 24, 10, "GND", 9, 25, 11, 8, "GND", 7, "DNC", "DNC" , 5, "GND", 6, 12, 13, "GND", 19, 16, 26, 20, "GND", 21]

try:
    with open("/proc/cpuinfo") as f:
        rc = re.compile("Revision\s*:\s(.*)\n")
        info = f.read()
        result = rc.search(info)
        if result != None:
            hex_cpurev = result.group(1)
            if hex_cpurev.startswith("1000"):
                hex_cpurev = hex_cpurev[-4:]
            cpurev = int(hex_cpurev, 16)
            if cpurev < 0x04:
              BOARD_REVISION = 1
            elif cpurev < 0x10:
              BOARD_REVISION = 2
            else:
              BOARD_REVISION = 3

except:
    pass

try:
    with open("/etc/apt/sources.list") as f:
        sources = f.read()
        if "wheezy" in sources:
            OS_VERSION = OS_RASPBIAN_WHEEZY
        elif "jessie" in sources:
            OS_VERSION = OS_RASPBIAN_JESSIE
            
except:
    pass

MAPPING = _MAPPING[BOARD_REVISION]
