#coder :- Marco Tulio R Braga

import sys
import os
import time
#import datetime
#import random
import json
import telepot
import StringIO

#############
# constants:
global config_file, file_stdout
config_file = 'config.json'
file_stdout = '/tmp/command.out'

#############
# Config: read config.json and save in config_bot
def config_read():
    with open(config_file) as j_data:
        d = j_data.read()
    return json.loads(d)

#####################
# Command interpreter
def run_cmd(command):
    answer = "STDOUT of command [%s] : \n " % command
    command = command + " > " + file_stdout
    os.system(command)
    with open(file_stdout, 'r') as f:
        str = f.read()

    answer += str
    return answer

def cmd_help():
    msg = '\n\t MTpi BotHELP:'
    msg += '\nhelp        \t - Show this help'
    msg += '\ncmd COMMAND \t - Run a command on Linux System, debian-based OS [raspbian]'
    msg += '\ncmd ALIAS   \t - Run pre formated commands'
    msg += '\n> ALIAS:    \t - ALIAS avaliable'
    msg += '\n\t iface      \t - ALIAS to list interfaces names'
    msg += '\n\t ip         \t - ALIAS to show all interfaces and its attribs'
    msg += '\n\t ipub4      \t - ALIAS to show public ipv4'
    msg += '\n\t ipub6      \t - ALIAS to show public ipv6'
    return msg

def bot_handler_command(command):
    if command =='help':
       return cmd_help()
    elif command.startswith('cmd') :
        if len(command) <= 3 :
            return "## missing arguments.##"

        cmd_str = StringIO.StringIO(command)
        str_cmd = cmd_str.read(4)
        str_args = cmd_str.read()
        if str_args == 'ip':
            return run_cmd('ip address list')
        elif str_args == 'ipub6':
            return run_cmd('curl -s https://jsonip.com/')
        elif str_args == 'ipub4':
            return run_cmd('curl -s http://ip.42.pl/ip')
        elif str_args == 'iface':
            return run_cmd(' ifconfig  |grep ^[a-z] |awk \'{print$1}\' |tr "\n" " "')
        else:
            return run_cmd(str_args)
# handler will ignore messages unkwown?
    else:
        return "I don't understand your message, can you repeate, please?"

#####################
# Bot minimal security restriction per user id
def allowed_users(id_from):
    if config_bot.has_key('allowed_users'):
        for id_allow in config_bot['allowed_users']:
            if id_from == id_allow:
                return True
    return False

# Bot handler
def bot_handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    msg_id = msg['message_id']
    #print repr(msg)

    # 'allow/deny' check - login =p
    if allowed_users(msg['from']['id']):
        print '#%d> %s chat_id sends a message: %s' % (msg_id, chat_id, command)
        return bot.sendMessage(chat_id, bot_handler_command(command))
    else:
        msg_from = msg['from']
        if 'username' in msg_from:
            print '#%d> Ignoring message from username \"%s\" [%s], message: \n%s' % (msg_id,
                msg_from['username'], msg_from['id'], repr(msg))
        else:
            print '#%d> Ignoring message from username \"%s %s\" [%s], message: \n%s' % (msg_id,
                msg_from['first_name'], msg_from['last_name'], msg_from['id'], repr(msg))

#####################
# Starting

def main():
    try:
        # Initializations

        # Bot config
        global bot
        bot = telepot.Bot(config_bot['token'])
        bot.message_loop(bot_handle)
        print '\t%s\'s Bot %s is listening...' % (config_bot['provider'], config_bot['user'])

        #TODO: dev try/except and signals handle
        #TODO: run as a daemon, and not loop
        while 1:
            time.sleep(10)

    except:
        print "#### Exception catached - strace: "
        raise
        sys.exit(1)

if __name__ == "__main__":
    config_bot = config_read()
    main()
