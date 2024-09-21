from django.shortcuts import render,redirect
from .forms import ReaderForm
from .models import Reader
from django.http import HttpResponse

# Create your views here.


from django.shortcuts import render, redirect
from .forms import ReaderForm

def create_reader(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            
            return redirect('book_info')  # Redirect after successful form submission
    else:
        form = ReaderForm()

    return render(request, 'reader/reader_templates.html', {'form': form})

