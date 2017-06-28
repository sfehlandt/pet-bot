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
            task_id = msg['text'].split(" ")[1]

            if "/mytasks" in msg['text']
                tasks_list = my_tasks(chat_id)
                msg = "Èstas son tus Tareas actuales:\n\n"
                template = '''Nombre (id): {} ({})
                - Descripción: {}
                - Créditos: {}
                - Límite: {:%Y-%m-%d %H:%M}
                '''
                for task in task_list:
                    msg += template.format(task.name, task.id, task.description, task.credits, task.deadline)
                bot.sendMessage(chat_id, msg)

            elif "/starttask" in msg['text']
                bot.sendMessage(chat_id, start_task(chat_id, task_id))

            elif "/finishtask" in msg['text']
                bot.sendMessage(chat_id, finish_task(chat_id, task_id))

            elif "/mycredits" in msg['text']
                bot.sendMessage(chat_id, 'Tienes {} créditos'.format(str(my_credits(chat_id))))

            elif "/usecredits" in msg['text']
                bot.sendMessage(chat_id, use_credits(chat_id))

            elif "/freetasks" in msg['text']
                tasks_list = free_tasks(chat_id)
                msg = "Las Tareas disponibles son las siguientes:\n\n"
                template = '''Nombre (id): {} ({})
                - Descripción: {}
                - Créditos: {}
                - Límite: {:%Y-%m-%d %H:%M}
                '''
                for task in task_list:
                    msg += template.format(task.name, task.id, task.description, task.credits, task.deadline
                bot.sendMessage(chat_id, msg)


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