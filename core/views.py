from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Profile, Snippet
from .forms import SnippetForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def error404(request):
    return render(request, 'html/error404.html')


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'html/profile_list.html')
    


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    snippets = Snippet.objects.all()
    return render(request, 'html/profile.html', {'profile': profile, 'snippets': snippets})


def add_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass


def snippet(request):
    snippet = Snippet.objects.all()
    return render(request, 'html/snippets.html',)

def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'html/index.html',{'snippets': snippets})


def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SnippetForm()

    return render(request, 'html/add_snippet.html', {'form': form})
    


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'html/edit_snippet.html', {'form': form, 'snippet':snippet })


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect('/')

class SearchResultsView(ListView):
    model = Snippet
    template_name = 'html/search_results.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        snippet_list = Snippet.objects.filter(
            Q(title__icontains=query) | Q(language__icontains=query)
        )
        return snippet_list