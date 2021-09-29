from django import forms
from .models import Results

class PredictorForm (forms.Form):
    results = Results.objects.order_by('match_date').values_list('match_date','match_date').filter(match_date__range=['2020-01-01', '2020-01-31']).distinct()
    fixture_date = forms.ChoiceField(label='Pick Date', choices=results)