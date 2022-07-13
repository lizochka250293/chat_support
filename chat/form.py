from django import forms
from django.forms import Textarea
from django.utils.safestring import mark_safe

from .models import RatingStar, Rating, Number, StarChoises


class NumberForm(forms.Form):
    number = forms.IntegerField(label='Введите табельный номер')

    class Meta:
        model = Number
        fields = ("number")

class RatingForm(forms.ModelForm):


    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None,

    )
    comment = forms.CharField(label='', widget=Textarea(attrs={'rows': 3}))

    class Meta:
        model = Rating
        fields = ("star", 'comment',)

