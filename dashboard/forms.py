# forms.py
from django.forms import ModelForm
from django import forms
from .models import Party, AnnouncedPuResults

class DateInput(forms.DateTimeInput):
    input_type = 'date'

PARTY_CHOICES = [
    ("PDP","PDP"),
    ("DPP","DPP"),
    ("ACN","ACN"),
    ("PPA","PPA"),
    ("CDC","CDC"),
    ("JP","JP"),
    ("ANPP","ANPP"),
    ("LABOUR","LABOUR"),
    ("CPP","CPP"),
]

class AnnouncedPUResultForm(ModelForm):
    polling_unit_uniqueid = forms.CharField()
    party_abbreviation = forms.ChoiceField(choices=PARTY_CHOICES)
    party_score = forms.IntegerField()
    entered_by_user = forms.CharField()
    # date_entered = forms.DateField(widget=DateInput)
    user_ip_address = forms.CharField()
    class Meta:
        model = AnnouncedPuResults
        fields = ['polling_unit_uniqueid', 'party_abbreviation', 'party_score', 'entered_by_user', 'user_ip_address']
        exclude = ['result_id']

