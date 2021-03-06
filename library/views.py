from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from library.models import Book
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def get_auth(request):
    template = get_template('users/auth.html')
    return HttpResponse(template.render({}, request))


def authorize(request):
    username = request.POST.get('username', "")
    password = request.POST.get('password', "")
    print(username, password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/library/books/')
    else:
        return redirect('/library/auth/')


@login_required
def logout_view(request):
    logout(request)


@login_required
def index(request):
    latest_books_list = Book.objects.order_by('pub_date')
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
