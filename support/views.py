from django.shortcuts import render


def about(request):
    """ A view to return about us page"""

    return render(request, 'support/about.html')
