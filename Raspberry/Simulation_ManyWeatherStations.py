import subprocess
import sys


processes = []
script = r".\WeatherStation.py"
num_processes =  int(sys.argv[1])

print(f"Running #{num_processes} of file {script}")

for i in range(num_processes):
    p = subprocess.Popen(['python3', script])
    processes.append(p)

input(">> Press ENTER key to stop simulation.")
for p in processes:
    p.terminate()