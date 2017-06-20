from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    import sys
    import time
    import telepot
    from telepot.loop import MessageLoop

    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type == 'text':
            bot.sendMessage(chat_id, msg['text'])

    TOKEN = '391521158:AAFilAONR14D5N1CJrguMvbakVhbY7nHUdo'

    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print ('Listening ...')

    # Keep the program running.
    # while 1:
    #     time.sleep(10)
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

