"""
URL configuration for Tropicana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tropicanaapp import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('job-advert/', views.job_advert_form, name='job_advert_form'),
    path('recruitment/', views.recruitment_view, name='recruitment'),
    path('recruitment/thank-you/', views.thank_you_view, name='recruitment_thank_you'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('post-job/', views.post_job, name='post_job'),  # Admin can post new jobs
    path('jobs/', views.job_list, name='job_list'),  # Users can view jobs
    path('jobs/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),  # Users apply for jobs
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),

]

