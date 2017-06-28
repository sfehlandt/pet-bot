from django.shortcuts import render
from django.http import HttpResponse
from controller import *

from .models import Greeting

class SingletonTelegramBot:

  singleton_bot = None

  def __init__(self):
    import sys
    import time
    import telepot
    from telepot.loop import MessageLoop

    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type == 'text':
            if "/mytasks"in msg['text']
                bot.sendMessage(chat_id, mytasks(chat_id))
            elif "/starttask" in msg['text']
                task_id = msg['text'].split(" ")[1]
                bot.sendMessage(chat_id, start_task(chat_id, task_id))
            elif "/finishtask" in msg['text']
                task_id = msg['text'].split(" ")[1]
                bot.sendMessage(chat_id, finish_task(chat_id, task_id))

    TOKEN = '391521158:AAFilAONR14D5N1CJrguMvbakVhbY7nHUdo'

    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print ('Listening ...')

  @classmethod
  def init_bot(self):
    if not self.singleton_bot:
      self.singleton_bot = SingletonTelegramBot()
    return self.singleton_bot

# Create your views here.
def index(request):
  SingletonTelegramBot.init_bot()
  return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

