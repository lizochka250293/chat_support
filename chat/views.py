from channels.db import database_sync_to_async
from django.shortcuts import render, redirect
from .models import Number
import requests
# from config import api_token, channel_id
def number(request, room_name):
    # messagess = Number.objects.filter(number=room_name).annotate(Min('date'))
    ses_date = []
    for ses_dates in Number.objects.filter(number=room_name).values('session', 'date'):
        ses_date.append(ses_dates)
    collection_ses = []
    collection_ses_ans_date=[]
    for i in ses_date:
        key = i.get('session')
        if key not in collection_ses:
            collection_ses.append(key)
            collection_ses_ans_date.append(i)
    total=[]
    for i in collection_ses_ans_date:
        ses = i.get('session')
        dt = i.get('date')
        #получаем последнее сообщение nm
        qset = Number.objects.filter(date=dt, session=ses).values('message','session', 'date').order_by('-date')
        total.append(qset)
    to_send = total[-1]
    for i in to_send:
        message_to_send = i.get('message')
    send_telegram(message_to_send)
    return render(request, 'chat/index.html', {"messages":total, "room_name": room_name})


def room(request, room_name):
    return render(request,  'chat/room.html', context={"room_name": room_name})


def index(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        return redirect('index', room_name=number)
    return render(request, 'chat/number.html')

def send_telegram(text: str):
    api_token = ""
    url = "https://api.telegram.org/bot"
    channel_id = ""
    url += api_token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

