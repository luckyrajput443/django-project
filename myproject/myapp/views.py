from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry

def welcome(request):
    return render(request, 'welcome.html')

def result(request):
    entry = None
    error_message = None

    if request.method == 'POST':
        index = request.POST.get('index')

        try:
            entry = Entry.objects.get(id=index)
        except Entry.DoesNotExist:
            error_message = f"Entry with ID {index} does not exist."

    entries = Entry.objects.all()
    total_entries = Entry.objects.count()
    return render(request, 'result.html', {'entries': entries, 'entry': entry, 'error_message': error_message, 'total_entries': total_entries})

def add_entry(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        entry = Entry(first_name=first_name, last_name=last_name)
        entry.save()
        return redirect('welcome')  # Redirect to the welcome page after adding an entry
    return redirect('welcome')

def data_mining(request):
    entries = Entry.objects.all()
    return render(request, 'result.html', {'entries': entries})

def list_entries(request):
    entries_in_range = None

    if request.method == 'POST':
        start_range = request.POST.get('start_range')
        end_range = request.POST.get('end_range')

        if start_range and end_range:
            # Query entries within the specified range
            entries_in_range = Entry.objects.filter(id__range=[start_range, end_range])

    entries = Entry.objects.all()
    total_entries = Entry.objects.count()
    return render(request, 'result.html', {'entries': entries, 'entries_in_range': entries_in_range, 'total_entries': total_entries})

