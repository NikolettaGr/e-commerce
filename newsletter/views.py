from django.shortcuts import render, redirect
from .forms import EmailNewsNotificationForm


def newsletter(request):
    if request.method == 'POST':
        form = EmailNewsNotificationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = EmailNewsNotificationForm()

    return render(request, 'newsletter/newsletter.html', {'form': form})
