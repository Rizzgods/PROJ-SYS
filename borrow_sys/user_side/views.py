import json

from django.shortcuts import render, redirect
from .forms import UserForm
from .models import DEPARTMENTS, ITEM_CHOICES, Items

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
            return redirect('form')  
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserForm()
    return render(request, 'h.html', {'form': form, 'departments': DEPARTMENTS})

from django.shortcuts import render, redirect
from .models import Borrow_History, Items, Students, Prof
from .forms import BorrowHistoryForm

def submitBorrow(request):
    if request.method == "POST":
        form = BorrowHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BorrowHistoryForm()
    return render(request, 'h.html')

def form(request):
    item_true = Items.objects.filter(availability=True)
    professors = Prof.objects.all()
    return render(request, 'forms.html', {'items': item_true, 'professors': professors})

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

@csrf_exempt
def check_rfid(request):
    if request.method == 'POST':
        rfid = request.POST.get('rfid', None)
        if rfid:
            # Check if RFID exists in Students table
            if Students.objects.filter(RFID=rfid).exists():
                return HttpResponse('{"exists": true}', content_type='application/json')
            else:
                return HttpResponse('{"exists": false}', content_type='application/json')
        else:
            return HttpResponse('{"error": "RFID not provided"}', status=400, content_type='application/json')
    else:
        return HttpResponse('{"error": "Method not allowed"}', status=405, content_type='application/json')
