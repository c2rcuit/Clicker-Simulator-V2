import platform
import subprocess
import sys

def install_package(package_name: str):
    system = platform.system()

    pip_cmd = f'"{sys.executable}" -m pip install {package_name}'

    if system == "Windows":
        subprocess.Popen(f'start cmd /k {pip_cmd}', shell=True)

    elif system == "Darwin":
        subprocess.Popen([
            'osascript', '-e',
            f'tell application "Terminal" to do script "{pip_cmd}"'
        ])

    elif system == "Linux":
        subprocess.Popen([
            'gnome-terminal', '--', 'bash', '-c', f'{pip_cmd}; exec bash'
        ])

    else:
        print(f"Unsupported operating system: {system}")

if __name__ == "__main__":
    packages = ["pyautogui", "Pillow", "requests", "pynput", "dhooks --target dhooks_lib"]
    for pkg in packages:
        install_package(pkg)
