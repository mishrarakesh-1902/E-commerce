from django.shortcuts import render,redirect,HttpResponse
from app.models import Category,Product,Contact_us,Order,Brand
from django.contrib.auth import authenticate , login
from app.models import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart







from app.forms import FeedbackForm  # Correct if forms.py is in the same app


# naya code h 
# import json
# import hashlib
# import requests
# import paytmchecksum
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt

import json
import requests

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paytmchecksum import generateSignature, verifySignature







def Master(request):
    return render(request, 'master.html')

def Index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    # product_detailID = request.GET.get('product_detail')
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('sub_category')

    if categoryID:
        product=Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()



    context = {
        'category':category,
        'product' :product,
        'brand':brand, 
        
        

}

         
    

    return render(request, 'index.html' , context)


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            
            login(request , new_user)
            return redirect('index')
        
    else:
        form = UserCreateForm()

    context = {
        'form' : form,
    }    

    return render(request, 'registration/signup.html',context)



@login_required(login_url='/accounts/login/')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url='/accounts/login/')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='/accounts/login/')
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='/accounts/login/')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url='/accounts/login/')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='/accounts/login/')
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')



def Contact_Page(request):
    if request.method == "POST":
        contact = Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request,'contact.html')

def CheakOut(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)
        print(cart)



        # print(address , phone , pincode,cart,user)

        for i in cart:
            a= int(cart[i]['price'])
            b= cart[i]['quantity']
            total = a*b
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total ,
            )
            order.save()
        request.session['cart'] = {}    
        return redirect("index")

    return HttpResponse("Your order has been placed")


def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid)

    order = Order.objects.filter(user = user)
    context = {
        'order' : order,
    }


    return render(request , 'order.html' , context)

def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('sub_category')

    if categoryID:
        product=Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category' : category,
        'brand':brand,
        'product': product,
    }
    return render(request , 'product.html' , context)


def Product_Detail(request , id):
    product = Product.objects.filter(id = id).first()
    
    context = {
        'product' : product
        
        
    }
    return render(request, 'product_detail.html', context)

def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query) #this use for setup search bar

    context = {
        "product": product,
    }

    return render(request, 'search.html' , context) 

def Privecy(request):


    context ={
        
    }
    return render(request, 'privecy.html',context)



# yaha v code h naya wala=====

# def generate_paytm_checksum(order_id, amount):
#     """Generate checksum for Paytm transaction."""
#     paytm_params = {
#         "MID": settings.PAYTM_MERCHANT_ID,
#         "ORDER_ID": str(order_id),
#         "CUST_ID": "customer_123",
#         "TXN_AMOUNT": str(amount),
#         "CHANNEL_ID": settings.PAYTM_CHANNEL_ID,
#         "WEBSITE": settings.PAYTM_WEBSITE,
#         "CALLBACK_URL": settings.PAYTM_CALLBACK_URL,
#         "INDUSTRY_TYPE_ID": settings.PAYTM_INDUSTRY_TYPE_ID,
#     }

#     checksum = paytmchecksum.generateSignature(json.dumps(paytm_params), settings.PAYTM_MERCHANT_KEY)
#     paytm_params["CHECKSUMHASH"] = checksum
#     return paytm_params

# def checkout(request):
#     """Process checkout and redirect to Paytm payment."""
#     if request.method == "POST":
#         amount = request.POST.get("total_amount")
#         order_id = "ORD" + str(hash(amount))  # Generate unique order ID

#         paytm_params = generate_paytm_checksum(order_id, amount)

#         return render(request, "paytm_redirect.html", {"paytm_params": paytm_params})

#     return render(request, "checkout.html")


# def paytm_response(request):
#     """Handle Paytm response after payment."""
#     paytm_response = request.POST.dict()
#     paytm_checksum = paytm_response.pop("CHECKSUMHASH", None)

#     # Verify checksum
#     is_valid = paytmchecksum.verifySignature(paytm_response, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

#     if is_valid and paytm_response["RESPCODE"] == "01":
#         return JsonResponse({"message": "Payment successful", "status": "success"})
#     else:
#         return JsonResponse({"message": "Payment failed", "status": "failure"})


def initiate_paytm_payment(request):
    if request.method == "POST":
        amount = request.session.get("cart_total_amount", 0)  # Fetch total amount from session
        order_id = str(request.user.id) + "ORD" + str(request.session.session_key)

        # Paytm parameters
        paytm_params = {
            "MID": settings.PAYTM_MERCHANT_ID,
            "ORDER_ID": order_id,
            "CUST_ID": str(request.user.id),
            "TXN_AMOUNT": str(amount),
            "CHANNEL_ID": settings.PAYTM_CHANNEL_ID,
            "WEBSITE": settings.PAYTM_WEBSITE,
            "INDUSTRY_TYPE_ID": settings.PAYTM_INDUSTRY_TYPE_ID,
            "CALLBACK_URL": settings.PAYTM_CALLBACK_URL,
        }

        # Generate checksum hash
        paytm_params["CHECKSUMHASH"] = generateSignature(paytm_params, settings.PAYTM_MERCHANT_KEY)

        return render(request, "paytm_redirect.html", {"paytm_params": paytm_params})

    return redirect("cart")  # Redirect to cart if GET request


@csrf_exempt
def paytm_response(request):
    received_data = dict(request.POST)
    paytm_checksum = received_data.pop("CHECKSUMHASH", None)[0]
    
    is_valid_checksum = verifySignature(received_data, settings.PAYTM_MERCHANT_KEY, paytm_checksum)
    
    if is_valid_checksum:
        if received_data["STATUS"][0] == "TXN_SUCCESS":
            return render(request, "payment_success.html", {"data": received_data})
        else:
            return render(request, "payment_failed.html", {"data": received_data})
    else:
        return render(request, "payment_failed.html", {"data": "Checksum Mismatch! Payment Failed."})



def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  # Redirect after submission
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_success.html')  # A simple success message



