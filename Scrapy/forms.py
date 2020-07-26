from django import forms


class ScrapForm(forms.Form):
    UrlsName = forms.CharField(label="Enter urls",max_length=500)
