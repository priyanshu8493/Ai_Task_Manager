from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('it worked')


urlpatterns = [
    path('', home, name = 'home'),
]

