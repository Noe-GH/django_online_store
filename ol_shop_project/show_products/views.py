from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class IndexView(ListView):
    model = Item
    template_name = 'show_products/index.html'
    context_object_name = 'item_list'


class ItemDetail(DetailView):
    model = Item
    template_name = 'show_products/detail.html'


class CreateItem(CreateView):
    model = Item
    template_name = 'show_products/item_form.html'
    fields = ['name', 'description', 'price', 'image']

    def form_valid(self, form):
        form.instance.userid = self.request.user

        return super().form_valid(form)


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    context = {'form': form, 'item': item}

    if form.is_valid():
        form.save()
        return redirect('show_products:index')
    return render(request, 'show_products/item_form.html', context)


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('show_products:index')
    return render(request, 'show_products/del_item.html', context)
