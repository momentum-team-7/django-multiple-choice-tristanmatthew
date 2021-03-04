from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Profile, Snippet


# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'html/profile_list.html')
    


def profile(request):
    user_profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'html/profile.html')


def add_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass


def snippet(request):
    snippet = Snippet.objects.all()
    return render(request, 'html/snippets.html')


def add_snippet(request):
    pass


def edit_snippet(request):
    pass


def delete_snippet(request):
    pass