from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Order, OrderItem
from .patterns import OrderBuilder, InvoiceGenerator
from cart.models import Cart


@login_required
def checkout(request):
    try:
        cart = request.user.cart
        items = cart.items.all()
        
        if not items:
            messages.error(request, 'Your cart is empty!')
            return redirect('cart')
        
        context = {
            'cart': cart,
            'items': items,
        }
        return render(request, 'orders/checkout.html', context)
    except Cart.DoesNotExist:
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')


@login_required
def process_payment(request):
    if request.method == 'POST':
        try:
            cart = request.user.cart
            items = cart.items.all()
            
            if not items:
                messages.error(request, 'Giỏ hàng của bạn trống!')
                return redirect('cart')
            
            selected_items = request.POST.getlist('selected_items')
            if not selected_items:
                messages.error(request, 'Vui lòng chọn ít nhất một mặt hàng để mua!')
                return redirect('checkout')
            
            # Use OrderBuilder to create the order
            builder = OrderBuilder()
            builder.set_user(request.user)
            
            for item in items:
                if str(item.id) in selected_items:
                    builder.add_item(
                        book=item.book,
                        quantity=item.quantity,
                        price=item.book.price
                    )
            
            order = builder.build()
            
            # Remove purchased items from cart
            for item in items:
                if str(item.id) in selected_items:
                    item.delete()
            
            messages.success(request, 'Giao dịch thanh toán thành công! Đơn hàng của bạn đã được đặt.')
            return redirect('payment_success', order_id=order.id)
            
        except Cart.DoesNotExist:
            messages.error(request, 'Giỏ hàng của bạn trống!')
            return redirect('cart')


@login_required
def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/payment_success.html', {'order': order})


@login_required
def download_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Use InvoiceGenerator singleton to generate invoice
    generator = InvoiceGenerator()
    invoice_content = generator.generate_invoice(order)
    
    response = HttpResponse(invoice_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="invoice_order_{order.id}.txt"'
    return response


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
