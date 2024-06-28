from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('home', views.home, name='home'),
    path('submit_user_form/', views.submit_user_form, name='submit_user_form'),
    path('form/', views.form, name='form'),
    path('entries', views.entries, name="entries"),
    path('validate_rfid/', views.validate_rfid, name='validate_rfid'),
    path('fail/', views.fail, name='fail'),
    path('submitBorrow', views.submitBorrow, name='submitBorrow'),
    path('check-rfid/', views.check_rfid, name='check_rfid'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
