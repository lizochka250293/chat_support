# from .form import NumberForm
import requests
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordContextMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, FormView
from rest_framework import generics
from .form import RatingForm, RegisterUserForm, Auntification, NumberForm
from .models import Number, NumberView, Rating
from .serializers import NumberSerializer


# from config import api_token, channel_id
# def number(request, room_name):
#     messages = NumberView.objects.filter(numberview=room_name).order_by("-dateview")
#     return render(request, 'chat/index.html',
#                   {"messages": messages, "room_name": room_name, 'session_id': request.session.session_key})
# класс личного кабинета
class PersonalArea(ListView, FormMixin):
    model = NumberView
    template_name = 'chat/index.html'
    context_object_name = "messages"
    form_class = RatingForm
# забираем контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RatingForm()
        context['room_name'] = self.kwargs['room_name']
        context['session_id'] = self.request.session.session_key
        return context
# формируем сообщения для оценки
    def get_queryset(self):
        return NumberView.objects.filter(numberview=self.kwargs['room_name']).order_by("-dateview")

# забираем оценку
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            number = get_object_or_404(Number, id=self.kwargs['room_name'])
            message = get_object_or_404(NumberView, id=request.POST.get('message_1'))
            rating = Rating.objects.create(number=number, star_1=request.POST.get('star_1'), star_2=request.POST.get('star_2'),message=message,  )


    # def get_success_url(self):
    #     return reverse('room', kwargs={'room_name': self.kwargs['room_name']})


# def room(request, room_name):
#     last_message = Number.objects.filter(number=room_name, session=request.session.session_key).last().message
#     return render(request, 'chat/room.html', context={"room_name": room_name, 'last_message': last_message})
# класс комнаты
class PersonalRoom(DetailView):
    model = Number
    template_name = 'chat/room.html'
    pk_url_kwarg = 'room_name'
# получаем контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_message'] = Number.objects.filter(number=self.kwargs['room_name'],
                                                        session=self.request.session.session_key).last().message
        context['room_name'] = self.kwargs['room_name']
        return context

    def get_queryset(self):
        return Number.objects.filter(number=self.kwargs['room_name'])


# def index(request):
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         return redirect('index', room_name=number)
#     return render(request, 'chat/number.html')


# class NumberFormView(FormView):
#     template_name = 'chat/number.html'
#     form_class = NumberForm
#
#     def get_success_url(self):
#         room_number = self.request.POST.get('number')
#         return reverse('index', kwargs={'room_name': room_number})

# титульная страница авторизации
class LoginViewList(LoginView):
    form_class = Auntification
    template_name = 'chat/number.html'

    def get_success_url(self):
        room_number = self.request.POST.get('username')
        return reverse('index', kwargs={'room_name': room_number})

# регистрация
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'chat/register.html'
    success_url = reverse_lazy('title')


# отправка сообщения в тг
def send_telegram(text: str, number: str):
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

# выход из авторизации
def login_out(reguest):
    logout(reguest)
    return redirect('title')

# забыли свой пароль

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'chat/password_reset.html'
    success_url = 'password_reset_confirm'


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    template_name = 'chat/password_reset_confirm.html'
    success_url = 'title'

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
