import requests
import datetime
import traceback
import threading
import json
import time
from .utils import get_sys_stats, take_screenshot

class discord_logger:
    def __init__(self, webhook, uid=None):
        self.url = webhook
        self.uid = uid

    def _send(self, payload, img=None):
        try:
            f = {}
            if img:
                f = {'file': ('error.png', img, 'image/png')}
            requests.post(self.url, data={'payload_json': json.dumps(payload)}, files=f)
        except:
            pass

    def _build(self, title, desc, color, ping=False, snap=False):
        s = get_sys_stats()
        e = {
            "title": title,
            "description": desc,
            "color": color,
            "fields": [{"name": "stats", "value": s, "inline": False}],
            "footer": {"text": f"logger | {datetime.datetime.now().strftime('%H:%M:%S')}"}
        }
        c = ""
        if ping and self.uid:
            c = f"<@{self.uid}>"
        
        p = {"content": c, "embeds": [e]}
        i = None
        if snap:
            i = take_screenshot()
        
        threading.Thread(target=self._send, args=(p, i)).start()

    def info(self, m):
        self._build("info", m, 3447003)

    def success(self, m):
        self._build("success", m, 3066993)

    def error(self, m):
        self._build("crash", m, 15158332, ping=True, snap=True)

    def track(self, f):
        def w(*a, **k):
            n = f.__name__
            self.info(f"start {n}")
            try:
                r = f(*a, **k)
                self.success(f"done {n}")
                return r
            except Exception as e:
                t = traceback.format_exc()
                self.error(f"error in {n}:\n```{str(e)}```\n```{t[-800:]}```")
                raise e
        return w