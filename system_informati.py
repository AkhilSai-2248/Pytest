## Reference - https://www.thepythoncode.com/article/get-hardware-system-information-python

## pip install psutil

##psutil (process and system utilities) is a cross-platform library for retrieving information
##on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.
##It is useful mainly for system monitoring, profiling and limiting process resources and
##management of running processes. It implements many functionalities offered by classic UNIX
##command line tools such as ps, top, iotop, lsof, netstat, ifconfig, free and others.
##psutil currently supports the following platforms: Linux,Windows, macOS, FreeBSD, OpenBSD, NetBSD
##Sun Solaris, AIX
#!/usr/bin/python3.9
import psutil
import platform
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Boot Time
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# CPU information
print("="*40, "CPU Info", "="*40)

# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# Memory Information
print("="*40, "Memory Information", "="*40)

#Memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)

#Swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")

# Disk Information
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")

#All disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")

#IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

# Network information
print("="*40, "Network Information", "="*40)

# Network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")

#IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")


##Output
##======== RESTART: /media/sf_P_DRIVE/system_information_17_April_2021.py ========
##======================================== System Information ========================================
##System: Linux
##Node Name: kali
##Release: 5.9.0-kali1-amd64
##Version: #1 SMP Debian 5.9.1-1kali2 (2020-10-29)
##Machine: x86_64
##Processor: 
##======================================== Boot Time ========================================
##Boot Time: 2021/4/24 22:27:37
##======================================== CPU Info ========================================
##Physical cores: 1
##Total cores: 1
##Max Frequency: 0.00Mhz
##Min Frequency: 0.00Mhz
##Current Frequency: 1190.40Mhz
##CPU Usage Per Core:
##Core 0: 1.0%
##Total CPU Usage: 6.5%
##======================================== Memory Information ========================================
##Total: 3.85GB
##Available: 3.11GB
##Used: 520.41MB
##Percentage: 19.3%
##==================== SWAP ====================
##Total: 975.00MB
##Free: 975.00MB
##Used: 0.00B
##Percentage: 0.0%
##======================================== Disk Information ========================================
##Partitions and Usage:
##=== Device: /dev/sda1 ===
##  Mountpoint: /
##  File system type: ext4
##  Total Size: 48.02GB
##  Used: 12.33GB
##  Free: 33.23GB
##  Percentage: 27.1%
##Total read: 329.04MB
##Total write: 19.99MB
##======================================== Network Information ========================================
##=== Interface: lo ===
##  IP Address: 127.0.0.1
##  Netmask: 255.0.0.0
##  Broadcast IP: None
##=== Interface: lo ===
##=== Interface: lo ===
##  MAC Address: 00:00:00:00:00:00
##  Netmask: None
##  Broadcast MAC: None
##=== Interface: eth0 ===
##  IP Address: 10.0.2.15
##  Netmask: 255.255.255.0
##  Broadcast IP: 10.0.2.255
##=== Interface: eth0 ===
##=== Interface: eth0 ===
##  MAC Address: 08:00:27:15:3f:d8
##  Netmask: None
##  Broadcast MAC: ff:ff:ff:ff:ff:ff
##Total Bytes Sent: 42.74KB
##Total Bytes Received: 42.35KB

