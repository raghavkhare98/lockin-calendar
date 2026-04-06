from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginSignupView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)