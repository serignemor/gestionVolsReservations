from django.shortcuts import render, redirect, get_object_or_404

from apps.compagnie.forms import CompagnieForm
from apps.compagnie.models import Compagnie


def index(request):
    compagnies = Compagnie.objects.all()
    return render(request, 'compagnie/index.html', {'compagnies': compagnies})


def create(request):
    context = {}
    if request.method == 'POST':
        form = CompagnieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['form'] = CompagnieForm()
            return render(request, 'compagnie/create.html', context)
        else:
            context['errors'] = form.errors
            context['form'] = form
            return render(request, 'compagnie/create.html', context)

    context['form'] = CompagnieForm()
    return render(request, 'compagnie/create.html', context)


def edit(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    if request.method == 'POST':
        form = CompagnieForm(request.POST, request.FILES, instance=compagnie)
        if form.is_valid():
            form.save()
            return redirect('compagnie_list')
    else:
        form = CompagnieForm(instance=compagnie)
    return render(request, 'compagnie/edit.html', {'form': form})


def delete(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    compagnie.delete()
    return redirect('compagnie_list')