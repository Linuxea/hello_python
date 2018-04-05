import os
import subprocess

print('$ nslookup www.python.org')
print("pid: %s" % os.getpid())
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
