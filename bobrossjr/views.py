from django.shortcuts import render
from django.http import JsonResponse
from .models import Birthday

# Create your views here.
def index(request):
    return render(request, 'bobrossjr/index.html')

def birthday_list(request):
    #return render(request, 'bobrossjr/index.html')
    birthdays = Birthday.objects.all().values()
    birthday_list = list(birthdays)
    return JsonResponse(birthday_list, safe=False)