from django.core.management.base import BaseCommand
from books.models import Grade, Subject, Book


class Command(BaseCommand):
    help = 'Setup initial grades, subjects, and sample books'

    def handle(self, *args, **kwargs):
        grades = [
            ('Lớp 1', 1), ('Lớp 2', 2), ('Lớp 3', 3), ('Lớp 4', 4),
            ('Lớp 5', 5), ('Lớp 6', 6), ('Lớp 7', 7), ('Lớp 8', 8),
            ('Lớp 9', 9), ('Lớp 10', 10), ('Lớp 11', 11), ('Lớp 12', 12),
        ]
        
        for name, order in grades:
            Grade.objects.get_or_create(name=name, defaults={'order': order})
        
        subjects = [
            'Toán', 'Tiếng Việt', 'Tiếng Anh', 'Vật Lý', 'Hóa Học',
            'Sinh Học', 'Lịch Sử', 'Địa Lý', 'Tin Học', 'Công Nghệ',
        ]
        
        for name in subjects:
            Subject.objects.get_or_create(name=name)
        
        self.stdout.write(self.style.SUCCESS('Successfully created grades and subjects'))
        
        if Book.objects.count() == 0:
            grade_1 = Grade.objects.get(name='Lớp 1')
            tieng_anh = Subject.objects.get(name='Tiếng Anh')
            toan = Subject.objects.get(name='Toán')
            
            Book.objects.create(
                name='Tiếng Anh Lớp 1',
                price=45000,
                grade=grade_1,
                subject=tieng_anh,
                description='Sách giáo khoa Tiếng Anh lớp 1 theo chương trình mới'
            )
            
            Book.objects.create(
                name='Toán Lớp 1',
                price=42000,
                grade=grade_1,
                subject=toan,
                description='Sách giáo khoa Toán lớp 1 theo chương trình mới'
            )
            
            self.stdout.write(self.style.SUCCESS('Successfully created sample books'))
