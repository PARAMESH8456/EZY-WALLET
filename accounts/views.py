from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from wallet.models import Wallet
from django.contrib import auth


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/Login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            auth.login(request, user)

            return redirect('home')
        return render(request, 'accounts/Login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/Register.html')

    def post(self, request):
        username = request.POST['username']
        if not username:
            messages.error(request, 'Username Empty')
            return render(request, 'accounts/Register.html')
        email = request.POST['email']
        if not email:
            messages.error(request, 'Email Empty')
            return render(request, 'accounts/Register.html')
        password = request.POST['password']
        if not password:
            messages.error(request, 'Password Empty')
            return render(request, 'accounts/Register.html')
        phone = request.POST['phone']
        if not phone:
            messages.error(request, 'Mobile number Empty')
            return render(request, 'accounts/Register.html')
        dob = request.POST['dob']
        if not dob:
            messages.error(request, 'DOB Empty')
            return render(request, 'accounts/Register.html')
        proof = request.POST['proof']
        if not proof:
            messages.error(request, 'Proof ID Empty')
            return render(request, 'accounts/Register.html')
        country = request.POST['country']
        if not country:
            messages.error(request, 'Country Empty')
            return render(request, 'accounts/Register.html')
        state = request.POST['state']
        if not state:
            messages.error(request, 'State Empty')
            return render(request, 'accounts/Register.html')
        city = request.POST['city']
        if not city:
            messages.error(request, 'City Empty')
            return render(request, 'accounts/Register.html')
        address = request.POST['address']
        if not address:
            messages.error(request, 'Address Empty')
            return render(request, 'accounts/Register.html')
        if len(phone)>10:
            messages.error(request,'phone number invalid')
            return render(request,'accounts/register.html')
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                user = User(username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()

                wallet = Wallet()
                wallet.owner = user
                wallet.phone = phone
                wallet.dob = dob
                wallet.proof = proof
                wallet.country = country
                wallet.state = state
                wallet.city = city
                wallet.address = address
                wallet.save()

                messages.success(request, 'Account Successfully Created')
                return redirect('login')
            messages.error(request, 'Email already exists')
            return render(request, 'accounts/Register.html')

        messages.error(request, 'Username already exists')
        return render(request, 'accounts/Register.html')
