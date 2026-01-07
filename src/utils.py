import psutil
import pyautogui
import io
import socket

def get_sys_stats():
    h = socket.gethostname()
    try:
        ip = socket.gethostbyname(h)
    except:
        ip = "unknown"
    c = psutil.cpu_percent()
    r = psutil.virtual_memory().percent
    return f"cpu: {c}% | ram: {r}% | host: {h} | ip: {ip}"

def take_screenshot():
    try:
        s = pyautogui.screenshot()
        b = io.BytesIO()
        s.save(b, format='png')
        b.seek(0)
        return b
    except:
        return None