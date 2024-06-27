from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('home', views.home, name='home'),
    path('submit_user_form/', views.submit_user_form, name='submit_user_form'),
    path('success/', views.success, name='success'),  # Define a success view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
