from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
                                form.save()
                                return HttpResponseRedirect('/')

                else:
                        print('error')
                        messages.warning(request,'Please, provide a valid URL')
                        return HttpResponseRedirect('/')
        
        context = {
                'form': form,
                'parentlinks': parentlinks,
                'childlinks': childlinks,
                'grandchildlinks': grandchildlinks
        }

        return render(request, 'index.html', context)
