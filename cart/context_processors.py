from .cart import Cart

#creat context processors so the cart can work on all pages
def cart(request):
    #return the default data from our cart
    return{'cart':Cart(request)}