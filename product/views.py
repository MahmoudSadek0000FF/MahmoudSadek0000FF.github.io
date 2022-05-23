import imp
from venv import create
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
# Create your views here.
from sre_constants import CATEGORY_DIGIT
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import category,product,order

# Create your views here.
def home(request):
    categoryList = category.objects.all()
    productList = product.objects.all()
    orderproduct = product.objects.all().order_by("-id")

    return render(request,'pages/index.html',{"productList":productList,"categoryList":categoryList,"orderproduct":orderproduct})

def Category(request,categoryid):
    categoryList = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    productList = product.objects.all().filter(category_id = categoryid)

    return render(request,'pages/category.html',{"productList":productList,"categoryList":categoryList,"mycategory":mycategory})

def Product(request,productid):
    categoryList = category.objects.all()
    myproduct = product.objects.get(id=productid)
    return render(request,'pages/product.html',{"categoryList":categoryList,"myproduct":myproduct})

def shop(request):
    categoryList = category.objects.all()
    productList = product.objects.all()
    orderproduct = product.objects.all().order_by("-id")

    return render(request,'pages/shop.html',{"productList":productList,"categoryList":categoryList,"orderproduct":orderproduct})

# def Productorder(request):
#     categoryOrder = category.objects.all()
#     orderproduct = product.objects.all().order_by("-id")

#     return render(request,'pages/index.html',{"orderproduct":orderproduct,"categoryOrder":categoryOrder})
# def cart(request):
#     categoryList = category.objects.all()
#     productList = product.objects.all()


#     return render(request,'pages/cart.html',{"productList":productList,"categoryList":categoryList,})

# def add_to_cart(request, slug) :
#     product = get_object_or_404(product,slug=slug)
#     order_product= OrderProduct.objects.create(product=product)
#     order_qs = Order.objects.filter(user = request.user,ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.products.filter(product__slug=product.slug).exists():
#             order_product.quantity += 1
#             order_product.save()
#     else:
#         ordered_date = timezone.now()
#         order =Order.objects.create(user=request.user,ordered_date=ordered_date)
#         order.products.add(order_product)
#     return redirect("product:product",slug=slug)

@login_required(login_url='/login/')
def addcart(request,proid):
    quantity=int(order.objects.filter(productid=proid).count())
    if quantity >= 1:
        ca=order.objects.get(productid=proid)
        order.objects.filter(productid=proid).update(num=int(ca.num)+1)
    else:
        id = request.user.id
        carts=order(productid=proid,user_id=id,num=1)
        carts.save()
    return redirect("/cart/")

@login_required(login_url='/login/')
def deleteitem(request,proid):
    item=order.objects.get(id=proid)
    item.delete()
    return redirect("/cart/")


@login_required(login_url='/login/')
def cartitem(request):
    categoryList = category.objects.all()
    quantity = 0
    price =0
    products = product.objects.all()
    orderss = order.objects.filter(user_id=request.user.id)
    for v in orderss:
        quantity=quantity+int(v.num)
        for f in product.objects.all():
            if v.productid ==f.id:
                price =price +(int(f.price)*int(v.num))
    return render(request, 'pages/cart.html',{"products":products,'quantity':quantity,"price":price,"orders":orderss,"categoryList":categoryList})
