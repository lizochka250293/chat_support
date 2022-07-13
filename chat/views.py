from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .form import NumberForm
import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import FormMixin
from rest_framework import generics

from .form import NumberForm, RatingForm
from .models import Number, NumberView, Rating
from .serializers import NumberSerializer


# from config import api_token, channel_id
# def number(request, room_name):
#     messages = NumberView.objects.filter(numberview=room_name).order_by("-dateview")
#     return render(request, 'chat/index.html',
#                   {"messages": messages, "room_name": room_name, 'session_id': request.session.session_key})

class PersonalArea(ListView, FormMixin):
    model = NumberView
    template_name = 'chat/index.html'
    context_object_name = "messages"
    form_class = RatingForm



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['comment_form'] = RatingForm()
        return context

    def get_queryset(self):
        return NumberView.objects.filter(numberview=self.kwargs['room_name']).order_by("-dateview")

# def room(request, room_name):
#     last_message = Number.objects.filter(number=room_name, session=request.session.session_key).last().message
#     return render(request, 'chat/room.html', context={"room_name": room_name, 'last_message': last_message})

class PersonalRoom(DetailView, FormMixin):
    model = Number
    template_name = 'chat/room.html'
    pk_url_kwarg = 'room_name'
    success_url = 'room'

    def get_queryset(self):
        return Number.objects.filter(number=self.kwargs['room_name'])

# def index(request):
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         return redirect('index', room_name=number)
#     return render(request, 'chat/number.html')


class NumberFormView(FormView):
    template_name = 'chat/number.html'
    form_class = NumberForm

    def get_success_url(self):
        room_number = self.request.POST.get('number')
        return reverse('index', kwargs={'room_name': room_number})



def send_telegram(text: str, number:str):
    api_token = ""
    url = "https://api.telegram.org/bot"
    channel_id = ""
    url += api_token
    method = url + "/sendMessage"
    to_send = f'{text}, http://127.0.0.1:8000/chat/{number}/'
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": to_send
    })


class NumberCreateApiView(generics.CreateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    def perform_create(self, serializer):
        serializer.save()
        number = serializer.data['number']
        session = serializer.data['session']
        message = serializer.data['message']
        NumberView.objects.create(numberview=number, sessionview=session, messageview=message)
        # send_telegram(serializer.data['message'], serializer.data['number'])

class AddStarRating(View):

    def get_number(self):
        number = self.kwargs['room_name']

    def post(self, request):
        form = RatingForm(request.POST)
        assert False, request.POST
        if form.is_valid():
            Rating.objects.update_or_create(
                number=self.get_number(),
                message_id=int(request.POST.get("message")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
