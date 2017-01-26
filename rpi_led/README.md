
BOT to control Raspberry Pi LEDs

>>> ATTENTION: this bot was tested only in Telegram platform

## SETUP

1) LEDs

Pin the leds on rpi GPIO, as in following image:

![Alt text](https://halckemy.s3.amazonaws.com/uploads/attachments/247656/simpl_IzA7ZC8BCH.PNG)

2) Connect in your Raspberry

2.1) Install project dependencies

`pip install -r requirements.txt`

2.2) Start your boot

`./boot_rpi_led.py`

2.2) [Optional] You can start in background

`nohup ./boot_rpi_led.py >>/tmp/boot_rpi_led.log 2>>&1 &`

## USAGE

Send to your boot following commands:
* on  - turn LED on
* off - turn LED off


## CREDITS

This bot was inspired in [this post](https://www.hackster.io/Salman_faris_vp/telegram-bot-with-raspberry-pi-f373da) .
