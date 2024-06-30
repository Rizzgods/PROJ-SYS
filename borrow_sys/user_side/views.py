import json

from django.shortcuts import render, redirect
from .forms import UserForm
from .models import DEPARTMENTS, ITEM_CHOICES, Items



def home(request):
    departments = DEPARTMENTS
    return render(request, 'user.html', {'departments': departments})

def submit_user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('form')  
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserForm()
    return render(request, 'h.html', {'form': form, 'departments': DEPARTMENTS})

from django.shortcuts import render, redirect
from .models import Borrow_History, Items, Students, Prof
from .forms import BorrowHistoryForm

# views.py
from django.shortcuts import render, redirect
from .forms import BorrowHistoryForm

def submitBorrow(request):
    if request.method == "POST":
        form = BorrowHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace with your actual success URL
    else:
        form = BorrowHistoryForm()  # Initialize an instance of the form
    return render(request, 'h.html', {'form': form})


def borrow_form(request):
    professors = Prof.objects.all()
    items = Items.objects.all()
    form = BorrowHistoryForm()
    return render(request, 'borrow_registration.html', {'professors': professors, 'items': items, 'form': form, 'student': {}})


def form(request):
    item_true = Items.objects.filter(availability=True)
    professors = Prof.objects.all()
    students = Students.objects.all()
    return render(request, 'forms.html', {'items': item_true, 'professors': professors, 'students': students})

def fail(request):
    return render(request, 'h.html')

def entries(request):
    return render(request, 'add.html')

from django.http import JsonResponse
from .models import Students

def validate_rfid(request):
    if request.method == 'POST':
        rfid = json.loads(request.body).get('rfid', '')
        student = Students.objects.filter(RFID=rfid).first()
        if student:
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})
    return JsonResponse({'valid': False})

def success(request):
    return render(request, 'suc.html')

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Students

from django.http import JsonResponse
from .models import Students

def scan_rfid(request):
    if request.method == 'POST':
        rfid = request.POST.get('rfid')
        try:
            student = Students.objects.get(RFID=rfid)
            response = {
                'success': True,
                'student_name': student.Name
            }
        except Students.DoesNotExist:
            response = {
                'success': False,
                'message': 'RFID not found'
            }
        return JsonResponse(response)

from django.shortcuts import render
from .models import Students, Items, Prof
from .forms import BorrowHistoryForm

def borrow_form(request):
    if request.method == 'GET':
        professors = Prof.objects.all()
        items = Items.objects.all()
        form = BorrowHistoryForm()
        return render(request, 'borrow_registration.html', {'professors': professors, 'items': items, 'form': form, 'student': {}})
    elif request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Students.objects.get(pk=student_id)
        form = BorrowHistoryForm(request.POST)
        if form.is_valid():
            borrow_history = form.save(commit=False)
            borrow_history.Borrower_Name = student
            borrow_history.save()
            return redirect('success')  # Change to your success URL
        else:
            professors = Prof.objects.all()
            items = Items.objects.all()
            return render(request, 'forms.html', {'professors': professors, 'items': items, 'form': form, 'student': student})


