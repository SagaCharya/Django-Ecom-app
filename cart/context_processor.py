from .cart import Cart
# Create context processor so our page can work in all pages

def cart(request):
    # Returing the default data from cart
    return {'cart':Cart(request)}

