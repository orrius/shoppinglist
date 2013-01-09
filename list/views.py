from django.template import Context, loader,RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404,render
from list.models import ShoppingList

# Create your views here.

def index(request):
    sl_list = ShoppingList.objects.all()
    return render(request,'list/index.html', {'sl_list': sl_list}, context_instance=RequestContext(request))

def detail(request, list_name):
    p = get_object_or_404(ShoppingList, name=list_name)
    return render(request,'list/detail.html', {'list': p}, context_instance=RequestContext(request))
    #return render_to_response('list/detail.html', {'list': p})


def editamount(request, pk, amount):
    p = get_object_or_404(Item,id=pk)
    p.update(amount=amount)
    return HttpResponse(200)
