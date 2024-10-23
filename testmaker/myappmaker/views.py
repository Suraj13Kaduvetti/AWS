from django.shortcuts import render
from .forms import InputForm

def home_view(request):
    result = ""
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['input_text']  # Get the input text
    else:
        form = InputForm()
    
    return render(request, 'myapp/home.html', {'form': form, 'result': result})
