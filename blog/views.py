from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Bearing
from .forms import OrderForm, ContactForm, SendBidForm
from django.forms import ModelForm
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


def home(request):
    data = {
    'title' : 'Подшипники в Мурманске'
    }
    return render(request, 'blog/home.html', data)

def mail_send(request):

    return render(request, 'blog/mail_send.html')

def contacts(request):
    data = {
    'adress': 'г. Мурманск, ул. Декабристов, 26',
    'tel' : '+7-(8152)-255- 065',
    'mob' : '+7-(911)-306-1650',
    'mail': 'srtm@mail.ru',
    'title' : 'Контакты',
    }
    return render(request, 'blog/contacts.html', data)

def photos(request):
    return render(request, 'blog/photos.html')

def about(request):

    return render(request, 'blog/about.html')

def proezd(request):
    data = {
    'title' : 'Схема проезда',
    }

    return render(request, 'blog/proezd.html', data)


def search(request):
    return render(request, 'blog/search.html')

global figure

def search_code(request):
    search_query = request.GET.get('search')
    global figure
    if search_query:
        figure = Bearing.objects.filter(code=search_query)
        if figure:
            return render(request, 'blog/search_code.html', {'figure': figure})
        else:
            return redirect('fororder')
        #return render(request, 'blog/order.html', {'figure': figure})
        #return {'figure': figure}

#@csrf_exempt
def order(request):
    global figure
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            subject = 'Заказ с сайта подшипников, со склада'
            mess = "Артикул: {},Описание:  {}, Количество: {}, Почта: {}, Телефон: {}" .format(form.cleaned_data['code_order'], form.cleaned_data['description_order'] ,form.cleaned_data['amaunt_order'], form.cleaned_data['email'], form.cleaned_data['phone'])
            mail = send_mail(subject, mess, form.cleaned_data['email'],  ['srtm@mail.ru'],  fail_silently=False)
            if mail:
                messages.success(request, 'Mail Send')
                return redirect('mail_send')
            else:
                messages.error(request, "Mail error")
        else:
            messages.error(request, "Enter error")
    else:
        form = OrderForm()
    return render(request, 'blog/order.html', {'form': form, 'figure': figure})

def OrderFormComf(request):
    return render(request, 'blog/order.html', {'figure': figure})

def ContactUs(request):
    if request.method == "POST":
        data = ContactForm(request.POST)
        if data.is_valid():
            mail_us = send_mail(data.cleaned_data['subject'], data.cleaned_data['content'], 'daionvolkov@gmail.com', ['srtm@mail.ru'],  fail_silently=True)
            if mail_us:
                messages.success(request, 'Mail Send')
                return redirect('/')
            else:
                messages.error(request, "Mail error")
        else:
            messages.error(request, "Enter error")
    else:
        data = ContactForm()
    return render(request, 'blog/contactus.html', {'data': data})


def fororder(request):
    return render(request, 'blog/fororder.html')

def ordersend(request):
    return render(request, 'blog/ordersend.html')



def sendbid(request):
    if request.method == "POST":
        data_bid = SendBidForm(request.POST)
        if data_bid.is_valid():
            subject = 'Заказ на поставку подшипников'
            mess = "Артикул: {},Описание:  {}, Количество: {}, Почта: {}, Телефон: {}".format(
                data_bid.cleaned_data['code_bid'], data_bid.cleaned_data['description_bid'],
                data_bid.cleaned_data['amaunt_bid'], data_bid.cleaned_data['email'], data_bid.cleaned_data['phone'])
            mail_bid = send_mail(subject, mess, data_bid.cleaned_data['email'], ['srtm@mail.ru'], fail_silently=False)
            if mail_bid:
                messages.success(request, 'Mail Send')
                return redirect('ordersend')
            else:
                messages.error(request, "Mail error")
        else:
            messages.error(request, "Enter error")
    else:
        data_bid = SendBidForm()
    return render(request, 'blog/sendbid.html', {'data_bid': data_bid})
