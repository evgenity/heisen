from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from partners.models import Partner
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'partners/index.html'
    context_object_name = 'partners_list'
    def get_queryset(self):
        return Partner.objects.all()
