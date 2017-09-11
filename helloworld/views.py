from django.http import HttpResponse


def greeting(request):
       return HttpResponse('Greetings from Hello World!')