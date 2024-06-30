from datetime import timezone
from django.contrib.auth.models import Group
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

ITEM_CHOICES = [
    ('projector','Projector'),
    ('monitor','Monitor'),
    ('system unit','System Unit'),
    ('peripherals','Peripherals'),
]

DEPARTMENTS = [
    ('ceit','CEIT'),
    ('caba','CABA'),
    ('coed','COED'),
    ('bacta','BACTA'),
]

from django.db import models
from django.utils import timezone

DEPARTMENTS = [
    ('ceit', 'CEIT'),
    ('caba', 'CABA'),
    ('coed', 'COED'),
    ('bacta', 'BACTA'),
]

# Create your models here.


class Items(models.Model):
    item =  models.CharField(max_length=100, choices=ITEM_CHOICES, default='projector')
    number = models.CharField(max_length=100, default="")
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.item + ' no.' + self.number

class Borrow_History(models.Model):
    Borrower_Name = models.CharField(max_length=100, null=True,blank=True) #reference student table
    item = models.ForeignKey('Items', on_delete=models.CASCADE)  #reference item table
    Professor_Name = models.ForeignKey('Prof', on_delete=models.CASCADE, null=True,blank=True)
    Room = models.CharField(max_length=100, null=True,blank=True)
    Exp_Time_Ret = models.TimeField(null=True)
    Date_Borrowed = models.DateTimeField(default=timezone.now, null=True)
    Time_Ret = models.TimeField(null=True)
    Date_Returned = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.Time_borrowed = timezone.now()
        super(Borrow_History, self).save(*args, **kwargs)

    def __str__(self):
         return f"{self.Borrower_Name} - {self.item}"


class Students (models.Model):
    Name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length= 100, null= True, unique= True)
    course = models.CharField(max_length=100, choices=DEPARTMENTS, default='ceit')
    student_No = models.CharField(max_length=7, unique=True)
    RFID = models.CharField(max_length=10, null=True, unique=True)
    pic = models.ImageField(upload_to='selfies/', null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.Name
    
@receiver(post_save, sender=Students)
def create_user_and_assign_to_group(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(
            username=instance.student_No,
            email=instance.email,
            password=instance.RFID,
            first_name=instance.Name,
        )
        student_group, _ = Group.objects.get_or_create(name='Student')
        user.groups.add(student_group)


class Prof (models.Model):
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100, choices=DEPARTMENTS, default='ceit')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name
    
class Borrow_Logs(models.Model):
    Name = models.ForeignKey('Borrow_History', on_delete=models.CASCADE)
    


# views.py

from django.http import JsonResponse
from .models import Students

def check_rfid(request):
    if request.method == 'POST' and request.is_ajax():
        rfid = request.POST.get('rfid', None)
        if rfid:
            try:
                student = Students.objects.get(RFID=rfid)
                return JsonResponse({'success': True, 'name': student.Name})
            except Students.DoesNotExist:
                return JsonResponse({'success': False})
    return JsonResponse({'success': False})
