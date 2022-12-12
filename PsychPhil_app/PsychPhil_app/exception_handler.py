from django.shortcuts import render


def page_not_found(request, *args, **kwargs):
    return render(request, '404_handler.html')

