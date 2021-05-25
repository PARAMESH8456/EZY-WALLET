from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from wallet.models import Wallet, Transaction
from django.contrib import messages


def logout(request):
    auth.logout(request)
    return redirect('login')


# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    user = request.user
    if user.is_superuser:
        auth.logout(request)
        return redirect('login')
    wallet = Wallet.objects.get(owner=user)
    return render(request, 'ezy_wallet/index.html', context={"user": user, "balance": wallet.balance})


def user_wallet(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    if request.method == 'POST':
        amount = float(request.POST['amount'])
        description = request.POST['description']
        if not description:
            description = 'No Description'
        wallet.balance += amount
        wallet.save()

        Transaction.objects.create(owner=user, transaction_type='income', amount=amount, expense=False,
                                   description=description)
        messages.success(request, f'Rs-{amount} was added to your wallet')
    return render(request, 'ezy_wallet/Wallet.html', context={"user": user, "balance": wallet.balance})


def user_transactions(request):
    user = request.user
    transactions = user.transaction_set.all()
    context = {'transactions': transactions}
    return render(request, 'ezy_wallet/Transactions.html', context=context)


def ElectricityBill(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    context = {"user": user, 'balance': wallet.balance}
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        bill_no = request.POST['bill_no']
        description = 'No Description'
        if bill_no:
            description = f'Paid Electricity Bill {bill_no}'

        if not amount:
            messages.error(request, 'Amount not entered')
            return render(request, 'Payment/Electricity.html', context=context)

        if wallet.balance - amount > 0:
            wallet.balance -= amount
            wallet.save()
            Transaction.objects.create(owner=user, transaction_type='electricity bill', amount=amount, expense=True,
                                       description=description)
            return redirect(home)
        else:
            messages.error(request, 'Not enough funds')
            return render(request, 'Payment/Electricity.html', context=context)

    return render(request, 'Payment/Electricity.html', context=context)


def MobileRecharge(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    context = {"user": user, 'balance': wallet.balance}
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        vendor = request.POST['vendor']
        m_no = str(request.POST['m_no'])

        if vendor == '--Select--':
            messages.error(request, 'Vendor not selected')
            return render(request, 'Payment/Mobile.html', context=context)

        if not amount:
            messages.error(request, 'Amount not entered')
            return render(request, 'Payment/Mobile.html', context=context)

        if not m_no:
            messages.error(request, 'Mobile number not entered')
            return render(request, 'Payment/Mobile.html', context=context)

        if not len(m_no) == 10:
            messages.error(request, 'Mobile number not valid')
            return render(request, 'Payment/Mobile.html', context=context)

        description = f'Your {vendor} mobile {m_no} was recharged'

        if wallet.balance - amount > 0:
            wallet.balance -= amount
            wallet.save()
            Transaction.objects.create(owner=user, transaction_type='mobile recharge', amount=amount, expense=True,
                                       description=description)
            return redirect(home)
        else:
            messages.error(request, 'Not enough funds')
            return render(request, 'Payment/Mobile.html', context=context)

    return render(request, 'Payment/Mobile.html', context=context)


def DTH(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    context = {"user": user, 'balance': wallet.balance}
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        vendor = request.POST['vendor']
        m_no = str(request.POST['m_no'])

        if vendor == '--Select--':
            messages.error(request, 'Vendor not selected')
            return render(request, 'Payment/DTH.html', context=context)

        if not amount:
            messages.error(request, 'Amount not entered')
            return render(request, 'Payment/DTH.html', context=context)

        if not m_no:
            messages.error(request, 'DTH number not entered')
            return render(request, 'Payment/DTH.html', context=context)

        description = f'Your {vendor} DTH {m_no} was recharged'

        if wallet.balance - amount > 0:
            wallet.balance -= amount
            wallet.save()
            Transaction.objects.create(owner=user, transaction_type='DTH recharge', amount=amount, expense=True,
                                       description=description)
            return redirect(home)
        else:
            messages.error(request, 'Not enough funds')
            return render(request, 'Payment/DTH.html', context=context)

    return render(request, 'Payment/DTH.html', context=context)


def Broadband(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    context = {"user": user, 'balance': wallet.balance}
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        vendor = request.POST['vendor']
        m_no = str(request.POST['m_no'])

        if vendor == '--Select--':
            messages.error(request, 'Vendor not selected')
            return render(request, 'Payment/Broadband.html', context=context)

        if not amount:
            messages.error(request, 'Amount not entered')
            return render(request, 'Payment/Broadband.html', context=context)

        if not m_no:
            messages.error(request, 'broadband number not entered')
            return render(request, 'Payment/Broadband.html', context=context)

        description = f'Your {vendor} broadband {m_no} was recharged'

        if wallet.balance - amount > 0:
            wallet.balance -= amount
            wallet.save()
            Transaction.objects.create(owner=user, transaction_type='broadband recharge', amount=amount, expense=True,
                                       description=description)
            return redirect(home)
        else:
            messages.error(request, 'Not enough funds')
            return render(request, 'Payment/Broadband.html', context=context)

    return render(request, 'Payment/Broadband.html', context=context)


def Water(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    context = {"user": user, 'balance': wallet.balance}
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        bill_no = request.POST['bill_no']
        description = 'No Description'
        if bill_no:
            description = f'Paid WATER Bill {bill_no}'

        if not amount:
            messages.error(request, 'Amount not entered')
            return render(request, 'Payment/Water.html', context=context)

        if wallet.balance - amount > 0:
            wallet.balance -= amount
            wallet.save()
            Transaction.objects.create(owner=user, transaction_type='Water bill', amount=amount, expense=True,
                                       description=description)
            return redirect(home)
        else:
            messages.error(request, 'Not enough funds')
            return render(request, 'Payment/Water.html', context=context)

    return render(request, 'Payment/Water.html', context=context)


def FastTag(request):
    user = request.user
    wallet = Wallet.objects.get(owner=user)

    context = {"user": user, 'balance': wallet.balance}
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        vendor = request.POST['vendor']
        m_no = str(request.POST['m_no'])

        if vendor == '--Select--':
            messages.error(request, 'Vendor not selected')
            return render(request, 'Payment/Fast-tag.html', context=context)

        if not amount:
            messages.error(request, 'Amount not entered')
            return render(request, 'Payment/Fast-tag.html', context=context)

        if not m_no:
            messages.error(request, 'FAST_TAG ID not entered')
            return render(request, 'Payment/Fast-tag.html', context=context)

        description = f'Your {vendor} mobile {m_no} was recharged'

        if wallet.balance - amount > 0:
            wallet.balance -= amount
            wallet.save()
            Transaction.objects.create(owner=user, transaction_type='FAST_TAG recharge', amount=amount, expense=True,
                                       description=description)
            return redirect(home)
        else:
            messages.error(request, 'Not enough funds')
            return render(request, 'Payment/Fast-tag.html', context=context)

    return render(request, 'Payment/Fast-tag.html', context=context)
