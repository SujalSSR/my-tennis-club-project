from django.shortcuts import render
from .models import Member


def members(request):
    members = Member.objects.all()

    return render(request, 'myfirst.html', {
        'members': members
    })


def details(request, id):
    member = Member.objects.get(id=id)

    return render(request, 'details.html', {
        'member': member
    })


def main(request):
    return render(request, 'main.html')