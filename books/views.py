from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from .models import Book, Grade, Subject, Rating, Comment
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Đăng ký thành công!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'books/register.html', {'form': form})


def home(request):
    books = Book.objects.all()
    grades = Grade.objects.all()
    subjects = Subject.objects.all()

    grade_filter = request.GET.get('grade')
    subject_filter = request.GET.get('subject')
    search_query = request.GET.get('search')

    if grade_filter:
        books = books.filter(grade_id=grade_filter)
    if subject_filter:
        books = books.filter(subject_id=subject_filter)
    if search_query:
        books = books.filter(name__icontains=search_query)

    context = {
        'books': books,
        'grades': grades,
        'subjects': subjects,
        'selected_grade': grade_filter,
        'selected_subject': subject_filter,
        'search_query': search_query,
    }
    return render(request, 'books/home.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_rating = None
    if request.user.is_authenticated:
        try:
            user_rating = Rating.objects.get(book=book, user=request.user)
        except Rating.DoesNotExist:
            pass

    context = {
        'book': book,
        'user_rating': user_rating,
        'comments': book.comments.all(),
    }
    return render(request, 'books/book_detail.html', context)


@login_required
def add_rating(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        rating_value = request.POST.get('rating')
        
        if rating_value:
            Rating.objects.update_or_create(
                book=book,
                user=request.user,
                defaults={'rating': int(rating_value)}
            )
            messages.success(request, 'Đánh giá đã được thêm thành công!')
        
        return redirect('book_detail', pk=pk)


@login_required
def add_comment(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        text = request.POST.get('text')
        
        if text:
            word_count = len(text.split())
            if word_count > 200:
                messages.error(request, f'Bình luận vượt quá giới hạn 200 từ ({word_count} words). Vui lòng rút ngắn bình luận của bạn.')
                return redirect('book_detail', pk=pk)
            
            Comment.objects.create(
                book=book,
                user=request.user,
                text=text
            )
            messages.success(request, 'Bình luận đã được thêm thành công!')
        
        return redirect('book_detail', pk=pk)
