import time
import psutil

gnome_panel_procs = []
for process in psutil.process_iter():
    # I assume the gnome-panel processes correctly set their name
    # eventually you could use process.cmdline instead
    if process.name == 'gnome-panel':
        gnome_panel_procs.append(process)

for proc in gnome_panel_procs:
    for _ in range(60):
        # check cpu percentage over 1 second
        if proc.get_cpu_percent(1) < 80 or not proc.is_running():
            # less than 80% of cpu or process terminated
            break
    else:
        # process used 80% of cpu for over 1 minute
        proc.kill()