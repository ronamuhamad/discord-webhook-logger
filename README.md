# discord webhook logger

![license](https://img.shields.io/badge/license-MIT-blue.svg)
![python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)

simple, lightweight, and async logger for discord webhooks. supports automatic screenshots on error, system stats monitoring, and threading.

## features

- **async logging**: runs in background, doesn't block main thread.
- **auto screenshot**: captures screen when an exception occurs.
- **system stats**: logs cpu, ram, hostname, and ip.
- **decorator**: easy `@logger.track` usage.

## installation

clone the repo:

```bash
git clone https://github.com/ronadimoi/discord-webhook-logger.git
cd discord-webhook-logger
pip install -r requirements.txt
```

## usage

from src.core import discord_logger
import time

# config

```bash
webhook = "your_webhook_url"
user_id = "your_discord_id" # optional

log = discord_logger(webhook, user_id)

@log.track
def my_task():
    time.sleep(1)
    print("working...")
    # if this crashes, you get a ping + screenshot on discord

my_task()
```
