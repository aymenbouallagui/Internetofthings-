from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from newsadds.models import news


class FirstView (View):
    def get (self,request):
        news1=news.objects.all()
        cont={'news1':news1}
        return render(request,'newsadds/first.html',cont)


