# quoteapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/quote_list.html', {'quotes': quotes})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = AuthorForm()
    return render(request, 'quoteapp/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()
    return render(request, 'quoteapp/add_quote.html', {'form': form})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quoteapp/author_detail.html', {'author': author, 'quotes': quotes})

