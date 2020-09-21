from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms.models import model_to_dict
from .forms import LinkForm
from .models import ParentLink, ChildLink, GrandchildLink
from .services import find_and_save_links

def home(request):
    form = LinkForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if ParentLink.objects.filter(url=form.cleaned_data['url']).exists():
                messages.warning(request, 'This URL had already been registered')
            else:
                parent_link = form.save(commit=False)
                find_and_save_links(parent_link)
                return redirect('/')
        else:
            messages.warning(request,'Please, provide a valid URL')
            return redirect('/')

    parent_links = ParentLink.objects.all()
    child_links = ChildLink.objects.all()
    grandchild_links = GrandchildLink.objects.all()
     
    context = {
        'form': form,
        'parent_links': parent_links,
        'child_links': child_links,
        'grandchild_links': grandchild_links
    }

    return render(request, 'index.html', context)
