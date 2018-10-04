"""
    This program is designed as a home or office intrusion detection
    system that sends you notifications directly to your telegram account.

    Copyright (C) 2018 Irina Camacho
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from telegram.ext import Updater, CommandHandler, Job
import logging
import signal
import json
import serial
import time
from time import gmtime, strftime
import os, re, os.path
import Queue




chat_id = 12181301
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = "639956666:AAFwq2Wi9ryJwkwBlFx5sg_4D3UG1jZ-YGg"
q = Queue.Queue()
s = serial.Serial('/dev/ttyACM0', timeout = 1)
alarm_state = 0

"""
    Start call: will send description, help menu, and keyboard
"""
def start_call(bot, update):
    msg = 'Hello, I am Fluffy, and I\'m here to protect your home and guard the philosopher\'s stone... Ups, that was a secret \n' 
    msg += 'Here are the list of commands that you can use: \n' 
    msg += '/help for instructions on how to use me \n' 
    msg += '/alarm for turning on the alarm at home \n' 
    msg += '/home to turn off the alarm \n'
    msg += '/clear to clear images in your machine \n'
    msg += '/image to receive a picture if your alarm is on'
    update.message.reply_text(msg)
    #bot.send_message(chat_id, text='I\'m so fluffy, I\'m gonna spy')

"""
    Help call: sends help menu
"""
def help_call(bot, update):
    msg = 'Hello, I am Fluffy, and I\'m here to protect your home and guard the philosopher\'s stone... Ups, that was a secret \n' 
    msg += 'Here are the list of commands that you can use: \n' 
    msg += '/help for instructions on how to use me \n' 
    msg += '/alarm for turning on the alarm at home \n' 
    msg += '/home to turn off the alarm \n'
    msg += '/clear to clear images in your machine \n'
    msg += '/image to receive a picture if your alarm is on'
    update.message.reply_text(msg)


def gandalf(bot, job):
    #Read serial port
    halp = s.readline().rstrip()
    #If serial port has detected motion
    if halp == "Motion detected!":
        #Timestamp
        DATE= strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        #Send motion detection warning
        bot.send_message(chat_id, text='Motion detected!')
        #Capture image with timestamp as name, save in folder /home/pi/webcam/
        os.system('fswebcam -r 640x480 --no-banner --log /dev/null /home/pi/webcam/' + DATE + '.jpg')
        #Send image
        bot.send_photo(chat_id, photo=open('/home/pi/webcam/' + DATE + '.jpg'))
        os.system('ffmpeg -i /dev/video0 -t 10 -s 640x480 /home/pi/webcam/' + DATE +'.mp4')
##        time.sleep(10)
        #Send video
        bot.send_video(chat_id, video=open('/home/pi/webcam/' + DATE + '.mp4', 'rb'), supports_streaming=True)


def alarm_call(bot, update, job_queue):
    global alarm_state
    alarm_state = 1
    #Detect the user that has made the call to the bot
    user = update.message.from_user
    name = user.first_name
    #Send message with the user that has made the call to the bot
    bot.send_message(chat_id, text= name + ': says you shall not pass!')
    job_queue.run_repeating(gandalf, interval=6, first=0, name='gandalfdie')
    job_queue.run_repeating(gandalf, interval=6, first=3, name='gandalfdie')

def home_call(bot, update, job_queue):
    global alarm_state
    alarm_state = 0
    #Detect the user that has made the call to the bot
    user = update.message.from_user
    name = user.first_name
    #Send message with the user that has made the call to the bot
    bot.send_message(chat_id, text=name + ': who must not be named, has disabled the alarm!')
    bot.send_message(chat_id, text='No more spamming! Pinkie swear!')
    #Empty queue of running jobs
    while job_queue._queue.qsize() is not 0: 
        job_queue.get_jobs_by_name('gandalfdie')[0].schedule_removal()


def image_call(bot, update):
    global alarm_state
    if alarm_state == 1:
        DATE= strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        #Capture image with timestamp as name, save in folder /home/pi/webcam/
        os.system('fswebcam -r 640x480 --no-banner --log /dev/null /home/pi/webcam/' + DATE + '.jpg')
        #Send image
        bot.send_photo(chat_id, photo=open('/home/pi/webcam/' + DATE + '.jpg'))
    else:
        pass
        bot.send_message(chat_id, text='Alarm is not on')

def clear_call(bot, update):
    os.system('sudo rm -r /home/pi/webcam/*')
    bot.send_message(chat_id, text='Images cleared from the RPi')


def main():
    
    updater = Updater(TOKEN)
    job_queue = updater.job_queue
    dispatcher = updater.dispatcher

    #Command handler
    dispatcher.add_handler(CommandHandler('start', start_call))
    dispatcher.add_handler(CommandHandler('alarm', alarm_call, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('home', home_call, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('help', help_call))
    dispatcher.add_handler(CommandHandler('image', image_call))
    dispatcher.add_handler(CommandHandler('clear', clear_call))
    

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
