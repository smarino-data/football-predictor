from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Results
from .forms import PredictorForm



        
# Create your views here.
def home(request):
    #distinct values - use to request all matches from fixtures greater than today
    #results = Results.objects.order_by().values('match_date').filter(match_date__range=['2020-01-01', '2020-01-31']).distinct()
    
    if request.method == 'POST':
        form = PredictorForm(request.POST)
        if form.is_valid():
            note = 'Thanks - See available for %s matches below' %(form.cleaned_data['fixture_date']) 
            form = PredictorForm()
            print(note)
            args = {'matchesform': form, 'note':note}
            return render(request,'preds/home.html', args)


    else:
        form = PredictorForm()
    return render(request,'preds/home.html', {'matchesform': form})

    
        
        


