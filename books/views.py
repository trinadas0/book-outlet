from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# View to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# View to show details of a single book
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

# View to add a book to the cart
@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

# View to display the contents of the cart
@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    total_price = sum(item.get_total_price() for item in cart.items.all()) if cart else 0
    return render(request, 'books/cart_detail.html', {'cart': cart, 'total_price': total_price})

# View to update the quantity of an item in the cart
@login_required
def update_cart_item(request, book_id):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        return redirect('cart_detail')

    cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    
    return redirect('cart_detail')

# View to delete an item from the cart
@login_required
def delete_cart_item(request, book_id):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)
        cart_item.delete()
    return redirect('cart_detail')

# View to handle user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
