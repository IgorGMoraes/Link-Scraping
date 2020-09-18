from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import LinkForm
from .models import ParentLink, ChildLink, GrandChildLink

def home(request):
    form = LinkForm(request.POST or None)
    parentlinks = ParentLink.objects.all()
    childlinks = ChildLink.objects.all()
    grandchildlinks = GrandChildLink.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            if ParentLink.objects.filter(url=form.cleaned_data['url']).exists():
                messages.warning(request, 'This URL had already been registered')
            else:
                parentlink = form.save(commit=False)
                print(parentlink.url)
                form.save()
                return redirect('/')
        else:
            messages.warning(request,'Please, provide a valid URL')
            return redirect('/')
    
    context = {
        'form': form,
        'parentlinks': parentlinks,
        'childlinks': childlinks,
        'grandchildlinks': grandchildlinks
    }

    return render(request, 'index.html', context)
