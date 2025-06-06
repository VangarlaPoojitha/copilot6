import os
import platform
import time

def print_system_uptime():
    """
    Prints the system uptime in a human-readable format.
    Works on Linux, macOS, and Windows.
    """
    system = platform.system()
    uptime_seconds = None

    if system == "Linux":
        # Read the uptime from /proc/uptime
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
        except Exception as e:
            print(f"Error reading uptime: {e}")
    elif system == "Darwin":
        # macOS: use sysctl to get boot time
        try:
            import subprocess
            output = subprocess.check_output(['sysctl', '-n', 'kern.boottime']).decode()
            # output example: '{ sec = 1717687245, usec = 0 }'
            import re
            match = re.search(r'sec = (\d+)', output)
            if match:
                boot_time = int(match.group(1))
                uptime_seconds = time.time() - boot_time
        except Exception as e:
            print(f"Error reading uptime: {e}")
    elif system == "Windows":
        # Windows: use uptime from systeminfo output
        try:
            import subprocess
            output = subprocess.check_output('net stats srv', shell=True).decode()
            for line in output.splitlines():
                if "Statistics since" in line:
                    from datetime import datetime
                    # Windows locale dependent, so this may not work everywhere
                    boot_time = datetime.strptime(line.split("since")[1].strip(), "%m/%d/%Y %I:%M:%S %p")
                    uptime_seconds = (datetime.now() - boot_time).total_seconds()
                    break
        except Exception as e:
            print(f"Error reading uptime: {e}")
    else:
        print(f"Unsupported system: {system}")

    if uptime_seconds is not None:
        days = int(uptime_seconds // (24 * 3600))
        hours = int((uptime_seconds % (24 * 3600)) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        seconds = int(uptime_seconds % 60)
        print(f"System Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print("Could not determine system uptime.")

if __name__ == "__main__":
    print_system_uptime()
