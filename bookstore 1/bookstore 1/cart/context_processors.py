def cart_count(request):
    if request.user.is_authenticated:
        try:
            cart = request.user.cart
            count = sum(item.quantity for item in cart.items.all())
            return {'cart_count': count}
        except:
            return {'cart_count': 0}
    return {'cart_count': 0}
