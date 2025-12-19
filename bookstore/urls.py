from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from books import views as book_views
from cart import views as cart_views
from orders import views as order_views

admin.site.site_header = "ADC Book Admin"
admin.site.site_title = "ADC Book Admin"
admin.site.index_title = "Welcome to ADC Book Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', book_views.home, name='home'),
    path('register/', book_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('book/<int:pk>/', book_views.book_detail, name='book_detail'),
    path('book/<int:pk>/rating/', book_views.add_rating, name='add_rating'),
    path('book/<int:pk>/comment/', book_views.add_comment, name='add_comment'),
    
    path('cart/', cart_views.cart_view, name='cart'),
    path('cart/add/<int:pk>/', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:pk>/', cart_views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:pk>/', cart_views.remove_from_cart, name='remove_from_cart'),
    
    path('checkout/', order_views.checkout, name='checkout'),
    path('checkout/process/', order_views.process_payment, name='process_payment'),
    path('payment/success/<int:order_id>/', order_views.payment_success, name='payment_success'),
    path('invoice/download/<int:order_id>/', order_views.download_invoice, name='download_invoice'),
    path('orders/', order_views.order_history, name='order_history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
