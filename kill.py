import time
import psutil

for proc in psutil.process_iter():
    if proc.get_cpu_percent() > 80:
            proc.kill()
    else:
	print('nothing')
    break