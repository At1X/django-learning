from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import category, foodArgus
from django.views.generic.list import ListView

def home(request):
    content = foodArgus.objects.all()
    p = Paginator(content, 2)
    page = request.GET.get('page')
    pageCont = p.get_page(page)
    context = {
        'foods': pageCont,
        'cat' : category.objects.all()

    }
    return render(request, 'home.html', context)
def showDetail(request , func):
     context = {
         'foods': foodArgus.objects.get(slug=func),

     }
     return render(request, 'details.html', context)

def base(request, catID):
     context = {
         'capt': get_object_or_404(category , theslg=catID)
     }
     return render(request, 'category.html', context)
# Create your views here.

# 
