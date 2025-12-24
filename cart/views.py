from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import Cart, CartItem
from books.models import Book


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'items': cart.items.all(),
    }
    return render(request, 'cart/cart.html', context)


@login_required
def add_to_cart(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        messages.success(request, f'{book.name} được thêm vào giỏ hàng!')
        
        if request.htmx:
            return render(request, 'partials/toast.html')
        
        return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def update_cart_item(request, pk):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Giỏ hàng đã được cập nhật!')
        
        if request.htmx:
            context = {
                'cart': cart_item.cart,
                'items': cart_item.cart.items.all()
            }
            cart_content = render_to_string('cart/partials/cart_content.html', context, request=request)
            toast_content = render_to_string('partials/toast.html', request=request)
            return HttpResponse(cart_content + toast_content)
        
        return redirect('cart')


@login_required
def remove_from_cart(request, pk):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
        # Store cart reference before deletion if needed, but we can access user.cart
        cart = request.user.cart
        cart_item.delete()
        messages.success(request, 'Sản phẩm đã được xóa khỏi giỏ hàng!')
        
        if request.htmx:
            context = {
                'cart': cart,
                'items': cart.items.all()
            }
            cart_content = render_to_string('cart/partials/cart_content.html', context, request=request)
            toast_content = render_to_string('partials/toast.html', request=request)
            return HttpResponse(cart_content + toast_content)
        
        return redirect('cart')
