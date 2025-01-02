from django.shortcuts import render, redirect
from django.contrib import messages
from tropicanaapp.forms import ImageUploadForm, JobAdvertForm, RecruitmentInquiryForm
from tropicanaapp.models import ImageModel
from .models import ImageModel,JobAdvert,RecruitmentInquiry
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


# Create your views here.
# View for login
@login_required
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:

            # If the user is an admin, log them in and redirect to dashboard
            if user.is_staff:
                login(request, user)
                next_page = request.GET.get('next')
                return HttpResponseRedirect(next_page if next_page else 'admin_dashboard')  # Redirect to your admin dashboard
            else:
                messages.error(request, "You do not have permission to access the admin dashboard.")
                return redirect('index')  # Redirect back to login page for non-admins
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('admin_login')  # If authentication fails, show an error and stay on login page

    return render(request, 'admin_login.html')

# Admin dashboard view
@login_required
def admin_dashboard(request):
    # Add your data fetching logic here
    return render(request, 'admin_dashboard.html')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('index')
    # Fetch all data from the models
    job_adverts = JobAdvert.objects.all()
    recruitment_inquiries = RecruitmentInquiry.objects.all()
    images = ImageModel.objects.all()
    jobs = Job.objects.all()  # Fetch all job posts
    # Passing this data to the template
    return render(request, 'admin_dashboard.html', {
        'job_adverts': job_adverts,
        'recruitment_inquiries': recruitment_inquiries,
        'images': images,
        'jobs': jobs,
    })


def starter(request):
    return render(request, 'starter-page.html')

def index(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio-details.html')

def service(request):
    return render(request,'service-details.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def job_advert_form(request):
    if request.method == 'POST':
        form = JobAdvertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'success' with your success URL
    else:
        form = JobAdvertForm()
    return render(request, 'job_advert_form.html', {'form': form})


def recruitment_view(request):
    # Check if the form is being submitted via POST
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = RecruitmentInquiryForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Display a success message
            messages.success(request, "Your details have been submitted successfully!")

            # Redirect to a thank you page after successful submission
            return redirect('recruitment_thank_you')  # Ensure this is a valid URL pattern name in your urls.py

    else:
        # If the request is GET, create an empty form
        form = RecruitmentInquiryForm()

    # Render the form in the recruitment.html template
    return render(request, 'recruitment.html', {'form': form})


def thank_you_view(request):
    # Simply render the thank you page after a successful submission
    return render(request, 'recruitment_thank_you.html')

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import JobForm, JobApplicationForm
from .models import Job

@login_required
def post_job(request):
    if not request.user.is_staff:
        return redirect('login')  # Ensure only admin can access

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job posted successfully.")
            return render(request, 'post_job.html',{'form':JobForm()} )# Redirect to admin dashboard or jobs listing
    else:
        form = JobForm()

    return render(request, 'post_job.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def apply_for_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        messages.error(request, "Job not found.")
        return redirect('job_list')

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job  # Link application to the specific job
            application.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_list')  # Redirect to the job listing after successful submission
        else:
            # Print form errors for debugging
            print(form.errors)  # This will show validation errors for troubleshooting
            messages.error(request, "There were some errors in your submission.")
    else:
        form = JobApplicationForm()

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})