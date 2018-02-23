from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'music/index.html')


def register(request):
    return render(request, 'music/register.html')


def add_album(request):
    return render(request, 'music/add_album.html')

def user(request):
    return render(request,'music/user.html')
