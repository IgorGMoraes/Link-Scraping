from django import forms
from django.core.validators import URLValidator, ValidationError
import re
import requests
from requests.exceptions import ConnectionError


from .models import ParentLink

class LinkForm(forms.ModelForm):
    class Meta:
        model = ParentLink
        fields = ['url']

        widgets = {
            'url': forms.TextInput(attrs = {'class': 'form-control mr-2 w-50',
                                            'placeholder': 'example: "https://www.site.com", "site.com"'})
        }

    def clean_url(self, *args, **kwargs):
        url = self.cleaned_data.get('url')

        if not re.match('https?://', url):
            url = 'https://'+url

        validator = URLValidator()
        try:
            validator(url)   
        except ValidationError:
            print("URL not valid.")
            return
        try:
            request = requests.get(url)
            return url
        except ConnectionError:
            print("Error connecting to URL")
            return