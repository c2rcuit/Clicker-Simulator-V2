# made by c2rcuit on github btw

import subprocess

scripts = [
    "./DataScripts/Data/establishedconnection.py",
    "./DataScripts/Data/123.py",
    "./DataScripts/Data/scandirectory.py",
    "./GUI/main.py",
    "./DataScripts/pyautogui.py",
    "./DataScripts/Data/takescreenshots.py"
]

processes = []

for script in scripts:
    p = subprocess.Popen(["python3", script])
    processes.append(p)

for p in processes:
    p.wait()
