from django.views import View
from django.http import HttpResponse
__author__ = 'sb'

def index(request):
    return HttpResponse("OK")

class LoginView(View):
    pass