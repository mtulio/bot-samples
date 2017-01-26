import sys, time
import json
import telepot
import RPi.GPIO as GPIO
#import random
#import datetime

#############
# constants:
global config_file
config_file = 'config.json'

#############
# Config: read config.json and save in config_bot
def config_read():
    with open(config_file) as j_data:
        d = j_data.read()
    return json.loads(d)

# RPi methods
def rpi_init():
    GPIO.setmode(GPIO.BOARD)
    # set up GPIO output channel
    GPIO.setup(11, GPIO.OUT)

#LED
# to use Raspberry Pi board pin numbers
def rpi_gpio_on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return "ON"
def rpi_gpio_off(pin):
        GPIO.output(pin,GPIO.LOW)
        return "OFF"

################
# Telegram BOT
def bot_handle(msg):
    chat_id = msg['chat']['id']
    message = msg['text']

    print '# %s Bot Got message: %s' % (chat_id, message)

    if message =='on':
       bot.sendMessage(chat_id, rpi_gpio_on(11))
    elif message =='off':
       bot.sendMessage(chat_id, rpi_gpio_off(11))

def main():
    try:
        config_bot = config_read()
        rpi_init()

        bot = telepot.Bot(config_bot['token'])
        bot.message_loop(bot_handle)
        print '%s\'s Bot %s is listening...' % (config_bot['provider'], config_bot['name'])

        #TODO: dev try/except and signals handle
        while 1:
            time.sleep(10)

    except:
        print "#### Exception catached - strace: "
        raise
        sys.exit(1)

if __name__ == "__main__":
    main()
