from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Teacher
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')



def success(request):
    return render(request, 'success.html')


def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["melatmelkamu12@gmail.com"],
            fail_silently=False,
        )

        return render(request, "contact.html", {"success": "Message sent successfully!"})

    return render(request, "contact.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            
            if user.is_superuser:
                return redirect('/admin/')
            
            
            elif hasattr(user, 'teacher'):
                return redirect('teacher_dashboard')
            
            
            else:
                return redirect('student_dashboard')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(email=request.user.email)
    except Student.DoesNotExist:
        student = None

    return render(request, 'student_dashboard.html', {'student': student})


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required  
def logout_confirm(request):
    
    student = Student.objects.filter(user=request.user).first()
    
    
    teacher = Teacher.objects.filter(user=request.user).first()
    
    return render(request, 'logout_confirm.html', {
        'student': student,
        'teacher': teacher
    })
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def teacher_dashboard(request):
    
    all_students = Student.objects.all()
    
    return render(request, 'teacher_dashboard.html', {
        'students': all_students
    })

def login_success_redirect(request):
    print(f"DEBUG: User {request.user.username} is trying to log in.")

    
    if request.user.is_superuser:
        print("DEBUG: User is Admin. Sending to Admin panel.")
        return redirect('/admin/')

    
    if Teacher.objects.filter(user=request.user).exists():
        print("DEBUG: Teacher profile found! Sending to Teacher Dashboard.")
        return redirect('teacher_dashboard')

    
    if Student.objects.filter(user=request.user).exists():
        print("DEBUG: Student profile found! Sending to Student Dashboard.")
        return redirect('student_dashboard')

    
    print("DEBUG: No profile found for this user. Sending to Home.")
    return redirect('home')
    
def user_logout(request):
    logout(request)
    return redirect('home') 