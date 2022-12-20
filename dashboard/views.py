from django.shortcuts import render, redirect
from .models import *
from .forms import AnnouncedPUResultForm
from django.db.models import Sum
from django.contrib import messages

def pu_single(request):
    pu_names = PollingUnit.objects.values('polling_unit_name').distinct()
    if request.method == 'POST':
        # Get the selected value from the form
        selected_value = request.POST['dropdown']

        # Filter the data based on the selected value
        pu_ids_by_name = PollingUnit.objects.filter(polling_unit_name=selected_value).values('polling_unit_id').distinct()
        id = pu_ids_by_name[0]['polling_unit_id']
        pu_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=id)

        # Render the template with the filtered data   
        context = {
        'pu_results' : pu_results,
        'pu_names': pu_names,
        'pu_name' : selected_value,
        }
        return render(request, 'pu-single.html', context)
    else:
        pu_results = AnnouncedPuResults.objects.all()
        context = {
        'pu_results' : pu_results,
        'pu_names': pu_names,
        }
        return render(request, 'pu-single.html', context)

def add_results(request):
    if request.POST:
        form = AnnouncedPUResultForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result submitted successfully.')
            return render(request, 'add-results.html', {'form': AnnouncedPUResultForm,})
    return render(request, 'add-results.html', {'form': AnnouncedPUResultForm,})

# needs work
def lga_single(request):
    lga_names = Lga.objects.values('lga_name')
    if request.method == 'POST':
        # get state selected by user
        selected_value = request.POST['dropdown']

        # query lga table by lga name
        lga_ids_by_name = Lga.objects.filter(lga_name=selected_value).values('lga_id')

        # grab lga id
        selected_lga_id = lga_ids_by_name[0]['lga_id']

        # query polling unit table by lga id
        pu_ids_by_lga_id = PollingUnit.objects.filter(lga_id=selected_lga_id).values('polling_unit_id').distinct()
        total_score = 0
        for party_scores in pu_ids_by_lga_id.values():
            for key, value in party_scores.items():
                pu_single_sum = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=value).aggregate(Sum('party_score'))
                total_score += pu_single_sum[key]
        context = {
            'total score': total_score,
            'lga_names': lga_names,
            'lga_name': selected_value,
        }
        return render(request, 'lga-single.html', context)
    else:
        context = {
            'lga_names': lga_names,
        }
        return render(request, 'lga-single.html', context)


