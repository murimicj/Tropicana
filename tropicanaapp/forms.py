from django import forms
from tropicanaapp.models import ImageModel, JobAdvert, RecruitmentInquiry, Job, JobApplication


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields =  ['image','title','price']

class JobAdvertForm(forms.ModelForm):
    class Meta:
        model = JobAdvert
        fields = [
            'first_name', 'last_name', 'email', 'mobile_phone',
            'organization_name', 'title', 'job_title',
            'has_job_description', 'job_description_file',
            'preferred_service', 'payment_option'
        ]
        widgets = {
            'has_job_description': forms.RadioSelect(choices=[(True, "Yes - Please Upload Below"), (False, "No - Draft For Me")]),
            'preferred_service': forms.RadioSelect(),
            'payment_option': forms.RadioSelect(),
        }

class RecruitmentInquiryForm(forms.ModelForm):
    class Meta:
        model = RecruitmentInquiry
        fields = ['first_name', 'last_name', 'email', 'mobile_phone', 'organization_name', 'title', 'help_message']
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'organization_name', 'job_description', 'location']

# forms.py
from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job', 'full_name', 'id_no_or_passport', 'age', 'cv', 'id_copy', 'reason_for_consideration']
