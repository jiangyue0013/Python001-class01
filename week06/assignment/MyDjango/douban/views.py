from django.shortcuts import render

from .models import Comments

# Create your views here.
def index(request):
    comments = Comments.objects.filter(stars__gte=3)
    return render(request,'index.html', locals())
