from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse


def Flex(request):
    # return  HttpResponse("im good")
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        age = request.POST.get("age")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        password = make_password(request.POST.get("password"))

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number already exists")
            return redirect("signup")

        CustomUser.objects.create(
            username=username,
            age=age,
            phone_number=phone_number,
            email=email,
            password=password
        )

        messages.success(request, "Signup successful")
        return redirect("login")

    return render(request, "signup.html")


from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = CustomUser.objects.get(email=email)
            if check_password(password, user.password):
                request.session["user_id"] = user.id
                return redirect("teams")
            else:
                messages.error(request, "Wrong password")
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, "login.html")


def teams(request):
    return render(request, 'data.html')


from .forms import ImageForm, VideoForm, FileForm
from .models import Video, Image, File


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_images')  # Redirect to image view page
    else:
        form = ImageForm()
    return render(request, 'media/upload_image.html', {'form': form})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_videos')  # Redirect to video view page
    else:
        form = VideoForm()
    return render(request, 'media/upload_video.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_files')  # Redirect to file view page
    else:
        form = FileForm()
    return render(request, 'media/upload_file.html', {'form': form})


def view_images(request):
    images = Image.objects.all()
    return render(request, 'media/images.html', {'images': images})


def view_videos(request):
    videos = Video.objects.all()
    return render(request, 'media/videos.html', {'videos': videos})


# View to display files
def view_files(request):
    files = File.objects.all()
    return render(request, 'media/files.html', {'files': files})


def Media(request):
    return render(request, 'media/Media.html')


def products(request):
    return render(request, 'products.html')


def plan(request):
    return render(request, 'plan.html')


def company(request):
    return render(request, 'company.html')


def terms(request):
    return render(request, 'terms.html')


def area(request):
    return render(request, 'media/Flex.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Video


# Success page


@require_POST
def delete_video1(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return render(request, 'delete_video1.html')
    # return redirect('delete_video')  # ✅ FIX


from django.views.decorators.http import require_POST
from .models import Image


@require_POST
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('delete_image_success')


def delete_image_success(request):
    return render(request, 'delete_image1.html')


from django.views.decorators.http import require_POST
from .models import File


@require_POST
def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    file.delete()
    # return HttpResponse("<h1 style='color:red'>Your file deleted successfully!</h1>")
    return render(request, 'delete_file1.html')


# ----------------------------------------------------------------------------------
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import ResetPasswordForm
from django.http import HttpResponse


def delete_video(request):
    return render(request, 'delete_video1.html')


def delete_file1(request):
    return render(request, 'delete_file1.html')


# MAIL

from django.conf import settings


def send_email(request):
    context = {}

    if request.method == 'POST':
        from_email = request.POST.get('from_email')
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')  # ✅ NEW

        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,  # system sender
                to=[to_email],
                reply_to=[from_email],  # replies go here
            )

            # ✅ OPTIONAL ATTACHMENT
            if attachment:
                email.attach(
                    attachment.name,
                    attachment.read(),
                    attachment.content_type
                )

            email.send()
            context['success'] = "✅ Email sent successfully!"

        except Exception as e:
            context['error'] = f"❌ Failed to send email: {e}"

    return render(request, 'mail.html', context)


from django.shortcuts import render
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import time


def send_bulk(request):
    if request.method == 'POST':
        system_email = request.POST.get('system_email', '').strip()
        receivers = request.POST.get('receivers', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        attachment = request.FILES.get('attachment')

        # -------- VALIDATION --------
        if not system_email or not receivers or not subject or not message:
            return render(request, 'bulk.html', {
                'error': '❌ All fields except attachment are required'
            })

        try:
            validate_email(system_email)
        except ValidationError:
            return render(request, 'bulk.html', {
                'error': '❌ Invalid system sender email'
            })

        receiver_list = [e.strip() for e in receivers.split(',') if e.strip()]

        if len(receiver_list) == 0 or len(receiver_list) > 25:
            return render(request, 'bulk.html', {
                'error': '❌ Enter 1–25 receiver emails only'
            })

        for email in receiver_list:
            try:
                validate_email(email)
            except ValidationError:
                return render(request, 'bulk.html', {
                    'error': f'❌ Invalid receiver email: {email}'
                })

        # -------- SEND --------
        try:
            for email in receiver_list:
                mail = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=system_email,
                    to=[email],
                )

                # OPTIONAL ATTACHMENT
                if attachment:
                    mail.attach(
                        attachment.name,
                        attachment.read(),
                        attachment.content_type
                    )

                mail.send()
                time.sleep(1)  # anti-spam delay

            return render(request, 'bulk.html', {
                'success': f'✅ {len(receiver_list)} emails sent successfully'
            })

        except Exception as e:
            return render(request, 'bulk.html', {
                'error': f'❌ Failed to send emails: {str(e)}'
            })

    return render(request, 'bulk.html')
