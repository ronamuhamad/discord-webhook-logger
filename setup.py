from setuptools import setup, find_packages

setup(
    name="discord-webhook-logger",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "psutil",
        "pyautogui",
        "pillow"
    ],
    author="ronadimoi",
    description="async discord webhook logger with screenshot support"
)