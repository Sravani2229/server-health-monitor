import platform # to know which system we are using like windows,linux etc
import socket # used for hostname
import sys # used for python version
import psutil

print("====================================")
print("     SERVER HEALTH MONITOR")
print("====================================")
print(f"Hostname : {socket.gethostname()}")
print(f"Operating System : {platform.system()}")
print(f"Python Version : {sys.version.split()[0]}")
print("------------------------------------")
cpu_usage=psutil.cpu_percent(interval=1)
memory_usage=psutil.virtual_memory().percent
disk_usage=psutil.disk_usage("/").percent

print(f"CPU Usage     : {cpu_usage}%")
print(f"Memory Usage  : {memory_usage}%")
print(f"Disk usage    : {disk_usage}%")

print("-------------------------------------")

def get_status(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >=70:
        return "WARNING"
    else:
        return "HEALTHY"

cpu_status=get_status(cpu_usage)
memory_status=get_status(memory_usage)
disk_status=get_status(disk_usage)

print(f"CPU status     : {cpu_status}")
print(f"Memory Status  : {memory_status}")
print(f"Disk Status    : {disk_status}")

print("------------------------------------")
if "CRITICAL" in [cpu_status,memory_status,disk_status]:
    overall_status="CRITICAL"
elif "WARNING" in [cpu_status,memory_status,disk_status]:
    overall_status="WARNING"
else:
    overall_status="HEALTHY"
print(f"Overall status   : {overall_status}")
print("====================================")