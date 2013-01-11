from django.template import Context, loader,RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404,render
from list.models import ShoppingList,Item

# Create your views here.

def index(request):
    sl_list = ShoppingList.objects.all()
    return render(request,'list/index.html', {'sl_list': sl_list}, context_instance=RequestContext(request))

def detail(request, list_name):
    p = get_object_or_404(ShoppingList, name=list_name)
    return render(request,'list/detail.html', {'list': p}, context_instance=RequestContext(request))
    #return render_to_response('list/detail.html', {'list': p})


def editamount(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        amount = request.POST['value']
    else:
        return HttpResponse(404)
    p = get_object_or_404(Item,id=pk)
    p.amount = amount
    p.save()
    return HttpResponse(200)

def newitem(request):
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['value']
        list_pk = request.POST['list_pk']
        print name
        print amount
    else:
        return HttpResponse(404)
    newitem = Item(name=name,amount=amount,shoppinglist=ShoppingList.objects.get(pk=list_pk))
    newitem.save()
    return HttpResponse(200)
