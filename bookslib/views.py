from django.shortcuts import render, redirect
from .forms import AdminLoginForm, UserForm, BooksForm
from .utils import user_registered, user_authenticate
from django.contrib import messages
from .models import Books, User
# Create your views here.


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        form = AdminLoginForm()
        if user_registered(username):
            password = request.POST.get("password")
            if user_authenticate(username, password):
                request.session.__setitem__('uname', password)
                return redirect('/adminhome')
            return render(request, 'admin_login_page.html', {'form': form, 'msg': 'Invalid Password'})
        return render(request, 'admin_login_page.html', {'form': form, 'msg': 'User is not registered pls register first'})
    form = AdminLoginForm()
    return render(request, 'admin_login_page.html', {'form': form})


def admin_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if not user_registered(request.POST['username']):
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, f'{request.POST["username"]} is Successfully Registered')
                return redirect('/')
            return render(request, 'admin_registeration_form.html', {'form': form, 'errors': form.errors})
        msg = f'{request.POST["username"]} Is already Registered'
        return render(request, 'admin_registeration_form.html', {'form': form, 'msg': msg})
    form = UserForm()
    return render(request, 'admin_registeration_form.html', {'form': form})


def add_book(request):
    if 'uname' in request.session:
        if request.method == 'POST':
            form = BooksForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/adminhome')
            return render(request, 'add_book_form.html', {'form': form, 'errors': form.errors})
        form = BooksForm()
        return render(request, 'add_book_form.html', {'form': form})
    return redirect('/')


def update_book(request, pk):
    if 'uname' in request.session:
        if request.method == 'POST':
            form = BooksForm(request.POST, instance=Books.objects.get(pk=pk))
            if form.is_valid():
                form.save()
                return redirect('/adminhome')
            return render(request, 'add_book_form.html', {'form': form, 'errors': form.errors})
        instance = Books.objects.get(pk=pk)
        form = BooksForm(instance=instance)
        return render(request, 'add_book_form.html', {'form': form})
    return redirect('/')


def admin_home(request):
    if 'uname' in request.session:
        books = Books.objects.all()
        return render(request, 'admin_home.html', {'books': books})
    return redirect('/')


def book_detail(request, pk):
    if 'uname' in request.session:
        book = Books.objects.get(pk=pk)
        return render(request, 'book_detail_page.html' , {'book': book})
    return redirect('/')

def delete_book(request, pk):
    if 'uname' in request.session:
        if request.method == 'POST':
            book = Books.objects.get(pk=pk)
            book.delete()
            return redirect('/adminhome')
        return render(request, 'confirm_book_delete.html')
    return redirect('/')


def admin_logout(request):
    if 'uname' in request.session:
        del request.session['uname']
    return redirect('/')
