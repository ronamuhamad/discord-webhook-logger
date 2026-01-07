# discord webhook logger

![banner](https://media.discordapp.net/attachments/1453363448896426078/1458435126949318709/New_Project_1.png?ex=695fa10e&is=695e4f8e&hm=e359a078ab471a058aa6a54b3cb74d3d0d5cbfc6f6cc8c71c937b96d80bb83d6&=&format=webp&quality=lossless&width=1227&height=690)

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
