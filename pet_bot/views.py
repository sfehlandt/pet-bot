from django.shortcuts import render
from django.http import HttpResponse
from pet_bot.controller import *
import datetime
from .models import *

global bot

from .models import Greeting

class SingletonTelegramBot:

  singleton_bot = None

  def __init__(self):
    global bot
    import sys
    import time
    import telepot
    from telepot.loop import MessageLoop

    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type == 'text':

            if "/mytasks" in msg['text']:
                task_list = my_tasks(chat_id)
                msg = "Èstas son tus Tareas actuales:\n\n"
                template = '''Nombre (id): {} ({})
                - Descripción: {}
                - Créditos: {}
                - Límite: {:%Y-%m-%d %H:%M}
                '''
                for task in task_list:
                    msg += template.format(task.name, task.id, task.description, task.credits, task.deadline)
                bot.sendMessage(chat_id, msg)

            elif "/starttask " in msg['text']:
                task_id = msg['text'].split(" ")[1]
                bot.sendMessage(chat_id, start_task(chat_id, task_id))

            elif "/finishtask " in msg['text']:
                task_id = msg['text'].split(" ")[1]
                bot.sendMessage(chat_id, finish_task(chat_id, task_id))

            elif "/mycredits" in msg['text']:
                bot.sendMessage(chat_id, 'Tienes {} créditos'.format(str(my_credits(chat_id))))

            elif "/usecredits" in msg['text']:
                bot.sendMessage(chat_id, use_credits(chat_id))

            elif "/freetasks" in msg['text']:
                task_list = free_tasks(chat_id)
                msg = "Las Tareas disponibles son las siguientes:\n\n"
                template = '''Nombre (id): {} ({})
                - Descripción: {}
                - Créditos: {}
                - Límite: {:%Y-%m-%d %H:%M}
                '''
                for task in task_list:
                    msg += template.format(task.name, task.id, task.description, task.credits, task.deadline)
                bot.sendMessage(chat_id, msg)


    TOKEN = '447325365:AAE8SXS9AZqHbkg5TUUFKPJQS6ZJMHM0qro'

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

def check_tasks(request):
    global bot
    SingletonTelegramBot.init_bot()
    print("Helo!")
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    pets = Pet.objects.all()
    for pet in pets:
        tasks = Task.objects.filter(deadline__lte=tomorrow, pet=pet).exclude(status=Task.DONE)
        if len(tasks) > 0:
            msg = "Oh no! A tu " + pet.species + " le pasó algo!\n"
            pet.random_bad_state(500*len(tasks))
            msg = msg + "Condición: " + Pet.VERBOSE_STATE[pet.state] + "\n"
            msg = msg + "Para mejorarlo, necesitas conseguir créditos a través de completar estas tareas:\n"
            i = 1;
            for task in tasks:
                msg = msg + str(i) + ".-" + task.name + ": " + task.description + "\n"
                i = i + 1;
            bot.sendMessage(pet.owner_id,  msg)
    return render(request, 'check_tasks.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})