# coding=utf-8

import psutil

print(psutil.cpu_count())  # 8

print(psutil.cpu_count(logical=False))  # 4

print(psutil.cpu_times())

# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

print(psutil.virtual_memory())

print(psutil.swap_memory())

print(psutil.disk_partitions())

print(psutil.disk_usage("/"))

print(psutil.net_io_counters())

print(psutil.net_if_addrs())

print(psutil.net_if_stats())

print(psutil.net_connections())
