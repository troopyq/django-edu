from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, id = 1):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0}, Категория {1}</h2>".format(id, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Admin")
    output = "<h2>Пользователь</h2><h3>id: {0} \nИмя: {1}".format(id, name)
    return HttpResponse(output)