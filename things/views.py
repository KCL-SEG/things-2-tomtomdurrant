from django.shortcuts import render

from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            pass
    return render(request, 'home.html', {'form': ThingForm})
