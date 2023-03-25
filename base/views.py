from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.







def home(request):
    return render(request,'home.html')

def resume(request):
    return render(request,'resume.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    return render(request,'contact.html')


# def send_email(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         send_mail(
#             'New message from contact form',
#             f'Name: {name}\nEmail: {email}\n\n{message}',
#             email,  # sender's email address
#             ['ben.angmortey@gmail.com'],  # recipient email address
#             fail_silently=False,
#         )
#         return render(request, 'contact.html', {'success': True})
#     return render(request, 'contact.html')


