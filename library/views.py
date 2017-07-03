from django.shortcuts import render
from library.models import Book
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required


def get_auth(request):
    template = get_template('users/auth.html')
    return HttpResponse(template.render({}, request))


@login_required
def index(request):
    latest_books_list = Book.objects.order_by('pub_date')[:5]
    template = get_template('books/index.html')
    context = {
        'latest_books_list': latest_books_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def detail(request, book_id):
    latest_books_list = Book.objects.order_by('-pub_date')[:5]
    template = get_template('books/index.html')
    context = {
        'latest_books_list': latest_books_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def results(request, book_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % book_id)


@login_required
def vote(request, book_id):
    return HttpResponse("You're voting on question %s." % book_id)
