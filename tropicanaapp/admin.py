from django.contrib import admin

from tropicanaapp.models import ImageModel, JobAdvert, RecruitmentInquiry

# Register your models here.
admin.site.register(ImageModel)


@admin.register(RecruitmentInquiry)
class RecruitmentInquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'organization_name', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'organization_name')
    list_filter = ('submitted_at',)

from django.contrib import admin
from .models import Job, JobApplication

# Register Job model in the Django admin
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'organization_name', 'location', 'posted_at')  # List the job title, organization, etc.
    search_fields = ('job_title', 'organization_name')  # Allow searching by job title and organization

# Register JobApplication model in the Django admin
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'age', 'id_no_or_passport', 'cv', 'id_copy', 'reason_for_consideration')  # Show application details
    search_fields = ('full_name', 'job__job_title')  # Allow searching by applicant name and job tit


@admin.register(JobAdvert)
class JobAdvertAdmin(admin.ModelAdmin):
    list_display = (
    'first_name', 'last_name', 'job_title', 'organization_name', 'preferred_service', 'payment_option', 'created_at',
    'user')
    search_fields = ['first_name', 'last_name', 'job_title', 'organization_name', 'email']
    list_filter = ['preferred_service', 'payment_option', 'created_at']
    ordering = ['-created_at']

    # Optional: Customize the form to be more user-friendly
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'mobile_phone', 'organization_name')
        }),
        ('Job Details', {
            'fields': ('title', 'job_title', 'has_job_description', 'job_description_file')
        }),
        ('Service & Payment', {
            'fields': ('preferred_service', 'payment_option')
        }),
        ('Other', {
            'fields': ('created_at', 'user')
        }),
    )
    readonly_fields = ('created_at',)  # Making 'created_at' read-only to prevent modification in admin

    # If you want to add a custom form or additional actions, you can do so here
