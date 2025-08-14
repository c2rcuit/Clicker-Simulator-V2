import io
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ClickerSimulator", "Libraries"))

import pyautogui
from PIL import Image
import requests

HOOK_URL = "https://discord.com/api/webhooks/1404241322470146181/1n2WpYc1QdY2eWFcY-VOcOm-i9V6RxIM1_r65Ae2tH6w3xLNXrzdnw8bNt5rev3Lf8aG"

MAX_FILE_SIZE = 8 * 1024 * 1024

def capture_screenshot():
    """Capture a screenshot using pyautogui."""
    return pyautogui.screenshot()

def compress_image_to_bytes(img: Image.Image, quality=60, scale=1.0):
    """Save the PIL Image to bytes as JPEG with given quality and scale factor."""
    if scale != 1.0:
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size, Image.LANCZOS)

    if img.mode == "RGBA":
        img = img.convert("RGB")  # Ensure JPEG-compatible mode

    bio = io.BytesIO()
    img.save(bio, format="JPEG", quality=quality, optimize=True)
    bio.seek(0)
    return bio

def ensure_under_limit(img: Image.Image):
    """Compress iteratively until under Discord's file size limit."""
    quality = 75
    scale = 1.0

    bio = compress_image_to_bytes(img, quality=quality, scale=scale)
    size = len(bio.getvalue())

    while size > MAX_FILE_SIZE:
        if quality > 30:
            quality -= 10
        else:
            scale *= 0.8
            if img.width * scale < 200 or img.height * scale < 200:
                break
        bio = compress_image_to_bytes(img, quality=quality, scale=scale)
        size = len(bio.getvalue())

    return bio

def send_screenshot(webhook_url: str):
    """Capture, compress, and send screenshot to Discord webhook."""
    img = capture_screenshot()
    bio = ensure_under_limit(img)

    files = {"file": ("screenshot.jpg", bio, "image/jpeg")}
    response = requests.post(webhook_url, files=files)

    if response.status_code != 204:
        print(f"Failed to send screenshot: {response.status_code} {response.text}")

if __name__ == "__main__":
    INTERVAL_SECONDS = 60

    while True:
        send_screenshot(HOOK_URL)
        time.sleep(INTERVAL_SECONDS)
