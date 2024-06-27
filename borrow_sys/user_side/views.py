from django.shortcuts import render, redirect
from .forms import UserForm
from .models import DEPARTMENTS

def home(request):
    departments = DEPARTMENTS
    return render(request, 'user.html', {'departments': departments})

def home(request):
    departments = DEPARTMENTS
    return render(request, 'user.html', {'departments': departments})

def submit_user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Make sure 'success' URL is defined in urls.py
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserForm()
    return render(request, 'h.html', {'form': form, 'departments': DEPARTMENTS})

def success(request):
    return render(request, 'suc.html')