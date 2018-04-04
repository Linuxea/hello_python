import psutil

r = psutil.cpu_count()  # CPU逻辑数量

print(r)

real = psutil.cpu_count(logical=False)
print(real)

time = psutil.cpu_times()
print(time)
