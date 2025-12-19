from django.contrib import admin
from .models import Grade, Subject, Book, Rating, Comment


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'grade', 'subject', 'created_at']
    list_filter = ['grade', 'subject']
    search_fields = ['name', 'description']
    list_per_page = 20


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['book__name', 'user__username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['book__name', 'user__username', 'text']
