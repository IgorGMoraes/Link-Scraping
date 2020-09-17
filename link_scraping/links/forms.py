from django import forms

from .models import ParentLink

class LinkForm(forms.ModelForm):
    class Meta:
        model = ParentLink
        fields = ['url']
    
        widgets = {
            'url': forms.TextInput(attrs = {'class': 'form-control mr-2 w-50', 'placeholder': 'URL'})
        }
        
    def clean_url(self, *args, **kwargs):
        url = self.cleaned_data.get('url')
        
        if not "www" in url:
            raise forms.ValidationError('Please, provide a valid URL')
        return url
