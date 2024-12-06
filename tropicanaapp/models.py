from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class JobAdvert(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=15)
    organization_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    job_title = models.CharField(max_length=150)
    has_job_description = models.BooleanField()
    job_description_file = models.FileField(upload_to='job_descriptions/', null=True, blank=True)
    preferred_service = models.CharField(
        max_length=50,
        choices=[
            ('Job Advertising Only', 'Job Advertising Only'),
            ('Job Advertising & Shortlisting Service', 'Job Advertising & Shortlisting Service')
        ]
    )
    payment_option = models.CharField(
        max_length=50,
        choices=[
            ('Mobile Money', 'Mobile Money'),
            ('Bank Transfer', 'Bank Transfer')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

    def clean(self):
        pass

class RecruitmentInquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=15)
    organization_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    help_message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Processed', 'Processed')],
                              default='Pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.organization_name}"
    def clean(self):
        pass



# Model for job postings
class Job(models.Model):
    job_title = models.CharField(max_length=150)
    organization_name = models.CharField(max_length=200)
    job_description = models.TextField()
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.organization_name}"

# Model for job applications
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # Link to the Job
    full_name = models.CharField(max_length=255)
    id_no_or_passport = models.CharField(max_length=50)
    age = models.IntegerField()
    cv = models.FileField(upload_to='cv_uploads/')
    id_copy = models.FileField(upload_to='id_copy_uploads/')
    reason_for_consideration = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.job.job_title}"
