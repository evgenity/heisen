from django.http import HttpResponse
from django.shortcuts import render_to_response, render

def index(request):
    template_name = 'contacts/index.html'
    return render(request,template_name)
