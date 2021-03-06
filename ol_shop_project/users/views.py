from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Signed in correctly. Welcome, '
                                      f'{username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'users/reg_user.html', context)


@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
