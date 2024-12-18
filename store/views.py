from django.shortcuts import render,redirect
from . models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from payment.froms import ShippingFrom
from payment.models import ShippingAddress
from django import forms
from django.db.models import Q
import json
from cart.cart import Cart



def search(request):
    #Determine form is filled
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched == "":
            messages.success(request, "Product not found")
            return render(request, 'search.html', {})

        # in porduct db

        searched = Product.objects.filter(Q(name__icontains = searched)| Q(description__icontains = searched))
        #test for null
        if not searched:
            messages.success(request, "Product not found")
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': searched})
    else:
        return render(request, 'search.html', {})





def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id= request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id)
        form = UserInfoForm(request.POST or None, instance = current_user)
        shipping_form = ShippingFrom(request.POST or None, instance= shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Your info have been updated")
            return redirect('home')
        return render(request, 'update_info.html', {'form': form, 'shipping_form': shipping_form})
    else:
        messages.success(request, "You must be loggedIN to access that page")
        return redirect('home')

    



def update_password(request):
    current_user = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password have been updated.")
                login(request, current_user)
                return redirect('update_password')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.success(request, "You must be loggedIN to access that page")
        return redirect('home')



def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id= request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance = current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "User have been updated")
            return redirect('home')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
         messages.success(request, "You must be loggedIN to access that page")
         return redirect('home')




def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {'categories': categories})



def category(request, foo):
    foo = foo.replace('-', ' ')
    #Grab the category from the url
    try:
        category = Category.objects.get(name = foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That category didnt exist"))
        return redirect('home')



def product(request , pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})




# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            # Do some cart stuff
            current_user = Profile.objects.get(user__id = request.user.id)
            # Get their savd cart from db
            saved_cart = current_user.old_cart

            # string to dictonary
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add( product= key, quantity = value )


            messages.success(request, ("You have been logged In"))
            return redirect('home')

        else:
            messages.success(request, ("There was an error, LOgging In"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logout"))
    return redirect('home')



def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
            return redirect('update_info')
        else:
            messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
            return redirect('register')
    else:
    	return render(request, 'register.html', {'form':form})