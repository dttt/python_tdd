from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from .forms import ItemForm
from .models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can not have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
