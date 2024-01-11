from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . models import Cake_studio
from .forms import CakeBookingForm
from django.contrib.auth.decorators import login_required
from .models import Product,CartItem







def index(request):
    return render(request,'index.html')



def loginn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})







def register(request):
    if request.method == "POST":
        # ... (your registration logic)
        return redirect('logi')  # Redirect to the login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # Create a new user object
#             user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
#             # You can also set other user attributes like 'first_name', 'last_name', 'gender', 'phone_no' here
#             user.first_name = cd['username']
#             user.save()
#             return render('login.html')  # Redirect to the login page after successful registration
#         else:
#             return HttpResponse("Registration not successful")
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})


def home(request):
    cakes=Cake_studio.objects.all()
    return render(request,'home.html',{'cakes':cakes})







def cake_booking(request):
    cakes = Cake_studio.objects.all()

    if request.method == 'POST':
        form = CakeBookingForm(request.POST)
        if form.is_valid():
            # Process the form data and create a booking
            # ...
            return redirect('booking_success')  # Redirect to booking success template

    else:
        form = CakeBookingForm()

    context = {
        'cakes': cakes,
        'form': form,
    }

    return render(request,'booking.html', context)

def booking_success(request):
    return render(request,'booking_success.html')



@login_required
def profile(request):
    return render(request, 'profile.html')
def admin_page(request):
    return render(request, 'admin_page.html')




def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")




# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
    
#     if request.user.is_authenticated:
#         cart_item, created = CartItem.objects.get_or_create(
#             user=request.user, product=product)
        
#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
    
#     return redirect('cart_view')

# def cart_view(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
    
#     return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})



def add_to_cart(request, product_id):
    user=request.user

    product=Product.objects.get(id=product_id)
    CartItem(user=user,product=product).save()
    return redirect('/')


def showCart(request):
    user=request.user
    cart=cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.price
        amount += value
    total_amount=amount + 40
    return render(request,'cart.html',locals())



def cart(request):
   
    return render(request, 'cart.html')














